from flask import Blueprint, request
from App.Utilities.Get import Get_Entity

Entity_Bp = Blueprint("Entity", __name__)

@Entity_Bp.route("/entity/create", methods=["POST"])
def Entity_Create():
    return Get_Entity.Get_Create()
@Entity_Bp.route("/entity/read/all", methods=["GET"])
def Entity_Read_All():
    return Get_Entity.Get_Read_All()
@Entity_Bp.route("/entity/read/<int:Entity_ID>", methods=["GET"])
def Entity_Read_One(Entity_ID):
    return Get_Entity.Get_Read_One(Entity_ID)
@Entity_Bp.route("/entity/read/search", methods=["GET"])
def Entity_Read_By():
    Field = request.args.get("Field")
    Value = request.args.get("Value")
    return Get_Entity.Get_Read_By(Field, Value)
@Entity_Bp.route("/entity/update/<int:Entity_ID>", methods=["PUT"])
def Entity_Update(Entity_ID):
    return Get_Entity.Get_Update(Entity_ID)
@Entity_Bp.route("/entity/delete/<int:Entity_ID>", methods=["PUT"])
def Entity_Delete(Entity_ID):
    return Get_Entity.Get_Delete(Entity_ID)