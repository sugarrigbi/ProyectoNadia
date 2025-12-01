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
Estado_Valores = {
    "Caso_00": "Caso Pendiente",
    "Caso_01": "Caso Activo",
    "Caso_02": "Caso Finalizado",
    "Caso_03": "Caso Eliminado"
}
correo_emisor = "bot@gaialink.online"
contraseña = "1145224601Aa*"
correo_receptor1 = "administrador@gaialink.online"

class Caso: 
    def __init__(self, Nombre, Codigo, Fecha, Descripcion, Personas_Afectadas, Usuario, incidente, departamento, tipo_caso, estado):
        self.Nombre = Nombre
        self.Codigo = Codigo
        self.Fecha = Fecha
        self.Descripcion = Descripcion
        self.Personas_Afectadas = Personas_Afectadas
        self.Usuario = Usuario
        self.incidente = incidente
        self.departamento = departamento
        self.tipo_caso = tipo_caso
        self.estado = estado
    def Crear_Caso(self, Datos):
        conexion, cursor = Get_BaseDatos()
        usuario = session["username"]
        id_usuario = session["usuario_id"]

        fecha_antes = Datos["Fecha_Incidente"]
        fecha = datetime.strptime(fecha_antes, "%Y-%m-%d").date()

        cursor.execute("SELECT tbl_adic_persona.Email FROM tbl_usuario JOIN tbl_persona ON tbl_usuario.Id_usuario = tbl_persona.fk_Usuario JOIN tbl_adic_persona on tbl_persona.Id_Persona = tbl_adic_persona.fk_persona Where tbl_usuario.Id_usuario = %s", (id_usuario,))
        Correo = cursor.fetchone()
        if not Correo:
            return "No se encontro el Correo", "error"

        def generar_id(tabla, prefijo, longitud):
            cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
            resultado = cursor.fetchone()
            count = resultado.get('COUNT(*)', 0) if resultado else 0
            return str(count + 1).zfill(longitud) + prefijo      
        
        Id_Caso_Incidente = generar_id("tbl_caso", "CAD", longitud=3)
        radicado = generar_id("tbl_num_caso", "R", longitud=6)
        id_entidad = generar_id("tbl_num_caso", "NUC", longitud=3)
        id_caso = "Caso"

        cursor.execute("SELECT id_usuario FROM tbl_usuario WHERE Nombre = %s", (usuario,))
        resultado_usuario = cursor.fetchone()
        print("Usuario en sesión:", usuario)
        if not resultado_usuario:
            return "El usuario no se encontro", "error"
        
        id_estado = "Caso_00"
        id_departamento = "001DEP"

        try:
            if not conexion.in_transaction:
                conexion.start_transaction()

            cursor.execute("INSERT INTO tbl_caso (Id_Caso_Incidente, Fecha, Descripción, Personas_Afectadas, Fk_Usuario, Fk_Incidente, Fk_Dep, Fk_Tipo_Caso, Fk_Estado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (Id_Caso_Incidente, fecha, Datos["Descripcion"], Datos["Personas_Afectadas"], id_usuario, Datos["Tipo_Incidente"], id_departamento, id_caso, id_estado))
            cursor.execute("INSERT INTO tbl_num_caso (Id_num_caso, Radicado, Fk_Caso) VALUES (%s, %s, %s)", (id_entidad, radicado, Id_Caso_Incidente)) 
            conexion.commit()
            return "Caso creado con exito", "exito"
        except mysql.connector.Error as err:
            conexion.rollback()
            return f"Ocurrio un error al almacenar los datos: {err}", "error"
        finally:
            mensaje = MIMEMultipart()
            mensaje["From"] =   formataddr(("Soporte GaiaLink", correo_emisor))
            mensaje["To"] = Correo["Email"]
            mensaje["Subject"] = f"Confirmación de Generación de Caso: {radicado}"
            mensaje['Date'] = formatdate(localtime=True)
            mensaje['Message-ID'] = make_msgid(domain="gaialink.online")
            cuerpo = f"""
Estimado/a {usuario},

Te confirmamos que tu solicitud ha sido recibida correctamente.
Un ticket ha sido generado con el ID: {radicado}.

Nuestro equipo está trabajando en tu solicitud y te contactará en breve para resolver tu problema.

Si necesitas más detalles sobre el estado de tu ticket, puedes seguirlo a través de nuestro sistema o contactar a soporte.
Gracias por confiar en nosotros.

Atentamente,  
El equipo de soporte de GaiaLink
"""
            mensaje.attach(MIMEText(cuerpo, "plain"))

            mensaje2 = MIMEMultipart()
            mensaje2["From"] =   formataddr(("Soporte GaiaLink", correo_emisor))
            mensaje2["To"] = correo_receptor1
            mensaje2["Subject"] = f"Caso creado: {radicado}"
            mensaje2['Date'] = formatdate(localtime=True)
            mensaje2['Message-ID'] = make_msgid(domain="gaialink.online")
            cuerpo2 = f"""
Estimado miembro del equipo de soporte,

Se ha generado un nuevo caso con el ID: {radicado}, registrado por el usuario {usuario}.

Por favor, revisa los detalles en la plataforma y procede con la atención correspondiente.

Atentamente,  
Sistema de notificaciones de GaiaLink
"""
            mensaje2.attach(MIMEText(cuerpo2, "plain"))
            try:
                servidor = smtplib.SMTP_SSL("gaialink.online", 465)
                servidor.login(correo_emisor, contraseña)
                servidor.send_message(mensaje)
                servidor.send_message(mensaje2)
                servidor.quit()
            except Exception as e:
                print(f"Error al enviar el correo: {e}")
            Close_BaseDatos(conexion, cursor)        
    def Buscar_Casos(self, Nombre):
        conexion, cursor = Get_BaseDatos()
        Numeros = []
        Estados = []
        Incidentes = []
        lista_fusionada = []

        cursor.execute("SELECT Id_usuario FROM prueba.tbl_usuario WHERE Nombre = %s", (Nombre,))
        id_usuario = cursor.fetchone()
        if not id_usuario:
            return "El usuario no existe", "error"
        id_usuario = id_usuario["Id_usuario"]
        
        cursor.execute("SELECT Id_Caso_Incidente FROM prueba.tbl_caso WHERE Fk_Usuario = %s ORDER BY Id_Caso_Incidente", (id_usuario,))
        casos = cursor.fetchall()
        if not casos:
            Close_BaseDatos(conexion, cursor)
            return "No existen casos", "error"
        
        for i in casos:
            id_caso = i["Id_Caso_Incidente"]
            cursor.execute("SELECT Radicado FROM tbl_num_caso WHERE Fk_Caso = %s", (id_caso,))
            radicado = cursor.fetchone()
            if radicado:
                Numeros.append(radicado)

        cursor.execute("SELECT Fecha FROM prueba.tbl_caso WHERE Fk_Usuario = %s ORDER BY Id_Caso_Incidente", (id_usuario,))
        Fecha = cursor.fetchall()

        cursor.execute("SELECT Descripción FROM prueba.tbl_caso WHERE Fk_Usuario = %s ORDER BY Id_Caso_Incidente", (id_usuario,))
        Descripción = cursor.fetchall()

        cursor.execute("SELECT Personas_Afectadas FROM prueba.tbl_caso WHERE Fk_Usuario = %s ORDER BY Id_Caso_Incidente", (id_usuario,))
        Personas_Afectadas = cursor.fetchall()

        cursor.execute("SELECT Nombre FROM prueba.tbl_usuario WHERE Id_usuario = %s", (id_usuario,))
        Nombre = cursor.fetchall()

        cursor.execute("SELECT Fk_Incidente FROM prueba.tbl_caso WHERE Fk_Usuario = %s ORDER BY Id_Caso_Incidente", (id_usuario,))
        Fk_Incidente = cursor.fetchall()
        for i in Fk_Incidente:
            convertir = i["Fk_Incidente"]
            Incidente = Incidente_Valores.get(convertir)
            if Incidente:
                Incidentes.append(Incidente)            

        query = """
            SELECT tbl_departamento.Nom_departamento 
            FROM tbl_caso 
            JOIN tbl_departamento on tbl_caso.Fk_Dep = tbl_departamento.Id_dep
            WHERE Fk_Usuario = %s
        """
        cursor.execute(query, (id_usuario,))
        Departamento = cursor.fetchall()  

        cursor.execute("SELECT Fk_Estado FROM prueba.tbl_caso WHERE Fk_Usuario = %s  ORDER BY Id_Caso_Incidente", (id_usuario,))
        Fk_Estado = cursor.fetchall()     
        for i in Fk_Estado:
            convertir = i["Fk_Estado"]
            Estado = Estado_Valores.get(convertir)
            if Estado:
                Estados.append(Estado)

        for i in range(len(Numeros)):
            try:
                if (i < len(Fecha) and i < len(Descripción) and i < len(Personas_Afectadas) and i < len(Incidentes) and i < len(Departamento) and i < len(Estados)):                
                    caso = {
                        "Radicado": Numeros[i]["Radicado"],
                        "Fecha": Fecha[i]["Fecha"],
                        "Descripción": Descripción[i]["Descripción"],
                        "Personas_Afectadas": Personas_Afectadas[i]["Personas_Afectadas"],
                        "Nombre": Nombre[0]["Nombre"],
                        "Incidente": Incidentes[i],
                        "Departamento": Departamento[i]["Nom_departamento"],
                        "Estado": Estados[i]
                    }
                if all(caso.values()) and caso["Radicado"]:
                    lista_fusionada.append(caso)                    
            except Exception as e:
                print(f"⚠️ Error procesando caso {i}: {e}")
                continue                    
        Close_BaseDatos(conexion, cursor)
        print(lista_fusionada[1]["Radicado"])
        print(lista_fusionada[1]["Fecha"])
        print(lista_fusionada[1]["Descripción"])
        print(lista_fusionada[1]["Personas_Afectadas"])
        print(lista_fusionada[1]["Nombre"])
        print(lista_fusionada[1]["Incidente"])
        print(lista_fusionada[1]["Departamento"])
        print(lista_fusionada[1]["Estado"])
        return lista_fusionada
class Caso_Admin:
    def __init__(self, Codigo, Fecha, Descripcion, Personas_Afectadas, Direccion, Usuario, incidente, departamento, tipo_caso, estado, Radicado):
        self.Codigo = Codigo
        self.Fecha = Fecha
        self.Descripcion = Descripcion
        self.Personas_Afectadas = Personas_Afectadas
        self.Usuario = Usuario
        self.Direccion = Direccion
        self.incidente = incidente
        self.departamento = departamento
        self.tipo_caso = tipo_caso
        self.estado = estado
        self.Radicado = Radicado
    def Buscar_Caso_Admin(self):
        conexion, cursor = Get_BaseDatos()
        Numeros = []
        Usuarios = []
        Estados = []
        Departamentos = []
        Incidentes = []
        lista_fusionada = []

        cursor.execute("SELECT Id_Caso_Incidente FROM prueba.tbl_caso JOIN tbl_num_caso ON tbl_num_caso.Fk_Caso = Id_Caso_Incidente WHERE Radicado = %s", (self.Radicado,))
        casos = cursor.fetchall()
        if not casos:
            Close_BaseDatos(conexion, cursor)
            return "No existen casos", "error"

        cursor.execute("SELECT Fecha FROM prueba.tbl_caso JOIN tbl_num_caso ON tbl_num_caso.Fk_Caso = Id_Caso_Incidente WHERE Radicado = %s", (self.Radicado,))
        fechas = cursor.fetchall()
        if not fechas:
            Close_BaseDatos(conexion, cursor)
            return "No existen casos", "error"

        cursor.execute("SELECT Descripción FROM prueba.tbl_caso JOIN tbl_num_caso ON tbl_num_caso.Fk_Caso = Id_Caso_Incidente WHERE Radicado = %s", (self.Radicado,))
        descripciones = cursor.fetchall()
        if not descripciones:
            Close_BaseDatos(conexion, cursor)
            return "No existen casos", "error"

        cursor.execute("SELECT Personas_Afectadas FROM prueba.tbl_caso JOIN tbl_num_caso ON tbl_num_caso.Fk_Caso = Id_Caso_Incidente WHERE Radicado = %s", (self.Radicado,))
        personas = cursor.fetchall()
        if not personas:
            Close_BaseDatos(conexion, cursor)
            return "No existen casos", "error"
        
        cursor.execute("SELECT Id_usuario FROM prueba.tbl_usuario JOIN tbl_caso ON tbl_caso.Fk_Usuario = Id_usuario JOIN tbl_num_caso ON tbl_num_caso.Fk_Caso = Id_Caso_Incidente WHERE Radicado = %s", (self.Radicado,))
        usuarios = cursor.fetchall()
        if usuarios:
            Usuarios.append(usuarios) 
        
        cursor.execute("SELECT Incidente FROM prueba.tbl_incidente JOIN tbl_caso ON tbl_caso.Fk_Incidente = Id_incidente JOIN tbl_num_caso ON tbl_num_caso.Fk_Caso = Id_Caso_Incidente WHERE Radicado = %s", (self.Radicado,))
        Fk_Incidente = cursor.fetchall()
        if Fk_Incidente:
            Incidentes.append(Fk_Incidente)

        cursor.execute("SELECT Direccion FROM prueba.tbl_caso JOIN tbl_num_caso ON tbl_num_caso.Fk_Caso = Id_Caso_Incidente WHERE Radicado = %s", (self.Radicado,))
        departamento = cursor.fetchall()
        if not departamento:
            Close_BaseDatos(conexion, cursor)
            return "No existen casos", "error"

        cursor.execute("SELECT Id_estado FROM prueba.tbl_estado JOIN tbl_caso ON tbl_caso.Fk_Estado = Id_estado JOIN tbl_num_caso ON tbl_num_caso.Fk_Caso = Id_Caso_Incidente WHERE Radicado = %s", (self.Radicado,))
        estado_name = cursor.fetchone()
        if estado_name:
            Estados.append(estado_name)

        radicados = self.Radicado
        if not radicados:
            Close_BaseDatos(conexion, cursor)
            return "No existen casos", "error"

        try:                
            caso = {
                "Codigo": casos[0]["Id_Caso_Incidente"],
                "Fecha": fechas[0]["Fecha"].strftime("%Y-%m-%d"),
                "Descripcion": descripciones[0]["Descripción"],
                "Persona": personas[0]["Personas_Afectadas"],
                "Id_usuario": Usuarios[0][0]["Id_usuario"],
                "Incidente": Incidentes[0][0]["Incidente"],
                "Departamento": departamento[0]["Direccion"],
                "Estado": Estados[0]["Id_estado"],
                "Radicado": radicados
            }
            if all(caso.values()):
                lista_fusionada.append(caso)
        except Exception as e:
            return f"⚠️ Error procesando caso: {e}"
        Close_BaseDatos(conexion, cursor)
        return lista_fusionada
    def Buscar_Casos_Admin(self):
        conexion, cursor = Get_BaseDatos()
        Numeros = []
        Usuarios = []
        Estados = []
        Departamentos = []
        Incidentes = []
        lista_fusionada = []

        cursor.execute("SELECT Id_Caso_Incidente FROM prueba.tbl_caso ORDER BY Id_Caso_Incidente")
        casos = cursor.fetchall()
        if not casos:
            Close_BaseDatos(conexion, cursor)
            return "No existen casos", "error"

        cursor.execute("SELECT Fecha FROM prueba.tbl_caso ORDER BY Id_Caso_Incidente")
        fechas = cursor.fetchall()
        if not fechas:
            Close_BaseDatos(conexion, cursor)
            return "No existen casos", "error"

        cursor.execute("SELECT Descripción FROM prueba.tbl_caso ORDER BY Id_Caso_Incidente")
        descripciones = cursor.fetchall()
        if not descripciones:
            Close_BaseDatos(conexion, cursor)
            return "No existen casos", "error"

        cursor.execute("SELECT Personas_Afectadas FROM prueba.tbl_caso ORDER BY Id_Caso_Incidente")
        personas = cursor.fetchall()
        if not personas:
            Close_BaseDatos(conexion, cursor)
            return "No existen casos", "error"
        
        cursor.execute("SELECT Fk_Usuario FROM prueba.tbl_caso ORDER BY Id_Caso_Incidente")
        usuarios = cursor.fetchall()
        for i in usuarios:
            cursor.execute("SELECT Nombre FROM prueba.tbl_usuario WHERE Id_usuario = %s", (i["Fk_Usuario"],))
            nombre = cursor.fetchone()
            if nombre:
                Usuarios.append(nombre) 
        
        cursor.execute("SELECT Fk_Incidente FROM prueba.tbl_caso ORDER BY Id_Caso_Incidente")
        Fk_Incidente = cursor.fetchall()
        for i in Fk_Incidente:
            convertir = i["Fk_Incidente"]
            Incidente = Incidente_Valores.get(convertir)
            if Incidente:
                Incidentes.append(Incidente)

        cursor.execute("SELECT Direccion FROM prueba.tbl_caso ORDER BY Id_Caso_Incidente")
        departamento = cursor.fetchall()
        if not departamento:
            Close_BaseDatos(conexion, cursor)
            return "No existen casos", "error"

        cursor.execute("SELECT Fk_Estado FROM prueba.tbl_caso ORDER BY Id_Caso_Incidente")
        estado = cursor.fetchall()
        for i in estado:
            cursor.execute("SELECT Estado FROM prueba.tbl_estado WHERE Id_estado = %s", (i["Fk_Estado"],))
            estado_name = cursor.fetchone()
            if estado_name:
                Estados.append(estado_name)

        cursor.execute("SELECT Radicado FROM prueba.tbl_num_caso ORDER BY Fk_Caso")
        radicados = cursor.fetchall()
        if not radicados:
            Close_BaseDatos(conexion, cursor)
            return "No existen casos", "error"

        for i in range(len(casos)):
            try:
                if (i < len(fechas) and i < len(descripciones) and i < len(personas) and i < len(Usuarios) and i < len(Incidentes) and i < len(departamento) and i < len(Estados) and i < len(radicados)):                
                    caso = {
                        "Codigo": casos[i]["Id_Caso_Incidente"],
                        "Fecha": fechas[i]["Fecha"],
                        "Descripcion": descripciones[i]["Descripción"],
                        "Persona": personas[i]["Personas_Afectadas"],
                        "Nombre": Usuarios[i]["Nombre"],
                        "Incidente": Incidentes[i],
                        "Departamento": departamento[i]["Direccion"],
                        "Estado": Estados[i]["Estado"],
                        "Radicado": radicados[i]["Radicado"]
                    }
                    print(caso["Departamento"])
                if all(caso.values()) and caso["Estado"] != "Caso Eliminado":
                    lista_fusionada.append(caso)
            except Exception as e:
                print(f"⚠️ Error procesando caso {i}: {e}")
                continue                    
        Close_BaseDatos(conexion, cursor)
        return lista_fusionada       
    def Crear_Caso_Admin(self):
        conexion, cursor = Get_BaseDatos()
        id_usuario = self.Usuario
        fecha_antes = self.Fecha
        fecha = datetime.strptime(fecha_antes, "%Y-%m-%d").date()
        id_departamento = "001DEP"
        id_caso = "Caso"

        hoy = datetime.today()
        Fecha2 = datetime.strptime(self.Fecha, "%Y-%m-%d")

        if Fecha2 > hoy:
            return "El caso no puede ocurrir en el futuro", "error"

        cursor.execute("SELECT tbl_adic_persona.Email FROM tbl_usuario JOIN tbl_persona ON tbl_usuario.Id_usuario = tbl_persona.fk_Usuario JOIN tbl_adic_persona on tbl_persona.Id_Persona = tbl_adic_persona.fk_persona Where tbl_usuario.Id_usuario = %s", (id_usuario,))
        Correo = cursor.fetchone()      
        if not Correo:
            return "No se encontro el Usuario", "error"      

        def generar_id(tabla, prefijo, longitud):
            cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
            resultado = cursor.fetchone()
            count = resultado.get('COUNT(*)', 0) if resultado else 0
            return str(count + 1).zfill(longitud) + prefijo      
        
        cursor.execute("SELECT Nombre FROM tbl_usuario WHERE id_usuario = %s", (id_usuario, ))
        Nombre_Usuario = cursor.fetchone()
        if not Nombre_Usuario:
            return "El usuario no se encontro", "error"     

        Id_Caso_Incidente = generar_id("tbl_caso", "CAD", longitud=3)
        radicado = generar_id("tbl_num_caso", "R", longitud=6)
        id_entidad = generar_id("tbl_num_caso", "NUC", longitud=3)    
        try:
            if not conexion.in_transaction:
                conexion.start_transaction()
            cursor.execute("INSERT INTO tbl_caso (Id_Caso_Incidente, Fecha, Descripción, Personas_Afectadas, Direccion, Fk_Usuario, Fk_Incidente, Fk_Dep, Fk_Tipo_Caso, Fk_Estado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (Id_Caso_Incidente, fecha, self.Descripcion, self.Personas_Afectadas, self.Direccion, id_usuario, self.incidente, id_departamento, id_caso, self.estado))
            cursor.execute("INSERT INTO tbl_num_caso (Id_num_caso, Radicado, Fk_Caso) VALUES (%s, %s, %s)", (id_entidad, radicado, Id_Caso_Incidente)) 
            conexion.commit()
            return "Caso creado con exito", "exito"
        except Exception as e:
            conexion.rollback()
            return f"Ocurrio un error al almacenar los datos: {e}", "error"             
        finally:
            mensaje = MIMEMultipart()
            mensaje["From"] =   formataddr(("Soporte GaiaLink", correo_emisor))
            mensaje["To"] = Correo["Email"]
            mensaje["Subject"] = f"Confirmación de Generación de Caso: {radicado}"
            mensaje['Date'] = formatdate(localtime=True)
            mensaje['Message-ID'] = make_msgid(domain="gaialink.online")
            cuerpo = f"""
Estimado/a {Nombre_Usuario},

Te confirmamos que tu solicitud ha sido recibida correctamente.
Un ticket ha sido generado por un admin asociado a tu cuenta con el ID: {radicado}.

Nuestro equipo está trabajando en tu solicitud y te contactará en breve para resolver tu problema.

Si necesitas más detalles sobre el estado de tu ticket, puedes seguirlo a través de nuestro sistema o contactar a soporte.
Gracias por confiar en nosotros.

Atentamente,  
El equipo de soporte de GaiaLink
"""
            mensaje.attach(MIMEText(cuerpo, "plain"))

            mensaje2 = MIMEMultipart()
            mensaje2["From"] =   formataddr(("Soporte GaiaLink", correo_emisor))
            mensaje2["To"] = correo_receptor1
            mensaje2["Subject"] = f"Caso creado: {radicado}"
            mensaje2['Date'] = formatdate(localtime=True)
            mensaje2['Message-ID'] = make_msgid(domain="gaialink.online")
            cuerpo2 = f"""
Estimado miembro del equipo de soporte,

ha generado un nuevo caso con el ID: {radicado}, registrado por un admin, asociado al usuario {Nombre_Usuario} identificado con el codigo {id_usuario}.

Por favor, revisa los detalles en la plataforma y procede con la atención correspondiente.

Atentamente,  
Sistema de notificaciones de GaiaLink
"""
            mensaje2.attach(MIMEText(cuerpo2, "plain"))
            try:
                servidor = smtplib.SMTP_SSL("gaialink.online", 465)
                servidor.login(correo_emisor, contraseña)
                servidor.send_message(mensaje)
                servidor.send_message(mensaje2)
                servidor.quit()
            except Exception as e:
                print(f"Error al enviar el correo: {e}")
            Close_BaseDatos(conexion, cursor) 
    def Modificar_Caso_Admin(self):
        conexion, cursor = Get_BaseDatos()
        id_usuario = self.Usuario
        self.departamento = "001DEP"
        hoy = datetime.today()
        Fecha2 = datetime.strptime(self.Fecha, "%Y-%m-%d")
        if Fecha2 > hoy:
            return "El caso no puede ocurrir en el futuro", "error"

        cursor.execute("SELECT Nombre FROM tbl_usuario WHERE id_usuario = %s", (id_usuario, ))
        Nombre_Usuario = cursor.fetchone()
        if not Nombre_Usuario:
            return "El usuario no se encontro", "error"     

        cursor.execute("SELECT tbl_adic_persona.Email FROM tbl_usuario JOIN tbl_persona ON tbl_usuario.Id_usuario = tbl_persona.fk_Usuario JOIN tbl_adic_persona on tbl_persona.Id_Persona = tbl_adic_persona.fk_persona Where tbl_usuario.Id_usuario = %s", (id_usuario,))
        Correo = cursor.fetchone()      
        if not Correo:
            return "No se encontro el Correo", "error"

        try:
            cursor.execute("UPDATE tbl_caso JOIN tbl_num_caso ON tbl_num_caso.Fk_Caso = Id_Caso_Incidente SET Fecha = %s, Descripción = %s, Personas_Afectadas = %s, Fk_Usuario = %s, Fk_Incidente = %s, Fk_Dep = %s, Fk_Estado = %s WHERE Radicado = %s",(self.Fecha, self.Descripcion, self.Personas_Afectadas, self.Usuario, self.incidente, self.departamento, self.estado, self.Radicado))
            conexion.commit()
            return "Caso modificado con exito", "exito"            
        except Exception as e:
            conexion.rollback()
            print(e)
            return f"no se pudo modificar el caso: {e}", "error"
        finally:
            mensaje = MIMEMultipart()
            mensaje["From"] =   formataddr(("Soporte GaiaLink", correo_emisor))
            mensaje["To"] = Correo["Email"]
            mensaje["Subject"] = f"Confirmación de Modificacion de Caso: {self.Radicado}"
            mensaje['Date'] = formatdate(localtime=True)
            mensaje['Message-ID'] = make_msgid(domain="gaialink.online")
            cuerpo = f"""
Estimado/a {Nombre_Usuario},

se a realizado una actualizacion en el estado de tu caso {self.Radicado} .

Nuestro equipo está trabajando en tu solicitud y te contactará en breve para resolver tu problema.

Si necesitas más detalles sobre el estado de tu ticket, puedes seguirlo a través de nuestro sistema o contactar a soporte.
Gracias por confiar en nosotros.

Atentamente,  
El equipo de soporte de GaiaLink
"""
            mensaje.attach(MIMEText(cuerpo, "plain"))

            mensaje2 = MIMEMultipart()
            mensaje2["From"] =   formataddr(("Soporte GaiaLink", correo_emisor))
            mensaje2["To"] = correo_receptor1
            mensaje2["Subject"] = f"Caso modificado: {self.Radicado}"
            mensaje2['Date'] = formatdate(localtime=True)
            mensaje2['Message-ID'] = make_msgid(domain="gaialink.online")
            cuerpo2 = f"""
Estimado miembro del equipo de soporte,

te informamos que la modificacion del caso {self.Radicado} ha sido exitosa.

Por favor, revisa los detalles en la plataforma y procede con la atención correspondiente.

Atentamente,  
Sistema de notificaciones de GaiaLink
"""
            mensaje2.attach(MIMEText(cuerpo2, "plain"))
            try:
                servidor = smtplib.SMTP_SSL("gaialink.online", 465)
                servidor.login(correo_emisor, contraseña)
                servidor.send_message(mensaje)
                servidor.send_message(mensaje2)
                servidor.quit()
            except Exception as e:
                print(f"Error al enviar el correo: {e}")
            Close_BaseDatos(conexion, cursor)
    def Eliminar_Caso_Admin(self):
        conexion, cursor = Get_BaseDatos()
        id_usuario = self.Usuario
        Estado = "Caso_03"

        cursor.execute("SELECT Fk_Estado FROM tbl_caso JOIN tbl_num_caso ON tbl_num_caso.Fk_Caso = tbl_caso.Id_Caso_Incidente WHERE Radicado = %s", (self.Radicado,))
        Estado3 = cursor.fetchone()
        if Estado3 == "Caso_03":
            return "El caso no existe", "error"

        cursor.execute("SELECT Nombre FROM tbl_usuario WHERE id_usuario = %s", (id_usuario, ))
        Nombre_Usuario = cursor.fetchone()
        if not Nombre_Usuario:
            return "El usuario no se encontro", "error"     

        cursor.execute("SELECT tbl_adic_persona.Email FROM tbl_usuario JOIN tbl_persona ON tbl_usuario.Id_usuario = tbl_persona.fk_Usuario JOIN tbl_adic_persona on tbl_persona.Id_Persona = tbl_adic_persona.fk_persona Where tbl_usuario.Id_usuario = %s", (id_usuario,))
        Correo = cursor.fetchone()      
        if not Correo:
            return "No se encontro el Correo", "error"

        try:
            cursor.execute("UPDATE tbl_caso JOIN tbl_num_caso ON tbl_num_caso.Fk_Caso = Id_Caso_Incidente SET Fk_Estado = %s WHERE Radicado = %s",(Estado, self.Radicado))
            conexion.commit()
            return "Caso eliminado con exito", "exito"            
        except Exception as e:
            conexion.rollback()
            print(e)
            return f"no se pudo eliminar el caso: {e}", "error"
        finally:
            mensaje = MIMEMultipart()
            mensaje["From"] =   formataddr(("Soporte GaiaLink", correo_emisor))
            mensaje["To"] = Correo["Email"]
            mensaje["Subject"] = f"Confirmación de Modificacion de Caso: {self.Radicado}"
            mensaje['Date'] = formatdate(localtime=True)
            mensaje['Message-ID'] = make_msgid(domain="gaialink.online")
            cuerpo = f"""
Estimado/a {Nombre_Usuario},

se a realizado la eliminacion de tu caso {self.Radicado} .

Si no fuiste tú quien solicitó esta acción, por favor comunícate de inmediato con nuestro equipo de soporte para garantizar la seguridad de tu cuenta..

Si necesitas asistencia adicional, no dudes en escribirnos.

Atentamente,  
El equipo de soporte de GaiaLink
"""
            mensaje.attach(MIMEText(cuerpo, "plain"))

            mensaje2 = MIMEMultipart()
            mensaje2["From"] =   formataddr(("Soporte GaiaLink", correo_emisor))
            mensaje2["To"] = correo_receptor1
            mensaje2["Subject"] = f"Caso modificado: {self.Radicado}"
            mensaje2['Date'] = formatdate(localtime=True)
            mensaje2['Message-ID'] = make_msgid(domain="gaialink.online")
            cuerpo2 = f"""
Estimado miembro del equipo de soporte,

Le informamos que se ha eliminado el caso  identificado con {self.Radicado} , del sistema GaiaLink.

Por favor, revisa los detalles en la plataforma y procede con la atención correspondiente.

Atentamente,  
Sistema de notificaciones de GaiaLink
"""
            mensaje2.attach(MIMEText(cuerpo2, "plain"))
            try:
                servidor = smtplib.SMTP_SSL("gaialink.online", 465)
                servidor.login(correo_emisor, contraseña)
                servidor.send_message(mensaje)
                servidor.send_message(mensaje2)
                servidor.quit()
            except Exception as e:
                print(f"Error al enviar el correo: {e}")
            Close_BaseDatos(conexion, cursor)            