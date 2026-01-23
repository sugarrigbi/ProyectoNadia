from App.Utilities.Extension import db
from App.Models.Catalog_Model import Books, Categories, Publisher, Authors, Books_Authors, Book_Copies
from sqlalchemy import and_

class Books_Service:
    @staticmethod
    def Create(Data):
        Book = Books(**Data)
        db.session.add(Book)
        db.session.commit()
        return Book
    @staticmethod
    def Read_All():
        return Books.query.order_by(Books.ID.asc()).all()
    @staticmethod
    def Read_One(Book_Id):
        Book = Books.query.get(Book_Id)

        if not Book:
            return False
        
        return Book
    @staticmethod
    def Read_By(Field, Value):
        if not hasattr(Books, Field):
            return False
        
        Column = getattr(Books, Field)

        return Books.query.filter(Column.ilike(f"%{Value}%")).all()
    @staticmethod
    def Update(Book_Id, Data):
        Book = Books.query.get(Book_Id)
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
        Book = Books.query.get(Book_Id)
        if not Book:
            return False
        
        Copies_Count = Book_Copies.query.filter_by(Fk_Book=Book_Id).count()

        if Copies_Count > 0:
            return False
        
        db.session.delete(Book)
        db.session.commit()
        
        return True
    @staticmethod
    def Delete_Selected(Books_List):
        for Book_Id in Books_List:
            Book = Books.query.get(Book_Id)
            if Book:
                db.session.delete(Book)  
        db.session.commit()
        return True
class Categories_Service:
    @staticmethod
    def Create(Data):
        Category = Categories(**Data)
        db.session.add(Category)
        db.session.commit()
        return Category
    @staticmethod
    def Read_All():
        return Categories.query.order_by(Categories.ID.asc()).all()
    @staticmethod
    def Read_One(Category_Id):
        Category = Categories.query.get(Category_Id)

        if not Category:
            return False
        
        return Category
    @staticmethod
    def Read_By(Name):
        Category = Categories.query.filter(Categories.Category_Name.ilike(f"%{Name}%")).all()

        if not Category:
            return False
        
        return Category    
    @staticmethod
    def Update(Category_Id, Data):
        Category = Categories.query.get(Category_Id)
    
        if not Category:
            return False
        
        for Key, Value in Data.items():
            setattr(Category, Key, Value)

        db.session.commit()
        return Category
    @staticmethod
    def Delete(Category_Id):
        Category = Categories.query.get(Category_Id)
        if not Category:
            return False
        
        Books_Count = Books.query.filter_by(Fk_Category=Category_Id).count()

        if Books_Count > 0:
            return False

        db.session.delete(Category)
        db.session.commit()
        
        return True
class Publisher_Service:
    @staticmethod
    def Create(Data):
        Publish = Publisher(**Data)
        db.session.add(Publish)
        db.session.commit()
        return Publish
    @staticmethod
    def Read_All():
        return Publisher.query.order_by(Publisher.ID.asc()).all()
    @staticmethod
    def Read_One(Publisher_Id):
        Publish = Publisher.query.get(Publisher_Id)

        if not Publish:
            return False
        
        return Publish
    @staticmethod
    def Read_By(Name):
        Publish = Publisher.query.filter(Publisher.Publisher_Name.ilike(f"%{Name}%")).all()
        if not Publish:
            return False
        
        return Publish
    @staticmethod
    def Update(Publisher_Id, Data):
        Publish = Publisher.query.get(Publisher_Id)
    
        if not Publish:
            return False
        
        for Key, Value in Data.items():
            setattr(Publish, Key, Value)

        db.session.commit()
        return Publish
    @staticmethod
    def Delete(Publisher_Id):
        Publish = Publisher.query.get(Publisher_Id)
        if not Publish:
            return False
        
        Books_Count = Books.query.filter_by(Fk_Publisher=Publisher_Id).count()

        if Books_Count > 0:
            return False

        db.session.delete(Publish)
        db.session.commit()
        
        return True
class Authors_Service:
    @staticmethod
    def Create(Data):
        Author = Authors(**Data)
        db.session.add(Author)
        db.session.commit()
        return Author
    @staticmethod
    def Read_All():
        return Authors.query.all()
    @staticmethod
    def Read_One(Authors_Id):
        return Authors.query.get(Authors_Id)
    @staticmethod
    def Read_By(Field, Value):
        if not hasattr(Authors, Field):
            return []
        
        Column = getattr(Authors, Field)

        if hasattr(Column.type, "length"):
            return Authors.query.filter(Column.ilike(f"%{Value}%")).all()
        
        return Authors.query.filter(Column == Value).all()
    @staticmethod
    def Update(Authors_Id, Data):
        Author = Authors.query.get(Authors_Id)
    
        if not Author:
            return False
        
        for Key, Value in Data.items():
            setattr(Author, Key, Value)

        db.session.commit()
        return Author
    @staticmethod
    def Delete(Authors_Id):
        Author = Authors.query.get(Authors_Id)
        if not Author:
            return False

        db.session.delete(Author)
        db.session.commit()
        
        return True
class Books_Authors_Service:
    @staticmethod
    def Read_By(Value):
        parts = Value.split()
        query = db.session.query(Books).join(Books_Authors, Books.ID == Books_Authors.c.Fk_Book).join(Authors, Authors.ID == Books_Authors.c.Fk_Author)

        for part in parts:
            query = query.filter((Authors.First_Name.ilike(f"%{part}%")) |(Authors.Last_Name.ilike(f"%{part}%")))

        return query.all()
