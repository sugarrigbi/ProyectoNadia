from flask import Blueprint
from App.Utilities.Get import Get_Account

Account_Bp = Blueprint("Account", __name__)

@Account_Bp.route("/device/read/all", methods=["GET"])
def Read_Devices():
    return Get_Account.Device_Read()
@Account_Bp.route("/device/delete/<int:Device_ID>", methods=["PUT"])
def Delete_Devices(Device_ID):
    return Get_Account.Device_Delete(Device_ID)