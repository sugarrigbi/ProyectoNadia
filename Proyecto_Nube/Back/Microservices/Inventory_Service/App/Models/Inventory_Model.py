from App.Utilities.Extension import db, Base_Model

class Book_Status(Base_Model):
    __tablename__ = "tbl_book_status"

    ID = db.Column(db.String(20), primary_key=True, nullable=False)
    Status_Name = db.Column(db.String(30), unique=True, nullable=False)

    Copies = db.relationship("BookCopy", backref="status", lazy=True)

    def __repr__(self):
        return f"<BookStatus {self.Status_Name}>"
class Inventory(Base_Model):
    __tablename__ = "tbl_inventory"

    ID = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    Barcode = db.Column(db.String(50), nullable=False, unique=True)
    Acquisition_Date = db.Column(db.DateTime, nullable=False)
    
    Created_At = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)

    Fk_Location = db.Column(db.String(50), db.ForeignKey("tbl_inventory_location.ID"), nullable=False)
    Fk_Book = db.Column(db.Integer, db.ForeignKey("tbl_books.ID"), nullable=False)
    Fk_Status = db.Column(db.String(20), db.ForeignKey("tbl_book_status.ID"), nullable=False)

    def __repr__(self):
        return f"<Book_Copy {self.Barcode} - Status {self.Fk_Status}>"
class Inventory_History(Base_Model):
    __tablename__ = "tbl_inventory_history"

    ID = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    Movement_Date = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    Notes = db.Column(db.String(255), nullable=False)
    
    Fk_Performed_By_User = db.Column(db.Integer, db.ForeignKey("tbl_user.ID"), nullable=False)
    Fk_Book_Copy = db.Column(db.Integer, db.ForeignKey("tbl_book_copies.ID"), nullable=False)
    Fk_Previous_Status = db.Column(db.String(20), db.ForeignKey("tbl_book_status.ID"), nullable=False)
    Fk_New_Status = db.Column(db.String(20), db.ForeignKey("tbl_book_status.ID"), nullable=False)

    def __repr__(self):
        return f"<Inventory_History {self.ID} - Notes {self.Notes}>"
class Inventory_Location(Base_Model):
    __tablename__ = "tbl_inventory_location"

    ID = db.Column(db.String(50), primary_key=True, nullable=False)
    Location_Name = db.Column(db.String(50), unique=True, nullable=False)

    Copies = db.relationship("BookCopy", backref="location", lazy=True)

    def __repr__(self):
        return f"<BookStatus {self.Status_Name}>"