from flask import request, jsonify
from App.Services import Catalog_Logic





def Books_Create():
    Data = request.get_json()

    if not Data:
        return jsonify({"Error": "No data provided"}), 400
    
    Book = Catalog_Logic.Books_Service.Create(Data)
    if not Book:
        return jsonify({"Error": "No book created"}), 400
    return jsonify({"Message": "Book created successfully"}), 201
def Books_Read_All():
    Book = Catalog_Logic.Books_Service.Read_All()
    return jsonify([B.to_dict() for B in Book]), 200
def Books_Read_One(Book_Id):
    Book = Catalog_Logic.Books_Service.Read_One(Book_Id)

    if Book == False:
        return jsonify({"Error": "No books finded"}), 404

    return jsonify(Book.to_dict()), 200
def Books_Read_By(Field, Value):
    Book = Catalog_Logic.Books_Service.Read_By(Field, Value)

    if Book == False:
        return jsonify({"Error": "No books finded"}), 400
    
    return jsonify([B.to_dict() for B in Book]), 200
def Books_Update(Book_Id):
    Data = request.get_json()

    if not Data:
        return jsonify({"Error": "No data provided"}), 400

    Book = Catalog_Logic.Books_Service.Update(Book_Id, Data)

    if Book == False:
        return jsonify({"Error": "No books updated"}), 400
    
    return jsonify({"Message": "Book updated successfully"}), 200
def Books_Delete(Book_Id):
    Book = Catalog_Logic.Books_Service.Delete(Book_Id)

    if Book == False:
        return jsonify({"Error": "No books updated"}), 400
    
    return jsonify({"Message": "Book deleted successfully"}), 200