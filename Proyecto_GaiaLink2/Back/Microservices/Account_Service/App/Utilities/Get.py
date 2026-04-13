from App.Services.Account_Logic import Account_Service
from flask import Response, jsonify
import json
from App.Utilities.Util import Validar_JWT

class Get_Account:
    @staticmethod
    def Device_Read():
        Auth_Data, Error = Validar_JWT()
        if Error:
            if Error in ["Token expirado", "Token invalido"]:
                return jsonify({"Error": Error}), 401
            return jsonify({"Error": Error}), 400
        User_ID = Auth_Data["user_id"]

        Dispositivos = Account_Service.Read_Devices(User_ID)
        if Dispositivos == "Auth":
            return jsonify({"Error": "No auth"}), 403
        
        return Response(json.dumps([D.to_dict() for D in Dispositivos], ensure_ascii=False, indent=2), status=200, mimetype='application/json')
    @staticmethod
    def Device_Delete(Device_ID):
        Auth_Data, Error = Validar_JWT()
        if Error:
            if Error in ["Token expirado", "Token invalido"]:
                return jsonify({"Error": Error}), 401
            return jsonify({"Error": Error}), 400
        User_ID = Auth_Data["user_id"]

        Dispositivo = Account_Service.Delete_Device(User_ID, Device_ID)
        if Dispositivo == "Auth":
            return jsonify({"Error": "No auth"}), 403
        if not Dispositivo:
            return jsonify({"Error": "No device found"}), 404
        
        return jsonify({"Message": "Device deleted successfully"}), 200