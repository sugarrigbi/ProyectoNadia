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
        
        cursor.execute("SELECT Id_Caso_Incidente FROM prueba.tbl_caso WHERE Fk_Usuario = %s", (id_usuario,))
        casos = cursor.fetchall()
        if not casos:
            Close_BaseDatos(conexion, cursor)
            return []
        
        for i in casos:
            id_caso = i["Id_Caso_Incidente"]
            cursor.execute("SELECT Radicado FROM tbl_num_caso WHERE Fk_Caso = %s", (id_caso,))
            radicado = cursor.fetchone()
            if radicado:
                Numeros.append(radicado)

        cursor.execute("SELECT Fecha FROM prueba.tbl_caso WHERE Fk_Usuario = %s", (id_usuario,))
        Fecha = cursor.fetchall()

        cursor.execute("SELECT Descripción FROM prueba.tbl_caso WHERE Fk_Usuario = %s", (id_usuario,))
        Descripción = cursor.fetchall()

        cursor.execute("SELECT Personas_Afectadas FROM prueba.tbl_caso WHERE Fk_Usuario = %s", (id_usuario,))
        Personas_Afectadas = cursor.fetchall()

        cursor.execute("SELECT Nombre FROM prueba.tbl_usuario WHERE Id_usuario = %s", (id_usuario,))
        Nombre = cursor.fetchall()

        cursor.execute("SELECT Fk_Incidente FROM prueba.tbl_caso WHERE Fk_Usuario = %s", (id_usuario,))
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

        cursor.execute("SELECT Fk_Estado FROM prueba.tbl_caso WHERE Fk_Usuario = %s", (id_usuario,))
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
        return lista_fusionada