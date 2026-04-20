from flask import Blueprint, request, jsonify
import requests
from App.Rate_Limit import Rate_Limit, DEFAULT_LIMIT

Entity_Service_Bp = Blueprint("Entity_Service", __name__)

MICROSERVICE_URL = "http://localhost:5004/entity"

@Entity_Service_Bp.route("/api/entity/create", methods=["POST"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["POST"])
def Api_Entity_Create():
    Data = request.get_json()

    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}

    Respuesta = requests.post(f"{MICROSERVICE_URL}/create", json=Data, headers=Header, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Entity_Service_Bp.route("/api/entity/read/all", methods=["GET"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["GET"])
def Api_Entity_Read_All():
    Auth = request.headers.get("Authorization")
    Headers = {"Authorization": Auth}

    Respuesta = requests.get(f"{MICROSERVICE_URL}/read/all", headers=Headers, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Entity_Service_Bp.route("/api/entity/read/search", methods=["GET"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["GET"])
def Api_Entity_Read_By():
    Filtros = request.args.to_dict(flat=False)

    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}

    Respuesta = requests.get(f"{MICROSERVICE_URL}/read/search", params=Filtros, headers=Header, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Entity_Service_Bp.route("/api/entity/update/<int:Entity_ID>", methods=["PUT"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["PUT"])
def Api_Entity_Update(Entity_ID):
    Data = request.get_json()

    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}

    Respuesta = requests.put(f"{MICROSERVICE_URL}/update/{Entity_ID}", json=Data, headers=Header, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Entity_Service_Bp.route("/api/entity/delete/<int:Entity_ID>", methods=["PUT"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["PUT"])
def Api_Entity_Delete(Entity_ID):
    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}

    Respuesta = requests.put(f"{MICROSERVICE_URL}/delete/{Entity_ID}", headers=Header, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code