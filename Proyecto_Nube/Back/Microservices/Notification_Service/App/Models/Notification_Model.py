from Config import db

class Notification(db.Model):
    __tablename__ = "tbl_notifications"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Title = db.Column(db.String(100), nullable=True)
    Message = db.Column(db.Text, nullable=False)
    Created_At = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    Fk_Status = db.Column(db.String(20),db.ForeignKey("tbl_notification_status.ID"),nullable=False)
    Fk_User = db.Column(db.Integer,db.ForeignKey("tbl_user.ID"),nullable=False)

    Status = db.relationship("NotificationStatus", backref="Notifications")

    def __repr__(self):
        return f"<Notification {self.ID}>"
class Notification_Status(db.Model):
    __tablename__ = "tbl_notification_status"

    ID = db.Column(db.String(20), primary_key=True)
    Status_Name = db.Column(db.String(30), nullable=False, unique=True)

    def __repr__(self):
        return f"<NotificationStatus {self.ID}>"
class Notification_History(db.Model):
    __tablename__ = "tbl_notification_history"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Event_Date = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    Notes = db.Column(db.String(255), nullable=True)

    Fk_Notification = db.Column(db.Integer,db.ForeignKey("tbl_notifications.ID"),nullable=True)

    Notification = db.relationship("Notification", backref="History")

    def __repr__(self):
        return f"<NotificationHistory {self.ID}>"

