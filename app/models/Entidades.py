import mysql.connector
from datetime import datetime, timedelta
from flask import flash, redirect, url_for, session, render_template
from app.utilities.Base_Datos import Get_BaseDatos, Close_BaseDatos, Get_Errores
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate, make_msgid, formataddr

Incidente_Valores = {
    "Despl": "Desplazamiento",
    "Despo": "Despojo de predios",
    "Expro": "Expropiacion",
    "Hurt": "Hurto"
}

correo_emisor = "bot@gaialink.online"
contraseña = "1145224601Aa*"
correo_receptor1 = "administrador@gaialink.online"

class Entidad():
    def __init__(self, Codigo, Nombre, Descripcion, IncidenteRelacionado, Direccion, Telefono, Web):
        self.Codigo = Codigo
        self.Nombre = Nombre
        self.Descripcion = Descripcion
        self.IncidenteRelacionado = IncidenteRelacionado
        self.Direccion = Direccion
        self.Telefono = Telefono
        self.Web = Web
    def Buscar_Entidades(self):
        conexion, cursor = Get_BaseDatos()
        Incidentes = []
        lista_fusionada = []

        cursor.execute("SELECT Id_entidad FROM prueba.tbl_entidad")
        Id_entidad = cursor.fetchall()
        if not Id_entidad:
            return "No existen entidades", "error" 

        cursor.execute("SELECT Nombre_Entidad FROM prueba.tbl_entidad")
        Nombre_Entidad = cursor.fetchall()
        if not Nombre_Entidad:
            return "No existen entidades", "error"

        cursor.execute("SELECT Descripción FROM prueba.tbl_entidad")
        Descripción = cursor.fetchall()
        if not Descripción:
            return "No existen entidades", "error"
        
        cursor.execute("SELECT Fk_Incidente FROM prueba.tbl_entidad")
        Fk_Incidente = cursor.fetchall()
        if not Fk_Incidente:
            return "No existen entidades", "error"
        
        for i in Fk_Incidente:
            convertir = i["Fk_Incidente"]
            Incidente = Incidente_Valores.get(convertir)
            if Incidente:
                Incidentes.append(Incidente)   

        cursor.execute("SELECT Direccion FROM prueba.tbl_adic_entidad")
        Direccion = cursor.fetchall()
        if not Direccion:
            return "No existen entidades", "error" 

        cursor.execute("SELECT Num_Contact FROM prueba.tbl_adic_entidad")
        Num_Contact = cursor.fetchall()
        if not Num_Contact:
            return "No existen entidades", "error" 
        
        cursor.execute("SELECT web_site FROM prueba.tbl_adic_entidad")
        web_site = cursor.fetchall()
        if not web_site:
            return "No existen entidades", "error" 

        for i in range(len(Id_entidad)):
            Entidad = {
                "Id_Entidad": Id_entidad[i]["Id_entidad"],
                "Nombre_Entidad": Nombre_Entidad[i]["Nombre_Entidad"],
                "Descripción": Descripción[i]["Descripción"],
                "Incidente": Incidentes[i],
                "Direccion": Direccion[i]["Direccion"],
                "Num_Contact": Num_Contact[i]["Num_Contact"],
                "web_site": web_site[i]["web_site"]
            }
            lista_fusionada.append(Entidad)
        Close_BaseDatos(conexion, cursor)
        return lista_fusionada
    def Buscar_Entidad(self):
        conexion, cursor = Get_BaseDatos()
        try:
            cursor.execute("""
                SELECT
                    tbl_entidad.Id_entidad,
                    tbl_entidad.Nombre_Entidad,
                    tbl_adic_entidad.Descripción,
                    tbl_incidente.Incidente,
                    tbl_adic_entidad.Direccion,
                    tbl_adic_entidad.Num_Contact,
                    tbl_adic_entidad.web_site
                FROM tbl_adic_entidad
                JOIN tbl_entidad ON tbl_adic_entidad.fk_entidad = tbl_entidad.Id_entidad
                JOIN tbl_incidente ON tbl_entidad.Fk_Incidente = tbl_incidente.Id_incidente
                WHERE tbl_entidad.Id_entidad = %s
            """,(self.Codigo, ))
            resultados = cursor.fetchone()
            if not resultados:
                return "la entidad no existe", "error" 
            entidad_datos = {
                "Codigo": resultados["Id_entidad"],
                "Nombre": resultados["Nombre_Entidad"],
                "Descripcion": resultados["Descripción"],
                "Incidente": resultados["Incidente"],
                "Direccion": resultados["Direccion"],
                "Telefono": resultados["Num_Contact"],
                "Web": resultados["web_site"]
                }
            conexion.commit()
            return entidad_datos, "exito"
        
        except mysql.connector.Error as err:
            Get_Errores(conexion, err)
            return {"error": str(err)}, "error"

        finally:
            Close_BaseDatos(conexion, cursor)
 
