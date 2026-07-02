from App.Utilities.Tables import db
from flask import request
import bcrypt
import json
import jwt
import os
import re

def Validar_JWT():
    Auth = request.headers.get("Authorization")
    if not Auth:
        return None, "Token requerido"
    try:
        Token = Auth.split(" ")[1]
        Payload = jwt.decode(Token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
        return Payload, None
    except jwt.ExpiredSignatureError:
        print("HI")
        return None, "Token expirado"
    except:
        return None, "Token invalido"
def Actualizar_Persona(Persona, Data, Tabla_Auditoria, Usuario_Modificador):
    Persona_json = json.dumps(Persona.to_dict(), default=str, ensure_ascii=False)           

    Persona.Primer_Nombre = Data["Primer_Nombre"]
    Persona.Primer_Apellido = Data["Primer_Apellido"]
    Persona.Tipo_Documento = Data["Tipo_Documento"]
    Persona.Telefono = Data["Telefono"]
    Persona.Segundo_Nombre = Data["Segundo_Nombre"]
    Persona.Segundo_Apellido = Data["Segundo_Apellido"]
    Persona.Documento = Data["Documento"]
    Persona.Fecha_Nacimiento = Data["Fecha_Nacimiento"]
    Persona.Direccion = Data["Direccion"]             

    Auditoria = Tabla_Auditoria(Accion="Persona modificada", Anterior=Persona_json, Modificado_Por=Usuario_Modificador, Persona_ID=Persona.ID)
    db.session.add(Auditoria) 
def Validar_Contraseña(Contraseña, Documento):
    if len(Contraseña) < 10:
        return "La contraseña debe tener 10 caracteres"
    if not any(C.isupper() for C in Contraseña):
        return "La contraseña debe contener una mayuscula"
    if not any(C.islower() for C in Contraseña):
        return "La contraseña debe contener una minuscula"        
    if not any(C.isdigit() for C in Contraseña):
        return "La contraseña debe contener un numero"
    if not re.search(r'[^A-Za-z0-9]', Contraseña):
        return "La contraseña debe contener un caracter especial"
    if Documento in Contraseña:
        return "La contraseña no puede contener el documento"
    return False
def Crear_Hash(Contraseña):
    Salt = bcrypt.gensalt()
    Contraseña_Pepper = Contraseña + os.getenv("PEPPER")
    Hash_Nuevo = bcrypt.hashpw(Contraseña_Pepper.encode("utf-8"), Salt)

    return Hash_Nuevo.decode("utf-8")
def Validar_Pw(Contraseña, Hash):
    return bcrypt.checkpw((Contraseña + os.getenv("PEPPER")).encode("utf-8"), Hash.encode("utf-8"))