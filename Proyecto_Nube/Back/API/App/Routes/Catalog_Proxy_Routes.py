from flask import Blueprint, request, jsonify, Response, json, render_template
import requests

Catalog_Bp = Blueprint("Catalog_Proxy", __name__, url_prefix="/Catalog")
MICROSERVICE_URL = "http://localhost:5003/Catalog"

@Catalog_Bp.route("/Books/Create", methods=["POST"])
def Bp_Books_Create():
    Data = request.json
    r = requests.post(f"{MICROSERVICE_URL}/Books/Create", json=Data)
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Catalog_Bp.route("/Books/Read/All", methods=["GET"])
def Bp_Books_Read_All():
    r = requests.get(f"{MICROSERVICE_URL}/Books/Read/All")
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Catalog_Bp.route("/Books/Read/<int:Book_Id>", methods=["GET"])
def Bp_Books_Read_One(Book_Id):
    r = requests.get(f"{MICROSERVICE_URL}/Books/Read/{Book_Id}")
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Catalog_Bp.route("/Books/Read/Search", methods=["GET"])
def Books_Read_By():
    params = {"Field": request.args.get("Field"), "Value": request.args.get("Value")}
    r = requests.get(f"{MICROSERVICE_URL}/Books/Read/Search", params=params)
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Catalog_Bp.route("/Books/Update/<int:Book_Id>", methods=["PUT"])
def Bp_Books_Update(Book_Id):
    Data = request.json
    r = requests.put(f"{MICROSERVICE_URL}/Books/Update/{Book_Id}", json=Data)
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Catalog_Bp.route("/Books/Delete/<int:Book_Id>", methods=["DELETE"])
def Bp_Books_Delete(Book_Id):
    r = requests.delete(f"{MICROSERVICE_URL}/Books/Delete/{Book_Id}")
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Catalog_Bp.route("/Books/Delete/Selected", methods=["POST"])
def Bp_Books_Delete_Selected():
    Book_List = request.json
    r = requests.delete(f"{MICROSERVICE_URL}/Books/Delete/Selected", json=Book_List)
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')

@Catalog_Bp.route("/Categories/Create", methods=["POST"])
def Bp_Categories_Create():
    Data = request.json
    r = requests.post(f"{MICROSERVICE_URL}/Categories/Create", json=Data)
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Catalog_Bp.route("/Categories/Read/All", methods=["GET"])
def Bp_Categories_Read_All():
    r = requests.get(f"{MICROSERVICE_URL}/Categories/Read/All")
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Catalog_Bp.route("/Categories/Read/<int:Category_Id>", methods=["GET"])
def Bp_Categories_Read_One(Category_Id):
    r = requests.get(f"{MICROSERVICE_URL}/Categories/Read/{Category_Id}")
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Catalog_Bp.route("/Categories/Read/Search", methods=["GET"])
def Bp_Categories_Read_By():
    params = {"Name": request.args.get("Name")}
    r = requests.get(f"{MICROSERVICE_URL}/Categories/Read/Search", params=params)
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Catalog_Bp.route("/Categories/Update/<int:Category_Id>", methods=["PUT"])
def Bp_Categories_Update(Category_Id):
    Data = request.json
    r = requests.put(f"{MICROSERVICE_URL}/Categories/Update/{Category_Id}", json=Data)
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Catalog_Bp.route("/Categories/Delete/<int:Category_Id>", methods=["DELETE"])
def Bp_Categories_Delete(Category_Id):
    r = requests.delete(f"{MICROSERVICE_URL}/Categories/Delete/{Category_Id}")
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')

@Catalog_Bp.route("/Publisher/Create", methods=["POST"])
def Bp_Publisher_Create():
    Data = request.json
    r = requests.post(f"{MICROSERVICE_URL}/Publisher/Create", json=Data)
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Catalog_Bp.route("/Publisher/Read/All", methods=["GET"])
def Bp_Publisher_Read_All():
    r = requests.get(f"{MICROSERVICE_URL}/Publisher/Read/All")
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Catalog_Bp.route("/Publisher/Read/<int:Publisher_Id>", methods=["GET"])
def Bp_Publisher_Read_One(Publisher_Id):
    r = requests.get(f"{MICROSERVICE_URL}/Publisher/Read/{Publisher_Id}")
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Catalog_Bp.route("/Publisher/Read/Search", methods=["GET"])
def Bp_Publisher_Read_By():
    params = {"Name": request.args.get("Name")}
    r = requests.get(f"{MICROSERVICE_URL}/Publisher/Read/Search", params=params)
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Catalog_Bp.route("/Publisher/Update/<int:Publisher_Id>", methods=["PUT"])
def Bp_Publisher_Update(Publisher_Id):
    Data = request.json
    r = requests.put(f"{MICROSERVICE_URL}/Publisher/Update/{Publisher_Id}", json=Data)
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Catalog_Bp.route("/Publisher/Delete/<int:Publisher_Id>", methods=["DELETE"])
def Bp_Publisher_Delete(Publisher_Id):
    r = requests.delete(f"{MICROSERVICE_URL}/Publisher/Delete/{Publisher_Id}")
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')

@Catalog_Bp.route("/Authors/Create", methods=["POST"])
def Bp_Authors_Create():
    Data = request.json
    r = requests.post(f"{MICROSERVICE_URL}/Authors/Create", json=Data)
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Catalog_Bp.route("/Authors/Read/All", methods=["GET"])
def Bp_Authors_Read_All():
    r = requests.get(f"{MICROSERVICE_URL}/Authors/Read/All")
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Catalog_Bp.route("/Authors/Read/<int:Authors_Id>", methods=["GET"])
def Bp_Authors_Read_One(Authors_Id):
    r = requests.get(f"{MICROSERVICE_URL}/Authors/Read/{Authors_Id}")
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Catalog_Bp.route("/Authors/Read/Search", methods=["GET"])
def Bp_Authors_Read_By():
    params = {"Field": request.args.get("Field"), "Value": request.args.get("Value")}
    r = requests.get(f"{MICROSERVICE_URL}/Authors/Read/Search", params=params)
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Catalog_Bp.route("/Authors/Update/<int:Authors_Id>", methods=["PUT"])
def Bp_Authors_Update(Authors_Id):
    Data = request.json
    r = requests.put(f"{MICROSERVICE_URL}/Authors/Update/{Authors_Id}", json=Data)
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')
@Catalog_Bp.route("/Authors/Delete/<int:Authors_Id>", methods=["DELETE"])
def Bp_Authors_Delete(Authors_Id):
    r = requests.delete(f"{MICROSERVICE_URL}/Authors/Delete/{Authors_Id}")
    return Response(json.dumps(r.json(), ensure_ascii=False, indent=2),status=r.status_code,mimetype='application/json')