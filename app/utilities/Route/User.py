from flask import render_template, request, session, redirect,url_for
from app.utilities.Autenticador import hash_verificar, Obtener_Contraseña, Obtener_DocumentoCodigo, Validar_Datos, Validar_Datos2
from app.models.Casos import Caso
from app.models.Entidades import Entidad
from datetime import datetime

from app.models.Entidades import Entidad
from app.models.Persona import Persona

def get_crear_caso():
    if request.method == "POST":
        datos = {
            "Tipo_Incidente": request.form["Tipo_Incidente"],
            "Fecha_Incidente": request.form["Fecha_Incidente"],
            "Direccion": request.form["Direccion"],
            "Personas_Afectadas": request.form["Personas_Afectadas"],
            "Descripcion": request.form["Descripcion"],
        }
        
        c = Caso(None, None, None, None, None, None, None, None, None, None)
        resultado, tipo = c.Crear_Caso(datos)
        return render_template("dashboard_usuario.html", confirmacion=resultado, tipo=tipo, datos=datos, frame_activo="FrameCrearCaso")    
    return render_template("dashboard_usuario.html")
def get_miscasos():
    nombre = session["username"]
    c = Caso(None, None, None, None, None, None, None, None, None, None)
    lista_casos = c.Buscar_Casos(nombre)

    return render_template("dashboard_usuario.html", lista_casos=lista_casos, frame_activo="FrameVerCasos")
def get_entidades():
    e = Entidad(None, None, None, None, None, None, None)
    lista_entidades = e.Buscar_Entidades()

    return render_template("dashboard_usuario.html", lista_entidades=lista_entidades, frame_activo="FrameBuscarEntidad3")
def get_entidad():
    if request.method == "POST":
        codigo = request.form.get("codigo")
        Entidad2 = Entidad(codigo, None, None, None, None, None, None)
        resultado, tipo = Entidad2.Buscar_Entidad()

        if not resultado:
            return render_template("dashboard_usuario.html", confirmacion="Error, Entidad no encontrada xd", tipo="error", frame_activo="Frame1")
        return render_template("dashboard_usuario.html", confirmacion=resultado, tipo=tipo, frame_activo="FrameBuscarEntidad2")
def get_misdatos(): 
    codigo = session["usuario_id"]
    Personas = Persona(codigo, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
    lista_persona = Personas.Buscar_Persona()

    return render_template("dashboard_usuario.html", lista_persona=lista_persona, frame_activo="FrameVerDatos")
def get_eliminardatos():
    codigo = session["usuario_id"]
    contraseña1 = request.form.get("contraseña")
    contraseña = Obtener_Contraseña(codigo)
    if contraseña is None:
        return render_template("dashboard_usuario.html", confirmacion="Usuario no encontrado", tipo="error", frame_activo="FrameEliminarUsuario")

    if not hash_verificar(contraseña, contraseña1):
        return render_template("dashboard_usuario.html", confirmacion="Contraseña incorrecta", tipo="error", frame_activo="FrameEliminarUsuario")
    Personas = Persona(codigo, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
    Personas.Eliminar_Persona()
    session.clear()
    return redirect(url_for("auth.login"))
def get_modificardatos1():
    codigo = session["usuario_id"]
    Personas1 = Persona(codigo, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
    lista_datos = Personas1.Buscar_Persona()

    datos = {
        "Documento": Obtener_DocumentoCodigo(session.get("usuario_id")),
        "Primer_Nombre": request.form.get("Primer_Nombre", ""),
        "Segundo_Nombre": request.form.get("Segundo_Nombre", ""),
        "Primer_Apellido": request.form.get("Primer_Apellido", ""),
        "Segundo_Apellido": request.form.get("Segundo_Apellido", ""),
        "Tipo_Documento": request.form.get("Tipo_Documento", ""),
        "Fecha_Nacimiento": request.form.get("Fecha_Nacimiento", ""),
        "Direccion": request.form.get("Direccion", ""),
        "Telefono": request.form.get("Numero_Contacto", ""),
        "Correo": request.form.get("Email", ""),
        "Usuario": request.form.get("Usuario", "")
    } 

    fecha_str = lista_datos["Fecha_Nacimiento"]
    if fecha_str:
        fecha_html = datetime.strptime(fecha_str, "%d/%m/%Y").strftime("%Y-%m-%d")
    else: 
        fecha_html = ""
    return render_template("dashboard_usuario.html", fecha=fecha_html,lista_datos=lista_datos, frame_activo="FrameModificarDatos")
def get_modificardatos2():
    if request.method == 'POST':
        codigo = session["usuario_id"]
        documento = Obtener_DocumentoCodigo(codigo)        
        Primer_Nombre = request.form['Primer_Nombre']
        Segundo_Nombre = request.form['Segundo_Nombre']
        Primer_Apellido = request.form['Primer_Apellido']
        Segundo_Apellido = request.form['Segundo_Apellido']
        Tipo_Documento = request.form['Tipo_Documento']
        Fecha_Nacimiento = request.form['Fecha_Nacimiento']
        Direccion = request.form['Direccion']
        Numero_Contacto = request.form['Numero_Contacto']
        Correo = request.form['Email']
        Usuario = request.form['Usuario']

        datos = {
            "Documento": Obtener_DocumentoCodigo(session.get("usuario_id")),
            "Primer_Nombre": request.form.get("Primer_Nombre", ""),
            "Segundo_Nombre": request.form.get("Segundo_Nombre", ""),
            "Primer_Apellido": request.form.get("Primer_Apellido", ""),
            "Segundo_Apellido": request.form.get("Segundo_Apellido", ""),
            "Tipo_Documento": request.form.get("Tipo_Documento", ""),
            "Fecha_Nacimiento": request.form.get("Fecha_Nacimiento", ""),
            "Direccion": request.form.get("Direccion", ""),
            "Numero_Contacto": request.form.get("Numero_Contacto", ""),
            "Email": request.form.get("Email", ""),
            "Nombre": request.form.get("Usuario", ""),
            "Usuario": request.form.get("Usuario", "")  
        } 
    
        Mensaje_Error = Validar_Datos2(datos)
        print (Mensaje_Error)
        if Mensaje_Error:
            return render_template("dashboard_usuario.html", errores3=Mensaje_Error, frame_activo="FrameModificarDatos", lista_datos=datos, fecha=datos.get("Fecha_Nacimiento"))

        persona = Persona(codigo, Tipo_Documento, documento, Primer_Nombre, Segundo_Nombre, Primer_Apellido, Segundo_Apellido, Fecha_Nacimiento, None, None, Direccion, None, None, None, None, Numero_Contacto, Correo, Usuario, None, None, None, None)
        resultado, tipo = persona.Modificar_Persona()
        return redirect("/dashboard/user")
