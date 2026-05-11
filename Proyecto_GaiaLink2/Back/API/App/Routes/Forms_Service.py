from flask import Blueprint, request, jsonify
from App.Rate_Limit import Rate_Limit
import requests
import os

Forms_Service_Bp = Blueprint("Forms_Service", __name__)

MICROSERVICE_URL = os.getenv("FORMS_URL")
DEFAULT_LIMIT = os.getenv("DEFAULT_LIMIT")

@Forms_Service_Bp.route("/forms/ayuda/create", methods=["POST"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["POST"])
def Api_Forms_Ayuda_Create():
    Data = request.get_json()
    Respuesta = requests.post(f"{MICROSERVICE_URL}/ayuda/create", json=Data, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Forms_Service_Bp.route("/forms/calificanos/create", methods=["POST"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["POST"])
def Api_Forms_Calificanos_Create():
    Data = request.get_json()
    Respuesta = requests.post(f"{MICROSERVICE_URL}/calificanos/create", json=Data, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Forms_Service_Bp.route("/forms/contactanos/create", methods=["POST"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["POST"])
def Api_Forms_Contactanos_Create():
    Data = request.get_json()
    Respuesta = requests.post(f"{MICROSERVICE_URL}/contactanos/create", json=Data, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code
