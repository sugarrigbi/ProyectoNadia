from Config import db

class Penalty(db.Model):
    __tablename__ = "tbl_penalties"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Amount = db.Column(db.Numeric(10, 2), nullable=False)
    Generated_Date = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    Fk_Status = db.Column(db.String(20),db.ForeignKey("tbl_penalties_status.ID"),nullable=False)
    Fk_Loan = db.Column(db.Integer,db.ForeignKey("tbl_loans.ID"),nullable=False)
    Fk_User = db.Column(db.Integer,db.ForeignKey("tbl_user.ID"),nullable=False)

    Status = db.relationship("PenaltyStatus", backref="Penalties")

    def __repr__(self):
        return f"<Penalty ID={self.ID} Amount={self.Amount}>"
class Penalty_Payment(db.Model):
    __tablename__ = "tbl_penalties_payments"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Payment_Date = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    Amount = db.Column(db.Numeric(10, 2), nullable=False)
    Payment_Method = db.Column(db.String(30), nullable=True)

    Fk_Penalty = db.Column(db.Integer,db.ForeignKey("tbl_penalties.ID"),nullable=False)

    Penalty = db.relationship("Penalty", backref="Payments")

    def __repr__(self):
        return f"<PenaltyPayment {self.ID}>"
class Penalty_Status(db.Model):
    __tablename__ = "tbl_penalties_status"

    ID = db.Column(db.String(20), primary_key=True)
    Status_Name = db.Column(db.String(30), nullable=False, unique=True)

    def __repr__(self):
        return f"<PenaltyStatus {self.ID}>"
class Penalty_History(db.Model):
    __tablename__ = "tbl_fine_history"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Change_Date = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    Fk_Performed_By = db.Column(db.Integer,db.ForeignKey("tbl_user.ID"),nullable=True)
    Fk_Penalty = db.Column(db.Integer,db.ForeignKey("tbl_penalties.ID"),nullable=False)
    Previous_Status = db.Column(db.String(20),db.ForeignKey("tbl_penalties_status.ID"),nullable=True)
    New_Status = db.Column(db.String(20),db.ForeignKey("tbl_penalties_status.ID"),nullable=True)

    Penalty = db.relationship("Penalty", backref="History")
    PreviousStatus = db.relationship("PenaltyStatus",foreign_keys=[Previous_Status])
    NewStatus = db.relationship( "PenaltyStatus", foreign_keys=[New_Status])

    def __repr__(self):
        return f"<FineHistory {self.ID}>"


