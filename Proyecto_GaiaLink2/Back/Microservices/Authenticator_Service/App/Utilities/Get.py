from flask import request, jsonify
import bcrypt
from App.Models.Authenticator_Models import Usuario as Tabla_Usuario, Dispositivos as Tabla_Dispositivos
from App.Utilities.Tables import db
from App.Utilities.Utils import Crear_Token, Get_Device, Get_Time
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

        Ahora = datetime.now(bogota_tz).replace(tzinfo=None)
        Ahora_Formated = Ahora.strftime("%d/%m/%Y %H:%M")

        Usuario = Tabla_Usuario.query.filter((Tabla_Usuario.Correo == Identificador) | (Tabla_Usuario.Nombre == Identificador)).first()

        if not Usuario:
            return jsonify({"Error": "Correo/Nombre o contraseña incorrectos"}), 401
        
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
        
        Data_D = Get_Device(Usuario.ID, Ahora, Device, Client_Payload)

        if not Device:
            Device = Data_D["Token"]
            Dispositivo = Tabla_Dispositivos(**Data_D)
            db.session.add(Dispositivo)
            db.session.commit()
            requests.post("http://127.0.0.1:5007/email",
                json={
                    "Template": "Nuevo_Dispositivo",
                    "Datos": {"Nombre": Usuario.Nombre, "Fecha": Ahora_Formated, "Dispositivo": Data_D["Dispositivo"], "Navegador": Data_D["Navegador"], "IP": Data_D["IP"]},
                    "Correo": Usuario.Correo,
                    "Asunto": "Nuevo inicio de sesión detectado"
                }
            )            

        return jsonify({"Token": Token, "Expires_At": Expira, "User": {"ID": Usuario.ID, "Username": Usuario.Nombre}, "Device": Device  }), 200
