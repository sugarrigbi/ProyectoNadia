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

@Forms_Service_Bp.route("/forms/ayuda/read/all", methods=["GET"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["GET"])
def Api_Forms_Ayuda_Read():
    Respuesta = requests.get(f"{MICROSERVICE_URL}/ayuda/read/all")
    return jsonify(Respuesta.json()), Respuesta.status_code

@Forms_Service_Bp.route("/forms/calificanos/read/all", methods=["GET"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["GET"])
def Api_Forms_Calificanos_Read():
    Respuesta = requests.get(f"{MICROSERVICE_URL}/calificanos/read/all")
    return jsonify(Respuesta.json()), Respuesta.status_code

@Forms_Service_Bp.route("/forms/contactanos/read/all", methods=["GET"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["GET"])
def Api_Forms_Contactanos_Read():
    Respuesta = requests.get(f"{MICROSERVICE_URL}/contactanos/read/all")
    return jsonify(Respuesta.json()), Respuesta.status_code

@Forms_Service_Bp.route("/forms/ayuda/delete/<int:ID>", methods=["DELETE"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["DELETE"])
def Api_Forms_Ayuda_Delete(ID):
    Respuesta = requests.delete(f"{MICROSERVICE_URL}/ayuda/delete/{ID}")
    return jsonify(Respuesta.json()), Respuesta.status_code

@Forms_Service_Bp.route("/forms/calificanos/delete/<int:ID>", methods=["DELETE"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["DELETE"])
def Api_Forms_Calificanos_Delete(ID):
    Respuesta = requests.delete(f"{MICROSERVICE_URL}/calificanos/delete/{ID}")
    return jsonify(Respuesta.json()), Respuesta.status_code

@Forms_Service_Bp.route("/forms/contactanos/delete/<int:ID>", methods=["DELETE"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["DELETE"])
def Api_Forms_Contactanos_Delete(ID):
    Respuesta = requests.delete(f"{MICROSERVICE_URL}/contactanos/delete/{ID}")
    return jsonify(Respuesta.json()), Respuesta.status_code
