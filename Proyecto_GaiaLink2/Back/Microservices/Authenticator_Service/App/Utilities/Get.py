from flask import request, jsonify
import bcrypt
from App.Models.Authenticator_Models import Usuario as Tabla_Usuario, Dispositivos as Tabla_Dispositivos, Persona as Tabla_Persona, Rol as Tabla_Rol
from App.Utilities.Tables import db
from App.Utilities.Utils import Crear_Token, Get_Device, Get_Time, Generar_Codigo, Guardar_Codigo, Obtener_Codigo, Hashear_Contraseña, Eliminar_Datos, Validar_Contraseña, Crear_Dispositivo
from datetime import datetime, timedelta
import pytz
import requests

bogota_tz = pytz.timezone("America/Bogota")
Pepper = "Gaialink2026*!"

class Get_Auth():
    @staticmethod
    def Login():
        Data = request.get_json()

        Identificador = Data["Identificador"]
        Contraseña = Data["Contraseña"]
        Remember_Me = Data["Remember_Me"]
        Device = Data["Dispositivo"]
        Client_Payload = Data["Client_Payload"]
        Client_IP = Data["Client_IP"]

        Ahora = datetime.now(bogota_tz).replace(tzinfo=None)
        Ahora_Formated = Ahora.strftime("%d/%m/%Y %H:%M")

        Usuario = Tabla_Usuario.query.filter((Tabla_Usuario.Correo == Identificador) | (Tabla_Usuario.Nombre == Identificador)).first()
        if not Usuario:
            return jsonify({"Error": "Correo/Nombre o contraseña incorrectos"}), 401
        Rol = Tabla_Rol.query.filter(Tabla_Rol.ID == Usuario.Rol_ID).first()
        if not Rol:
            return jsonify({"Error": "Rol incorrectos"}), 401        
        
        if Usuario.Estado_Usuario_ID == 2:
            return jsonify({"Error": "Tu cuenta está inactiva. Actívala para continuar"}), 403
        if Usuario.Estado_Usuario_ID == 3:
            return jsonify({"Error": "Tu cuenta está suspendida. Contacta a soporte"}), 403
        if Usuario.Estado_Usuario_ID == 4:
            return jsonify({"Error": "Tu cuenta está bloqueada permanentemente"}), 403               
        if Usuario.Estado_Usuario_ID == 5:
            return jsonify({"Error": "Correo/Nombre o contraseña incorrectos"}), 401  

        if Usuario.Bloqueado_Hasta and Usuario.Bloqueado_Hasta <= Ahora:
            Usuario.Bloqueado_Hasta = None
            Usuario.Intentos_Fallidos = 0
            db.session.commit()

        if Usuario.Bloqueado_Hasta and Usuario.Bloqueado_Hasta > Ahora:
            Minutos, Segundos = Get_Time(Usuario.Bloqueado_Hasta, Ahora)
            return jsonify({"Error": f"Demasiados intentos Fallidos, Intenta de nuevo en {Minutos:02d}:{Segundos:02d}"}), 401

        if not bcrypt.checkpw((Contraseña + Pepper).encode("utf-8"),Usuario.Contraseña.encode("utf-8")):
            Usuario.Intentos_Fallidos = Usuario.Intentos_Fallidos+1

            if Usuario.Intentos_Fallidos == 3:
                Usuario.Bloqueado_Hasta = (Ahora + timedelta(minutes=15)).replace(tzinfo=bogota_tz)
                db.session.commit()
                Minutos, Segundos = Get_Time(Usuario.Bloqueado_Hasta, Ahora)
                return jsonify({"Error": f"Demasiados intentos Fallidos, Intenta de nuevo en {Minutos:02d}:{Segundos:02d}"}), 401

            if Usuario.Intentos_Fallidos < 3:
                db.session.commit()
                Restantes = 3 - Usuario.Intentos_Fallidos
                return jsonify({"Error": f"Correo/Nombre o contraseña incorrectos"}), 401

        Usuario.Intentos_Fallidos = 0
        db.session.commit()
        
        Token, Expira = Crear_Token(Usuario.ID, Remember_Me)

        Device_Token = Device

        Dev_Existe = Tabla_Dispositivos.query.filter(Tabla_Dispositivos.Token == Device).first()
        if not Device or not Dev_Existe:
            Data_D = Get_Device(Usuario.ID, Ahora, Client_IP, Client_Payload)
            Device_Token = Crear_Dispositivo(Data_D, Usuario.Nombre, Usuario.Correo, Ahora_Formated)
        if Dev_Existe:
            Dev_Existe.Ultimo_Uso = Ahora
            db.session.commit()

        return jsonify({"Token": Token, "Expires_At": Expira, "User": {"Rol_ID": Usuario.Rol_ID, "Rol_Name": Rol.Nombre,"User_ID": Usuario.ID, "User_Name": Usuario.Nombre}, "Device": Device_Token}), 200
    @staticmethod
    def Recuperar():
        Data = request.get_json()

        Identificador = Data["Identificador"]

        Usuario = Tabla_Usuario.query.filter((Tabla_Usuario.Nombre == Identificador) | (Tabla_Usuario.Correo == Identificador)).first()
        if not Usuario:
            return jsonify({"Error": "El Correo/Nombre no existe"}), 401
        
        Codigo = Generar_Codigo()

        requests.post("http://127.0.0.1:5007/email",
            json={
                "Template": "Recuperar_Contraseña",
                "Datos": {"Nombre": Usuario.Nombre, "Codigo": Codigo},
                "Correo": Usuario.Correo,
                "Asunto": "Solicitud de recuperación de contraseña"
            }
        )

        Guardar_Codigo(Usuario.Correo, Codigo)

        return jsonify({"Message": "Codigo enviado con exito"}), 200
    @staticmethod
    def Recuperar_Codigo():
        Data = request.get_json()

        Identificador = Data["Identificador"]
        Codigo = Data["Codigo"]
        Contraseña = Data["Contraseña"]

        Usuario = Tabla_Usuario.query.filter((Tabla_Usuario.Nombre == Identificador) | (Tabla_Usuario.Correo == Identificador)).first()
        if not Usuario:
            return jsonify({"Error": "El Correo/Nombre no existe"}), 401        
        Persona = Tabla_Persona.query.filter_by(Usuario_ID=Usuario.ID).first()
        if not Persona:
            return jsonify({"Error": "El Correo/Nombre no existe"}), 401
        
        Codigo_Real = Obtener_Codigo(Usuario.Correo)
        if Codigo != Codigo_Real:
            return jsonify({"Error": "Codigo incorrecto"}), 401

        Error = Validar_Contraseña(Contraseña, Persona.Documento)
        if Error:
            return jsonify({"Error": Error}), 401

        Hash = Hashear_Contraseña(Contraseña)
        if not Hash:
            return jsonify({"Error": "Error al Hashear"}), 401

        if bcrypt.checkpw((Contraseña + Pepper).encode("utf-8"), Usuario.Contraseña.encode("utf-8")):
            return jsonify({"Error": "No se permite reutilizar contraseñas anteriores"}), 401
        
        Usuario.Contraseña = Hash
        db.session.commit()

        requests.post("http://127.0.0.1:5007/email",
            json={
                "Template": "Cambio_Contraseña",
                "Datos": {"Nombre": Usuario.Nombre},
                "Correo": Usuario.Correo,
                "Asunto": "Cambio de Contraseña"
            }
        )        

        Eliminar_Datos(Usuario.Correo)
        return jsonify({"Message": "Contraseña cambiada con exito"}), 200