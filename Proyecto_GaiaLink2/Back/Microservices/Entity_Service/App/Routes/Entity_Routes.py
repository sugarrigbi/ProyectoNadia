from flask import Blueprint, request, jsonify
from App.Utilities.Get import Get_Entity

Entity_Bp = Blueprint("Entity", __name__)

@Entity_Bp.route("/create", methods=["POST"])
def Entity_Create():
    return Get_Entity.Get_Create()
@Entity_Bp.route("/read/all", methods=["GET"])
def Entity_Read_All():
    return Get_Entity.Get_Read_All()
@Entity_Bp.route("/read/search", methods=["GET"])
def Entity_Read_By():
    Filtros = request.args.to_dict(flat=False)
    return Get_Entity.Get_Read_By(Filtros)
@Entity_Bp.route("/update/<int:Entity_ID>", methods=["PUT"])
def Entity_Update(Entity_ID):
    return Get_Entity.Get_Update(Entity_ID)
@Entity_Bp.route("/delete/<int:Entity_ID>", methods=["PUT"])
def Entity_Delete(Entity_ID):
    return Get_Entity.Get_Delete(Entity_ID)
@Entity_Bp.route("/health", methods=["GET"])
def Health():
    return jsonify({"Status": "OK"}), 200