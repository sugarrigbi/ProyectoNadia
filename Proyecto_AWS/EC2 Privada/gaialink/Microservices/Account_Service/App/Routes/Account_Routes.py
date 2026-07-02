from App.Utilities.Get import Get_Account
from flask import Blueprint, jsonify

Account_Bp = Blueprint("Account", __name__)

@Account_Bp.route("/device/delete/<int:Device_ID>", methods=["PUT"])
def Delete_Devices(Device_ID):
    return Get_Account.Device_Delete(Device_ID)
@Account_Bp.route("/health", methods=["GET"])
def Health():
    return jsonify({"Status": "OK"}), 200
@Account_Bp.route("/mfa", methods=["PUT"])
def Change_Mfa():
    return Get_Account.Cambiar_Mfa()
@Account_Bp.route("/account/data", methods=["GET"])
def Read_Data():
    return Get_Account.Read_Data()
@Account_Bp.route("/account/update", methods=["PUT"])
def Update_User():
    return Get_Account.Cambiar_Personal()
@Account_Bp.route("/account/update/place", methods=["PUT"])
def Update_Place():
    return Get_Account.Cambiar_Ubicacion()
@Account_Bp.route("/account/update/password", methods=["PUT"])
def Update_Password():
    return Get_Account.Cambiar_Contraseña()
@Account_Bp.route("/account/update/image", methods=["PUT"])
def Update_Image():
    return Get_Account.Cambiar_Imagen()
@Account_Bp.route("/account/delete/image", methods=["PUT"])
def Delete_Image():
    return Get_Account.Eliminar_Imagen()
@Account_Bp.route("/account/delete/devices", methods=["PUT"])
def Delete_Devices2():
    return Get_Account.Delete_All_Devices()
@Account_Bp.route("/account/delete/account", methods=["PUT"])
def Delete_Account():
    return Get_Account.Delete_Account()
