from App.Services.Entity_Logic import Entity_Service
from flask import request, jsonify, Response, json

class Get_Entity:
    @staticmethod
    def Get_Create():
        Data = request.get_json()

        if not Data:
            return jsonify({"Error": "No data provided"}), 400
        Entidad = Entity_Service.Create(Data)
        if not Entidad:
            return jsonify({"Error": "Entity creation failed"}), 400
        return jsonify({"Message": "Entity created successfully"}), 201
    @staticmethod
    def Get_Read_All():
        Entidades = Entity_Service.Read_All()
        if not Entidades:
            return jsonify({"Error": "No entitys found"}), 404
        return Response(json.dumps([E.to_dict() for E in Entidades], ensure_ascii=False, indent=2), status=200, mimetype='application/json')
    @staticmethod
    def Get_Read_One(Entity_ID):
        Entidad = Entity_Service.Read_One(Entity_ID)
        if not Entidad:
            return jsonify({"Error": "No entity found"}), 404
        return Response(json.dumps(Entidad.to_dict(), ensure_ascii=False, indent=2), status=200, mimetype='application/json')
    @staticmethod
    def Get_Read_By(Field, Value):
        Entidades = Entity_Service.Read_By(Field, Value)
        if not Entidades:
            return jsonify({"Error": "No entitys found"}), 404
        return Response(json.dumps([E.to_dict() for E in Entidades], ensure_ascii=False, indent=2), status=200, mimetype='application/json')
    @staticmethod
    def Get_Update(Entity_ID):
        Data = request.get_json()
        if not Data:
            return jsonify({"Error": "No data provided"}), 400
        
        Entidad = Entity_Service.Update(Entity_ID, Data)
        if not Entidad:
            return jsonify({"Error":"No entity found"}), 404
        
        return jsonify({"Message": "Entity updated successfully"}), 200
    @staticmethod
    def Get_Delete(Entity_ID):
        Entidad = Entity_Service.Delete(Entity_ID)
        if not Entidad:
            return jsonify({"Error":"No entity found"}), 404
        return jsonify({"Message": "Entity deleted successfully"}), 200

