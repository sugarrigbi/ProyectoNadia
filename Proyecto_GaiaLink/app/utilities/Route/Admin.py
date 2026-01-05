from flask import render_template, request, session, jsonify, redirect, url_for
from app.utilities import Autenticador
from app.models.Casos import Caso_Admin
from app.models.Entidades import Entidad_Admin
from app.models.Persona import Persona_Admin
from app.utilities.dispositivos import Buscar_Dispositivos, Eliminar_Dispositivos, obtener_token_actual
from datetime import datetime
from app.models.Entidades import Entidad

def get_buscar_casos_admin():
    c = Caso_Admin(None, None, None, None, None, None, None, None, None, None, None)
    lista_casos = c.Buscar_Casos_Admin()

    return render_template("dashboard_admin.html", lista_casos=lista_casos, frame_activo="FrameBuscarCasos")
def get_crear_casos_admin():
    nombres, estados, casos, prioridad, TipoCasos, Departamentos, Ciudades, Localidades, Barrios = Autenticador.Obtener_Datalist_CrearCaso()
    def return_rend(mensaje, datos):
        return render_template("dashboard_admin.html", Barrios=Barrios, Localidades=Localidades, Ciudades=Ciudades, Departamentos=Departamentos, TipoCasos=TipoCasos, prioridades=prioridad, casos=casos, estados=estados,nombres=nombres,confirmacion=mensaje, datos=datos, tipo="error", frame_activo="FrameCrearCaso")    
    if request.method == "POST":
        datos = {
            "Tipo_Incidente": request.form["Tipo_Incidente"],
            "Fecha_Incidente": request.form["Fecha_Incidente"],
            "Direccion": request.form["Direccion"],
            "Personas_Afectadas": request.form["Personas_Afectadas"],
            "Usuario_Relacionado": request.form["Usuario_Relacionado"],
            "Estado": request.form["Estado"],
            "Caso_Asociado": request.form["Caso_Asociado"],
            "Prioridad": request.form["Prioridad"],
            "Departamento": request.form["Departamento"].capitalize().strip(),
            "Ciudad": request.form["Ciudad"].capitalize().strip(),
            "Localidad": request.form["Localidad"].capitalize().strip(),
            "Barrio": request.form["Barrio"].capitalize().strip(),
            "Descripcion": request.form["Descripcion"]
        }

        if datos["Tipo_Incidente"] not in [TipoCaso["Incidente"] for TipoCaso in TipoCasos]:
            return return_rend("Error, el tipo de caso no existe", datos)
        if datos["Estado"] not in [estado["Estado"] for estado in estados]:
            return return_rend("Error, el estado no existe", datos)
        if datos["Prioridad"] not in [priorida["Prioridad"] for priorida in prioridad]:  
            return return_rend("Error, la prioridad no existe", datos)

        c = Caso_Admin(None, datos["Tipo_Incidente"], datos["Fecha_Incidente"], datos["Direccion"], datos["Personas_Afectadas"], datos["Usuario_Relacionado"], datos["Estado"], datos["Caso_Asociado"], datos["Prioridad"], datos["Departamento"], datos["Ciudad"], datos["Localidad"], datos["Barrio"], datos["Descripcion"])
        resultado, tipo = c.Crear_Caso_Admin()

        if tipo == "error":
            return return_rend(resultado, datos)
        elif tipo == "exito":
            return render_template("dashboard_admin.html",confirmacion=resultado, tipo=tipo, frame_activo="FrameCrearCaso")
    if request.method == "GET":
        return render_template("dashboard_admin.html", Barrios=Barrios, Localidades=Localidades, Ciudades=Ciudades, Departamentos=Departamentos, TipoCasos=TipoCasos, prioridades=prioridad, casos=casos, estados=estados,nombres=nombres, frame_activo="FrameCrearCaso")
def get_modificar_buscar_casos_admin():
    if request.method == "POST":
        codigo = request.form["Radicado"]
        session['Caso_Modificar'] = codigo
        Caso = Caso_Admin(None, None, None, None, None, None, None, None, None, None, codigo)
        lista_datos = Caso.Buscar_Caso_Admin()
        nombres = Autenticador.Obtener_Usuarios()
        estados = Autenticador.Obtener_Estados()

        Estado, tipo = Autenticador.Obtener_Estado_Caso(codigo)
        if Estado:
            return render_template("dashboard_admin.html", confirmacion=Estado, tipo=tipo, frame_activo="FrameModificarCasoBuscar")

        return render_template("dashboard_admin.html", estados=estados, datos=lista_datos[0], nombres=nombres,frame_activo="FrameModificarCaso")
