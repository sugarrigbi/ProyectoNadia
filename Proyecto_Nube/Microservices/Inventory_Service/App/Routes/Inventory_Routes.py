from flask import Blueprint, request
from App.Utilities import Get

Inventory_Bp = Blueprint("Inventory", __name__)

@Inventory_Bp.route("/Books/Create", methods=["POST"])
def Bp_Books_Create():
    return Get.Books_Create()
@Inventory_Bp.route("/Books/Read/All", methods=["GET"])
def Bp_Books_Read_All():
    return Get.Books_Read_All()
@Inventory_Bp.route("/Books/Read/<int:Book_Id>", methods=["GET"])
def Bp_Books_Read_One(Book_Id):
    return Get.Books_Read_One(Book_Id)
@Inventory_Bp.route("/Books/Read/Search", methods=["GET"])
def Books_Read_By():
    Field = request.args.get("Field")
    Value = request.args.get("Value")
    return Get.Books_Read_By(Field, Value)
@Inventory_Bp.route("/Books/Update/<int:Book_Id>", methods=["PUT"])
def Bp_Books_Update(Book_Id):
    return Get.Books_Update(Book_Id)
@Inventory_Bp.route("/Books/Delete/<int:Book_Id>", methods=["DELETE"])
def Bp_Books_Delete(Book_Id):
    return Get.Books_Delete(Book_Id)