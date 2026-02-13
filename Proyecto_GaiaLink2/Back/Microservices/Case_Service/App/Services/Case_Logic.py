from App.Utilities.Extension import db
from App.Models.Case_Model import *
from sqlalchemy import and_

class Case_Service:
    @staticmethod
    def Create(Data):
        Case = Caso(**Data)
        db.session.add(Case)
        db.session.commit()
        return Case
    @staticmethod
    def Read_All():
        return Caso.query.order_by(Caso.ID.asc()).all()
    @staticmethod
    def Read_One(Book_Id):
        Book = Caso.query.get(Book_Id)

        if not Book:
            return False
        
        return Book
    @staticmethod
    def Read_By(Field, Value):
        if not hasattr(Caso, Field):
            return False
        
        Column = getattr(Caso, Field)

        return Caso.query.filter(Column.ilike(f"%{Value}%")).all()
    @staticmethod
    def Update(Book_Id, Data):
        Book = Caso.query.get(Book_Id)
        if not Book:
            return False

        FIELD_MAP = {
            "Año": "Publication_Year",
            "Páginas": "Pages",
            "Idioma": "Language"
        }

        for key, value in Data.items():
            if value is None or value == "":
                continue

            if key in FIELD_MAP:
                setattr(Book, FIELD_MAP[key], value)

        # Relaciones (FK)
        if "Editorial" in Data and Data["Editorial"]:
            Book.Fk_Publisher = Data["Editorial"]

        if "Categoría" in Data and Data["Categoría"]:
            Book.Fk_Category = Data["Categoría"]

        db.session.commit()
        return Book
    @staticmethod
    def Delete(Book_Id):
        Book = Caso.query.get(Book_Id)
        if not Book:
            return False
        
        Copies_Count = Caso.query.filter_by(Fk_Book=Book_Id).count()

        if Copies_Count > 0:
            return False
        
        db.session.delete(Book)
        db.session.commit()
        
        return True
    @staticmethod
    def Delete_Selected(Books_List):
        for Book_Id in Books_List:
            Book = Caso.query.get(Book_Id)
            if Book:
                db.session.delete(Book)  
        db.session.commit()
        return True