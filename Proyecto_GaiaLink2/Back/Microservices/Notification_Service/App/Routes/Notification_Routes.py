from flask import Blueprint, request, jsonify
from App.Services.Notification_Logic import Email_Service

Notification_Service_Bp = Blueprint("Notification", __name__)

@Notification_Service_Bp.route("/email", methods=["POST"])
def Enviar_Email():

    Data = request.get_json()

    Correo = Data["Correo"]
    Asunto = Data["Asunto"]
    Mensaje = Data["Mensaje"]

    Respuesta = Email_Service.Send(Correo, Asunto, Mensaje)

    if "Error" in Respuesta:
        return jsonify(Respuesta), 400

    return jsonify({"Message": "Correo enviado"}), 200