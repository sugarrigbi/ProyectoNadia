from flask import Blueprint, request, jsonify
import requests
from App.Rate_Limit import Rate_Limit, DEFAULT_LIMIT

Account_Service_Bp = Blueprint("Account_Service", __name__)

MICROSERVICE_URL = "http://localhost:5002"

@Account_Service_Bp.route("/api/device/read/all", methods=["GET"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["GET"])
def Api_Device_Read_All():
    Auth = request.headers.get("Authorization")
    Headers = {"Authorization": Auth}

    Respuesta = requests.get(f"{MICROSERVICE_URL}/device/read/all", headers=Headers)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Account_Service_Bp.route("/api/device/delete/<int:Device_ID>", methods=["PUT"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["PUT"])
def Api_Device_Delete(Device_ID):
    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}

    Respuesta = requests.put(f"{MICROSERVICE_URL}/device/delete/{Device_ID}", headers=Header)
    return jsonify(Respuesta.json()), Respuesta.status_code
