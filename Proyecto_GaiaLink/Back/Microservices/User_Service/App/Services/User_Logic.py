from App.Models.User_Model import (
    Persona as Tabla_Persona, 
    Usuario as Tabla_Usuario, 
    Departamento as T_Departamento, 
    Ciudad as T_Ciudad, 
    Localidad as T_Localidad, 
    Barrio as T_Barrio,
    Usuario_Auditoria as Td_Usuario,
    Persona_Auditoria as Td_Persona
) 
from App.Utilities.Util import (
    Normalizar_Datos, 
    Validar_Datos, 
    Generar_Codigo, 
    Guardar_Codigo, 
    Guardar_Datos, 
    Obtener_Codigo, 
    Obtener_Datos, 
    Eliminar_Datos, 
    Hashear_Contraseña
) 
from App.Utilities.Tables import db
import requests
import json
import os

class User_Service:
    @staticmethod
    def Registro(Data_U, Data_P):
        Error = Validar_Datos(Data_U, Data_P)
        if Error:
            return Error
        
        Codigo = Generar_Codigo()

        requests.post(os.getenv("EMAIL_SERVICE"),
            json={
                "Template": "Verificar_Codigo",
                "Datos": {"Nombre": Data_U["Nombre"], "Codigo": Codigo},
                "Correo": Data_U["Correo"],
                "Asunto": "Creacion de cuenta"
            }
        )

        Guardar_Codigo(Data_U["Correo"], Codigo)
        Guardar_Datos(Data_U["Correo"], Data_U, Data_P)

        return "Codigo Enviado"
    @staticmethod
    def Create(Correo, Codigo):
        Codigo_Real = Obtener_Codigo(Correo)
        
        if Codigo != Codigo_Real:
            return {"Error": "Codigo Incorrecto"}
        
        Data_UN, Data_PN = Obtener_Datos(Correo)
        
        Data_U, Data_P, Data_C = Normalizar_Datos(Data_UN, Data_PN)

        Dep_Existe = T_Departamento.query.filter_by(Nombre=Data_C["Departamento_ID"], Pais_ID=1).first()
        if not Dep_Existe:
            Dep_Existe = T_Departamento(Nombre=Data_C["Departamento_ID"], Pais_ID=1)
            db.session.add(Dep_Existe)
            db.session.commit()
        Ciu_Existe = T_Ciudad.query.filter_by(Nombre=Data_C["Ciudad_ID"], Departamento_ID=Dep_Existe.ID).first()
        if not Ciu_Existe:
            Ciu_Existe = T_Ciudad(Nombre=Data_C["Ciudad_ID"], Departamento_ID=Dep_Existe.ID)
            db.session.add(Ciu_Existe)
            db.session.commit()
        Loc_Existe = T_Localidad.query.filter_by(Nombre=Data_C["Localidad_ID"], Ciudad_ID=Ciu_Existe.ID).first()
        if not Loc_Existe:
            Loc_Existe = T_Localidad(Nombre=Data_C["Localidad_ID"], Ciudad_ID=Ciu_Existe.ID)
            db.session.add(Loc_Existe)
            db.session.commit()
        Bar_Existe = T_Barrio.query.filter_by(Nombre=Data_C["Barrio_ID"], Localidad_ID=Loc_Existe.ID).first()
        if not Bar_Existe:
            Bar_Existe = T_Barrio(Nombre=Data_C["Barrio_ID"], Localidad_ID=Loc_Existe.ID)
            db.session.add(Bar_Existe)
            db.session.commit()                                   
        Data_P["Barrio_ID"] = Bar_Existe.ID

        Data_U["Contraseña"] = Hashear_Contraseña(Data_U["Contraseña"])

        Usuario = Tabla_Usuario(**Data_U)
        db.session.add(Usuario)
        db.session.flush()

        Usuario_json = json.dumps(Usuario.to_dict(), default=str, ensure_ascii=False)
        Auditoria_u = Td_Usuario(Accion="Usuario creado", Anterior=Usuario_json, Modificado_Por=Usuario.ID, Usuario_ID=Usuario.ID)
        db.session.add(Auditoria_u)

        Data_P["Usuario_ID"] = Usuario.ID

        Persona = Tabla_Persona(**Data_P)
        db.session.add(Persona)
        db.session.flush()

        Persona_json = json.dumps(Persona.to_dict(), default=str, ensure_ascii=False)
        Auditoria_p = Td_Persona(Accion="Persona creada", Anterior=Persona_json, Modificado_Por=Usuario.ID, Persona_ID=Persona.ID)
        db.session.add(Auditoria_p)

        db.session.commit()
        
        requests.post(os.getenv("EMAIL_SERVICE"),
            json={
                "Template": "Bienvenido",
                "Datos": {"Nombre": Data_P["Primer_Nombre"]+" "+Data_P["Primer_Apellido"]},
                "Correo": Data_U["Correo"],
                "Asunto": "Bienvenido a Gaialink"
            }
        )

        Eliminar_Datos(Correo)
        return Usuario