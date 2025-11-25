import mysql.connector
from datetime import datetime, timedelta
from flask import flash, redirect, url_for, session, render_template
from app.utilities.Base_Datos import Get_BaseDatos, Close_BaseDatos, Get_Errores
import smtplib
from email.mime.text import MIMEText
from urllib.parse import urlparse
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

        cursor.execute("SELECT Id_entidad FROM prueba.tbl_entidad ORDER BY Id_entidad")
        Id_entidad = cursor.fetchall()
        if not Id_entidad:
            return "No existen entidades", "error" 
        cursor.execute("SELECT Nombre_Entidad FROM prueba.tbl_entidad ORDER BY Id_entidad")
        Nombre_Entidad = cursor.fetchall()
        if not Nombre_Entidad:
            return "No existen entidades", "error"

        cursor.execute("SELECT Descripción FROM prueba.tbl_adic_entidad ORDER BY fk_entidad")
        Descripción = cursor.fetchall()
        if not Descripción:
            return "No existen entidades", "error"
        
        cursor.execute("SELECT Fk_Incidente FROM prueba.tbl_entidad ORDER BY Id_entidad")
        Fk_Incidente = cursor.fetchall()
        if not Fk_Incidente:
            return "No existen entidades", "error"
        
        for i in Fk_Incidente:
            convertir = i["Fk_Incidente"]
            Incidente = Incidente_Valores.get(convertir)
            if Incidente:
                Incidentes.append(Incidente)   

        cursor.execute("SELECT Fk_Estado FROM prueba.tbl_entidad ORDER BY Id_entidad")
        Estados = cursor.fetchall()
        if not Estados:
            return "No existen entidades", "error" 

        cursor.execute("SELECT Direccion FROM prueba.tbl_adic_entidad ORDER BY fk_entidad")
        Direccion = cursor.fetchall()
        if not Direccion:
            return "No existen entidades", "error" 

        cursor.execute("SELECT Num_Contact FROM prueba.tbl_adic_entidad ORDER BY fk_entidad")
        Num_Contact = cursor.fetchall()
        if not Num_Contact:
            return "No existen entidades", "error" 
        
        cursor.execute("SELECT web_site FROM prueba.tbl_adic_entidad ORDER BY fk_entidad")
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
                "web_site": web_site[i]["web_site"],
                "Estado": Estados[i]["Fk_Estado"]
            }
            if all(Entidad.values()) and Entidad["Estado"] != "Entidad_00":
                lista_fusionada.append(Entidad)            
        Close_BaseDatos(conexion, cursor)
        return lista_fusionada
