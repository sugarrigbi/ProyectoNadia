from flask import request, jsonify, Response, json
from App.Services import Case_Logic

class Get_Case:
    @staticmethod
    def Case_Read_All():
        Case = Case_Logic.Case_Service.Read_All() 
        return Response(json.dumps([C.to_dict() for C in Case], ensure_ascii=False, indent=2),status=200,mimetype='application/json')
'''
class Get_Case_prueba:
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
    def Books_Read_One(Book_Id):
        Book = Catalog_Logic.Books_Service.Read_One(Book_Id)

        if Book == False:
            return jsonify({"Error": "No books finded"}), 404

        return Response(json.dumps(Book.to_dict(), ensure_ascii=False, indent=2),status=200,mimetype='application/json')
    @staticmethod
    def Books_Read_By(Field, Value):
        Book = Catalog_Logic.Books_Service.Read_By(Field, Value)

        if Book == False:
            return jsonify({"Error": "No books finded"}), 400
        
        return Response(json.dumps([B.to_dict() for B in Book], ensure_ascii=False, indent=2),status=200,mimetype='application/json')
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
            return jsonify({"Error": "No book deleted"}), 400
        
        return jsonify({"Message": "Book deleted successfully"}), 200
    @staticmethod
    def Books_Delete_Selected(Book_List):
        Book = Catalog_Logic.Books_Service.Delete_Selected(Book_List)

        if Book == False:
            return jsonify({"Error": "No books deleted"}), 400
        
        return jsonify({"Message": "Books deleted successfully"}), 200    
    @staticmethod
    def Books_Authors_Read_By(Value):
        Books_List = Catalog_Logic.Books_Authors_Service.Read_By(Value)

        if not Books_List:
            return jsonify({"Error": "No books found"}), 400

        return Response(json.dumps([B.to_dict() for B in Books_List], ensure_ascii=False, indent=2),status=200,mimetype='application/json')
'''