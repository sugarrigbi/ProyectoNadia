from flask import request, jsonify, Response, json
from App.Services.Case_Logic import Case_Service

class Get_Case:
    @staticmethod
    def Case_Create():
        Data = request.get_json()
        if not Data:
            return jsonify({"Error": "No data provided"}), 400
        
        Data_C = {
            "Nombre": Data["CasoNuevo_Nombre"],
            "Descripcion": Data["CasoNuevo_Descripcion"],
            "Usuario_Creador_ID": Data["CasoNuevo_Usuario_Creador"],
            "Usuario_Asociado_ID": Data["CasoNuevo_Usuario_Cargo"],
            "Creacion": Data["CasoNuevo_Fecha_Creacion"],
            "Estado_Caso_ID": Data["CasoNuevo_Estado"],
            "Prioridad_ID": Data["CasoNuevo_Prioridad"],
            "Incidente_ID": Data["CasoNuevo_Incidente"],
            "Afectados": Data["CasoNuevo_Afectados"],
            "Direccion": Data["CasoNuevo_Direccion"]
        }
        Data_C_C = {
            "Mensaje": Data["CasoNuevo_Comentario"],
            "Usuario_ID": Data["Usuario_Id"]
        }
        Data_L = {
            "Barrio": Data["Caso_Barrio_Nombre"],
            "Barrio_ID": Data["Caso_Barrio_ID"],
            "Localidad": Data["Caso_Localidad_Nombre"],
            "Localidad_ID": Data["Caso_Localidad_ID"],
            "Ciudad": Data["Caso_Ciudad_Nombre"],
            "Ciudad_ID": Data["Caso_Ciudad_ID"],
            "Departamento": Data["Caso_Departamento_Nombre"],
            "Departamento_ID": Data["Caso_Departamento_ID"]
        }
        if Data.get('CasoNuevo_Relacion_Radicado') and Data.get("CasoNuevo_Relacion_Tipo"):
            Data_R = {
                "Relacion_Radicado": Data['CasoNuevo_Relacion_Radicado'],
                "Relacion_Tipo": Data['CasoNuevo_Relacion_Tipo']
            }
        else:
            Data_R = {}        
        
        Caso = Case_Service.Create(Data_C, Data_C_C, Data_L, Data_R)
        if not Caso:
            return jsonify({"Error": "Case creation failed"}), 400
        return jsonify({"Message": "Case created successfully"}), 201
    @staticmethod
    def Case_Read_All():
        Casos = Case_Service.Read_All()
        if not Casos:
            return jsonify({"Error": "No cases found"}), 404
        Casos_Dict = []

        for C in Casos:
            Data = C.to_dict(include_relationships=True)
            Data["Creacion"] = Data["Creacion"].split("T")[0]
            Casos_Dict.append(Data)

        return Response(json.dumps(Casos_Dict, ensure_ascii=False, indent=2), status=200, mimetype='application/json')
    @staticmethod
    def Case_Read_One(Case_ID):
        Caso = Case_Service.Read_One(Case_ID)
        if not Caso:
            return jsonify({"Error", "No cases found"}), 404
        
        Data = Caso.to_dict(include_relationships=True)
        Data["Creacion"] = Data["Creacion"].split("T")[0]       
        
        return Response(json.dumps(Data, ensure_ascii=False, indent=2), status=200, mimetype='application/json')
    @staticmethod
    def Case_Read_By(Filtros):
        Casos = Case_Service.Read_By(Filtros)
        if not Casos:
            return jsonify({"Error", "No cases found"}), 404
        Casos_Dict = []

        for C in Casos:
            Data = C.to_dict(include_relationships=True)
            Data["Creacion"] = Data["Creacion"].split("T")[0]
            Casos_Dict.append(Data)        

        return Response(json.dumps(Casos_Dict, ensure_ascii=False, indent=2), status=200, mimetype='application/json')
    @staticmethod
    def Case_Update(Case_ID):
        Data = request.get_json()
        if not Data:
            return jsonify({"Error": "No data provided"}), 400
        
        Data_C = {
            "ID": Data["Caso_Id"],
            "Creacion": Data['Caso_Fecha_Creacion'], 
            "Nombre": Data["Caso_Nombre"], 
            "Descripcion": Data["Caso_Descripcion"], 
            "Afectados": Data["Caso_Afectados"], 
            "Direccion": Data["Caso_Direccion"], 
            "Usuario_Creador_ID": Data["Caso_Usuario_Creador"], 
            "Usuario_Asociado_ID": Data["Caso_Usuario_Cargo"],
            "Incidente_ID": Data["Caso_Incidente"], 
            "Estado_Caso_ID": Data["Caso_Estado"], 
            "Prioridad_ID": Data["Caso_Prioridad"], 
            "Barrio_ID": Data["Caso_Barrio_ID"]
        }            
        Data_C_C = {
            "Caso_ID": Data['Caso_Id'], 
            "Usuario_ID": Data['Usuario_Id'], 
            "Mensaje": Data['Caso_Comentario']       
        }
        Data_L = {
            "Barrio": Data['Caso_Barrio_Nombre'],
            "Barrio_ID": Data['Caso_Barrio_ID'],
            "Localidad": Data['Caso_Localidad_Nombre'],
            "Localidad_ID": Data['Caso_Localidad_ID'],
            "Ciudad": Data['Caso_Ciudad_Nombre'],
            "Ciudad_ID": Data['Caso_Ciudad_ID'],
            "Departamento": Data['Caso_Departamento_Nombre'],
            "Departamento_ID": Data['Caso_Departamento_ID']
        }
        if Data.get('Caso_Relacion_Radicado') and Data.get("Caso_Relacion_Tipo"):
            Data_R = {
                "Relacion_Radicado": Data['Caso_Relacion_Radicado'],
                "Relacion_Tipo": Data['Caso_Relacion_Tipo']
            }
        else:
            Data_R = {}

        Caso = Case_Service.Update(Case_ID, Data_C, Data_C_C, Data_L, Data_R)
        if not Caso:
            return jsonify({"Error": "No case found"}), 404
        
        return jsonify({"Message": "Case updated successfully"}), 200
    @staticmethod
    def Case_Delete(Case_ID, User_ID):
        Caso = Case_Service.Delete(Case_ID, User_ID)
        if not Caso:
            return jsonify({"Error": "No case found"}), 404
        return jsonify({"Message": "Case deleted successfully"}), 200
    @staticmethod
    def Case_Data():
        Usuarios, Estados, Prioridades, Incidentes, Barrios, Localidades, Ciudades, Departamentos, Relaciones = Case_Service.Obtener_Datos()
        Data = {
            "Usuarios": [u.to_dict() for u in Usuarios],
            "Estados": [u.to_dict() for u in Estados],
            "Prioridades": [u.to_dict() for u in Prioridades],
            "Incidentes": [u.to_dict() for u in Incidentes],
            "Barrios": [u.to_dict() for u in Barrios],
            "Localidades": [u.to_dict() for u in Localidades],
            "Ciudades": [u.to_dict() for u in Ciudades],
            "Departamentos": [u.to_dict() for u in Departamentos],
            "Relaciones": [u.to_dict() for u in Relaciones]
        }
        if not Usuarios or not Estados or not Prioridades or not Incidentes or not Barrios or not Localidades or not Ciudades or not Departamentos or not Relaciones:
            return jsonify({"Error": "No cases found"}), 404
        return jsonify(Data), 200
    @staticmethod
    def Delete_Relacion(CasePadre_Rad, CasoHijo_Rad, Tipo_Relacion, User_ID):
        Caso = Case_Service.Delete_Relacion(CasePadre_Rad, CasoHijo_Rad, Tipo_Relacion, User_ID)
        if not Caso:
            return jsonify({"Error": "No relation found"}), 404
        return jsonify({"Message": "Relation deleted successfully"}), 200
    @staticmethod
    def Case_Read_Linea():
        Linea = Case_Service.Linea_Tiempo()
        if not Linea:
            return jsonify({"Error": "No info found"}), 404
        return Response(json.dumps([L.to_dict2() for L in Linea], ensure_ascii=False, indent=2), status=200, mimetype='application/json')    