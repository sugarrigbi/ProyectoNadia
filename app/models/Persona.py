import mysql.connector
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
from flask import flash, redirect, url_for, session, render_template
from app.utilities.Autenticador import Verificar_Rol, verificar_estado_usuario, hash_contraseña
from app.utilities.Base_Datos import Get_BaseDatos, Close_BaseDatos, Get_Errores
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate, make_msgid, formataddr

MAX_INTENTOS = 3
BLOQUEO_MINUTOS = 15
bloqueado_hasta = datetime.now() + timedelta(minutes=BLOQUEO_MINUTOS)
correo_emisor = "bot@gaialink.online"
contraseña = "1145224601Aa*"
correo_receptor1 = "administrador@gaialink.online"
Tipo_Documento_Valores2 = {
    "Cedula Ciudadania": "CC",
    "Cedula Extranjeria": "CE",
    "Pasaporte": "PA",
    "Registro Civil": "RC",
    "Tarjeta de identidad": "TI"
}
Tipo_Documento_Valores = {
    "CC": "Cedula Ciudadania",
    "CE": "Cedula Extranjeria",
    "PA": "Pasaporte",
    "RC": "Registro Civil",
    "TI": "Tarjeta de identidad"
}
class Persona:
    def __init__(self, Codigo, Tipo_Documento, Documento, Primer_Nombre,
                Segundo_Nombre, Primer_Apellido, Segundo_Apellido,
                Fecha_Nacimiento, Codigo_Adic, Edad, Direccion, Departamento,
                Ciudad, Localidad, Barrio, Numero_Contacto, Email, Usuario, Contraseña, Rol, Estado, Terminos):
        self.Codigo = Codigo
        self.Tipo_Documento = Tipo_Documento
        self.Documento = Documento
        self.Primer_Nombre = Primer_Nombre
        self.Segundo_Nombre = Segundo_Nombre
        self.Primer_Apellido = Primer_Apellido
        self.Segundo_Apellido = Segundo_Apellido
        self.Fecha_Nacimiento = Fecha_Nacimiento
        self.Codigo_Adic = Codigo_Adic
        self.Edad = Edad
        self.Direccion = Direccion
        self.Departamento = Departamento
        self.Ciudad = Ciudad
        self.Localidad = Localidad
        self.Barrio = Barrio
        self.Numero_Contacto = Numero_Contacto
        self.Email = Email
        self.Usuario = Usuario
        self.Contraseña = Contraseña
        self.Rol = Rol
        self.Estado = Estado
        self.Terminos = Terminos
    def Buscar_Persona(self):
        conexion, cursor = Get_BaseDatos()
        try:
            conexion, cursor = Get_BaseDatos()
            if conexion is None:
                return {"error": "No se pudo conectar a la base de datos"}

            cursor.execute("SELECT Id_Persona FROM tbl_persona JOIN tbl_usuario ON tbl_persona.fk_Usuario = tbl_usuario.Id_usuario WHERE tbl_persona.fk_Usuario = %s", (self.Codigo,))
            Resultado2 = cursor.fetchone()
            if not Resultado2:
                return
            self.Documento = Resultado2["Id_Persona"]

            Buscar_Codigo = self.Documento        
            cursor.execute("SELECT fk_usuario FROM tbl_persona WHERE Id_Persona = %s", (Buscar_Codigo,))
            Resultado_Usuario = cursor.fetchone()
        
            if not Resultado_Usuario:
                return
            Id_Usuario = Resultado_Usuario["fk_usuario"]

            cursor.execute("SELECT fk_estado FROM tbl_usuario WHERE Id_usuario = %s", (Id_Usuario,))
            Resultado_Estado = cursor.fetchone()
            if not Resultado_Estado:
                return None
        
            Estado_Actual = Resultado_Estado["fk_estado"]
            if Estado_Actual == "Usuario_00":
                return

            cursor.execute("""
                SELECT 
                    tbl_persona.Id_Persona, 
                    tbl_persona.fk_Tipo_documento, 
                    tbl_persona.Pri_Nom, 
                    tbl_persona.Seg_Nom, 
                    tbl_persona.Pri_Ape, 
                    tbl_persona.Seg_Ape, 
                    tbl_persona.Fecha_nacimiento, 
                    tbl_adic_persona.Id_Adic_Persona, 
                    tbl_adic_persona.Edad, 
                    tbl_adic_persona.Dirección, 
                    tbl_ciudad.Nom_ciudad, 
                    tbl_localidad.Localidad, 
                    tbl_barrio.Barrio, 
                    tbl_adic_persona.Num_Contact, 
                    tbl_adic_persona.Email, 
                    tbl_departamento.Nom_departamento,
                    tbl_usuario.Nombre,
                    tbl_usuario.Contraseña,
                    tbl_usuario.fk_rol,
                    tbl_usuario.fk_estado
                FROM tbl_adic_persona JOIN tbl_persona ON tbl_adic_persona.fk_persona = tbl_persona.Id_persona 
                JOIN tbl_tipo_documento ON tbl_persona.fk_Tipo_documento = tbl_tipo_documento.Id_Documento 
                JOIN tbl_usuario ON tbl_persona.fk_usuario = tbl_usuario.Id_usuario JOIN tbl_barrio ON tbl_adic_persona.fk_dir = tbl_barrio.Id_barrio 
                JOIN tbl_localidad ON tbl_barrio.fk_local = tbl_localidad.Id_local JOIN tbl_ciudad ON tbl_localidad.fk_ciudad = tbl_ciudad.Id_ciudad 
                JOIN tbl_departamento ON tbl_ciudad.Fk_Dep = tbl_departamento.Id_dep WHERE tbl_usuario.Id_usuario = %s
                """, (Id_Usuario,))
            Resultado = cursor.fetchone()
            if not Resultado:
                return None  

            persona_data = {
                "Codigo": Id_Usuario,
                "Tipo_Documento": Tipo_Documento_Valores.get(Resultado["fk_Tipo_documento"]),
                "Documento": Resultado["Id_Persona"],
                "Primer_Nombre": Resultado["Pri_Nom"],
                "Segundo_Nombre": Resultado["Seg_Nom"],
                "Primer_Apellido": Resultado["Pri_Ape"],
                "Segundo_Apellido": Resultado["Seg_Ape"],
                "Fecha_Nacimiento": Resultado["Fecha_nacimiento"].strftime("%d/%m/%Y") if Resultado["Fecha_nacimiento"] else "",
                "Codigo_Adic": Resultado["Id_Adic_Persona"],
                "Edad": Resultado["Edad"],
                "Direccion": Resultado["Dirección"],
                "Departamento": Resultado["Nom_departamento"],
                "Ciudad": Resultado["Nom_ciudad"],
                "Localidad": Resultado["Localidad"],
                "Barrio": Resultado["Barrio"],
                "Numero_Contacto": Resultado["Num_Contact"],
                "Email": Resultado["Email"],
                "Nombre": Resultado["Nombre"],
                "Contraseña": Resultado["Contraseña"],
                "Rol": Resultado ["fk_rol"],
                "Estado": Resultado ["fk_estado"],
                }

            conexion.commit()
            return persona_data

        except mysql.connector.Error as err:
            Get_Errores(conexion, err)
            return {"error": str(err)}

        finally:
            Close_BaseDatos(conexion, cursor) 
    def Crear_Persona(self):
        conexion, cursor = Get_BaseDatos()
        contraseña_hasheada = hash_contraseña(self.Contraseña)
        
        fecha_nacimiento = self.Fecha_Nacimiento
        fecha_nac_obj = datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
        hoy = datetime.today().date()
        edad = hoy.year - fecha_nac_obj.year
        if (hoy.month, hoy.day) < (fecha_nac_obj.month, fecha_nac_obj.day):
            edad -= 1

        def generar_id(tabla, prefijo):
            cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
            resultado = cursor.fetchone()
            count = resultado.get('COUNT(*)', 0) if resultado else 0
            return str(count + 1).zfill(3) + prefijo      
        id_rol = "Usu"
        id_activo = "usuario_01"
        id_usuario = generar_id("tbl_usuario", "USU")
        id_barrio = generar_id("tbl_barrio", "BAR")
        id_ciudad = generar_id("tbl_ciudad", "CIU")
        id_departamento = generar_id("tbl_departamento", "DEP")
        id_localidad = generar_id("tbl_localidad", "LOC")
        id_adic_persona = generar_id("tbl_adic_persona", "PAD")

        try:
            if not conexion.in_transaction:
                conexion.start_transaction()

            cursor.execute("SELECT Id_dep FROM tbl_departamento WHERE Nom_departamento = %s", (self.Departamento,))
            dep = cursor.fetchone()
            id_departamento = dep["Id_dep"] if dep else generar_id("tbl_departamento", "DEP")
            if not dep:
                cursor.execute("INSERT INTO tbl_departamento (Id_dep, Nom_departamento) VALUES (%s, %s)",(id_departamento, self.Departamento))        

            cursor.execute("SELECT Id_ciudad FROM tbl_ciudad WHERE Nom_ciudad = %s", (self.Ciudad,))
            ciu = cursor.fetchone()
            id_ciudad = ciu["Id_ciudad"] if ciu else generar_id("tbl_ciudad", "CIU")
            if not ciu:
                cursor.execute("INSERT INTO tbl_ciudad (Id_ciudad, Nom_ciudad, Fk_Dep) VALUES (%s, %s, %s)",(id_ciudad, self.Ciudad, id_departamento))

            cursor.execute("SELECT Id_local FROM tbl_localidad WHERE Localidad = %s", (self.Localidad,))
            loc = cursor.fetchone()
            id_localidad = loc["Id_local"] if loc else generar_id("tbl_localidad", "LOC")
            if not loc:
                cursor.execute("INSERT INTO tbl_localidad (Id_local, Localidad, fk_ciudad) VALUES (%s, %s, %s)",
                            (id_localidad, self.Localidad, id_ciudad))   

            cursor.execute("SELECT Id_barrio FROM tbl_barrio WHERE Barrio = %s AND fk_local = %s", (self.Barrio, id_localidad))
            bar = cursor.fetchone()
            id_barrio = bar["Id_barrio"] if bar else generar_id("tbl_barrio", "BAR")
            if not bar:
                cursor.execute("INSERT INTO tbl_barrio (Id_barrio, Barrio, fk_local) VALUES (%s, %s, %s)",
                            (id_barrio, self.Barrio, id_localidad))  

            id_usuario = generar_id("tbl_usuario", "USU")
            cursor.execute("INSERT INTO tbl_usuario (Id_usuario, Nombre, Contraseña, fk_rol, fk_estado, Intentos_fallidos) VALUES (%s, %s, %s, %s, %s, %s)", 
                        (id_usuario, self.Usuario, contraseña_hasheada, id_rol, id_activo, 0)) 

            cursor.execute("INSERT INTO tbl_persona (Id_Persona, Pri_Nom, Seg_Nom, Pri_Ape, Seg_Ape, fk_Tipo_documento, Fecha_nacimiento, fk_Usuario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                        (self.Documento, self.Primer_Nombre, self.Segundo_Nombre, self.Primer_Apellido ,self.Segundo_Apellido ,self.Tipo_Documento, self.Fecha_Nacimiento, id_usuario))

            cursor.execute("INSERT INTO tbl_adic_persona (Id_Adic_Persona, Edad, Dirección, Num_Contact, Email, fk_persona, fk_dir, Terminos_Condiciones) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                        (id_adic_persona, edad, self.Direccion, self.Numero_Contacto, self.Email, self.Documento, id_barrio, self.Terminos))   
            
            conexion.commit()
            return "Exito, usuario creado correctamente.", "exito"
        except Exception as e:
            conexion.rollback()
            return f"Ocurrió un error al guardar los datos: {e}", "error"
        finally:
            mensaje = MIMEMultipart()
            mensaje["From"] =   formataddr(("Soporte GaiaLink", correo_emisor))
            mensaje["To"] = self.Email
            mensaje["Subject"] = f"Estimado/a {self.Usuario}"
            mensaje['Date'] = formatdate(localtime=True)
            mensaje['Message-ID'] = make_msgid(domain="gaialink.online")
            cuerpo = '''
Queremos informarte que tu usuario ha sido creado exitosamente en nuestro sistema.

Si no fuiste tú quien realizó este registro, por favor comunícate de inmediato con nuestro equipo de soporte para garantizar la seguridad de tu cuenta.

Si necesitas ayuda o asistencia adicional, no dudes en escribirnos.

Atentamente,  
El equipo de soporte de GaiaLink
'''
            mensaje.attach(MIMEText(cuerpo, "plain"))

            mensaje2 = MIMEMultipart()
            mensaje2["From"] = correo_emisor
            mensaje2["To"] = correo_receptor1
            mensaje2["Subject"] = f"Estimado/a Soporte"
            cuerpo2 = f'''
Buen día,

Le informamos que un nuevo usuario ha creado una cuenta en el sistema GaiaLink, identificado con {self.Tipo_Documento} {self.Documento}.

Por favor, revise los registros de actividad y la información del usuario para garantizar la integridad y seguridad del sistema.

Para cualquier duda o requerimiento adicional, no dude en ponerse en contacto con nuestro equipo de soporte.

Atentamente,
El equipo de soporte de GaiaLink
'''
            mensaje2.attach(MIMEText(cuerpo2, "plain"))
            try:
                servidor = smtplib.SMTP_SSL("gaialink.online", 465)
                servidor.login(correo_emisor, contraseña)
                servidor.send_message(mensaje)
                servidor.send_message(mensaje2)
                servidor.quit()
                print('Correo del usuario:', self.Email)
                print("Correo enviado exitosamente")
            except Exception as e:
                print(f"Error al enviar el correo: {e}")
            Close_BaseDatos(conexion, cursor)      
    def Eliminar_Persona(self):
        conexion, cursor = Get_BaseDatos()
        Estado = "Usuario_00"

        cursor.execute("SELECT tbl_adic_persona.Email FROM tbl_adic_persona JOIN tbl_persona ON tbl_adic_persona.fk_persona = tbl_persona.Id_persona JOIN tbl_tipo_documento ON tbl_persona.fk_Tipo_documento = tbl_tipo_documento.Id_Documento JOIN tbl_usuario ON tbl_persona.fk_usuario = tbl_usuario.Id_usuario WHERE tbl_usuario.Id_usuario = %s", (self.Codigo,))
        resultado_Correo = cursor.fetchone()
        if not resultado_Correo:
            return "Correo no encontrado", "error"
        self.Email = resultado_Correo["Email"]

        cursor.execute("SELECT Nombre FROM tbl_usuario WHERE Id_usuario = %s", (self.Codigo,))
        Resultado3 = cursor.fetchone()
        if not Resultado3:
            return "persona no encontrada", "error"
        self.Usuario = Resultado3["Nombre"]

        try:
            cursor.execute("UPDATE tbl_usuario SET fk_estado = %s WHERE Id_usuario = %s",(Estado, self.Codigo))
            conexion.commit()
        except:
            conexion.rollback()
            return "no se pudo eliminar el usuario", "error"
        finally:
            mensaje = MIMEMultipart()
            mensaje["From"] = correo_emisor
            mensaje["To"] = self.Email
            mensaje["Subject"] = f"Estimado/a {self.Usuario}"
            cuerpo = '''
Queremos informarte que se ha eliminado tu cuenta de nuestro sistema.

Si no fuiste tú quien solicitó esta acción, por favor comunícate de inmediato con nuestro equipo de soporte para garantizar la seguridad de tu cuenta.

Si necesitas asistencia adicional, no dudes en escribirnos.

Atentamente,  
El equipo de soporte de GaiaLink
'''
            mensaje.attach(MIMEText(cuerpo, "plain"))

            mensaje2 = MIMEMultipart()
            mensaje2["From"] = correo_emisor
            mensaje2["To"] = correo_receptor1
            mensaje2["Subject"] = f"Estimado/a Soporte"
            cuerpo2 = f'''
Buen dia
    
Le informamos que se ha eliminado la cuenta de un usuario identificado con {self.Tipo_Documento} {self.Documento}, del sistema GaiaLink.

Si esta acción no fue realizada por usted o no estaba programada, por favor revise los registros de actividad y comuníquese con el equipo de soporte para garantizar la integridad del sistema.

Para cualquier duda o requerimiento adicional, no dude en ponerse en contacto con nosotros.

Atentamente,  
El equipo de soporte de GaiaLink
'''
            mensaje2.attach(MIMEText(cuerpo2, "plain"))

            try:
                servidor = smtplib.SMTP_SSL("gaialink.online", 465)
                servidor.login(correo_emisor, contraseña)
                servidor.send_message(mensaje)
                servidor.send_message(mensaje2)
                servidor.quit()
                print('Correo del usuario:', self.Email)
                print("Correo enviado exitosamente")
            except Exception as e:
                print(f"Error al enviar el correo: {e}")
            Close_BaseDatos(conexion, cursor)
    def Modificar_Persona(self):
        conexion, cursor = Get_BaseDatos()

        fecha_nacimiento = self.Fecha_Nacimiento
        fecha_nac_obj = datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
        hoy = datetime.today().date()
        edad = hoy.year - fecha_nac_obj.year
        if (hoy.month, hoy.day) < (fecha_nac_obj.month, fecha_nac_obj.day):
            edad -= 1

        try:
            cursor.execute("UPDATE tbl_adic_persona SET Edad = %s, Dirección = %s, Num_Contact = %s, Email = %s WHERE fk_persona = %s",(edad, self.Direccion, self.Numero_Contacto, self.Email, self.Documento))
            cursor.execute("UPDATE tbl_persona SET Pri_Nom = %s, Seg_Nom = %s, Pri_Ape = %s, Seg_Ape = %s, fk_Tipo_documento = %s, Fecha_nacimiento = %s WHERE Id_Persona = %s",(self.Primer_Nombre, self.Segundo_Nombre, self.Primer_Apellido, self.Segundo_Apellido, self.Tipo_Documento, fecha_nacimiento, self.Documento))
            cursor.execute("UPDATE tbl_usuario SET Nombre = %s WHERE Id_usuario = %s",(self.Usuario, self.Codigo))
            conexion.commit()
            return "Datos modificados con exito", "exito"
        except Exception as e:
            conexion.rollback()
            print(e)
            return f"no se pudo modificar el usuario: {e}", "error"
        finally:
            mensaje = MIMEMultipart()
            mensaje["From"] = correo_emisor
            mensaje["To"] = self.Email
            mensaje["Subject"] = f"Estimado/a {self.Usuario}"
            cuerpo = '''
Queremos informarte que los datos de tu cuenta han sido modificados exitosamente en el módulo de usuarios del sistema GaiaLink.

Si no fuiste tú quien solicitó esta acción, por favor comunícate de inmediato con nuestro equipo de soporte para garantizar la seguridad de tu cuenta.

Si necesitas asistencia adicional, no dudes en escribirnos.

Atentamente,  
El equipo de soporte de GaiaLink
'''
            mensaje.attach(MIMEText(cuerpo, "plain"))

            mensaje2 = MIMEMultipart()
            mensaje2["From"] = correo_emisor
            mensaje2["To"] = correo_receptor1
            mensaje2["Subject"] = f"Estimado/a Soporte"
            cuerpo2 = f'''
Le informamos que se ha modificado la cuenta de un usuario identificado con {self.Tipo_Documento} {self.Documento}, del sistema GaiaLink.

Si esta acción no fue realizada por usted o no estaba programada, por favor revise los registros de actividad y comuníquese con el equipo de soporte para garantizar la integridad del sistema.

Para cualquier duda o requerimiento adicional, no dude en ponerse en contacto con nosotros.

Atentamente,  
El equipo de soporte de GaiaLink
'''
            mensaje2.attach(MIMEText(cuerpo2, "plain"))

            try:
                servidor = smtplib.SMTP_SSL("gaialink.online", 465)
                servidor.login(correo_emisor, contraseña)
                servidor.send_message(mensaje)
                servidor.send_message(mensaje2)
                servidor.quit()
                print('Correo del usuario:', self.Email)
                print("Correo enviado exitosamente")
            except Exception as e:
                print(f"Error al enviar el correo: {e}")
            Close_BaseDatos(conexion, cursor) 
    def Modificar_Contraseña(self):
        conexion, cursor = Get_BaseDatos()
        contraseña_hasheada = hash_contraseña(self.Contraseña)
        
        cursor.execute("SELECT tbl_adic_persona.Email FROM tbl_adic_persona JOIN tbl_persona ON tbl_adic_persona.fk_persona = tbl_persona.Id_persona JOIN tbl_tipo_documento ON tbl_persona.fk_Tipo_documento = tbl_tipo_documento.Id_Documento JOIN tbl_usuario ON tbl_persona.fk_usuario = tbl_usuario.Id_usuario WHERE tbl_usuario.Id_usuario = %s", (self.Codigo,))
        resultado_Correo = cursor.fetchone()
        if not resultado_Correo:
            return "Correo no encontrado", "error"
        self.Email = resultado_Correo["Email"]

        cursor.execute("SELECT Nombre FROM tbl_usuario WHERE Id_usuario = %s", (self.Codigo,))
        Resultado3 = cursor.fetchone()
        if not Resultado3:
            return "persona no encontrada", "error"
        self.Usuario = Resultado3["Nombre"]

        try:
            cursor.execute("UPDATE tbl_usuario SET Contraseña = %s WHERE Id_usuario = %s",(contraseña_hasheada, self.Codigo))
            conexion.commit()
            return "Contraseña modificada con exito", "exito"
        except Exception as e:
            conexion.rollback()
            print(e)
            return f"no se pudo modificar la contraseña: {e}", "error"
        finally:
            mensaje = MIMEMultipart()
            mensaje["From"] = correo_emisor
            mensaje["To"] = self.Email
            mensaje["Subject"] = f"Estimado/a {self.Usuario}"
            cuerpo = '''
Queremos informarte que la contraseña de tu cuenta han sido modificada exitosamente en el módulo de usuarios del sistema GaiaLink.

Si no fuiste tú quien solicitó esta acción, por favor comunícate de inmediato con nuestro equipo de soporte para garantizar la seguridad de tu cuenta.

Si necesitas asistencia adicional, no dudes en escribirnos.

Atentamente,  
El equipo de soporte de GaiaLink
'''
            mensaje.attach(MIMEText(cuerpo, "plain"))

            mensaje2 = MIMEMultipart()
            mensaje2["From"] = correo_emisor
            mensaje2["To"] = correo_receptor1
            mensaje2["Subject"] = f"Estimado/a Soporte"
            cuerpo2 = f'''
Le informamos que se ha modificado la contraseña de un usuario identificado con {self.Documento}, del sistema GaiaLink.

Si esta acción no fue realizada por usted o no estaba programada, por favor revise los registros de actividad y comuníquese con el equipo de soporte para garantizar la integridad del sistema.

Para cualquier duda o requerimiento adicional, no dude en ponerse en contacto con nosotros.

Atentamente,  
El equipo de soporte de GaiaLink
'''
            mensaje2.attach(MIMEText(cuerpo2, "plain"))

            try:
                servidor = smtplib.SMTP_SSL("gaialink.online", 465)
                servidor.login(correo_emisor, contraseña)
                servidor.send_message(mensaje)
                servidor.send_message(mensaje2)
                servidor.quit()
                print('Correo del usuario:', self.Email)
                print("Correo enviado exitosamente")
            except Exception as e:
                print(f"Error al enviar el correo: {e}")
            Close_BaseDatos(conexion, cursor)                        
