from flask import Blueprint, request
from App.Utilities.Get import Get_Inventory

Inventory_Bp = Blueprint("Inventory", __name__)

@Inventory_Bp.route("/Books/Create", methods=["POST"])
def Bp_Inventory_Create():
    return Get_Inventory.Inventory_Create()
@Inventory_Bp.route("/Books/Read/All", methods=["GET"])
def Bp_Inventory_Read_All():
    return Get_Inventory.Inventory_Read_All()
@Inventory_Bp.route("/Books/Read/<int:Book_Id>", methods=["GET"])
def Bp_Inventory_Read_One(Book_Id):
    return Get_Inventory.Inventory_Read_One(Book_Id)
@Inventory_Bp.route("/Books/Read/Search", methods=["GET"])
def Inventory_Read_By():
    Field = request.args.get("Field")
    Value = request.args.get("Value")
    return Get_Inventory.Inventory_Read_By(Field, Value)
@Inventory_Bp.route("/Books/Update/<int:Book_Id>", methods=["PUT"])
def Bp_Inventory_Update(Book_Id):
    return Get_Inventory.Inventory_Update(Book_Id)
@Inventory_Bp.route("/Books/Delete/<int:Book_Id>", methods=["DELETE"])
def Bp_Inventory_Delete(Book_Id):
    return Get_Inventory.Inventory_Delete(Book_Id)
@Inventory_Bp.route("/Books/Delete/Selected", methods=["DELETE"])
def Bp_Inventory_Delete_Selected():
    Book_List = request.get_json()
    return Get_Inventory.Inventory_Delete_Selected(Book_List)