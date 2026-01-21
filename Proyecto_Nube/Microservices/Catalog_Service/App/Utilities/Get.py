from flask import request, jsonify
from App.Services import Catalog_Logic
from App.Utilities.Extension import Base_Model

class Get_Books:
    @staticmethod
    def Books_Create():
        Data = request.get_json()

        if not Data:
            return jsonify({"Error": "No data provided"}), 400
        
        Book = Catalog_Logic.Books_Service.Create(Data)
        if not Book:
            return jsonify({"Error": "No book created"}), 400
        return jsonify({"Message": "Book created successfully"}), 201
    @staticmethod
    def Books_Read_All():
        Book = Catalog_Logic.Books_Service.Read_All()
        json = [B.to_dict() for B in Book]
        return Base_Model.to_json(json, 200)
    @staticmethod
    def Books_Read_One(Book_Id):
        Book = Catalog_Logic.Books_Service.Read_One(Book_Id)

        if Book == False:
            return jsonify({"Error": "No books finded"}), 404

        return jsonify(Book.to_dict()), 200
    @staticmethod
    def Books_Read_By(Field, Value):
        Book = Catalog_Logic.Books_Service.Read_By(Field, Value)

        if Book == False:
            return jsonify({"Error": "No books finded"}), 400
        
        return jsonify([B.to_dict() for B in Book]), 200
    @staticmethod
    def Books_Update(Book_Id):
        Data = request.get_json()

        if not Data:
            return jsonify({"Error": "No data provided"}), 400

        Book = Catalog_Logic.Books_Service.Update(Book_Id, Data)

        if Book == False:
            return jsonify({"Error": "No books updated"}), 400
        
        return jsonify({"Message": "Book updated successfully"}), 200
    @staticmethod
    def Books_Delete(Book_Id):
        Book = Catalog_Logic.Books_Service.Delete(Book_Id)

        if Book == False:
            return jsonify({"Error": "No books updated"}), 400
        
        return jsonify({"Message": "Book deleted successfully"}), 200
class Get_Categories:
    @staticmethod
    def Categories_Create():
        Data = request.get_json()

        if not Data:
            return jsonify({"Error": "No data provided"}), 400
        
        Category = Catalog_Logic.Categories_Service.Create(Data)
        if not Category:
            return jsonify({"Error": "No category created"}), 400
        return jsonify({"Message": "Category created successfully"}), 201
    @staticmethod
    def Categories_Read_All():
        Category = Catalog_Logic.Categories_Service.Read_All()
        return jsonify([C.to_dict() for C in Category]), 200
    @staticmethod
    def Categories_Read_One(Category_Id):
        Category = Catalog_Logic.Categories_Service.Read_One(Category_Id)

        if Category == False:
            return jsonify({"Error": "No Categories finded"}), 404

        return jsonify(Category.to_dict()), 200
    @staticmethod
    def Categories_Read_By(Name):
        Category = Catalog_Logic.Categories_Service.Read_By(Name)

        if Category == False:
            return jsonify({"Error": "No Categories finded"}), 400
        
        return jsonify([C.to_dict() for C in Category]), 200
    @staticmethod
    def Categories_Update(Category_Id):
        Data = request.get_json()

        if not Data:
            return jsonify({"Error": "No data provided"}), 400

        Category = Catalog_Logic.Categories_Service.Update(Category_Id, Data)

        if Category == False:
            return jsonify({"Error": "No Categories updated"}), 400
        
        return jsonify({"Message": "Category updated successfully"}), 200
    @staticmethod
    def Categories_Delete(Category_Id):
        Category = Catalog_Logic.Categories_Service.Delete(Category_Id)

        if Category == False:
            return jsonify({"Error": "No Categories updated"}), 400
        
        return jsonify({"Message": "Category deleted successfully"}), 200
