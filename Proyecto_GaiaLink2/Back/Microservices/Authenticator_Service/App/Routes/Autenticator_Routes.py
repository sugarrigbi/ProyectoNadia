from App.Utilities.Get import Get_Auth
from flask import Blueprint, request, jsonify

Auth_Service_Bp = Blueprint("Auth", __name__)

@Auth_Service_Bp.route("/auth/login", methods=["POST"])
def Auth_Login():
    Mensaje, Status = Get_Auth.Login()
    return jsonify(Mensaje.get_json()), Status
@Auth_Service_Bp.route("/auth/login/mfa", methods=["POST"])
def Auth_Login_Codigo():
    Mensaje, Status = Get_Auth.Login_Codigo()
    return jsonify(Mensaje.get_json()), Status
@Auth_Service_Bp.route("/auth/recuperar", methods=["POST"])
def Auth_Recuperar():
    Mensaje, Status = Get_Auth.Recuperar()
    return jsonify(Mensaje.get_json()), Status
@Auth_Service_Bp.route("/auth/recuperar/codigo", methods=["POST"])
def Auth_Recuperar_Codigo():
    Mensaje, Status = Get_Auth.Recuperar_Codigo()
    return jsonify(Mensaje.get_json()), Status
@Auth_Service_Bp.route("/auth/health", methods=["GET"])
def Health():
    return jsonify({"Status": "OK"}), 200