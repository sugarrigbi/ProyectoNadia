from flask import Blueprint, request, jsonify
from App.Rate_Limit import Rate_Limit
import requests
import os

Account_Service_Bp = Blueprint("Account_Service", __name__)

MICROSERVICE_URL = os.getenv("ACCOUNT_URL")
DEFAULT_LIMIT = os.getenv("DEFAULT_LIMIT")

@Account_Service_Bp.route("/device/delete/<int:Device_ID>", methods=["PUT"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["PUT"])
def Api_Device_Delete(Device_ID):
    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}

    Respuesta = requests.put(f"{MICROSERVICE_URL}/device/delete/{Device_ID}", headers=Header, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Account_Service_Bp.route("/account/mfa", methods=["PUT"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["PUT"])
def Api_Change_Mfa():
    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}

    Respuesta = requests.put(f"{MICROSERVICE_URL}/mfa", headers=Header, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code  

@Account_Service_Bp.route("/account/data", methods=["GET"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["GET"])
def Api_Read_Data():
    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}

    Respuesta = requests.get(f"{MICROSERVICE_URL}/account/data", headers=Header, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code    

@Account_Service_Bp.route("/account/update", methods=["PUT"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["PUT"])
def Api_Update_User():
    Data = request.get_json()

    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}

    Respuesta = requests.put(f"{MICROSERVICE_URL}/account/update", json=Data, headers=Header, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Account_Service_Bp.route("/account/update/place", methods=["PUT"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["PUT"])
def Api_Update_Place():
    Data = request.get_json()

    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}   

    Respuesta = requests.put(f"{MICROSERVICE_URL}/account/update/place", json=Data, headers=Header, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Account_Service_Bp.route("/account/update/password", methods=["PUT"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["PUT"])
def Api_Update_Password():
    Data = request.get_json()

    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}   

    Respuesta = requests.put(f"{MICROSERVICE_URL}/account/update/password", json=Data, headers=Header, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Account_Service_Bp.route("/account/update/image", methods=["PUT"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["PUT"])
def Api_Update_Image():
    Image = request.files.get("imagen_usuario")
    Archivo = {"imagen_usuario": (Image.filename, Image.stream, Image.mimetype)} 

    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}   

    Respuesta = requests.put(f"{MICROSERVICE_URL}/account/update/image", files=Archivo, headers=Header, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Account_Service_Bp.route("/account/delete/image", methods=["PUT"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["PUT"])
def Api_Delete_Image():
    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}   

    Respuesta = requests.put(f"{MICROSERVICE_URL}/account/delete/image", headers=Header, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Account_Service_Bp.route("/account/delete/devices", methods=["PUT"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["PUT"])
def Api_Delete_Devices():
    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}

    Respuesta = requests.put(f"{MICROSERVICE_URL}/account/delete/devices", headers=Header, timeout=5)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Account_Service_Bp.route("/account/delete/account", methods=["PUT"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["PUT"])
def Api_Delete_Account():
    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}

    Respuesta = requests.put(f"{MICROSERVICE_URL}/account/delete/account", headers=Header, timeout=5)
    return jsonify(Respuesta.json()), Respuesta.status_code