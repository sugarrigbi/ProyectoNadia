from App.Models.Entity_Models import (
    Entidad as Tabla_Entidad, 
    Usuario as Tabla_Usuario, 
    RolAPermiso as Tabla_Permiso, 
    EntidadAuditoria as Tabla_Auditoria, 
    EstadoEntidad as Tabla_Estado, 
    Incidente as Tabla_Incidente
)
from App.Utilities.Tables import db
import requests
import json
import os

class Entity_Service:
    @staticmethod
    def Create(Data, User_ID):
        if not User_ID:
            return "Auth"
        
        Usuario_Validar = Tabla_Usuario.query.get(User_ID)
        if not Usuario_Validar:
            return "Auth"
        Permisos = Tabla_Permiso.query.filter(Tabla_Permiso.Rol_ID == Usuario_Validar.Rol_ID).all()
        Nombres = [P.to_dict()["Nombre"] for P in Permisos]
        if "entidad_crear" not in Nombres:
            return "Auth"

        Entidad = Tabla_Entidad(**Data)
        db.session.add(Entidad)
        db.session.flush()

        Entidad_json = Entidad.to_dict()
        Entidad_json_text = json.dumps(Entidad_json, default=str, ensure_ascii=False)

        Auditoria = Tabla_Auditoria(Accion="Entidad creada", Anterior=Entidad_json_text, Modificado_Por=Usuario_Validar.ID, Entidad_ID=Entidad.ID)
        db.session.add(Auditoria)
        db.session.commit()   

        requests.post(os.getenv("EMAIL_SERVICE"),
            json={
                "Template": "Entidad_Creada",
                "Datos": {
                    "Nombre": Usuario_Validar.Nombre, 
                    "Entidad": Entidad.ID, 
                    },
                "Correo": Usuario_Validar.Correo,
                "Asunto": f"Entidad {Entidad.ID} creada"
            }
        )             
        return Entidad
    @staticmethod
    def Read_All(User_ID):
        if not User_ID:
            return "Auth"
        
        Usuario_Validar =  Tabla_Usuario.query.get(User_ID)
        if not Usuario_Validar:
            return "Auth"        
        Permisos = Tabla_Permiso.query.filter(Tabla_Permiso.Rol_ID == Usuario_Validar.Rol_ID).all()
        Nombres = [P.to_dict()["Nombre"] for P in Permisos]
        if "entidad_ver" not in Nombres:
            return "Auth"

        Entidades = Tabla_Entidad.query.filter(Tabla_Entidad.Estado_Entidad_ID != 4).order_by(Tabla_Entidad.ID.asc()).all()
        return Entidades
    @staticmethod
    def Obtener_Datos(User_ID):
        if not User_ID:
            return "Auth"
        
        Usuario_Validar = Tabla_Usuario.query.get(User_ID)
        Permisos = Tabla_Permiso.query.filter(Tabla_Permiso.Rol_ID == Usuario_Validar.Rol_ID).all()
        Nombres = [p.to_dict()["Nombre"] for p in Permisos]            
        if "entidad_ver" in Nombres:
            Estados = Tabla_Estado.query.filter(Tabla_Estado.ID != 4).order_by(Tabla_Estado.ID.asc()).all()
            Incidentes = Tabla_Incidente.query.order_by(Tabla_Incidente.ID.asc()).all()
            Data = {
                "Estados": [e.to_dict() for e in Estados],
                "Incidentes": [i.to_dict() for i in Incidentes],
            }
        else:
            return "Auth"       
        return Data      
    @staticmethod
    def Read_By(Filtros, User_ID):
        if not User_ID:
            return "Auth"
        
        Usuario_Validar =  Tabla_Usuario.query.get(User_ID)
        if not Usuario_Validar:
            return "Auth"            
        Permisos = Tabla_Permiso.query.filter(Tabla_Permiso.Rol_ID == Usuario_Validar.Rol_ID).all()
        Nombres = [P.to_dict()["Nombre"] for P in Permisos]
        if "entidad_ver" not in Nombres:
            return "Auth"
        
        Entidades = Tabla_Entidad.query
        if Filtros.get("Nombre"):
            nombre = Filtros['Nombre'][0]
            Entidades = Entidades.filter(Tabla_Entidad.Nombre.ilike(f"%{nombre}%"))
        if Filtros.get("Incidente"):
            Entidades = Entidades.filter(Tabla_Entidad.Incidente_ID.in_(Filtros["Incidente"]))
        if Filtros.get("Estado"):
            Entidades = Entidades.filter(Tabla_Entidad.Estado_Entidad_ID.in_(Filtros["Estado"]))

        return Entidades
    @staticmethod
    def Update(Entity_ID, Data, User_ID):
        if not User_ID:
            return "Auth"
        
        Usuario_Validar = Tabla_Usuario.query.get(User_ID)
        if not Usuario_Validar:
            return "Auth"            
        Permisos = Tabla_Permiso.query.filter(Tabla_Permiso.Rol_ID == Usuario_Validar.Rol_ID).all()
        if "entidad_editar" not in [p.to_dict()["Nombre"] for p in Permisos]:
            return "Auth"

        Entidad = Tabla_Entidad.query.get(Entity_ID)

        if not Entidad:
            return False

        Entidad_json = Entidad.to_dict()
        Entidad_json_text = json.dumps(Entidad_json, default=str, ensure_ascii=False)

        Auditoria = Tabla_Auditoria(Accion="Entidad editada", Anterior=Entidad_json_text, Modificado_Por=Usuario_Validar.ID, Entidad_ID=Entidad.ID)
        db.session.add(Auditoria)

        for Key, Value in Data.items():
            if Value not in (None, "") and hasattr(Entidad, Key):
                setattr(Entidad, Key, Value)
        db.session.commit()

        return Entidad      
    @staticmethod
    def Delete(Entity_ID, User_ID):
        if not User_ID:
            return "Auth"
        
        Usuario_Validar = Tabla_Usuario.query.get(User_ID)
        if not Usuario_Validar:
            return "Auth"            
        Permisos = Tabla_Permiso.query.filter(Tabla_Permiso.Rol_ID == Usuario_Validar.Rol_ID).all()
        if "entidad_eliminar" not in [p.to_dict()["Nombre"] for p in Permisos]:
            return "Auth"

        Entidad = Tabla_Entidad.query.get(Entity_ID)
        if not Entidad:
            return False

        Entidad_json = Entidad.to_dict()
        Entidad_json_text = json.dumps(Entidad_json, default=str, ensure_ascii=False)

        Auditoria = Tabla_Auditoria(Accion="Entidad eliminada", Anterior=Entidad_json_text, Modificado_Por=Usuario_Validar.ID, Entidad_ID=Entidad.ID)
        db.session.add(Auditoria)
        
        Entidad.Estado_Entidad_ID = 4

        db.session.commit()

        requests.post(os.getenv("EMAIL_SERVICE"),
            json={
                "Template": "Entidad_Eliminada",
                "Datos": {
                    "Nombre": Usuario_Validar.Nombre, 
                    "Entidad": Entidad.ID, 
                    },
                "Correo": Usuario_Validar.Correo,
                "Asunto": f"Entidad {Entidad.ID} eliminada"
            }
        )           
        return Entidad

