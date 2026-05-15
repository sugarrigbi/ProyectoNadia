from App.Models.Forms_Models import Ayuda, Calificanos, Contactanos
from flask import Blueprint, request, jsonify
from App.Utilities.Get import Get_Forms

Forms_Bp = Blueprint("Forms", __name__)

@Forms_Bp.route("/ayuda/create", methods=["POST"])
def Forms_Create_Ayuda():
    return Get_Forms.Get_Create(Ayuda)
@Forms_Bp.route("/calificanos/create", methods=["POST"])
def Forms_Create_Calificanos():
    return Get_Forms.Get_Create(Calificanos)
@Forms_Bp.route("/contactanos/create", methods=["POST"])
def Forms_Create_Contactanos():
    return Get_Forms.Get_Create(Contactanos)
@Forms_Bp.route("/ayuda/read/all", methods=["GET"])
def Forms_Read_All_Ayuda():
    return Get_Forms.Get_Read_All(Ayuda)
@Forms_Bp.route("/calificanos/read/all", methods=["GET"])
def Forms_Read_All_Calificanos():
    return Get_Forms.Get_Read_All(Calificanos)
@Forms_Bp.route("/contactanos/read/all", methods=["GET"])
def Forms_Read_All_Contactanos():
    return Get_Forms.Get_Read_All(Contactanos)
@Forms_Bp.route("/ayuda/read/<int:Forms_ID>", methods=["GET"])
def Forms_Read_One_Ayuda(Forms_ID):
    return Get_Forms.Get_Read_One(Ayuda,Forms_ID)
@Forms_Bp.route("/calificanos/read/<int:Forms_ID>", methods=["GET"])
def Forms_Read_One_Calificanos(Forms_ID):
    return Get_Forms.Get_Read_One(Calificanos,Forms_ID)
@Forms_Bp.route("/contactanos/read/<int:Forms_ID>", methods=["GET"])
def Forms_Read_One_Contactanos(Forms_ID):
    return Get_Forms.Get_Read_One(Contactanos,Forms_ID)
@Forms_Bp.route("/ayuda/read/search", methods=["GET"])
def Forms_Read_By_Ayuda():
    Field = request.args.get("Field")
    Value = request.args.get("Value")
    return Get_Forms.Get_Read_By(Ayuda,Field,Value)
@Forms_Bp.route("/calificanos/read/search", methods=["GET"])
def Forms_Read_By_Calificanos():
    Field = request.args.get("Field")
    Value = request.args.get("Value")    
    return Get_Forms.Get_Read_By(Calificanos,Field,Value)
@Forms_Bp.route("/contactanos/read/search", methods=["GET"])
def Forms_Read_By_Contactanos():
    Field = request.args.get("Field")
    Value = request.args.get("Value")    
    return Get_Forms.Get_Read_By(Contactanos,Field,Value)
@Forms_Bp.route("/ayuda/delete/<int:ID>", methods=["DELETE"])
def Forms_Delete_Ayuda(ID):
    return Get_Forms.Get_Delete(Ayuda, ID)
@Forms_Bp.route("/calificanos/delete/<int:ID>", methods=["DELETE"])
def Forms_Delete_Calificanos(ID):
    return Get_Forms.Get_Delete(Calificanos, ID)
@Forms_Bp.route("/contactanos/delete/<int:ID>", methods=["DELETE"])
def Forms_Delete_Contactanos(ID):
    return Get_Forms.Get_Delete(Contactanos, ID)

@Forms_Bp.route("/health", methods=["GET"])
def Health():
    return jsonify({"Status": "OK"}), 200