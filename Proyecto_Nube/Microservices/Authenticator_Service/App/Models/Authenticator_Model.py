from Config import db

class User(db.Model):
    __tablename__ = "tbl_user"

    ID = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    Username = db.Column(db.String(50), nullable=False, unique=True)
    Password_Hash = db.Column(db.String(255), nullable=False)
    Created_At = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    Is_Blocked = db.Column(db.Boolean, nullable=False, default=0)
    Failed_Attempts = db.Column(db.Integer, nullable=False, default=0)
    Active_2FA = db.Column(db.Boolean, nullable=False, default=0)
    SecretKey_2FA = db.Column(db.String(255), )

    Fk_Role = db.Column(db.String(50), db.ForeignKey("tbl_user_roles.ID"), nullable=False)
    Fk_State = db.Column(db.String(50), db.ForeignKey("tbl_user_states.ID"), nullable=False)

    def __repr__(self):
        return f"<Username {self.Username}>"
class User_Roles(db.Model):
    __tablename__ = "tbl_user_roles"

    ID = db.Column(db.String(50), primary_key=True, nullable=False)
    Role_Name = db.Column(db.String(50), nullable=False, unique=True)

    Roles = db.relationship("User", backref="roles", lazy=True)

    def __repr__(self):
        return f"<Role_Name {self.Role_Name}>"
class User_States(db.Model):
    __tablename__ = "tbl_user_states"

    ID = db.Column(db.String(50), primary_key=True, nullable=False)
    Status_Name = db.Column(db.String(50), nullable=False, unique=True)

    States = db.relationship("User", backref="status", lazy=True)

    def __repr__(self):
        return f"<Status_Name {self.Status_Name}>"
class Refresh_Token(db.Model):
    __tablename__ = "tbl_refresh_tokens"

    ID = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    Token = db.Column(db.String(255), nullable=False)
    Expires_At = db.Column(db.DateTime, nullable=False)
    Revoked = db.Column(db.Boolean, nullable=False, default=0)
    Created_At = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    Fk_User = db.Column(db.Integer, db.ForeignKey("tbl_user.ID"), nullable=False)

    Token = db.relationship("User", backref="token", lazy=True)

    def __repr__(self):
        return f"<Token {self.Token}>"