import jwt
from flask import request

SECRET_KEY = "Gaialink2026!*ClaveSuperSeguraJWT!!"

def Validar_JWT():
    Auth = request.headers.get("Authorization")
    if not Auth:
        return None, "Token requerido"
    try:
        Token = Auth.split(" ")[1]
        Payload = jwt.decode(Token, SECRET_KEY, algorithms=["HS256"])
        return Payload, None
    except jwt.ExpiredSignatureError:
        print("HI")
        return None, "Token expirado"
    except:
        return None, "Token invalido"