from flask import Blueprint, request
from App.Utilities.Get import Get_Books, Get_Categories

Catalog_Bp = Blueprint("Catalog", __name__)

@Catalog_Bp.route("/Books/Create", methods=["POST"])
def Bp_Books_Create():
    return Get_Books.Books_Create()
@Catalog_Bp.route("/Books/Read/All", methods=["GET"])
def Bp_Books_Read_All():
    return Get_Books.Books_Read_All()
@Catalog_Bp.route("/Books/Read/<int:Book_Id>", methods=["GET"])
def Bp_Books_Read_One(Book_Id):
    return Get_Books.Books_Read_One(Book_Id)
@Catalog_Bp.route("/Books/Read/Search", methods=["GET"])
def Books_Read_By():
    Field = request.args.get("Field")
    Value = request.args.get("Value")
    return Get_Books.Books_Read_By(Field, Value)
@Catalog_Bp.route("/Books/Update/<int:Book_Id>", methods=["PUT"])
def Bp_Books_Update(Book_Id):
    return Get_Books.Books_Update(Book_Id)
@Catalog_Bp.route("/Books/Delete/<int:Book_Id>", methods=["DELETE"])
def Bp_Books_Delete(Book_Id):
    return Get_Books.Books_Delete(Book_Id)

@Catalog_Bp.route("/Categories/Create", methods=["POST"])
def Bp_Categories_Create():
    return Get_Categories.Categories_Create()
@Catalog_Bp.route("/Categories/Read/All", methods=["GET"])
def Bp_Categories_Read_All():
    return Get_Categories.Categories_Read_All()
@Catalog_Bp.route("/Categories/Read/<int:Category_Id>", methods=["GET"])
def Bp_Categories_Read_One(Category_Id):
        return Get_Categories.Categories_Read_One(Category_Id)
@Catalog_Bp.route("/Categories/Read/Search", methods=["GET"])
def Bp_Categories_Read_By():
    Name = request.args.get("Name")
    return Get_Categories.Categories_Read_By(Name)
@Catalog_Bp.route("/Categories/Update/<int:Category_Id>", methods=["PUT"])
def Bp_Categories_Update(Category_Id):
    return Get_Categories.Categories_Update(Category_Id)
@Catalog_Bp.route("/Categories/Delete/<int:Category_Id>", methods=["DELETE"])
def Bp_Categories_Delete(Category_Id):
    return Get_Categories.Categories_Delete(Category_Id)