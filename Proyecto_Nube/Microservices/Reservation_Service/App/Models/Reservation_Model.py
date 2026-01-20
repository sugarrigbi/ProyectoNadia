from Config import db

class Reservation(db.Model):
    __tablename__ = "tbl_reservations"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Reservation_Date = db.Column(db.DateTime,server_default=db.func.current_timestamp())
    Expiration_Date = db.Column(db.DateTime, nullable=False)

    Fk_Book = db.Column(db.Integer,db.ForeignKey("tbl_books.ID"),nullable=False)
    Fk_User = db.Column(db.Integer,db.ForeignKey("tbl_user.ID"),nullable=False)
    Fk_Status = db.Column(db.String(20),db.ForeignKey("tbl_reservation_status.ID"),nullable=False)

    Status = db.relationship("ReservationStatus", backref="Reservations")

    def __repr__(self):
        return f"<Reservation ID={self.ID}>"
class Reservation_Status(db.Model):
    __tablename__ = "tbl_reservation_status"

    ID = db.Column(db.String(20), primary_key=True)
    Status_Name = db.Column(db.String(20), nullable=False, unique=True)

    def __repr__(self):
        return f"<ReservationStatus {self.ID}>"
class Reservation_History(db.Model):
    __tablename__ = "tbl_reservations_history"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Action_Date = db.Column(db.DateTime,server_default=db.func.current_timestamp())
    Action = db.Column(db.String(50), nullable=False)

    Fk_Performed_By = db.Column(db.Integer,db.ForeignKey("tbl_user.ID"),nullable=True)
    Fk_Reservation = db.Column(db.Integer,db.ForeignKey("tbl_reservations.ID"),nullable=False)

    Reservation = db.relationship("Reservation", backref="History")

    def __repr__(self):
        return f"<ReservationHistory {self.ID} {self.Action}>"
