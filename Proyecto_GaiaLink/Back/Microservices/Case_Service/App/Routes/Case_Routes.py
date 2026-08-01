from flask import Blueprint, request, jsonify, current_app
from App.Utilities.Get import Get_Case

Case_Bp = Blueprint("Caso", __name__)

@Case_Bp.route("/create", methods=["POST"])
def Case_Create():
    return Get_Case.Case_Create()
@Case_Bp.route("/read/all/<int:Pagina>", methods=["GET"])
def Case_Read_All(Pagina):
    return Get_Case.Case_Read_All(Pagina)
@Case_Bp.route("/read/search/<int:Pagina>", methods=["GET"])
def Case_Read_By(Pagina):
    Filtros = request.args.to_dict(flat=False)
    return Get_Case.Case_Read_By(Filtros, Pagina)
@Case_Bp.route("/update/<int:Case_ID>", methods=["PUT"])
def Case_Update(Case_ID):
    return Get_Case.Case_Update(Case_ID)
@Case_Bp.route("/delete/<int:Case_ID>/<int:User_ID>", methods=["PUT"])
def Case_Delete(Case_ID, User_ID):
    return Get_Case.Case_Delete(Case_ID, User_ID)
@Case_Bp.route("/delete/relation/<string:Case_ID2>/<string:Case_ID1>/<int:Case_ID3>/<int:User_ID>", methods=["DELETE"])
def Case_Delete_Relation(Case_ID1, Case_ID2, Case_ID3,User_ID):
    return Get_Case.Delete_Relacion(Case_ID1, Case_ID2, Case_ID3,User_ID)
@Case_Bp.route("/health", methods=["GET"])
def Health():
    return jsonify({"Status": "OK"}), 200
@Case_Bp.route("/estadistica", methods=["GET"])
def Estadisticas():
    current_app.json.sort_keys = False
    return Get_Case.Estadisticas()
@Case_Bp.route("/excel", methods=["GET"])
def Excel():
    return Get_Case.Exportar_Excel()