def get_modificar_enviar_casos_admin():
    if request.method == "POST":
        Radicado = session['Caso_Modificar']

        datos = {
            "Fecha": request.form.get("Fecha", ""),
            "Persona": request.form.get("Personas_Afectadas", ""),
            "Id_usuario": request.form.get("Usuario", ""),
            "Incidente": request.form.get("Tipo_Incidente", ""),
            "Departamento": request.form.get("Departamento", ""),
            "Estado": request.form.get("Estado", ""),
            "Descripcion": request.form.get("Descripcion", "")
        }
        nombres = Autenticador.Obtener_Usuarios()
        estados = Autenticador.Obtener_Estados()   

        if datos["Estado"] not in [estado["Id_estado"] for estado in estados]:
            return render_template("dashboard_admin.html", estados=estados,nombres=nombres,confirmacion="Error, el estado no existe", datos=datos, tipo="error", frame_activo="FrameModificarCaso")

        c = Caso_Admin(None, datos["Fecha"], datos["Descripcion"], datos["Persona"], datos["Departamento"],datos["Id_usuario"], datos["Incidente"], None, None, datos["Estado"], Radicado)
        resultado, tipo = c.Modificar_Caso_Admin()
        return render_template("dashboard_admin.html", estados=estados,nombres=nombres, confirmacion=resultado, tipo=tipo, datos=datos, frame_activo="FrameModificarCaso") 
    if request.method == "GET":
        nombres = Autenticador.Obtener_Usuarios()
        estados = Autenticador.Obtener_Estados()
        return render_template("dashboard_admin.html", estados=estados,nombres=nombres, frame_activo="FrameModificarCaso")             
def get_eliminar_casos_admin():
    Radicado = request.form["Radicado"]
    Usuario = session["usuario_id"]
    Caso = Caso_Admin(None, None, None, None, None, Usuario, None, None, None, None, Radicado)

    Estado, tipo = Autenticador.Obtener_Estado_Caso(Radicado)
    if Estado:
        return render_template("dashboard_admin.html", confirmacion=Estado, tipo=tipo, frame_activo="FrameEliminarCaso")

    resultado, tipo = Caso.Eliminar_Caso_Admin()
    return render_template("dashboard_admin.html", frame_activo="FrameEliminarCaso", confirmacion=resultado, tipo=tipo)
def get_buscar_entidades_admin():
    e = Entidad(None, None, None, None, None, None, None)
    lista_entidades = e.Buscar_Entidades()

    return render_template("dashboard_admin.html", lista_entidades=lista_entidades, frame_activo="FrameBuscarEntidad")   
def get_crear_entidades_admin():
    Estados = Autenticador.Obtener_Estados2()
    if request.method == "POST":
        datos = {
            "Nombre_Entidad": request.form["Nombre_Entidad"],
            "Descripcion_Entidad": request.form["Descripcion_Entidad"],
            "Incidente_Entidad": request.form["Incidente_Entidad"],
            "Direccion_Entidad": request.form["Direccion_Entidad"],
            "Telefono_Entidad": request.form["Telefono_Entidad"],
            "Web_Entidad": request.form["Web_Entidad"],
            "Estado_Entidad": request.form["Estado_Entidad"]
        }

        if datos["Estado_Entidad"] not in [estado["Id_estado"] for estado in Estados]:
            return render_template("dashboard_admin.html", estados=Estados, confirmacion="Error, el estado no existe", datos=datos, tipo="error", frame_activo="FrameCrearEntidad")

        e = Entidad_Admin(None, datos["Nombre_Entidad"], datos["Descripcion_Entidad"], datos["Incidente_Entidad"], datos["Direccion_Entidad"], datos["Telefono_Entidad"], datos["Web_Entidad"], datos["Estado_Entidad"])
        resultado, tipo = e.Crear_Entidad_Admin()
        if tipo == "error":
            return render_template("dashboard_admin.html",confirmacion=resultado, datos=datos, tipo=tipo, frame_activo="FrameCrearEntidad")
        elif tipo == "exito":
            return render_template("dashboard_admin.html",confirmacion=resultado, tipo=tipo, frame_activo="FrameCrearEntidad")
    if request.method == "GET":
        return render_template("dashboard_admin.html", estados=Estados, frame_activo="FrameCrearEntidad")
