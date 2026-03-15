from flask import request
import jwt
from datetime import datetime, timedelta
from App.Models.Authenticator_Models import Dispositivos as Tabla_Dispositivos
from App.Utilities.Tables import db
from App.Config import SECRET_KEY
import secrets
from user_agents import parse as ua_parse

def Crear_Token(User_ID, Remember):
    if Remember:
        exp = datetime.utcnow() + timedelta(days=7)
    else:
        exp = datetime.utcnow() + timedelta(minutes=90)

    Payload = {
        "user_id": User_ID,
        "exp": int(exp.timestamp())
    }
    return jwt.encode(Payload, SECRET_KEY, algorithm="HS256"), exp
def Get_Time(Bloqueado_Hasta, Ahora):
    restante = Bloqueado_Hasta-Ahora
    total_segundos = int(restante.total_seconds())
    minutos = total_segundos // 60
    segundos = total_segundos % 60

    return minutos, segundos
def Get_Device(Usuario_ID, Ultimo_Uso, DeviceToken=None, Client_Payload=None):
    if DeviceToken:
        Dispositivo = Tabla_Dispositivos.query.filter_by(Token=DeviceToken).first()
        if Dispositivo:
            Dispositivo.Ultimo_Uso = Ultimo_Uso
            db.session.commit()
            return None
    Token = secrets.token_hex(32)
    Ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    if Ip and "," in Ip:
        Ip = Ip.split(",")[0].strip()

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
