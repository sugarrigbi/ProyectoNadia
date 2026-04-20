from flask import Blueprint, request, jsonify
import requests
from App.Rate_Limit import Rate_Limit, DEFAULT_LIMIT

Auth_Service_Bp = Blueprint("Auth_Service", __name__)

MICROSERVICE_URL = "http://localhost:5008/auth"

@Auth_Service_Bp.route("/api/login", methods=["POST"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["POST"])
def Api_Auth_Login():
    Data = request.get_json()
    Ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    Data["Client_IP"] = Ip

    Respuesta = requests.post(f"{MICROSERVICE_URL}/login", json=Data, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code
@Auth_Service_Bp.route("/api/login/mfa", methods=["POST"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["POST"])
def Api_Auth_Login_Mfa():
    Data = request.get_json()

    Respuesta = requests.post(f"{MICROSERVICE_URL}/login/mfa", json=Data, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Auth_Service_Bp.route("/api/recuperar", methods=["POST"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["POST"])
def Api_Auth_Recuperar():
    Data = request.get_json()
    Respuesta = requests.post(f"{MICROSERVICE_URL}/recuperar", json=Data, timeout=10)

    return jsonify(Respuesta.json()), Respuesta.status_code

@Auth_Service_Bp.route("/api/recuperar/codigo", methods=["POST"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["POST"])
def Api_Auth_Recuperar_Codigo():
    Data = request.get_json()
    Respuesta = requests.post(f"{MICROSERVICE_URL}/recuperar/codigo", json=Data, timeout=10)

    return jsonify(Respuesta.json()), Respuesta.status_code

