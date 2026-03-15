from flask import Blueprint, request, jsonify
import requests

Auth_Service_Bp = Blueprint("Auth_Service", __name__)

MICROSERVICE_URL = "http://localhost:5008/auth"

@Auth_Service_Bp.route("/api/login", methods=["POST"])
def Api_Auth_Login():
    Data = request.get_json()
    Respuesta = requests.post(f"{MICROSERVICE_URL}/login", json=Data)

    return jsonify(Respuesta.json()), Respuesta.status_code

