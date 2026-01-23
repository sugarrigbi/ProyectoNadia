from App.Utilities.Extension import db, Base_Model

Books_Authors = db.Table(
    'tbl_book_authors',
    db.Column('Fk_Book', db.Integer, db.ForeignKey('tbl_books.ID'), primary_key=True),
    db.Column('Fk_Author', db.Integer, db.ForeignKey('tbl_authors.ID'), primary_key=True)
)
class Books(Base_Model):
    __tablename__ = "tbl_books"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Title = db.Column(db.String(200), nullable=False)
    Isbn = db.Column(db.String(20), nullable=False, unique=True)
    Publication_Year = db.Column(db.Integer, nullable=False)
    Pages = db.Column(db.Integer, nullable=False)
    Language = db.Column(db.String(30), nullable=False)
    Created_At = db.Column(db.DateTime, default=db.func.current_timestamp())

    Fk_Category = db.Column(db.String(100),db.ForeignKey("tbl_categories.ID"),nullable=False)
    Fk_Publisher = db.Column(db.String(100),db.ForeignKey("tbl_publishers.ID"),nullable=False)

    Category = db.relationship("Categories", backref="Books")
    Publisher = db.relationship("Publisher", backref="Books")
    Authors = db.relationship("Authors",secondary=Books_Authors,back_populates="Books")

    def __repr__(self):
        return f"<Books {self.Title}>"
class Categories(Base_Model):
    __tablename__ = "tbl_categories"

    ID = db.Column(db.String(100), primary_key=True, nullable=False)
    Category_Name = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"<Category {self.Category_Name}>"
class Publisher(Base_Model):
    __tablename__ = "tbl_publishers"

    ID = db.Column(db.String(100), primary_key=True, nullable=False)
    Publisher_Name = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"<Publisher {self.Publisher_Name}>"
class Authors(Base_Model):
    __tablename__ = "tbl_authors"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    First_Name = db.Column(db.String(50), nullable=True)
    Last_Name = db.Column(db.String(50), nullable=True)

    Books = db.relationship("Books",secondary=Books_Authors,back_populates="Authors")
    
    def __repr__(self):
        return f"<Author {self.First_Name} {self.Last_Name}>"
class Book_Copies(Base_Model):
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