def get_modificar_buscar_entidades_admin():
    if request.method == "POST":
        codigo = request.form["Codigo_Entidad"]
        session['Entidad_Modificar'] = codigo
        Entidad = Entidad_Admin(codigo, None, None, None, None, None, None, None)
        lista_datos = Entidad.Buscar_Entidad_Admin()
        estados = Autenticador.Obtener_Estados2()
        Estado, tipo = Autenticador.Obtener_Estado_Entidad(codigo)
        if Estado:
            return render_template("dashboard_admin.html", confirmacion=Estado, tipo=tipo, frame_activo="FrameModificarEntidadBuscar")

        return render_template("dashboard_admin.html", estados=estados, datos=lista_datos, frame_activo="FrameModificarEntidad")
def get_modificar_enviar_entidades_admin():
    estados = Autenticador.Obtener_Estados2()
    if request.method == "POST":
        codigo = session['Entidad_Modificar']
        datos = {
            "Nombre_Entidad": request.form.get("Nombre_Entidad", ""),
            "Incidente_Entidad": request.form.get("Incidente_Entidad", ""),
            "Estado_Entidad": request.form.get("Estado_Entidad", ""),
            "Direccion_Entidad": request.form.get("Direccion_Entidad", ""),
            "Telefono_Entidad": request.form.get("Telefono_Entidad", ""),
            "Web_Entidad": request.form.get("Web_Entidad", ""),
            "Descripción_Entidad": request.form.get("Descripción_Entidad", "")
        }   
        if datos["Estado_Entidad"] not in [estado["Id_estado"] for estado in estados]:
            return render_template("dashboard_admin.html", estados=estados,confirmacion="Error, el estado no existe", datos=datos, tipo="error", frame_activo="FrameModificarEntidad")
        
        e = Entidad_Admin(codigo, datos["Nombre_Entidad"], datos["Descripción_Entidad"], datos["Incidente_Entidad"], datos["Direccion_Entidad"], datos["Telefono_Entidad"], datos["Web_Entidad"], datos["Estado_Entidad"])
        resultado, tipo = e.Modificar_Entidad_Admin()
        return render_template("dashboard_admin.html", estados=estados, confirmacion=resultado, tipo=tipo, datos=datos, frame_activo="FrameModificarEntidad") 
    if request.method == "GET":
        Codigo = session['Entidad_Modificar']
        return render_template("dashboard_admin.html", Codigo=Codigo, estados=estados, frame_activo="FrameModificarEntidad")  
def get_eliminar_entidades_admin():
    Codigo = request.form["Entidad_Eliminar"]
    
    e = Entidad_Admin(Codigo, None, None, None, None, None, None, None)

    Estado, tipo = Autenticador.Obtener_Estado_Entidad(Codigo)
    if Estado:
        return render_template("dashboard_admin.html", confirmacion=Estado, tipo=tipo, frame_activo="FrameEliminarEntidad")

    resultado, tipo = e.Eliminar_Entidad_Admin()
    return render_template("dashboard_admin.html", frame_activo="FrameEliminarEntidad", confirmacion=resultado, tipo=tipo)
