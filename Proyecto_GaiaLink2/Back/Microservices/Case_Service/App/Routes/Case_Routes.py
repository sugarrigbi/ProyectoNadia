from flask import Blueprint, request, jsonify
from App.Utilities.Get import Get_Case

Case_Bp = Blueprint("Case", __name__)

@Case_Bp.route("/Case/Read/All", methods=["GET"])
def Bp_Case_Read_All():
    return Get_Case.Case_Read_All()
