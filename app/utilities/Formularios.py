from app.utilities.Base_Datos import Get_BaseDatos, Close_BaseDatos, Get_Errores
from datetime import datetime, timedelta
from flask import flash, redirect, url_for, session, render_template
import mysql.connector

def Enviar_Form_Ayuda(Nombre, mensaje):
    conexion, cursor = Get_BaseDatos()

    try:
        cursor.execute("SELECT COUNT(*) AS total FROM tbl_usuario WHERE Nombre = %s", (Nombre,))
        resultado = cursor.fetchone()
        if resultado["total"] == 0:
            return "El nombre ingresado no está registrado como usuario.", "error"
                
        if not conexion.in_transaction:
            conexion.start_transaction()
        cursor.execute("INSERT INTO tbl_ayuda (Nombre, Mensaje) VALUES (%s, %s)",(Nombre, mensaje))
        conexion.commit()
        return "Se creo el ticket de ayuda con exito", "exito"
    except mysql.connector.Error as err:
        conexion.rollback()
        return f"Ocurrió un error al guardar los datos: {err}", "error"
def Enviar_Form_Calificanos(Nombre, Pregunta1, Pregunta2, Pregunta3, Pregunta4):
    conexion, cursor = Get_BaseDatos()

    try:
        cursor.execute("SELECT COUNT(*) AS total FROM tbl_usuario WHERE Nombre = %s", (Nombre,))
        resultado = cursor.fetchone()
        if resultado["total"] == 0:
            return "El nombre ingresado no está registrado como usuario.", "error"

        if not conexion.in_transaction:
            conexion.start_transaction()
        cursor.execute("INSERT INTO tbl_calificanos (Nombre, Pregunta1, Pregunta2, Pregunta3, Pregunta4) VALUES (%s, %s, %s, %s, %s)",(Nombre, Pregunta1, Pregunta2, Pregunta3, Pregunta4))
        conexion.commit()
        return "Se creo la calificacion con exito", "exito"
    except mysql.connector.Error as err:
        conexion.rollback()
        return f"Ocurrió un error al guardar los datos: {err}", "error"
def Enviar_Form_Contactanos(Nombre, Telefono, Correo, Descripcion):
    conexion, cursor = Get_BaseDatos()
    hora_actual = datetime.now()
    hora_str = hora_actual.strftime("%Y-%m-%d %H:%M:%S")

    try:
        if not conexion.in_transaction:
            conexion.start_transaction()
        cursor.execute("INSERT INTO tbl_contactanos (nombre, telefono, correo, mensaje, fecha_envio) VALUES (%s, %s, %s, %s, %s)",(Nombre, Telefono, Correo, Descripcion, hora_str))
        conexion.commit()
        return "Se creo el contacto con exito", "exito"
    except mysql.connector.Error as err:
        conexion.rollback()
        return f"Ocurrió un error al guardar los datos: {err}", "error"    