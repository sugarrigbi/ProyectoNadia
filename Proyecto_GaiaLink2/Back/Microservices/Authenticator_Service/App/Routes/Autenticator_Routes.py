from App.Utilities.Get import Get_Auth
from flask import Blueprint, request, jsonify

Auth_Service_Bp = Blueprint("Auth", __name__)

@Auth_Service_Bp.route("/auth/login", methods=["POST"])
def Auth_Login():
    Mensaje, Status = Get_Auth.Login()
    return jsonify(Mensaje.get_json()), Status