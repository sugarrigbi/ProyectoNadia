from flask import Blueprint, request, jsonify
import requests
from App.Rate_Limit import Rate_Limit, DEFAULT_LIMIT
import json

Response2 = requests.get("http://127.0.0.1:5003/case/data")

Case_Service_Bp = Blueprint("Case_Service", __name__)

MICROSERVICE_URL = "http://localhost:5003/case"

@Case_Service_Bp.route("/api/case/create", methods=["POST"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["POST"])
def Api_Case_Create():
    Data = request.get_json()

    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}

    Respuesta = requests.post(f"{MICROSERVICE_URL}/create", json=Data, headers=Header)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Case_Service_Bp.route("/api/case/read/all", methods=["GET"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["GET"])
def Api_Case_Read_All():
    Auth = request.headers.get("Authorization")
    Headers = {"Authorization": Auth}

    Respuesta = requests.get(f"{MICROSERVICE_URL}/read/all", headers=Headers)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Case_Service_Bp.route("/api/case/read/tiempo", methods=["GET"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["GET"])
def Api_Case_Read_Tiempo():
    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}

    Respuesta = requests.get(f"{MICROSERVICE_URL}/read/linea/tiempo", headers=Header)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Case_Service_Bp.route("/api/case/read/data", methods=["GET"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["GET"])
def Api_Case_Read_Data():
    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}

    Respuesta = requests.get(f"{MICROSERVICE_URL}/data", headers=Header)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Case_Service_Bp.route("/api/case/update/<int:Case_ID>", methods=["PUT"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["PUT"])
def Api_Case_Update(Case_ID):
    Data = request.get_json()

    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}    

    Respuesta = requests.put(f"{MICROSERVICE_URL}/update/{Case_ID}", json=Data, headers=Header)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Case_Service_Bp.route("/api/case/delete/<int:Case_ID>/<int:User_ID>", methods=["PUT"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["PUT"])
def Api_Case_Delete(Case_ID, User_ID):
    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}

    Respuesta = requests.put(f"{MICROSERVICE_URL}/delete/{Case_ID}/{User_ID}", headers=Header)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Case_Service_Bp.route("/api/case/read/search", methods=["GET"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["GET"])
def Api_Case_Read_By():
    Filtros = request.args.to_dict(flat=False)

    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}

    Respuesta = requests.get(f"{MICROSERVICE_URL}/read/search", params=Filtros, headers=Header)
    return jsonify(Respuesta.json()), Respuesta.status_code




@Case_Service_Bp.route("/api/case/read/<int:Case_ID>", methods=["GET"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["GET"])
def Api_Case_Read_One(Case_ID):
    Respuesta = requests.get(f"{MICROSERVICE_URL}/read/{Case_ID}")
    return jsonify(Respuesta.json()), Respuesta.status_code

@Case_Service_Bp.route("/api/case/delete/relation/<string:Case_ID2>/<string:Case_ID1>/<int:Case_ID3>/<int:User_ID>", methods=["DELETE"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["DELETE"])
def Api_Case_Delete_Relation(Case_ID2, Case_ID1, Case_ID3, User_ID):
    Respuesta = requests.delete(f"{MICROSERVICE_URL}/delete/relation/{Case_ID2}/{Case_ID1}/{Case_ID3}/{User_ID}")
    return jsonify(Respuesta.json()), Respuesta.status_code
