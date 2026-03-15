from datetime import datetime
from App.Models.User_Model import Persona as Tabla_Persona, Usuario as Tabla_Usuario, Departamento as T_Departamento, Ciudad as T_Ciudad, Localidad as T_Localidad, Barrio as T_Barrio
import re
import random
import requests
from App.Utilities.Redis import redis_client
from flask import json
import bcrypt

def Validar_Datos(Data_U, Data_P):
    Fecha_Nacimiento = datetime.strptime(Data_P["Fecha_Nacimiento"], "%Y-%m-%d").date()
    Hoy = datetime.today().date()
    Edad = Hoy.year - Fecha_Nacimiento.year - ((Hoy.month, Hoy.day) < (Fecha_Nacimiento.month, Fecha_Nacimiento.day))

    if Edad < 13 or Edad > 110:
        return {"Error": "La edad requerida es entre 13 y 110 años"}
    
    Doc_Existe = Tabla_Persona.query.filter_by(Documento=Data_P["Documento"]).first()
    if Doc_Existe:
        return {"Error": "El documento ya existe"}
    
    Correo_Existe = Tabla_Usuario.query.filter_by(Correo=Data_U["Correo"]).first()
    if Correo_Existe:
        return {"Error": "El correo ya existe"}
    
    Nombre_Existe = Tabla_Usuario.query.filter_by(Nombre=Data_U["Nombre"]).first()
    if Nombre_Existe:
        return {"Error": "El nombre de usuario ya existe"}

    if not any(c.isupper() for c in Data_U["Contraseña"]):
        return {"Error": "La contraseña debe contener una mayuscula"}
    
    if not any(c.isdigit() for c in Data_U["Contraseña"]):
        return {"Error": "la contraseña debe tener un numero"}
    
    if not re.search(r'[^A-Za-z0-9]', Data_U["Contraseña"]):
        return {"Error": "La contraseña debe tener un caracter especial"}
    
    if Data_P["Documento"] in Data_U["Contraseña"]:
        return {"Error": "La contraseña no puede contener el documento"}
def Normalizar_Datos(Data_UN, Data_PN):
    Data_P = {
        "Primer_Nombre": Data_PN["Primer_Nombre"].strip().capitalize(),
        "Segundo_Nombre": Data_PN["Segundo_Nombre"].strip().capitalize(),
        "Primer_Apellido": Data_PN["Primer_Apellido"].strip().capitalize(),
        "Segundo_Apellido": Data_PN["Segundo_Apellido"].strip().capitalize(),
        "Documento": Data_PN["Documento"].strip(),
        "Direccion": Data_PN["Direccion"].strip(),
        "Telefono": Data_PN["Telefono"].strip(),
        "Barrio_ID": Data_PN["Barrio_ID"].strip().capitalize(),
        "Tipo_Documento_ID": Data_PN["Tipo_Documento_ID"],
        "Fecha_Nacimiento": Data_PN["Fecha_Nacimiento"],
        "Usuario_ID": "No"
    }
    Data_U = {
        "Nombre": Data_UN["Nombre"].strip(),
        "Correo": Data_UN["Correo"].strip().lower(),
        "Contraseña": Data_UN["Contraseña"]
    }

    Data_C = {
        "Departamento_ID": Data_PN["Departamento_ID"].strip().capitalize(),
        "Ciudad_ID": Data_PN["Ciudad_ID"].strip().capitalize(),
        "Localidad_ID": Data_PN["Localidad_ID"].strip().capitalize(),
        "Barrio_ID": Data_PN["Barrio_ID"].strip().capitalize()
    }

    return Data_U, Data_P, Data_C
def Generar_Codigo():
    Codigo = str(random.randint(100000, 999999))
    return Codigo
def Guardar_Codigo(Correo, Codigo):
    redis_client.setex(
        f"registro:{Correo}:codigo",
        600,
        Codigo
    )
def Guardar_Datos(Correo, Data_U, Data_P):
    Datos = {
        "Usuario": Data_U,
        "Persona": Data_P
    }
    redis_client.setex(
        f"registro:{Correo}:datos",
        600,
        json.dumps(Datos)
    )
def Obtener_Codigo(Correo):
    Codigo = redis_client.get(
        f"registro:{Correo}:codigo"
    )
    if not Codigo:
        return {"Error": "El codigo expiro"}
    return Codigo
def Obtener_Datos(Correo):

    Datos = redis_client.get(
        f"registro:{Correo}:datos"
    )

    if not Datos:
        return None, None

    Datos = json.loads(Datos)

    return Datos["Usuario"], Datos["Persona"]    
def Eliminar_Datos(Correo):
    redis_client.delete(f"registro:{Correo}:codigo")
    redis_client.delete(f"registro:{Correo}:datos")
def Hashear_Contraseña(Contraseña):
    Pepper = "Gaialink2026*!"
    Salt = bcrypt.gensalt()

    Contraseña_Pepper = (Contraseña + Pepper)
    Hash = bcrypt.hashpw(Contraseña_Pepper.encode("utf-8"), Salt)

    return Hash.decode("utf-8")
