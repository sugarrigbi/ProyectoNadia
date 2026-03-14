from App.Utilities.Get import Get_User
from flask import Blueprint, request

User_Service_Bp = Blueprint("User", __name__)

@User_Service_Bp.route("/user/registro", methods=["POST"])
def User_Registro():
    Respuesta, Status = Get_User.Registro()
    return Respuesta, Status 
@User_Service_Bp.route("/user/codigo", methods=["POST"])
def User_Codigo():
    return Get_User.Create()