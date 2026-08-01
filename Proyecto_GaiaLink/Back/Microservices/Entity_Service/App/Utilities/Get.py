from App.Services.Entity_Logic import Entity_Service
from flask import request, jsonify, Response, json
from App.Utilities.Util import Validar_JWT

class Get_Entity:
    @staticmethod
    def Get_Create():
        Data = request.get_json()
        if not Data:
            return jsonify({"Error": "No data provided"}), 400
        
        Auth_Data, Error = Validar_JWT()
        if Error:
            if Error in ["Token expirado", "Token inválido"]:
                return jsonify({"Error": Error}), 401
            return jsonify({"Error": Error}), 400
        User_ID = Auth_Data["user_id"]

        Entidad = Entity_Service.Create(Data, User_ID)
        if Entidad == "Auth":
            return jsonify({"Error": "No Auth"}), 403
        if not Entidad:
            return jsonify({"Error": "Entity creation failed"}), 400
        return jsonify({"Message": "Entity created successfully"}), 201
    @staticmethod
    def Get_Read_All():
        Auth_Data, Error = Validar_JWT()
        if Error:
            if Error in ["Token expirado", "Token inválido"]:
                return jsonify({"Error": Error}), 401
            return jsonify({"Error": Error}), 400
        User_ID = Auth_Data["user_id"]

        Entidades = Entity_Service.Read_All(User_ID)
        Datos_Obtener = Entity_Service.Obtener_Datos(User_ID)     
        if Entidades == "Auth":
            return jsonify({"Error": "No Auth"}), 403
        if not Entidades or not Datos_Obtener:
            return jsonify({"Error": "No entities found"}), 404
        
        return Response(json.dumps({"Entidades": [E.to_dict() for E in Entidades], "Datos": Datos_Obtener}, ensure_ascii=False, indent=2), status=200, mimetype='application/json')
    @staticmethod
    def Get_Read_By(Filtros):
        Auth_Data, Error = Validar_JWT()
        if Error:
            if Error in ["Token expirado", "Token inválido"]:
                return jsonify({"Error": Error}), 401
            return jsonify({"Error": Error}), 400
        User_ID = Auth_Data["user_id"]

        Entidades = Entity_Service.Read_By(Filtros, User_ID)
        Datos_Obtener = Entity_Service.Obtener_Datos(User_ID)            
        if Entidades == "Auth":
            return jsonify({"Error": "No Auth"}), 403
        if not Entidades or not Datos_Obtener:
            return jsonify({"Error": "No entities found"}), 404
        return Response(json.dumps({"Entidades": [E.to_dict() for E in Entidades], "Datos": Datos_Obtener}, ensure_ascii=False, indent=2), status=200, mimetype='application/json')
    @staticmethod
    def Get_Update(Entity_ID):
        Data = request.get_json()
        if not Data:
            return jsonify({"Error": "No data provided"}), 400

        Auth_Data, Error = Validar_JWT()
        if Error:
            if Error in ["Token expirado", "Token inválido"]:
                return jsonify({"Error": Error}), 401
            return jsonify({"Error": Error}), 400
        User_ID = Auth_Data["user_id"]

        Entidad = Entity_Service.Update(Entity_ID, Data, User_ID)
        if Entidad == "Auth":
            return jsonify({"Error": "No Auth"}), 403
        if not Entidad:
            return jsonify({"Error": "No entity found"}), 404
        return jsonify({"Message": "Entity updated successfully"}), 200
    @staticmethod
    def Get_Delete(Entity_ID):
        Auth_Data, Error = Validar_JWT()
        if Error:
            if Error in ["Token expirado", "Token inválido"]:
                return jsonify({"Error": Error}), 401
            return jsonify({"Error": Error}), 400
        User_ID = Auth_Data["user_id"]

        Entidad = Entity_Service.Delete(Entity_ID, User_ID)
        if Entidad == "Auth":
            return jsonify({"Error": "No Auth"}), 403
        if not Entidad:
            return jsonify({"Error": "No entity found"}), 404
        return jsonify({"Message": "Entity deleted successfully"}), 200

