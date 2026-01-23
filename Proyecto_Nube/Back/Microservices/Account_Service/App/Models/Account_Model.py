from Config import db

class Person(db.Model):
    __tablename__ = "tbl_person"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    First_Name = db.Column(db.String(50), nullable=False)
    Second_Name = db.Column(db.String(50), nullable=True)
    First_LastName = db.Column(db.String(50), nullable=False)
    Second_LastName = db.Column(db.String(50), nullable=True)
    Birth_Date = db.Column(db.Date, nullable=True)

    Fk_DocumentType = db.Column(db.String(50),db.ForeignKey("tbl_document_type.ID"),nullable=True)
    Fk_User = db.Column(db.Integer,db.ForeignKey("tbl_user.ID"),nullable=True)
    Fk_Address = db.Column(db.Integer,db.ForeignKey("tbl_address.ID"),nullable=False)
    Extra = db.relationship("AdditionalPersonData", backref="person", uselist=False)

    def __repr__(self):
        return f"<Person {self.First_Name} {self.First_LastName}>"
class Address(db.Model):
    __tablename__ = "tbl_address"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Address = db.Column(db.Text, nullable=True)
    Country = db.Column(db.String(50), nullable=True)
    City = db.Column(db.String(50), nullable=True)

    Persons = db.relationship("Person", backref="address", lazy=True)

    def __repr__(self):
        return f"<Address {self.City}, {self.Country}>"
class Contacts(db.Model):
    __tablename__ = "tbl_contacts"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Email = db.Column(db.String(100), nullable=True)
    Phone = db.Column(db.String(20), nullable=True)

    AddPerson = db.relationship("AdditionalPersonData", backref="contacts", uselist=False)

    def __repr__(self):
        return f"<Contacts {self.Email}>"
class Additional_Person(db.Model):
    __tablename__ = "tbl_add_person"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Privacy_Terms = db.Column(db.Boolean, default=False)

    Fk_Person = db.Column(db.Integer,db.ForeignKey("tbl_person.ID"),nullable=True)
    Fk_Contacts = db.Column(db.Integer,db.ForeignKey("tbl_contacts.ID"),nullable=False)

    def __repr__(self):
        return f"<AdditionalPersonData Privacy={self.Privacy_Terms}>"
class Document_Type(db.Model):
    __tablename__ = "tbl_document_type"

    ID = db.Column(db.String(50), primary_key=True, nullable=False)
    Document_Type = db.Column(db.String(50), nullable=False, unique=True)

    Persons = db.relationship("Person", backref="document_type", lazy=True)

    def __repr__(self):
        return f"<DocumentType {self.Document_Type}>"