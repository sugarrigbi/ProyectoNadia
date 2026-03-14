from flask import request, jsonify, Response, json
from App.Services.Case_Logic import Case_Service

class Get_Case:
    @staticmethod
    def Case_Create():
        Data = request.get_json()
        
        if not Data:
            return jsonify({"Error": "No data provided"}), 400
        
        Caso = Case_Service.Create(Data)
        if not Caso:
            return jsonify({"Error": "Case creation failed"}), 400
        return jsonify({"Message": "Case created successfully"}), 201
    @staticmethod
    def Case_Read_All():
        Casos = Case_Service.Read_All()
        if not Casos:
            return jsonify({"Error", "No cases found"}), 404
        return Response(json.dumps([C.to_dict() for C in Casos], ensure_ascii=False, indent=2), status=200, mimetype='application/json')
    @staticmethod
    def Case_Read_One(Case_ID):
        Caso = Case_Service.Read_One(Case_ID)

        if not Caso:
            return jsonify({"Error", "No cases found"}), 404
        
        return Response(json.dumps(Caso.to_dict(), ensure_ascii=False, indent=2), status=200, mimetype='application/json')
    @staticmethod
    def Case_Read_By(Field, Value):
        Casos = Case_Service.Read_By(Field, Value)
        if not Casos:
            return jsonify({"Error", "No cases found"}), 404
        return Response(json.dumps([C.to_dict() for C in Casos], ensure_ascii=False, indent=2), status=200, mimetype='application/json')
    @staticmethod
    def Case_Update(Case_ID):
        Data = request.get_json()
        if not Data:
            return jsonify({"Error": "No data provided"}), 400
        
        Caso = Case_Service.Update(Case_ID, Data)
        if not Caso:
            return jsonify({"Error": "No case found"}), 404
        
        return jsonify({"Message": "Case updated successfully"}), 200
    @staticmethod
    def Case_Delete(Case_ID):
        Caso = Case_Service.Delete(Case_ID)
        if not Caso:
            return jsonify({"Error": "No case found"}), 404
        return jsonify({"Message": "Case deleted successfully"}), 200
        