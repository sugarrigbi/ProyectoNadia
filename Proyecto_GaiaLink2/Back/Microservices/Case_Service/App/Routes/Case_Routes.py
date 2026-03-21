from flask import Blueprint, request
from App.Utilities.Get import Get_Case

Case_Bp = Blueprint("Caso", __name__)

@Case_Bp.route("/case/create", methods=["POST"])
def Case_Create():
    return Get_Case.Case_Create()
@Case_Bp.route("/case/read/all", methods=["GET"])
def Case_Read_All():
    return Get_Case.Case_Read_All()
@Case_Bp.route("/case/read/<int:Case_ID>", methods=["GET"])
def Case_Read_One(Case_ID):
    return Get_Case.Case_Read_One(Case_ID)
@Case_Bp.route("/case/read/search", methods=["GET"])
def Case_Read_By():
    Field = request.args.get("Field")
    Value = request.args.get("Value")
    return Get_Case.Case_Read_By(Field, Value)
@Case_Bp.route("/case/update/<int:Case_ID>", methods=["PUT"])
def Case_Update(Case_ID):
    return Get_Case.Case_Update(Case_ID)
@Case_Bp.route("/case/delete/<int:Case_ID>/<int:User_ID>", methods=["PUT"])
def Case_Delete(Case_ID, User_ID):
    return Get_Case.Case_Delete(Case_ID, User_ID)
@Case_Bp.route("/case/delete/relation/<string:Case_ID2>/<string:Case_ID1>/<int:Case_ID3>/<int:User_ID>", methods=["DELETE"])
def Case_Delete_Relation(Case_ID1, Case_ID2, Case_ID3,User_ID):
    return Get_Case.Delete_Relacion(Case_ID1, Case_ID2, Case_ID3,User_ID)
@Case_Bp.route("/case/data", methods=["GET"])
def Case_Data():
    return Get_Case.Case_Data()