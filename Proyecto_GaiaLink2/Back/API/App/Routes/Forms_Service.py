from flask import Blueprint, request, jsonify
import requests
from App.Rate_Limit import Rate_Limit, DEFAULT_LIMIT

Forms_Service_Bp = Blueprint("Forms_Service", __name__)

MICROSERVICE_URL = "http://localhost:5005/forms"

@Forms_Service_Bp.route("/api/forms/ayuda/create", methods=["POST"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["POST"])
def Api_Forms_Ayuda_Create():
    Data = request.get_json()
    Respuesta = requests.post(f"{MICROSERVICE_URL}/ayuda/create", json=Data)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Forms_Service_Bp.route("/api/forms/calificanos/create", methods=["POST"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["POST"])
def Api_Forms_Calificanos_Create():
    Data = request.get_json()
    Respuesta = requests.post(f"{MICROSERVICE_URL}/calificanos/create", json=Data)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Forms_Service_Bp.route("/api/forms/contactanos/create", methods=["POST"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["POST"])
def Api_Forms_Contactanos_Create():
    Data = request.get_json()
    Respuesta = requests.post(f"{MICROSERVICE_URL}/contactanos/create", json=Data)
    return jsonify(Respuesta.json()), Respuesta.status_code
