from App.Utilities.Get import Get_User
from flask import Blueprint, jsonify

User_Service_Bp = Blueprint("User", __name__)

@User_Service_Bp.route("/registro", methods=["POST"])
def User_Registro():
    Respuesta, Status = Get_User.Registro()
    return Respuesta, Status 
@User_Service_Bp.route("/codigo", methods=["POST"])
def User_Codigo():
    return Get_User.Create()
@User_Service_Bp.route("/health", methods=["GET"])
def Health():
    return jsonify({"Status": "OK"}), 200