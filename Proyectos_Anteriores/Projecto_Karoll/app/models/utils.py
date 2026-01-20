from datetime import datetime
from app.extensions import mail
from flask_mail import Message
from flask import render_template
import locale
import os

# ======================== Funciones generales para el funcionamiento del proyecto ========================

locale.setlocale(locale.LC_TIME, 'spanish') 

# Función para formatear fechas al formato "Día, DD de Mes de YYYY"
def formatear_fecha(fecha):
    if isinstance(fecha, datetime):
        fecha_formateada = fecha.strftime("%A, %d de %B de %Y").capitalize()
    else:
        try:
            fecha_obj = datetime.strptime(str(fecha), "%a, %d %b %Y %H:%M:%S %Z")
            fecha_formateada = fecha_obj.strftime("%A, %d de %B de %Y").capitalize()
        except:
            fecha_formateada = str(fecha)
    
    return fecha_formateada

def validar_fecha(fecha):
    try:
        fecha_caso = datetime.strptime(fecha, "%Y-%m-%d").date()
        fecha_actual = datetime.now().date()
        
        if fecha_caso > fecha_actual:
            return fecha
        
    except ValueError:
        return fecha
    
    return None

def enviar_correo_registro(primer_nombre,primer_apellido,email,username):
    try:
        asunto = "Bienvenido a VITARIA SOS"
        cuerpo = render_template('correos/correo_registro.html',
                             nombre=primer_nombre, apellido=primer_apellido, username=username, email= email)
    
        msg = Message(
            subject=asunto,
            recipients=[email], 
            html=cuerpo
            )
        logo_path = os.path.join("app", "static", "img", "logo_correo.png")
        
        if os.path.exists(logo_path):
                with open(logo_path, "rb") as f:
                    msg.attach(
                        filename="logo_vitaria.png",
                        content_type="image/png",
                        data=f.read(),
                        headers={"Content-ID": "<logo_vitaria>"}
                    )
        else:
            print(f"Logo no encontrado en: {logo_path}. Se enviará sin imagen.")
            
        mail.send(msg)
        print(f"Correo de registro enviado a {email}")

    except Exception as e:
        print(f" Error al enviar correo de registro: {e}")
        
def enviar_correo_caso(fecha,descripcion,personas_afectadas,email,nombre,apellido,desastre):
    try:
        print("DEBUG DATOS CORREO:")
        print("nombre:", type(nombre), nombre)
        print("apellido:", type(apellido), apellido)
        print("fecha:", type(fecha), fecha)
        print("descripcion:", type(descripcion), descripcion)
        print("personas_afectadas:", type(personas_afectadas), personas_afectadas)
        print("desastre:", type(desastre), desastre)

        asunto = "Registro de Caso exitoso"
        cuerpo = render_template('correos/correo_registro_caso.html',
                             nombre=nombre, apellido=apellido, fecha= fecha,descripcion= descripcion, personas_afectadas= personas_afectadas,desastre=desastre)
        
        msg = Message(
            subject=asunto, 
            recipients=[email], 
            html=cuerpo
            )

        logo_path = os.path.join("app", "static", "img", "logo_correo.png")
        
        if os.path.exists(logo_path):
                with open(logo_path, "rb") as f:
                    msg.attach(
                        filename="logo_vitaria.png",
                        content_type="image/png",
                        data=f.read(),
                        headers={"Content-ID": "<logo_vitaria>"}
                    )
        else:
            print(f"Logo no encontrado en: {logo_path}. Se enviará sin imagen.")

        mail.send(msg)
        print(f"Enviando correo a {email} con datos: {nombre} {apellido} - {desastre}")


    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f" Error al enviar correo de registro: {e}")

def enviar_correo_actualización_datos(nombre,apellido, direccion, email,telefono, edad, username):
    try:
    
        asunto = "Actualización de datos"
        cuerpo = render_template('correos/correo_actualizacion.html',
                            nombre= nombre, apellido=apellido,
                            direccion= direccion, email= email, telefono=telefono, edad=edad, username=username
                            )
        
        msg = Message(
            subject=asunto, 
            recipients=[email], 
            html=cuerpo
            )

        logo_path = os.path.join("app", "static", "img", "logo_correo.png")
        
        if os.path.exists(logo_path):
                with open(logo_path, "rb") as f:
                    msg.attach(
                        filename="logo_vitaria.png",
                        content_type="image/png",
                        data=f.read(),
                        headers={"Content-ID": "<logo_vitaria>"}
                    )
        else:
            print(f"Logo no encontrado en: {logo_path}. Se enviará sin imagen.")

        mail.send(msg)
        print(f"Enviando correo a {email} con datos: {nombre} {apellido} - {username}")


    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f" Error al enviar correo de registro: {e}")
 



