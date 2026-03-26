from flask import request
import jwt
from datetime import datetime, timedelta
from App.Models.Authenticator_Models import Dispositivos as Tabla_Dispositivos
from App.Utilities.Tables import db
from App.Config import SECRET_KEY
import secrets
from user_agents import parse as ua_parse
import random
from App.Utilities.Redis import redis_client
import bcrypt
import re
import requests

def Crear_Token(User_ID, Remember, Device_Token):
    if Remember:
        exp = datetime.utcnow() + timedelta(days=7)
    else:
        exp = datetime.utcnow() + timedelta(minutes=90)

    Payload = {
        "user_id": User_ID,
        "session_id": Device_Token,
        "exp": int(exp.timestamp())
    }
    return jwt.encode(Payload, SECRET_KEY, algorithm="HS256"), exp
def Get_Time(Bloqueado_Hasta, Ahora):
    restante = Bloqueado_Hasta-Ahora
    total_segundos = int(restante.total_seconds())
    minutos = total_segundos // 60
    segundos = total_segundos % 60

    return minutos, segundos
def Get_Device(Usuario_ID, Ultimo_Uso, Client_IP, Client_Payload=None):
    Token = secrets.token_hex(32)
    Ip = Client_IP
    ua_string = ""
    if Client_Payload and Client_Payload.get("userAgent"):
        ua_string = Client_Payload.get("userAgent") or ""
    else:
        ua_string = request.headers.get("User-Agent", "") or ""
    ua = ua_parse(ua_string)

    Navegador = ua.browser.family + " " + (ua.browser.version_string or "")
    Sistema = ua.os.family + " " + (ua.os.version_string or "")

    if ua.is_mobile:
        Dispositivo = "Móvil"
    elif ua.is_tablet:
        Dispositivo = "Tablet"
    elif ua.is_pc:
        Dispositivo = "Computador"
    else:
        Dispositivo = "Desconocido"

    if Client_Payload and Client_Payload.get("uaData"): 
        uaData = Client_Payload.get("uaData") or {} 
        if uaData.get("platform"): 
            Sistema = uaData.get("platform")        

    Data_D = {
        "IP": Ip,
        "Token": Token,
        "Navegador": Navegador,
        "Sistema": Sistema,
        "Dispositivo": Dispositivo,
        "Ultimo_Uso": Ultimo_Uso,
        "Usuario_ID": Usuario_ID
    }

    return Data_D
def Crear_Dispositivo(Data_D, Usuario_Nombre, Usuario_Correo, Ahora):
    Dispositivo = Tabla_Dispositivos(**Data_D)
    Token = Dispositivo.Token
    db.session.add(Dispositivo)
    db.session.commit()
    requests.post("http://127.0.0.1:5007/email",
        json={
            "Template": "Nuevo_Dispositivo",
            "Datos": {"Nombre": Usuario_Nombre, "Fecha": Ahora, "Dispositivo": Data_D["Dispositivo"], "Navegador": Data_D["Navegador"], "IP": Data_D["IP"]},
            "Correo": Usuario_Correo,
            "Asunto": "Nuevo inicio de sesión detectado"
        }
    )
    return Token
def Generar_Codigo():
    Codigo = str(random.randint(100000, 999999))
    return Codigo
def Guardar_Codigo(Correo, Codigo):
    redis_client.setex(
        f"recuperar:{Correo}:codigo",
        600,
        Codigo
    )
def Obtener_Codigo(Correo):
    Codigo = redis_client.get(
        f"recuperar:{Correo}:codigo"
    )
    if not Codigo:
        return {"Error": "El codigo expiro"}
    return Codigo
def Hashear_Contraseña(Contraseña):
    Pepper = "Gaialink2026*!"
    Salt = bcrypt.gensalt()

    Contraseña_Pepper = (Contraseña + Pepper)
    Hash = bcrypt.hashpw(Contraseña_Pepper.encode("utf-8"), Salt)

    return Hash.decode("utf-8")
def Eliminar_Datos(Correo):
    redis_client.delete(f"recuperar:{Correo}:codigo")
def Validar_Contraseña(Contraseña, Documento):
    if not any(c.isupper() for c in Contraseña):
        return "La contraseña debe contener una mayuscula"
    
    if not any(c.isdigit() for c in Contraseña):
        return "La contraseña debe contener un numero"
    
    if not re.search(r'[^A-Za-z0-9]', Contraseña):
        return "La contraseña debe contener un caracter especial"
    
    if Documento in Contraseña:
        return "La contraseña no puede contener el documento"   