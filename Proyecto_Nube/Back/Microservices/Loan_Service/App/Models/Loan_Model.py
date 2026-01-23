from Config import db

class Loan(db.Model):
    __tablename__ = "tbl_loans"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Loan_Date = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    Due_Date = db.Column(db.Date, nullable=False)
    Return_Date = db.Column(db.DateTime, nullable=True)

    Fk_Book_Copy = db.Column(db.Integer, db.ForeignKey("tbl_book_copies.ID"), nullable=False)
    Fk_User = db.Column(db.Integer, db.ForeignKey("tbl_user.ID"), nullable=False)
    Fk_Status = db.Column(db.String(20), db.ForeignKey("tbl_loan_status.ID"), nullable=False)
    Fk_Created_By = db.Column(db.Integer, db.ForeignKey("tbl_user.ID"), nullable=False)

    Status = db.relationship("LoanStatus", backref="Loans")

    def __repr__(self):
        return f"<Loan {self.ID}>"
class Loan_Status(db.Model):
    __tablename__ = "tbl_loan_status"

    ID = db.Column(db.String(20), primary_key=True)
    Status_Name = db.Column(db.String(30), nullable=False, unique=True)

    def __repr__(self):
        return f"<LoanStatus {self.ID}>"
class Loan_History(db.Model):
    __tablename__ = "tbl_loan_history"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Change_Date = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    Notes = db.Column(db.String(255), nullable=True)

    Fk_Loan = db.Column(db.Integer, db.ForeignKey("tbl_loans.ID"), nullable=False)
    Fk_Previous_Status = db.Column(db.String(20), db.ForeignKey("tbl_loan_status.ID"))
    Fk_New_Status = db.Column(db.String(20), db.ForeignKey("tbl_loan_status.ID"))
    Fk_Performed_By = db.Column(db.Integer, db.ForeignKey("tbl_user.ID"))

    Loan = db.relationship("Loan", backref="History")
    Previous_Status = db.relationship("LoanStatus",foreign_keys=[Fk_Previous_Status],backref="Previous_History")
    New_Status = db.relationship("LoanStatus",foreign_keys=[Fk_New_Status],backref="New_History")

    def __repr__(self):
        return f"<LoanHistory {self.ID}>"


