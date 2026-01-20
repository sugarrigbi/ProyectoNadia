from Config import db

tbl_book_authors = db.Table(
    "tbl_book_authors",
    db.Column("Fk_Book",db.Integer,db.ForeignKey("tbl_books.ID"),primary_key=True),
    db.Column("Fk_Author",db.Integer,db.ForeignKey("tbl_authors.ID"),primary_key=True)
)
class Books(db.Model):
    __tablename__ = "tbl_books"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Title = db.Column(db.String(200), nullable=False)
    Isbn = db.Column(db.String(20), nullable=True, unique=True)
    Publication_Year = db.Column(db.Integer, nullable=True)
    Pages = db.Column(db.Integer, nullable=True)
    Language = db.Column(db.String(30), nullable=True)
    Created_At = db.Column(db.DateTime, default=db.func.current_timestamp())

    Fk_Category = db.Column(db.Integer,db.ForeignKey("tbl_categories.ID"),nullable=True)
    Fk_Publisher = db.Column(db.Integer,db.ForeignKey("tbl_publishers.ID"),nullable=True)

    Authors = db.relationship("Author",secondary=tbl_book_authors,back_populates="Books")

    def __repr__(self):
        return f"<Books {self.Title}>"
class Category(db.Model):
    __tablename__ = "tbl_categories"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Category_Name = db.Column(db.String(100), nullable=False, unique=True)

    Books = db.relationship("Books", backref="category", lazy=True)

    def __repr__(self):
        return f"<Category {self.Category_Name}>"
class Publisher(db.Model):
    __tablename__ = "tbl_publishers"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Publisher_Name = db.Column(db.String(100), nullable=False, unique=True)

    Books = db.relationship("Books", backref="publisher", lazy=True)

    def __repr__(self):
        return f"<Publisher {self.Publisher_Name}>"
class Author(db.Model):
    __tablename__ = "tbl_authors"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    First_Name = db.Column(db.String(50), nullable=True)
    Last_Name = db.Column(db.String(50), nullable=True)

    Books = db.relationship("Books",secondary=tbl_book_authors,back_populates="Authors")
    
    def __repr__(self):
        return f"<Author {self.First_Name} {self.Last_Name}>"


