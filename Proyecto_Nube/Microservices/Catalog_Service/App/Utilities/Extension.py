from flask_sqlalchemy import SQLAlchemy
from flask import Response, json
db = SQLAlchemy()

class Base_Model(db.Model):
    __abstract__ = True

    def to_dict(self):
        return {c.name: getattr(self, c.name) if getattr(self, c.name) is not None else "" for c in self.__table__.columns}