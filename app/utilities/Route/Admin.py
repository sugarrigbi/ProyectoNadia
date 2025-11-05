from flask import render_template, request, session, redirect,url_for
from app.utilities.Autenticador import hash_verificar, Obtener_Contraseña, Obtener_DocumentoCodigo, Validar_Datos2, Comparar_Contraseñas4, Obtener_Usuarios, Obtener_Estados
from app.models.Casos import Caso_Admin
from app.models.Entidades import Entidad
from datetime import datetime

from app.models.Entidades import Entidad
from app.models.Persona import Persona

def get_buscar_casos_admin():
    c = Caso_Admin(None, None, None, None, None, None, None, None, None, None)
    lista_casos = c.Buscar_Casos_Admin()

    return render_template("dashboard_admin.html", lista_casos=lista_casos, frame_activo="FrameVerCasos")
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
        c = Caso_Admin(None, datos["Fecha_Incidente"], datos["Descripcion"], datos["Personas_Afectadas"], datos["Usuario_Relacionado"], datos["Tipo_Incidente"], None, None, datos["Estado"], None)
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
        Caso = Caso_Admin(None, None, None, None, None, None, None, None, None, codigo)
        lista_datos = Caso.Buscar_Caso_Admin()
        nombres = Obtener_Usuarios()
        estados = Obtener_Estados()

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

        c = Caso_Admin(None, datos["Fecha"], datos["Descripcion"], datos["Persona"], datos["Id_usuario"], datos["Incidente"], None, None, datos["Estado"], Radicado)
        resultado, tipo = c.Modificar_Caso_Admin()
        return render_template("dashboard_admin.html", estados=estados,nombres=nombres, confirmacion=resultado, tipo=tipo, datos=datos, frame_activo="FrameModificarCaso") 
    if request.method == "GET":
        nombres = Obtener_Usuarios()
        estados = Obtener_Estados()
        return render_template("dashboard_admin.html", estados=estados,nombres=nombres, frame_activo="FrameModificarCaso")             
def get_eliminar_casos_admin():
    Radicado = request.form["Radicado"]
    Usuario = session["usuario_id"]
    Caso = Caso_Admin(None, None, None, None, Usuario, None, None, None, None, Radicado)
    resultado, tipo = Caso.Eliminar_Caso_Admin()
    return render_template("dashboard_admin.html", frame_activo="FrameEliminarCaso", confirmacion=resultado, tipo=tipo)             