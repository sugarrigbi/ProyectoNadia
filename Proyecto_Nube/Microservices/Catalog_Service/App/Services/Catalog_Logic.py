from App.Utilities.Extension import db
from App.Models.Catalog_Model import Books, Categories, Publisher, Authors, Books_Authors

class Books_Service:
    @staticmethod
    def Create(Data):
        Book = Books(**Data)
        db.session.add(Book)
        db.session.commit()
        return Book
    @staticmethod
    def Read_All():
        return Books.query.all()    
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

        if hasattr(Column.type, "length"):
            return Books.query.filter(Column.ilike(f"%{Value}%")).all()
        return Books.query.filter(Column == Value).all()
    @staticmethod
    def Update(Book_Id, Data):
        Book = Books.query.get(Book_Id)
        if not Book:
            return False
        
        for Key, Value in Data.items():
            setattr(Book, Key, Value)

        db.session.commit()
        return Book
    @staticmethod
    def Delete(Book_Id):
        Book = Books.query.get(Book_Id)
        if not Book:
            return False
        
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
        return Categories.query.all()
    @staticmethod
    def Read_One(Category_Id):
        Category = Categories.query.get(Category_Id)

        if not Category:
            return False
        
        return Category
    @staticmethod
    def Read_By(Name):
        Category = Categories.query.filter_by(Category_Name=Name).all()

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
        return Publisher.query.all()
    @staticmethod
    def Read_One(Publisher_Id):
        return Publisher.query.get(Publisher_Id)
    @staticmethod
    def Read_By(Name):
        return Publisher.query.filter_by(Publisher_Name=Name).all()
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
        
        Books_Count = Books_Authors.query.filter_by(Fk_Author=Authors_Id).count()
        if Books_Count > 0:
            return False

        db.session.delete(Author)
        db.session.commit()
        
        return True
class Books_Authors_Service:
    @staticmethod
    def Assign_Author_Book(Book_Id, Author_Id):
        Book = Books.query.get(Book_Id)
        Author = Authors.query.get(Author_Id)

        if not Book or not Author:
            return False
        
        Exists = Books_Authors.query.filter_by(Fk_Book=Book_Id,Fk_Author=Author_Id).first()

        if Exists:
            return False
        
        Relation = Books_Authors(Fk_Book=Book_Id,Fk_Author=Author_Id)

        db.session.add(Relation)
        db.session.commit()

        return Relation
    @staticmethod
    def Delete_Author_Book(Book_Id, Author_Id):
        Relation = Books_Authors.query.filter_by(Fk_Book=Book_Id,Fk_Author=Author_Id).first()

        if not Relation:
            return False
        
        db.session.delete(Relation)
        db.session.commit()

        return True
    @staticmethod
    def Read_All_Author_Book():
        return Books_Authors.query.all()
    @staticmethod
    def Read_One_Author_Book(Book_Id, Author_Id):
        return Books_Authors.query.filter_by(Fk_Book=Book_Id,Fk_Author=Author_Id).first()
    @staticmethod
    def Read_By_Author_Book(Field, Value):
        if not hasattr(Books_Authors, Field):
            return []
        
        Column = getattr(Books_Authors, Field)

        if hasattr(Column.type, "length"):
            return Books_Authors.query.filter(Column.ilike(f"%{Value}%")).all()
        
        return Books_Authors.query.filter(Column == Value).all()
