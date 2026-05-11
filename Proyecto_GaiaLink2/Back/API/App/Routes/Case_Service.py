from flask import Blueprint, request, jsonify, current_app, Response
from App.Rate_Limit import Rate_Limit
import requests
import os

Case_Service_Bp = Blueprint("Case_Service", __name__)

MICROSERVICE_URL = os.getenv("CASE_URL")
DEFAULT_LIMIT = os.getenv("DEFAULT_LIMIT")

@Case_Service_Bp.route("/case/create", methods=["POST"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["POST"])
def Api_Case_Create():
    Data = request.get_json()

    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}

    Respuesta = requests.post(f"{MICROSERVICE_URL}/create", json=Data, headers=Header, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Case_Service_Bp.route("/case/read/all", methods=["GET"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["GET"])
def Api_Case_Read_All():
    Auth = request.headers.get("Authorization")
    Headers = {"Authorization": Auth}

    Respuesta = requests.get(f"{MICROSERVICE_URL}/read/all", headers=Headers, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Case_Service_Bp.route("/case/read/search", methods=["GET"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["GET"])
def Api_Case_Read_By():
    Filtros = request.args.to_dict(flat=False)

    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}

    Respuesta = requests.get(f"{MICROSERVICE_URL}/read/search", params=Filtros, headers=Header, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Case_Service_Bp.route("/case/update/<int:Case_ID>", methods=["PUT"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["PUT"])
def Api_Case_Update(Case_ID):
    Data = request.get_json()

    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}    

    Respuesta = requests.put(f"{MICROSERVICE_URL}/update/{Case_ID}", json=Data, headers=Header, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Case_Service_Bp.route("/case/delete/<int:Case_ID>/<int:User_ID>", methods=["PUT"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["PUT"])
def Api_Case_Delete(Case_ID, User_ID):
    Auth = request.headers.get("Authorization")
    Header = {"Authorization": Auth}

    Respuesta = requests.put(f"{MICROSERVICE_URL}/delete/{Case_ID}/{User_ID}", headers=Header, timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Case_Service_Bp.route("/case/delete/relation/<string:Case_ID2>/<string:Case_ID1>/<int:Case_ID3>/<int:User_ID>", methods=["DELETE"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["DELETE"])
def Api_Case_Delete_Relation(Case_ID2, Case_ID1, Case_ID3, User_ID):
    Respuesta = requests.delete(f"{MICROSERVICE_URL}/delete/relation/{Case_ID2}/{Case_ID1}/{Case_ID3}/{User_ID}", timeout=10)
    return jsonify(Respuesta.json()), Respuesta.status_code

@Case_Service_Bp.route("/case/estadisticas", methods=["GET"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["GET"])
def Api_Case_Estadisticas():
    Auth = request.headers.get("Authorization")
    Headers = {"Authorization": Auth}

    Respuesta = requests.get(f"{MICROSERVICE_URL}/estadistica", headers=Headers, timeout=10)
    current_app.json.sort_keys = False  
    return jsonify(Respuesta.json()), Respuesta.status_code

@Case_Service_Bp.route("/case/excel", methods=["GET"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["GET"])
def Api_Case_Excel():
    Auth = request.headers.get("Authorization")
    Headers = {"Authorization": Auth}

    Respuesta = requests.get(f"{MICROSERVICE_URL}/excel", headers=Headers, timeout=10)
    return Response(Respuesta.content, status=Respuesta.status_code, content_type=Respuesta.headers.get("Content-Type"), headers={"Content-Disposition": Respuesta.headers.get("Content-Disposition")})