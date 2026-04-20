from flask import Blueprint, request, jsonify
from App.Services.Notification_Logic import Email_Service

Notification_Service_Bp = Blueprint("Notification", __name__)

@Notification_Service_Bp.route("/email", methods=["POST"])
def Registro_Codigo():
    Data = request.get_json()

    Template = Data["Template"]
    Datos = Data["Datos"]
    Correo = Data["Correo"]
    Asunto = Data["Asunto"]

    Respuesta = Email_Service.Envio(Template, Datos, Correo, Asunto)
    if "Error" in Respuesta:
        return jsonify(Respuesta), 400
    return jsonify({"Message": "Correo enviado"}), 200
@Notification_Service_Bp.route("/email/health", methods=["GET"])
def Health():
    return jsonify({"Status": "OK"}), 200