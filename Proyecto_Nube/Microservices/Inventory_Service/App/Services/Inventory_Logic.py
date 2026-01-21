from Config import db
from App.Models.Inventory_Model import Book_Copies, Book_Status, Inventory_History

class Book_Service:
    @staticmethod
    def Create(data):
        Book = Book_Copies(**data)
        db.session.add(Book)
        db.session.commit()
        return Book
    
    @staticmethod
    def Read_All():
        return Book_Copies.query.all()
    
    @staticmethod
    def Read_One(Book_Id):
        return Book_Copies.query.get(Book_Id)
    
    @staticmethod
    def Update(Book_Id, data):
        Book = Book_Copies.query.get(Book_Id)
        if not Book:
            return False
        
        for Key, Value in data.items():
            setattr(Book,   Key, Value)

        db.session.commit()
        return Book
    
    @staticmethod
    def Delete(Book_Id):
        Book = Book_Copies.query.get(Book_Id)
        if not Book:
            return False
        
        db.session.delete(Book)
        db.session.commit()
        
        return True



