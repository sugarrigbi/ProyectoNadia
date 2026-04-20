from flask import Blueprint, jsonify
from App.Utilities.Get import Get_Account

Account_Bp = Blueprint("Account", __name__)

@Account_Bp.route("/device/read/all", methods=["GET"])
def Read_Devices():
    return Get_Account.Device_Read()
@Account_Bp.route("/device/delete/<int:Device_ID>", methods=["PUT"])
def Delete_Devices(Device_ID):
    return Get_Account.Device_Delete(Device_ID)
@Account_Bp.route("/account/health", methods=["GET"])
def Health():
    return jsonify({"Status": "OK"}), 200
@Account_Bp.route("/account/mfa", methods=["PUT"])
def Change_Mfa():
    return Get_Account.Cambiar_Mfa()
@Account_Bp.route("/account/mfa/get", methods=["GET"])
def Obtain_Mfa():
    return Get_Account.Obtener_Mfa()