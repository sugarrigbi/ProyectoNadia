from flask import request
import jwt
import os

def Validar_JWT():
    Auth = request.headers.get("Authorization")
    if not Auth:
        return None, "Token requerido"
    try:
        Token = Auth.split(" ")[1]
        Payload = jwt.decode(Token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
        return Payload, None
    except jwt.ExpiredSignatureError:
        return None, "Token expirado"
    except:
        return None, "Token inválido"    
