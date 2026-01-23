from App.Utilities.Extension import db
from App.Models.Inventory_Model import Inventory, Book_Status, Inventory_Location, Inventory_History

class Inventory_Service:
    @staticmethod
    def Create(Data):
        Copy = Inventory(**Data)
        db.session.add(Copy)
        db.session.commit()
        return Copy
    @staticmethod
    def Read_All():
        return Inventory.query.order_by(Inventory.ID.asc()).all()
    @staticmethod
    def Read_One(Copy_Id):
        Copy = Inventory.query.get(Copy_Id)
        if not Copy:
            return False
        return Copy
    @staticmethod
    def Read_By(Field, Value):
        if not hasattr(Inventory, Field):
            return False

        Column = getattr(Inventory, Field)
        return Inventory.query.filter(Column == Value).all()
    @staticmethod
    def Update(Copy_Id, Data):
        Copy = Inventory.query.get(Copy_Id)
        if not Copy:
            return False

        for Key, Value in Data.items():
            setattr(Copy, Key, Value)

        db.session.commit()
        return Copy
    @staticmethod
    def Delete(Copy_Id):
        Copy = Inventory.query.get(Copy_Id)
        if not Copy:
            return False

        db.session.delete(Copy)
        db.session.commit()
        return True
    def Delete_Selected(Books_List):
        for Book_Id in Books_List:
            Book = Inventory.query.get(Book_Id)
            if Book:
                db.session.delete(Book)  
        db.session.commit()
        return True
class Inventory_Status_Service:
    @staticmethod
    def Create(Data):
        Status = Book_Status(**Data)
        db.session.add(Status)
        db.session.commit()
        return Status
    @staticmethod
    def Read_All():
        return Book_Status.query.all()
class Inventory_Location_Service:
    @staticmethod
    def Create(Data):
        Location = Inventory_Location(**Data)
        db.session.add(Location)
        db.session.commit()
        return Location
    @staticmethod
    def Read_All():
        return Inventory_Location.query.all()
class Inventory_History_Service:
    @staticmethod
    def Create(Data):
        History = Inventory_History(**Data)
        db.session.add(History)
        db.session.commit()
        return History
    @staticmethod
    def Read_By_Copy(Copy_Id):
        return Inventory_History.query.filter_by(Fk_Book_Copy=Copy_Id).all()