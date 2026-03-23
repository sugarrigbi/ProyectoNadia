from App.Utilities.Tables import db
import requests
import json
from App.Models.Case_Models import Caso as Tabla_Caso, Usuario as Tabla_Usuario, Estado_Caso as Tabla_Estado, Prioridad as Tabla_Prioridad, Incidente as Tabla_Incidente, Barrio as Tabla_Barrio, Localidad as Tabla_Localidad, Ciudad as Tabla_Ciudad, Departamento as Tabla_Dep, Tipo_Relacion as Tabla_Relacion, Caso_Discusion as Tabla_Discusion, Departamento as T_Departamento, Ciudad as T_Ciudad, Localidad as T_Localidad, Barrio as T_Barrio, Casos_a_Casos as Tabla_Casos_a_Casos, Radicado_Caso as Tabla_Radicado, Caso_Auditoria as Tabla_Auditoria

class Case_Service():
    @staticmethod
    def Create(Data_C, Data_C_C, Data_L, Data_R):
        if Data_L:
            if Data_L["Departamento_ID"]:
                Departamento = T_Departamento.query.get(int(Data_L["Departamento_ID"]))
            else:
                Departamento_Norm = Data_L["Departamento"].capitalize().strip()
                Departamento = T_Departamento.query.filter_by(Nombre=Departamento_Norm).first()
                if not Departamento:
                    Departamento = T_Departamento(Nombre=Departamento_Norm, Pais_ID=1)
                    db.session.add(Departamento)
                    db.session.flush()
            if Data_L["Ciudad_ID"]:
                Ciudad = T_Ciudad.query.get(int(Data_L["Ciudad_ID"]))
            else:
                Ciudad_Norm = Data_L["Ciudad"].capitalize().strip()
                Ciudad = T_Ciudad.query.filter_by(Nombre=Ciudad_Norm).first()
                if not Ciudad:
                    if Data_L["Departamento_ID"]:
                        Ciudad = T_Ciudad(Nombre=Ciudad_Norm, Departamento_ID=int(Data_L["Departamento_ID"]))
                        db.session.add(Ciudad)
                        db.session.flush()
                    else:
                        Ciudad = T_Ciudad(Nombre=Ciudad_Norm, Departamento_ID=Departamento.ID)
                        db.session.add(Ciudad)
                        db.session.flush() 
            if Data_L["Localidad_ID"]:
                Localidad = T_Localidad.query.get(int(Data_L["Localidad_ID"]))       
            else:
                Localidad_Norm = Data_L["Localidad"].capitalize().strip()
                Localidad = T_Localidad.query.filter_by(Nombre=Localidad_Norm).first()
                if not Localidad:
                    if Data_L["Ciudad_ID"]:
                        Localidad = T_Localidad(Nombre=Localidad_Norm, Ciudad_ID=int(Data_L["Ciudad_ID"]))
                        db.session.add(Localidad)
                        db.session.flush()                        
                    else:
                        Localidad = T_Localidad(Nombre=Localidad_Norm, Ciudad_ID=Ciudad.ID)  
                        db.session.add(Localidad)
                        db.session.flush()   
            if Data_L["Barrio_ID"]:
                Barrio = T_Barrio.query.get(int(Data_L["Barrio_ID"]))
            else:
                Barrio_Norm = Data_L["Barrio"].capitalize().strip()
                Barrio = T_Barrio.query.filter_by(Nombre=Barrio_Norm).first()
                if not Barrio:
                    if Data_L["Localidad_ID"]:
                        Barrio = T_Barrio(Nombre=Barrio_Norm, Localidad_ID=int(Data_L["Localidad_ID"]))
                        db.session.add(Barrio)
                        db.session.flush()
                    else:
                        Barrio = T_Barrio(Nombre=Barrio_Norm, Localidad_ID=Localidad.ID)
                        db.session.add(Barrio)
                        db.session.flush()  

        if Data_C:
            Data_C["Barrio_ID"] = Barrio.ID
            Caso = Tabla_Caso(**Data_C)
            db.session.add(Caso)
            db.session.flush()            

            Radicados = Tabla_Radicado.query.order_by(Tabla_Radicado.ID.desc()).first()
            Radicado_text = int(Radicados.Radicado.rstrip("R"))+1
            Radicado_com = f"{Radicado_text:06d}R"          
            Radicado_Final = Tabla_Radicado(Radicado=Radicado_com, Caso_ID=Caso.ID)
            db.session.add(Radicado_Final)
            db.session.flush() 

        if Data_R.get("Relacion_Radicado"):
            Caso_a_Relacionar = Tabla_Caso.query.filter_by(ID=Data_R["Relacion_Radicado"]).first()
            if not Caso_a_Relacionar:
                return False
            else:
                Relacion = Tabla_Casos_a_Casos(Caso_Principal_ID=Caso.ID,Caso_Asociado_ID=int(Data_R["Relacion_Radicado"]), Tipo_Relacion_ID=int(Data_R["Relacion_Tipo"]))
                db.session.add(Relacion)
                db.session.flush()

        Caso_json = Caso.to_dict(include_relationships=True)
        Caso_json_text = json.dumps(Caso_json, default=str, ensure_ascii=False)

        if Data_C_C["Mensaje"]:
            Data_C_C["Caso_ID"] = Caso.ID
            Caso_Discucion = Tabla_Discusion(**Data_C_C)
            db.session.add(Caso_Discucion)
            db.session.flush()

        Auditoria = Tabla_Auditoria(Accion="Caso creado", Anterior=Caso_json_text, Modificado_Por=Data_C_C["Usuario_ID"], Caso_ID=Caso.ID)
        db.session.add(Auditoria)
        db.session.commit()

        requests.post("http://127.0.0.1:5007/email",
            json={
                "Template": "Caso_Creado",
                "Datos": {
                    "Nombre": Caso_json["usuario_creador"]["Persona"]["Primer_Nombre"]+" "+Caso_json["usuario_creador"]["Persona"]["Primer_Apellido"], 
                    "Radicado": Caso_json["radicados"][0]["Radicado"], 
                    },
                "Correo": Caso_json["usuario_creador"]["Correo"],
                "Asunto": f"Caso {Caso_json["radicados"][0]["Radicado"]} creado"
            }
        )
        return Caso
    @staticmethod
    def Read_All():
        Casos = Tabla_Caso.query.filter(Tabla_Caso.Estado_Caso_ID != 4).order_by(Tabla_Caso.ID.asc()).all()
        return Casos
    @staticmethod
    def Read_One(Case_ID):
        Caso = Tabla_Caso.query.get(Case_ID)

        if not Caso:
            return False

        return Caso
    @staticmethod
    def Read_By(Field, Value):
        if not hasattr(Tabla_Caso, Field):
            return False
        Column = getattr(Tabla_Caso, Field)
        Casos = Tabla_Caso.query.filter(Column.ilike(f"%{Value}%")).all()
        return Casos
    @staticmethod
    def Update(Case_ID, Data_C, Data_C_C, Data_L, Data_R):
        Caso = Tabla_Caso.query.get(Case_ID)
        Caso_json = Caso.to_dict(include_relationships=True)
        Caso_json_text = json.dumps(Caso_json, default=str, ensure_ascii=False)
        if not Caso:
            return False
        
        if Data_L:
            if Data_L["Departamento_ID"]:
                Departamento = T_Departamento.query.get(int(Data_L["Departamento_ID"]))
            else:
                Departamento_Norm = Data_L["Departamento"].capitalize().strip()
                Departamento = T_Departamento.query.filter_by(Nombre=Departamento_Norm).first()
                if not Departamento:
                    Departamento = T_Departamento(Nombre=Departamento_Norm, Pais_ID=1)
                    db.session.add(Departamento)
                    db.session.flush()
            if Data_L["Ciudad_ID"]:
                Ciudad = T_Ciudad.query.get(int(Data_L["Ciudad_ID"]))
            else:
                Ciudad_Norm = Data_L["Ciudad"].capitalize().strip()
                Ciudad = T_Ciudad.query.filter_by(Nombre=Ciudad_Norm).first()
                if not Ciudad:
                    if Data_L["Departamento_ID"]:
                        Ciudad = T_Ciudad(Nombre=Ciudad_Norm, Departamento_ID=int(Data_L["Departamento_ID"]))
                        db.session.add(Ciudad)
                        db.session.flush()
                    else:
                        Ciudad = T_Ciudad(Nombre=Ciudad_Norm, Departamento_ID=Departamento.ID)
                        db.session.add(Ciudad)
                        db.session.flush() 
            if Data_L["Localidad_ID"]:
                Localidad = T_Localidad.query.get(int(Data_L["Localidad_ID"]))       
            else:
                Localidad_Norm = Data_L["Localidad"].capitalize().strip()
                Localidad = T_Localidad.query.filter_by(Nombre=Localidad_Norm).first()
                if not Localidad:
                    if Data_L["Ciudad_ID"]:
                        Localidad = T_Localidad(Nombre=Localidad_Norm, Ciudad_ID=int(Data_L["Ciudad_ID"]))
                        db.session.add(Localidad)
                        db.session.flush()                        
                    else:
                        Localidad = T_Localidad(Nombre=Localidad_Norm, Ciudad_ID=Ciudad.ID)  
                        db.session.add(Localidad)
                        db.session.flush()   
            if Data_L["Barrio_ID"]:
                Barrio = T_Barrio.query.get(int(Data_L["Barrio_ID"]))
            else:
                Barrio_Norm = Data_L["Barrio"].capitalize().strip()
                Barrio = T_Barrio.query.filter_by(Nombre=Barrio_Norm).first()
                if not Barrio:
                    if Data_L["Localidad_ID"]:
                        Barrio = T_Barrio(Nombre=Barrio_Norm, Localidad_ID=int(Data_L["Localidad_ID"]))
                        db.session.add(Barrio)
                        db.session.flush()
                    else:
                        Barrio = T_Barrio(Nombre=Barrio_Norm, Localidad_ID=Localidad.ID)
                        db.session.add(Barrio)
                        db.session.flush()        

        Estado_Correo = Tabla_Estado.query.get(int(Data_C['Estado_Caso_ID']))
        if not Estado_Correo:
            return False

        nuevo_estado = int(Data_C['Estado_Caso_ID'])
        anterior_estado = Caso.Estado_Caso_ID

        if Data_C:
            Caso.Creacion = Data_C['Creacion']
            Caso.Nombre = Data_C['Nombre']
            Caso.Descripcion = Data_C['Descripcion']
            Caso.Afectados = Data_C['Afectados']
            Caso.Direccion = Data_C['Direccion']
            Caso.Usuario_Creador_ID = int(Data_C['Usuario_Creador_ID'])
            Caso.Usuario_Asociado_ID = int(Data_C['Usuario_Asociado_ID'])
            Caso.Incidente_ID = int(Data_C['Incidente_ID'])
            Caso.Estado_Caso_ID = int(Data_C['Estado_Caso_ID'])
            Caso.Prioridad_ID = int(Data_C['Prioridad_ID'])
            Caso.Creacion = Data_C['Creacion']
            Caso.Barrio_ID = Barrio.ID
            db.session.flush()

        if Data_C_C["Mensaje"]:
            Caso_Discucion = Tabla_Discusion(**Data_C_C)
            db.session.add(Caso_Discucion)
            db.session.flush()

        if Data_R.get("Relacion_Radicado"):
            Caso_a_Relacionar = Tabla_Caso.query.filter_by(ID=Data_R["Relacion_Radicado"]).first()
            if not Caso_a_Relacionar:
                return False
            else:
                Relacion = Tabla_Casos_a_Casos(Caso_Principal_ID=Caso.ID,Caso_Asociado_ID=int(Data_R["Relacion_Radicado"]), Tipo_Relacion_ID=int(Data_R["Relacion_Tipo"]))
                db.session.add(Relacion)
                db.session.flush()

        Auditoria = Tabla_Auditoria(Accion="Caso modificado", Anterior=Caso_json_text, Modificado_Por=Data_C_C["Usuario_ID"], Caso_ID=Case_ID)
        db.session.add(Auditoria)
        db.session.commit()

        if nuevo_estado == 3 and nuevo_estado != anterior_estado:
            requests.post("http://127.0.0.1:5007/email",
                json={
                    "Template": "Caso_Resuelto",
                    "Datos": {
                        "Nombre": Caso_json["usuario_creador"]["Persona"]["Primer_Nombre"]+" "+Caso_json["usuario_creador"]["Persona"]["Primer_Apellido"], 
                        "Radicado": Caso_json["radicados"][0]["Radicado"], 
                        "Estado": Estado_Correo.Nombre},
                    "Correo": Caso_json["usuario_creador"]["Correo"],
                    "Asunto": f"Caso {Caso_json["radicados"][0]["Radicado"]} resuelto"
                }
            )    
        elif nuevo_estado != 3:
            if nuevo_estado != anterior_estado:
                requests.post("http://127.0.0.1:5007/email",
                    json={
                        "Template": "Caso_Cambio",
                        "Datos": {
                            "Nombre": Caso_json["usuario_creador"]["Persona"]["Primer_Nombre"]+" "+Caso_json["usuario_creador"]["Persona"]["Primer_Apellido"], 
                            "Radicado": Caso_json["radicados"][0]["Radicado"], 
                            "Estado": Estado_Correo.Nombre},
                        "Correo": Caso_json["usuario_creador"]["Correo"],
                        "Asunto": "Cambio en el estado del caso"
                    }
                )        

        return Caso
    @staticmethod
    def Delete(Case_ID, User_ID):
        Caso = Tabla_Caso.query.get(Case_ID)
        Caso_json_text = json.dumps(Caso.to_dict(include_relationships=True), default=str, ensure_ascii=False)

        if not Caso:
            return False
        
        Caso.Estado_Caso_ID = 4

        Auditoria = Tabla_Auditoria(Accion="Caso eliminado", Anterior=Caso_json_text, Modificado_Por=User_ID, Caso_ID=Caso.ID)
        db.session.add(Auditoria)
        db.session.commit()

        return Caso
    @staticmethod
    def Obtener_Datos():
        Usuarios = Tabla_Usuario.query.order_by(Tabla_Usuario.ID.asc()).all()
        Estados = Tabla_Estado.query.filter(Tabla_Estado.ID != 4).order_by(Tabla_Estado.ID.asc()).all()
        Prioridades = Tabla_Prioridad.query.order_by(Tabla_Prioridad.ID.asc()).all()
        Incidentes = Tabla_Incidente.query.order_by(Tabla_Incidente.ID.asc()).all()
        Barrios = Tabla_Barrio.query.order_by(Tabla_Barrio.ID.asc()).all()
        Localidades = Tabla_Localidad.query.order_by(Tabla_Localidad.ID.asc()).all()
        Ciudades = Tabla_Ciudad.query.order_by(Tabla_Ciudad.ID.asc()).all()
        Departamentos = Tabla_Dep.query.order_by(Tabla_Dep.ID.asc()).all()
        Relaciones = Tabla_Relacion.query.filter(Tabla_Relacion.ID != 4).order_by(Tabla_Relacion.ID.asc()).all()

        return Usuarios, Estados, Prioridades, Incidentes, Barrios, Localidades, Ciudades, Departamentos, Relaciones
    @staticmethod
    def Delete_Relacion(CasoHijo_Rad, CasePadre_Rad, Tipo_Relacion, User_ID):
        Caso_Padre = Tabla_Radicado.query.filter(Tabla_Radicado.Radicado == CasePadre_Rad).first()
        Caso_Hijo = Tabla_Radicado.query.filter(Tabla_Radicado.Radicado == CasoHijo_Rad).first()

        Relacion = Tabla_Casos_a_Casos.query.filter(Tabla_Casos_a_Casos.Caso_Principal_ID == Caso_Padre.ID).filter(Tabla_Casos_a_Casos.Caso_Asociado_ID == Caso_Hijo.ID).filter(Tabla_Casos_a_Casos.Tipo_Relacion_ID == Tipo_Relacion).first()
        Relacion2 = Relacion.to_dict2()
        Relacion2_text = json.dumps(Relacion2, default=str, ensure_ascii=False)
        Auditoria = Tabla_Auditoria(Accion="Relacion Eliminada", Anterior=Relacion2_text, Modificado_Por=User_ID, Caso_ID=Caso_Padre.ID)
        db.session.add(Auditoria)        
        db.session.delete(Relacion)

        db.session.commit()        
        return Caso_Padre
    @staticmethod
    def Linea_Tiempo():
        Auditoria = Tabla_Auditoria.query.order_by(Tabla_Auditoria.ID.asc()).all()
        if not Auditoria:
            return False
        return Auditoria