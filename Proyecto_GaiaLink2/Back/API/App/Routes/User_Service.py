from flask import Blueprint, request, jsonify
from App.Rate_Limit import Rate_Limit
import requests
import os

User_Service_Bp = Blueprint("User_Service", __name__)

MICROSERVICE_URL = os.getenv("USER_URL")
DEFAULT_LIMIT = os.getenv("DEFAULT_LIMIT")

@User_Service_Bp.route("/registro", methods=["POST"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["POST"])
def Api_User_Registro():
    Data = request.get_json()
    Respuesta = requests.post(f"{MICROSERVICE_URL}/registro", json=Data, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code

@User_Service_Bp.route("/registro/codigo", methods=["POST"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["POST"])
def Api_User_Codigo():
    Data = request.get_json()
    Respuesta = requests.post(f"{MICROSERVICE_URL}/codigo", json=Data, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code
