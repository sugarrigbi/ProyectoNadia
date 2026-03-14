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
@Case_Bp.route("/case/delete/<int:Case_ID>", methods=["PUT"])
def Case_Delete(Case_ID):
    return Get_Case.Case_Delete(Case_ID)