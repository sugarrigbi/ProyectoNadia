from flask import Blueprint, request, jsonify
import requests
from App.Rate_Limit import Rate_Limit, DEFAULT_LIMIT

User_Service_Bp = Blueprint("User_Service", __name__)

MICROSERVICE_URL = "http://localhost:5006/user"

@User_Service_Bp.route("/api/registro", methods=["POST"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["POST"])
def Api_User_Registro():
    Data = request.get_json()
    Respuesta = requests.post(f"{MICROSERVICE_URL}/registro", json=Data, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code

@User_Service_Bp.route("/api/registro/codigo", methods=["POST"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["POST"])
def Api_User_Codigo():
    Data = request.get_json()
    Respuesta = requests.post(f"{MICROSERVICE_URL}/codigo", json=Data, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code
