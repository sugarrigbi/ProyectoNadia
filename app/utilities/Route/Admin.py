from flask import render_template, request, session, redirect,url_for
from app.utilities.Autenticador import hash_verificar, Obtener_Contraseña, Obtener_DocumentoCodigo, Validar_Datos2, Comparar_Contraseñas4, Obtener_Usuarios, Obtener_Estados, Obtener_Estado_Caso, Obtener_Estados2
from app.models.Casos import Caso_Admin
from app.models.Entidades import Entidad_Admin
from datetime import datetime

from app.models.Entidades import Entidad
from app.models.Persona import Persona

def get_buscar_casos_admin():
    c = Caso_Admin(None, None, None, None, None, None, None, None, None, None, None)
    lista_casos = c.Buscar_Casos_Admin()

    return render_template("dashboard_admin.html", lista_casos=lista_casos, frame_activo="FrameBuscarCasos")
def get_crear_casos_admin():
    nombres = Obtener_Usuarios()
    estados = Obtener_Estados()
    if request.method == "POST":
        datos = {
            "Fecha_Incidente": request.form["Fecha_Incidente"],
            "Descripcion": request.form["Descripcion"],
            "Personas_Afectadas": request.form["Personas_Afectadas"],
            "Usuario_Relacionado": request.form["Usuario_Relacionado"],
            "Tipo_Incidente": request.form["Tipo_Incidente"],
            "Direccion": request.form["Direccion"],
            "Estado": request.form["Estado"]
        }

        if datos["Estado"] not in [estado["Id_estado"] for estado in estados]:
            return render_template("dashboard_admin.html", estados=estados,nombres=nombres,confirmacion="Error, el estado no existe", datos=datos, tipo="error", frame_activo="FrameCrearCaso")
        
        c = Caso_Admin(None, datos["Fecha_Incidente"], datos["Descripcion"], datos["Personas_Afectadas"], datos["Direccion"],datos["Usuario_Relacionado"], datos["Tipo_Incidente"], None, None, datos["Estado"], None)
        resultado, tipo = c.Crear_Caso_Admin()
        if tipo == "error":
            return render_template("dashboard_admin.html", estados=estados,nombres=nombres,confirmacion=resultado, datos=datos, tipo=tipo, frame_activo="FrameCrearCaso")
        elif tipo == "exito":
            return render_template("dashboard_admin.html",confirmacion=resultado, tipo=tipo, frame_activo="FrameCrearCaso")
    if request.method == "GET":
        return render_template("dashboard_admin.html", estados=estados,nombres=nombres, frame_activo="FrameCrearCaso")
def get_modificar_buscar_casos_admin():
    if request.method == "POST":
        codigo = request.form["Radicado"]
        session['Caso_Modificar'] = codigo
        Caso = Caso_Admin(None, None, None, None, None, None, None, None, None, None, codigo)
        lista_datos = Caso.Buscar_Caso_Admin()
        nombres = Obtener_Usuarios()
        estados = Obtener_Estados()

        Estado, tipo = Obtener_Estado_Caso(codigo)
        ola = Obtener_Estado_Caso(codigo)
        print(ola)
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
        nombres = Obtener_Usuarios()
        estados = Obtener_Estados()   

        if datos["Estado"] not in [estado["Id_estado"] for estado in estados]:
            return render_template("dashboard_admin.html", estados=estados,nombres=nombres,confirmacion="Error, el estado no existe", datos=datos, tipo="error", frame_activo="FrameModificarCaso")

        c = Caso_Admin(None, datos["Fecha"], datos["Descripcion"], datos["Persona"], datos["Departamento"],datos["Id_usuario"], datos["Incidente"], None, None, datos["Estado"], Radicado)
        resultado, tipo = c.Modificar_Caso_Admin()
        return render_template("dashboard_admin.html", estados=estados,nombres=nombres, confirmacion=resultado, tipo=tipo, datos=datos, frame_activo="FrameModificarCaso") 
    if request.method == "GET":
        nombres = Obtener_Usuarios()
        estados = Obtener_Estados()
        return render_template("dashboard_admin.html", estados=estados,nombres=nombres, frame_activo="FrameModificarCaso")             
def get_eliminar_casos_admin():
    Radicado = request.form["Radicado"]
    Usuario = session["usuario_id"]
    Caso = Caso_Admin(None, None, None, None, None, Usuario, None, None, None, None, Radicado)

    Estado, tipo = Obtener_Estado_Caso(Radicado)
    if Estado:
        return render_template("dashboard_admin.html", confirmacion=Estado, tipo=tipo, frame_activo="FrameEliminarCaso")

    resultado, tipo = Caso.Eliminar_Caso_Admin()
    return render_template("dashboard_admin.html", frame_activo="FrameEliminarCaso", confirmacion=resultado, tipo=tipo)
def get_buscar_entidades_admin():
    e = Entidad(None, None, None, None, None, None, None)
    lista_entidades = e.Buscar_Entidades()

    return render_template("dashboard_admin.html", lista_entidades=lista_entidades, frame_activo="FrameBuscarEntidad")   
def get_crear_entidades_admin():
    Estados = Obtener_Estados2()
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
        e = Entidad_Admin(None, datos["Nombre_Entidad"], datos["Descripcion_Entidad"], datos["Incidente_Entidad"], datos["Direccion_Entidad"], datos["Telefono_Entidad"], datos["Web_Entidad"], datos["Estado_Entidad"])
        resultado, tipo = e.Crear_Entidad_Admin()
        if tipo == "error":
            return render_template("dashboard_admin.html",confirmacion=resultado, datos=datos, tipo=tipo, frame_activo="FrameCrearEntidad")
        elif tipo == "exito":
            return render_template("dashboard_admin.html",confirmacion=resultado, tipo=tipo, frame_activo="FrameCrearEntidad")
    if request.method == "GET":
        return render_template("dashboard_admin.html", estados=Estados, frame_activo="FrameCrearEntidad")