class Entidad_Admin():
    def __init__(self, Codigo, Nombre, Descripcion, IncidenteRelacionado, Direccion, Telefono, Web, Estado):
        self.Codigo = Codigo
        self.Nombre = Nombre
        self.Descripcion = Descripcion
        self.IncidenteRelacionado = IncidenteRelacionado
        self.Direccion = Direccion
        self.Telefono = Telefono
        self.Web = Web
        self.Estado = Estado
    def Buscar_Entidades_Admin(self):
        conexion, cursor = Get_BaseDatos()
        Incidentes = []
        lista_fusionada = []

        cursor.execute("SELECT Id_entidad FROM prueba.tbl_entidad ORDER BY Id_entidad")
        Id_entidad = cursor.fetchall()
        if not Id_entidad:
            return "No existen entidades", "error" 
        cursor.execute("SELECT Nombre_Entidad FROM prueba.tbl_entidad ORDER BY Id_entidad")
        Nombre_Entidad = cursor.fetchall()
        if not Nombre_Entidad:
            return "No existen entidades", "error"

        cursor.execute("SELECT Descripción FROM prueba.tbl_adic_entidad ORDER BY Id_entidad")
        Descripción = cursor.fetchall()
        if not Descripción:
            return "No existen entidades", "error"
        
        cursor.execute("SELECT Fk_Incidente FROM prueba.tbl_entidad ORDER BY Id_entidad")
        Fk_Incidente = cursor.fetchall()
        if not Fk_Incidente:
            return "No existen entidades", "error"
        
        for i in Fk_Incidente:
            convertir = i["Fk_Incidente"]
            Incidente = Incidente_Valores.get(convertir)
            if Incidente:
                Incidentes.append(Incidente)   

        cursor.execute("SELECT Direccion FROM prueba.tbl_adic_entidad ORDER BY Id_entidad")
        Direccion = cursor.fetchall()
        if not Direccion:
            return "No existen entidades", "error" 

        cursor.execute("SELECT Num_Contact FROM prueba.tbl_adic_entidad ORDER BY Id_entidad")
        Num_Contact = cursor.fetchall()
        if not Num_Contact:
            return "No existen entidades", "error" 
        
        cursor.execute("SELECT web_site FROM prueba.tbl_adic_entidad ORDER BY Id_entidad")
        web_site = cursor.fetchall()
        if not web_site:
            return "No existen entidades", "error" 
        
        cursor.execute("SELECT Fk_Estado FROM prueba.tbl_entidad ORDER BY Id_entidad")
        Estado = cursor.fetchall()
        if not Estado:
            return "No existen entidades", "error"

        for i in range(len(Id_entidad)):
            Entidad = {
                "Id_Entidad": Id_entidad[i]["Id_entidad"],
                "Nombre_Entidad": Nombre_Entidad[i]["Nombre_Entidad"],
                "Descripción": Descripción[i]["Descripción"],
                "Incidente": Incidentes[i],
                "Direccion": Direccion[i]["Direccion"],
                "Num_Contact": Num_Contact[i]["Num_Contact"],
                "web_site": web_site[i]["web_site"],
                "Estado": Estado[i]["Estado"]
            }
            lista_fusionada.append(Entidad)
        Close_BaseDatos(conexion, cursor)
        return lista_fusionada
    def Buscar_Entidad_Admin(self):
        conexion, cursor = Get_BaseDatos()

        cursor.execute("SELECT Nombre_Entidad FROM prueba.tbl_entidad WHERE Id_entidad = %s",(self.Codigo,))
        Nombre_Entidad = cursor.fetchone()
        if not Nombre_Entidad:
            return "La entidad no existe", "error"
        
        cursor.execute("SELECT Incidente FROM prueba.tbl_incidente JOIN tbl_entidad ON tbl_incidente.Id_incidente = tbl_entidad.Fk_Incidente WHERE Id_entidad = %s",(self.Codigo,))
        Incidente_Entidad = cursor.fetchone()
        if not Incidente_Entidad:
            return "La entidad no existe", "error"
        
        cursor.execute("SELECT Fk_Estado FROM prueba.tbl_entidad WHERE Id_entidad = %s",(self.Codigo,))
        Estado_Entidad = cursor.fetchone()
        if not Estado_Entidad:
            return "La entidad no existe", "error"
        
        cursor.execute("SELECT Direccion FROM prueba.tbl_adic_entidad JOIN tbl_entidad ON tbl_adic_entidad.fk_entidad = tbl_entidad.Id_entidad WHERE Id_entidad = %s",(self.Codigo,))
        Direccion_Entidad = cursor.fetchone()
        if not Direccion_Entidad:
            return "La entidad no existe", "error"
        
        cursor.execute("SELECT Num_Contact FROM prueba.tbl_adic_entidad JOIN tbl_entidad ON tbl_adic_entidad.fk_entidad = tbl_entidad.Id_entidad WHERE Id_entidad = %s",(self.Codigo,))
        Telefono_Entidad = cursor.fetchone()
        if not Telefono_Entidad:
            return "La entidad no existe", "error"
        
        cursor.execute("SELECT web_site FROM prueba.tbl_adic_entidad JOIN tbl_entidad ON tbl_adic_entidad.fk_entidad = tbl_entidad.Id_entidad WHERE Id_entidad = %s",(self.Codigo,))
        Web_Entidad = cursor.fetchone()
        if not Web_Entidad:
            return "La entidad no existe", "error"
        
        cursor.execute("SELECT Descripción FROM prueba.tbl_adic_entidad JOIN tbl_entidad ON tbl_adic_entidad.fk_entidad = tbl_entidad.Id_entidad WHERE Id_entidad = %s",(self.Codigo,))
        Descripción_Entidad = cursor.fetchone()
        if not Descripción_Entidad:
            return "La entidad no existe", "error"
        Entidad = {
            "Codigo_Entidad": self.Codigo,
            "Nombre_Entidad": Nombre_Entidad["Nombre_Entidad"],
            "Incidente_Entidad": Incidente_Entidad["Incidente"],
            "Estado_Entidad": Estado_Entidad["Fk_Estado"],
            "Direccion_Entidad": Direccion_Entidad["Direccion"],
            "Telefono_Entidad": Telefono_Entidad["Num_Contact"],
            "Web_Entidad": Web_Entidad["web_site"],
            "Descripción_Entidad": Descripción_Entidad["Descripción"]
        }
        Close_BaseDatos(conexion, cursor)
        return Entidad
    def Crear_Entidad_Admin(self):
        conexion, cursor = Get_BaseDatos()

        def generar_id(tabla, prefijo):
            cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
            resultado = cursor.fetchone()
            count = resultado.get('COUNT(*)', 0) if resultado else 0
            return str(count + 1).zfill(3) + prefijo     
        id_activo = "Entidad_01"
        id_Entidad = generar_id("tbl_entidad", "ENT")
        id_Adic_Entidad = generar_id("tbl_adic_entidad", "ENA")   
        try:
            if not conexion.in_transaction:
                conexion.start_transaction()

            def es_url(url: str) -> bool:
                try:
                    resultado = urlparse(url)
                    return resultado.scheme in ("http", "https") and bool(resultado.netloc)
                except:
                    return False

            if es_url(self.Web) == False:
                return "Error, la web no es valida", "error"
            
            if len(self.Telefono) < 10:
                return "Error, el telefono no es valido", "error"
                

            cursor.execute("INSERT INTO tbl_entidad (Id_entidad, Nombre_Entidad, Fk_Incidente, Fk_Estado) VALUES (%s, %s, %s, %s)",(id_Entidad, self.Nombre, self.IncidenteRelacionado, id_activo))           
            cursor.execute("INSERT INTO tbl_adic_entidad (Id_Adic_Entidad, Direccion, Num_Contact, web_site, fk_entidad, Descripción) VALUES (%s, %s, %s, %s, %s, %s)",(id_Adic_Entidad, self.Direccion, self.Telefono, self.Web, id_Entidad, self.Descripcion))
            conexion.commit()
            return "Exito, entidad creada correctamente.", "exito"
        except Exception as e:
            conexion.rollback()
            print(e)
            return f"Ocurrió un error al guardar los datos: {e}", "error"
        finally:
            mensaje = MIMEMultipart()
            mensaje["From"] =   formataddr(("Soporte GaiaLink", correo_emisor))
            mensaje["To"] = correo_receptor1
            mensaje["Subject"] = f"Estimado/a Administrador"
            mensaje['Date'] = formatdate(localtime=True)
            mensaje['Message-ID'] = make_msgid(domain="gaialink.online")
            cuerpo = f'''
Queremos informarte que la entidad {id_Entidad} ha sido creada exitosamente por parte de un administrador del sistema.

Si no fuiste tú quien solicito este registro, por favor comunícate de inmediato con nuestro equipo de soporte.

Si necesitas ayuda o asistencia adicional, no dudes en escribirnos.

Atentamente,  
El equipo de soporte de GaiaLink
'''
            mensaje.attach(MIMEText(cuerpo, "plain"))

            try:
                servidor = smtplib.SMTP_SSL("gaialink.online", 465)
                servidor.login(correo_emisor, contraseña)
                servidor.send_message(mensaje)
                servidor.quit()
            except Exception as e:
                print(f"Error al enviar el correo: {e}")
            Close_BaseDatos(conexion, cursor)
    def Modificar_Entidad_Admin(self):
        conexion, cursor = Get_BaseDatos()
        try:
            if not conexion.in_transaction:
                conexion.start_transaction()

            def es_url(url: str) -> bool:
                try:
                    resultado = urlparse(url)
                    return resultado.scheme in ("http", "https") and bool(resultado.netloc)
                except:
                    return False

            if es_url(self.Web) == False:
                return "Error, la web no es valida", "error"    
            
            if len(self.Telefono) < 10:
                return "Error, el telefono no es valido", "error" 

            cursor.execute("UPDATE tbl_entidad SET Nombre_Entidad = %s, Fk_Incidente = %s, Fk_Estado = %s WHERE Id_entidad = %s",(self.Nombre, self.IncidenteRelacionado, self.Estado, self.Codigo))           
            cursor.execute("UPDATE tbl_adic_entidad SET Direccion = %s, Num_Contact = %s, web_site = %s, Descripción = %s WHERE fk_entidad = %s",(self.Direccion, self.Telefono, self.Web, self.Descripcion, self.Codigo))
            conexion.commit()
            return "Exito, entidad modificada correctamente.", "exito"
        except Exception as e:
            conexion.rollback()
            print(e)
            return f"Ocurrió un error al modificar los datos: {e}", "error"
        finally:
            mensaje = MIMEMultipart()
            mensaje["From"] =   formataddr(("Soporte GaiaLink", correo_emisor))
            mensaje["To"] = correo_receptor1
            mensaje["Subject"] = f"Estimado/a Administrador"
            mensaje['Date'] = formatdate(localtime=True)
            mensaje['Message-ID'] = make_msgid(domain="gaialink.online")
            cuerpo = f'''
Queremos informarte que la entidad {self.Codigo} ha sido modificada exitosamente por parte de un administrador del sistema.

Si no fuiste tú quien solicito este registro, por favor comunícate de inmediato con nuestro equipo de soporte.

Si necesitas ayuda o asistencia adicional, no dudes en escribirnos.

Atentamente,  
El equipo de soporte de GaiaLink
'''
            mensaje.attach(MIMEText(cuerpo, "plain"))

            try:
                servidor = smtplib.SMTP_SSL("gaialink.online", 465)
                servidor.login(correo_emisor, contraseña)
                servidor.send_message(mensaje)
                servidor.quit()
            except Exception as e:
                print(f"Error al enviar el correo: {e}")
            Close_BaseDatos(conexion, cursor)
    def Eliminar_Entidad_Admin(self):
        conexion, cursor = Get_BaseDatos()
        Estado_Eliminado = "Entidad_00"
        try:
            if not conexion.in_transaction:
                conexion.start_transaction()
            cursor.execute("UPDATE tbl_entidad SET Fk_Estado = %s WHERE Id_entidad = %s",(Estado_Eliminado, self.Codigo))
            conexion.commit()
            return "Exito, entidad eliminada correctamente.", "exito"
        except Exception as e:
            print(e)
            return f"Ocurrió un error al eliminar los datos: {e}", "error"
        finally:
            mensaje = MIMEMultipart()
            mensaje["From"] =   formataddr(("Soporte GaiaLink", correo_emisor))
            mensaje["To"] = correo_receptor1
            mensaje["Subject"] = f"Estimado/a Administrador"
            mensaje['Date'] = formatdate(localtime=True)
            mensaje['Message-ID'] = make_msgid(domain="gaialink.online")
            cuerpo = f'''
Queremos informarte que la entidad {self.Codigo} ha sido eliminada exitosamente por parte de un administrador del sistema.

Si no fuiste tú quien solicito este registro, por favor comunícate de inmediato con nuestro equipo de soporte.

Si necesitas ayuda o asistencia adicional, no dudes en escribirnos.

Atentamente,  
El equipo de soporte de GaiaLink
'''
            mensaje.attach(MIMEText(cuerpo, "plain"))

            try:
                servidor = smtplib.SMTP_SSL("gaialink.online", 465)
                servidor.login(correo_emisor, contraseña)
                servidor.send_message(mensaje)
                servidor.quit()
            except Exception as e:
                print(f"Error al enviar el correo: {e}")
            Close_BaseDatos(conexion, cursor)        