def get_buscar_usuarios_admin():
    p = Persona_Admin(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
    lista_personas = p.Buscar_Personas_Admin()
    
    return render_template("dashboard_admin.html", lista_personas=lista_personas, frame_activo="FrameBuscarPersona")
def get_crear_usuarios_admin():
    Estados = Autenticador.Obtener_Estados3()
    if request.method == "POST":
        datos = {
            "Nombre_Usuario": request.form.get("Nombre_Usuario"),
            "Bloqueado": request.form.get("Bloqueado"),
            "Rol": request.form.get("Rol"),
            "Estado_Entidad": request.form.get("Estado_Entidad"),
            "Documento": request.form.get("Documento"),
            "Tipo_Documento": request.form.get("Tipo_Documento"),
            "Fecha_Nacimiento": request.form.get("Fecha_Nacimiento"),
            "Primer_Nombre": request.form.get("Primer_Nombre"),
            "Segundo_Nombre": request.form.get("Segundo_Nombre"),
            "Primer_Apellido": request.form.get("Primer_Apellido"),
            "Segundo_Apellido": request.form.get("Segundo_Apellido"),
            "Direccion": request.form.get("Direccion"),
            "Telefono": request.form.get("Telefono"),
            "Correo": request.form.get("Correo"),
            "Departamento": request.form.get("Departamento"),
            "Ciudad": request.form.get("Ciudad"),
            "Localidad": request.form.get("Localidad"),
            "Barrio": request.form.get("Barrio"),
            "Contraseña": request.form.get("Contraseña1"),
            "Contraseña2": request.form.get("Contraseña2"),
        }

        Mensaje_Error = Autenticador.Validar_Datos3(datos)
        if Mensaje_Error:
            return render_template("dashboard_admin.html", confirmacion2=Mensaje_Error, datos=datos, tipo="error", frame_activo="FrameCrearPersona")

        if datos["Estado_Entidad"] not in [estado["Id_estado"] for estado in Estados]:
            return render_template("dashboard_admin.html", estados=Estados, confirmacion="Error, el estado no existe", datos=datos, tipo="error", frame_activo="FrameCrearPersona")

        p = Persona_Admin(Codigo=None,Codigo_Pers=None,Tipo_Documento=datos.get("Tipo_Documento"),Documento=datos.get("Documento"),Primer_Nombre=datos.get("Primer_Nombre"),Segundo_Nombre=datos.get("Segundo_Nombre"),Primer_Apellido=datos.get("Primer_Apellido"),Segundo_Apellido=datos.get("Segundo_Apellido"),Fecha_Nacimiento=datos.get("Fecha_Nacimiento"),Codigo_Pers_Adic=None,Edad=None,Direccion=datos.get("Direccion"),Departamento=datos.get("Departamento"),Ciudad=datos.get("Ciudad"),Localidad=datos.get("Localidad"),Barrio=datos.get("Barrio"),Numero_Contacto=datos.get("Telefono"),Email=datos.get("Correo"),Usuario=datos.get("Nombre_Usuario"),Contraseña=datos.get("Contraseña"),Rol=datos.get("Rol"),Estado=datos.get("Estado_Entidad"),Terminos=None,Bloqueo=datos.get("Bloqueado"),Intentos=None)
        resultado, tipo = p.Crear_Persona_Admin()
        if tipo == "error":
            return render_template("dashboard_admin.html",confirmacion=resultado, datos=datos, tipo=tipo, frame_activo="FrameCrearPersona")
        elif tipo == "exito":
            return render_template("dashboard_admin.html",confirmacion=resultado, tipo=tipo, frame_activo="FrameCrearPersona")
    if request.method == "GET":
        return render_template("dashboard_admin.html", estados=Estados, frame_activo="FrameCrearPersona")
def get_eliminar_usuarios_admin():
    Codigo = request.form["Codigo"]
    p = Persona_Admin(Codigo, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
    Estado, tipo = Autenticador.Obtener_Estado_Usuario(Codigo)
    if Estado:
        return render_template("dashboard_admin.html", confirmacion=Estado, tipo=tipo, frame_activo="FrameEliminarPersona")

    resultado, tipo = p.Eliminar_Persona_Admin()
    return render_template("dashboard_admin.html", frame_activo="FrameEliminarPersona", confirmacion=resultado, tipo=tipo)
def get_modificar_buscar_usuarios_admin():
    estados = Autenticador.Obtener_Estados3()
    if request.method == "POST":
        codigo = request.form["Codigo_Usuario"]
        session['Usuario_Modificar'] = codigo
        p = Persona_Admin(codigo, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
        lista_datos = p.Buscar_Persona_Admin()
        lista_datos["Fecha_Nacimiento"] = datetime.strptime(lista_datos["Fecha_Nacimiento"],"%d/%m/%Y").date()
        lista_datos["Id"] = codigo
        Estado, tipo = Autenticador.Obtener_Estado_Usuario(codigo)
        if Estado:
            return render_template("dashboard_admin.html", confirmacion=Estado, tipo=tipo, frame_activo="FrameModificarPersonaBuscar")
        return render_template("dashboard_admin.html", estados=estados, datos=lista_datos, frame_activo="FrameModificarPersona")
def get_modificar_enviar_usuarios_admin():
    estados = Autenticador.Obtener_Estados3()
    if request.method == "POST":
        codigo = session['Usuario_Modificar']
        datos = {
            "Nombre": request.form.get("Nombre_Usuario", ""),
            "Bloqueado": request.form.get("Bloqueado", ""),
            "Rol": request.form.get("Rol", ""),
            "Estado": request.form.get("Estado_Entidad", ""),
            "Codigo_Persona": request.form.get("Documento", ""),
            "Tipo_Documento": request.form.get("Tipo_Documento", ""),
            "Fecha_Nacimiento": request.form.get("Fecha_Nacimiento", ""),
            "Primer_Nombre": request.form.get("Primer_Nombre", ""),
            "Segundo_Nombre": request.form.get("Segundo_Nombre", ""),
            "Primer_Apellido": request.form.get("Primer_Apellido", ""),
            "Segundo_Apellido": request.form.get("Segundo_Apellido", ""),
            "Direccion": request.form.get("Direccion", ""),
            "Numero_Contacto": request.form.get("Telefono", ""),
            "Email": request.form.get("Correo", ""),
            "Departamento": request.form.get("Departamento", ""),
            "Ciudad": request.form.get("Ciudad", ""),
            "Localidad": request.form.get("Localidad", ""),
            "Barrio": request.form.get("Barrio", ""),
            "Contraseña": request.form.get("Contraseña1", ""),
            "Contraseña2": request.form.get("Contraseña2", ""),
            "Id": codigo
        }   
        Mensaje_Error = Autenticador.Validar_Datos4(datos)
        if Mensaje_Error:
            return render_template("dashboard_admin.html", confirmacion2=Mensaje_Error, datos=datos, tipo="error", frame_activo="FrameModificarPersona")

        if datos["Estado"] not in [estado["Id_estado"] for estado in estados]:
            return render_template("dashboard_admin.html", estados=estados, confirmacion="Error, el estado no existe", datos=datos, tipo="error", frame_activo="FrameModificarPersona")
        p = Persona_Admin(codigo, None, datos["Tipo_Documento"], datos["Codigo_Persona"], datos["Primer_Nombre"], datos["Segundo_Nombre"], datos["Primer_Apellido"], datos["Segundo_Apellido"], datos["Fecha_Nacimiento"], None, None, datos["Direccion"], datos["Departamento"], datos["Ciudad"], datos["Localidad"], datos["Barrio"], datos["Numero_Contacto"], datos["Email"], datos["Nombre"], datos["Contraseña"], datos["Rol"], datos["Estado"], None, datos["Bloqueado"], None)
        resultado, tipo = p.Modificar_Persona_Admin()
        return render_template("dashboard_admin.html", estados=estados, confirmacion=resultado, tipo=tipo, datos=datos, frame_activo="FrameModificarPersona") 
    if request.method == "GET":
        Codigo = session['Usuario_Modificar']
        return render_template("dashboard_admin.html", Codigo=Codigo, estados=estados, frame_activo="FrameModificarPersona")  
def get_buscar_dispositivos():
    codigo = session.get("usuario_id")
    if not codigo:
        return redirect(url_for("auth.login"))
    lista_dispositivos = Buscar_Dispositivos(codigo)
    
    return render_template("dashboard_admin.html", lista_dispositivos=lista_dispositivos, frame_activo="FrameBuscarDispositivos")    
def get_eliminar_dispositivos(id):
    if request.method == "POST":
        token_actual = session.get("token_session")
        token_db = obtener_token_actual(id)
        if token_db and token_db["Token"] == token_actual:
            session.clear()        
            print("sesion clear")
            return redirect(url_for("auth.login"))

        resultado = Eliminar_Dispositivos(id)
        if resultado:
            return jsonify({"status": "ok"})
        else:
            return jsonify({"status": "error"}), 500
def get_actualizar_2fa():
    if request.method == "POST":
        codigo = session["usuario_id"]
        p = Persona_Admin(codigo, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
        resultado, tipo = p.Actualizar_2FA()
        return resultado 
def get_cuenta_datos():
    if request.method == "GET":
        Codigo = session["usuario_id"]
        p = Persona_Admin(Codigo, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
        resultado = p.Buscar_Persona_Admin()
        return render_template("dashboard_admin.html", lista_persona=resultado, frame_activo="FrameCuentaDatos")