from flask import Blueprint, request, jsonify, Response, json, render_template
import requests

Inventory_Bp = Blueprint("Inventory_Proxy", __name__, url_prefix="/Inventory")
MICROSERVICE_URL = "http://localhost:5004/Inventory"

@Inventory_Bp.route("/Books/Create", methods=["POST"])
def Bp_Books_Create():
    Data = request.json
    r = requests.post(f"{MICROSERVICE_URL}/Books/Create", json=Data)
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Inventory_Bp.route("/Books/Read/All", methods=["GET"])
def Bp_Books_Read_All():
    r = requests.get(f"{MICROSERVICE_URL}/Books/Read/All")
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Inventory_Bp.route("/Books/Read/<int:Book_Id>", methods=["GET"])
def Bp_Books_Read_One(Book_Id):
    r = requests.get(f"{MICROSERVICE_URL}/Books/Read/{Book_Id}")
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Inventory_Bp.route("/Books/Read/Search", methods=["GET"])
def Books_Read_By():
    params = {"Field": request.args.get("Field"), "Value": request.args.get("Value")}
    r = requests.get(f"{MICROSERVICE_URL}/Books/Read/Search", params=params)
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Inventory_Bp.route("/Books/Update/<int:Book_Id>", methods=["PUT"])
def Bp_Books_Update(Book_Id):
    Data = request.json
    r = requests.put(f"{MICROSERVICE_URL}/Books/Update/{Book_Id}", json=Data)
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Inventory_Bp.route("/Books/Delete/<int:Book_Id>", methods=["DELETE"])
def Bp_Books_Delete(Book_Id):
    r = requests.delete(f"{MICROSERVICE_URL}/Books/Delete/{Book_Id}")
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Inventory_Bp.route("/Books/Delete/Selected", methods=["POST"])
def Bp_Books_Delete_Selected():
    Book_List = request.json
    r = requests.delete(f"{MICROSERVICE_URL}/Books/Delete/Selected", json=Book_List)
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')