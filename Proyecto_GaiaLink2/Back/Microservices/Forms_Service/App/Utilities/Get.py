from flask import Response, request, jsonify, json
from App.Services.Forms_logic import Forms_Service

class Get_Forms:
    @staticmethod
    def Get_Create(Tabla_Form):
        Data = request.get_json()
        if not Data:
            return jsonify({"Error": "No data provided"}), 400
        
        Formulario = Forms_Service.Form_Create(Tabla_Form, Data)
        if not Formulario:
            return jsonify({"Error": "Form creation failed"}), 400
        
        return jsonify({"Message": "Form created successfully"}), 201
    @staticmethod
    def Get_Read_All(Tabla_Form):
        Formularios = Forms_Service.Form_Read_All(Tabla_Form)
        if not Formularios:
            return jsonify({"Error": "No forms found"}), 404
        return Response(json.dumps([F.to_dict() for F in Formularios], ensure_ascii=False, indent=2), status=200, mimetype='application/json')
    @staticmethod
    def Get_Read_One(Tabla_Form, Forms_ID):
        Formulario = Forms_Service.Form_Read_One(Tabla_Form, Forms_ID)
        if not Formulario:
            return jsonify({"Error": "No form found"}), 404
        return Response(json.dumps(Formulario.to_dict(), ensure_ascii=False, indent=2), status=200, mimetype='application/json')
    @staticmethod
    def Get_Read_By(Tabla_Form, Field, Value):
        Formularios = Forms_Service.Form_Read_By(Tabla_Form, Field, Value)
        if not Formularios:
            return jsonify({"Error": "No forms found"}), 404
        return Response(json.dumps([F.to_dict() for F in Formularios], ensure_ascii=False, indent=2), status=200, mimetype='application/json')                        