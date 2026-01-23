from flask import request, jsonify, Response, json
from App.Services import Catalog_Logic

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
        return Response(json.dumps([B.to_dict() for B in Book], ensure_ascii=False, indent=2),status=200,mimetype='application/json')
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
        return Response(json.dumps([C.to_dict() for C in Category], ensure_ascii=False, indent=2),status=200,mimetype='application/json')
    @staticmethod
    def Categories_Read_One(Category_Id):
        Category = Catalog_Logic.Categories_Service.Read_One(Category_Id)

        if Category == False:
            return jsonify({"Error": "No Categories finded"}), 404

        return Response(json.dumps(Category.to_dict(), ensure_ascii=False, indent=2),status=200,mimetype='application/json')
    @staticmethod
    def Categories_Read_By(Name):
        Category = Catalog_Logic.Categories_Service.Read_By(Name)

        if Category == False:
            return jsonify({"Error": "No Categories finded"}), 400
        
        return Response(json.dumps([C.to_dict() for C in Category], ensure_ascii=False, indent=2),status=200,mimetype='application/json')
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
class Get_Publisher:
    @staticmethod
    def Publisher_Create():
        Data = request.get_json()

        if not Data:
            return jsonify({"Error": "No data provided"}), 400
        
        Publish = Catalog_Logic.Publisher_Service.Create(Data)
        if not Publish:
            return jsonify({"Error": "No publisher created"}), 400
        return jsonify({"Message": "publisher created successfully"}), 201
    @staticmethod
    def Publisher_Read_All():
        Publish = Catalog_Logic.Publisher_Service.Read_All()
        return Response(json.dumps([P.to_dict() for P in Publish], ensure_ascii=False, indent=2),status=200,mimetype='application/json')
    @staticmethod
    def Publisher_Read_One(Publisher_Id):
        Publish = Catalog_Logic.Publisher_Service.Read_One(Publisher_Id)

        if Publish == False:
            return jsonify({"Error": "No Publishers finded"}), 404

        return Response(json.dumps(Publish.to_dict(), ensure_ascii=False, indent=2),status=200,mimetype='application/json')
    @staticmethod
    def Publisher_Read_By(Name):
        Publish = Catalog_Logic.Publisher_Service.Read_By(Name)

        if Publish == False:
            return jsonify({"Error": "No Publishers finded"}), 400
        
        return Response(json.dumps([P.to_dict() for P in Publish], ensure_ascii=False, indent=2),status=200,mimetype='application/json')
    @staticmethod
    def Publisher_Update(Publisher_Id):
        Data = request.get_json()

        if not Data:
            return jsonify({"Error": "No data provided"}), 400

        Publish = Catalog_Logic.Publisher_Service.Update(Publisher_Id, Data)

        if Publish == False:
            return jsonify({"Error": "No Publisher updated"}), 400
        
        return jsonify({"Message": "Publisher updated successfully"}), 200
    @staticmethod
    def Publisher_Delete(Publisher_Id):
        Publish = Catalog_Logic.Publisher_Service.Delete(Publisher_Id)

        if Publish == False:
            return jsonify({"Error": "No Publisher updated"}), 400
        
        return jsonify({"Message": "Publisher deleted successfully"}), 200    
class Get_Authors:
    @staticmethod
    def Authors_Create():
        Data = request.get_json()

        if not Data:
            return jsonify({"Error": "No data provided"}), 400
        
        Author = Catalog_Logic.Authors_Service.Create(Data)
        if not Author:
            return jsonify({"Error": "No author created"}), 400
        return jsonify({"Message": "author created successfully"}), 201
    @staticmethod
    def Authors_Read_All():
        Author = Catalog_Logic.Authors_Service.Read_All()
        return Response(json.dumps([A.to_dict() for A in Author], ensure_ascii=False, indent=2),status=200,mimetype='application/json')
    @staticmethod
    def Authors_Read_One(Authors_Id):
        Author = Catalog_Logic.Authors_Service.Read_One(Authors_Id)

        if Author == False:
            return jsonify({"Error": "No Author finded"}), 404

        return Response(json.dumps(Author.to_dict(), ensure_ascii=False, indent=2),status=200,mimetype='application/json')
    @staticmethod
    def Authors_Read_By(Field, Value):
        Author = Catalog_Logic.Authors_Service.Read_By(Field, Value)

        if Author == False:
            return jsonify({"Error": "No Authors finded"}), 400
        
        return Response(json.dumps([A.to_dict() for A in Author], ensure_ascii=False, indent=2),status=200,mimetype='application/json')
    @staticmethod
    def Authors_Update(Authors_Id):
        Data = request.get_json()

        if not Data:
            return jsonify({"Error": "No data provided"}), 400

        Author = Catalog_Logic.Authors_Service.Update(Authors_Id, Data)

        if Author == False:
            return jsonify({"Error": "No Author updated"}), 400
        
        return jsonify({"Message": "Author updated successfully"}), 200
    @staticmethod
    def Authors_Delete(Authors_Id):
        Author = Catalog_Logic.Authors_Service.Delete(Authors_Id)

        if Author == False:
            return jsonify({"Error": "No Author updated"}), 400
        
        return jsonify({"Message": "Author deleted successfully"}), 200     
class Get_Books_Authors:
    @staticmethod
    def Books_Authors_Read_By(Value):
        Books_List = Catalog_Logic.Books_Authors_Service.Read_By(Value)

        if not Books_List:
            return jsonify({"Error": "No books found"}), 400

        return Response(json.dumps([B.to_dict() for B in Books_List], ensure_ascii=False, indent=2),status=200,mimetype='application/json')