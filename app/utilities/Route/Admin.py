from flask import render_template, request, session, redirect,url_for
from app.utilities.Autenticador import hash_verificar, Obtener_Contraseña, Obtener_DocumentoCodigo, Validar_Datos2, Comparar_Contraseñas4, Obtener_Usuarios, Obtener_Estados
from app.models.Casos import Caso_Admin
from app.models.Entidades import Entidad
from datetime import datetime

from app.models.Entidades import Entidad
from app.models.Persona import Persona

def get_miscasos_admin():
    c = Caso_Admin(None, None, None, None, None, None, None, None, None, None)
    lista_casos = c.Buscar_Casos_Admin()

    return render_template("dashboard_admin.html", lista_casos=lista_casos, frame_activo="FrameVerCasos")
def get_crear_caso_admin():
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
        return render_template("dashboard_admin.html", confirmacion=resultado, tipo=tipo, datos=datos, frame_activo="FrameCrearCaso") 
    if request.method == "GET":
        nombres = Obtener_Usuarios()
        estados = Obtener_Estados()
        return render_template("dashboard_admin.html", estados=estados,nombres=nombres, frame_activo="FrameCrearCaso")