from flask import request, jsonify, Response, json
from App.Services import Inventory_Logic

class Get_Inventory:
    @staticmethod
    def Inventory_Create():
        Data = request.get_json()
        if not Data:
            return jsonify({"Error": "No data provided"}), 400

        Inventory_Logic.Inventory_Service.Create(Data)
        return jsonify({"Message": "Inventory created successfully"}), 201
    @staticmethod
    def Inventory_Read_All():
        Copies = Inventory_Logic.Inventory_Service.Read_All()
        return Response(json.dumps([C.to_dict() for C in Copies], ensure_ascii=False, indent=2),status=200,mimetype="application/json")
    @staticmethod
    def Inventory_Read_One(Copy_Id):
        Copy = Inventory_Logic.Inventory_Service.Read_One(Copy_Id)
        if not Copy:
            return jsonify({"Error": "Copy not found"}), 404

        return Response(json.dumps(Copy.to_dict(), ensure_ascii=False, indent=2),status=200,mimetype="application/json")
    @staticmethod
    def Inventory_Read_By(Field, Value):
        Copy = Inventory_Logic.Inventory_Service.Read_By(Field, Value)

        if Copy == False:
            return jsonify({"Error": "No books finded"}), 400
        
        return Response(json.dumps([C.to_dict() for C in Copy], ensure_ascii=False, indent=2),status=200,mimetype='application/json')
    @staticmethod
    def Inventory_Update(Copy_Id):
        Data = request.get_json()
        if not Data:
            return jsonify({"Error": "No data provided"}), 400

        Copy = Inventory_Logic.Inventory_Service.Update(Copy_Id, Data)
        if not Copy:
            return jsonify({"Error": "Copy not updated"}), 400

        return jsonify({"Message": "Inventory updated successfully"}), 200
    @staticmethod
    def Inventory_Delete(Copy_Id):
        Copy = Inventory_Logic.Inventory_Service.Delete(Copy_Id)
        if not Copy:
            return jsonify({"Error": "Copy not deleted"}), 400

        return jsonify({"Message": "Inventory deleted successfully"}), 200
    @staticmethod
    def Inventory_Delete_Selected(Book_List):
        Book = Inventory_Logic.Inventory_Service.Delete_Selected(Book_List)

        if Book == False:
            return jsonify({"Error": "No books deleted"}), 400
        
        return jsonify({"Message": "Books deleted successfully"}), 200 