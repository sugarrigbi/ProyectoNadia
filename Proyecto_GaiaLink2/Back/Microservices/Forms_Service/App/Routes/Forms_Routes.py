from App.Utilities.Get import Get_Forms
from App.Models.Forms_Models import Ayuda, Calificanos, Contactanos
from flask import Blueprint, request

Forms_Bp = Blueprint("Forms", __name__)

@Forms_Bp.route("/forms/ayuda/create", methods=["POST"])
def Forms_Create_Ayuda():
    return Get_Forms.Get_Create(Ayuda)
@Forms_Bp.route("/forms/calificanos/create", methods=["POST"])
def Forms_Create_Calificanos():
    return Get_Forms.Get_Create(Calificanos)
@Forms_Bp.route("/forms/contactanos/create", methods=["POST"])
def Forms_Create_Contactanos():
    return Get_Forms.Get_Create(Contactanos)
@Forms_Bp.route("/forms/ayuda/read/all", methods=["GET"])
def Forms_Read_All_Ayuda():
    return Get_Forms.Get_Read_All(Ayuda)
@Forms_Bp.route("/forms/calificanos/read/all", methods=["GET"])
def Forms_Read_All_Calificanos():
    return Get_Forms.Get_Read_All(Calificanos)
@Forms_Bp.route("/forms/contactanos/read/all", methods=["GET"])
def Forms_Read_All_Contactanos():
    return Get_Forms.Get_Read_All(Contactanos)
@Forms_Bp.route("/forms/ayuda/read/<int:Forms_ID>", methods=["GET"])
def Forms_Read_One_Ayuda(Forms_ID):
    return Get_Forms.Get_Read_One(Ayuda,Forms_ID)
@Forms_Bp.route("/forms/calificanos/read/<int:Forms_ID>", methods=["GET"])
def Forms_Read_One_Calificanos(Forms_ID):
    return Get_Forms.Get_Read_One(Calificanos,Forms_ID)
@Forms_Bp.route("/forms/contactanos/read/<int:Forms_ID>", methods=["GET"])
def Forms_Read_One_Contactanos(Forms_ID):
    return Get_Forms.Get_Read_One(Contactanos,Forms_ID)
@Forms_Bp.route("/forms/ayuda/read/search", methods=["GET"])
def Forms_Read_By_Ayuda():
    Field = request.args.get("Field")
    Value = request.args.get("Value")
    return Get_Forms.Get_Read_By(Ayuda,Field,Value)
@Forms_Bp.route("/forms/calificanos/read/search", methods=["GET"])
def Forms_Read_By_Calificanos():
    Field = request.args.get("Field")
    Value = request.args.get("Value")    
    return Get_Forms.Get_Read_By(Calificanos,Field,Value)
@Forms_Bp.route("/forms/contactanos/read/search", methods=["GET"])
def Forms_Read_By_Contactanos():
    Field = request.args.get("Field")
    Value = request.args.get("Value")    
    return Get_Forms.Get_Read_By(Contactanos,Field,Value)