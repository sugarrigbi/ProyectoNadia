from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect
from datetime import datetime

db = SQLAlchemy()

class Modelo_Base(db.Model):
    __abstract__ = True

    def to_dict(self, include_relationships=False, exclude=None):
        if exclude is None:
            exclude = []
        resultado = {}

        for column in self.__table__.columns:
            if column.name in exclude:
                continue
            valor = getattr(self, column.name)
            if isinstance(valor, datetime):
                valor = valor.isoformat()
            resultado[column.name] = valor

        if include_relationships:
            for rel in self.__mapper__.relationships:
                if rel.key in exclude:
                    continue
                valor = getattr(self, rel.key)
                if valor is None:
                    resultado[rel.key] = None
                elif rel.uselist:
                    resultado[rel.key] = [v.to_dict(exclude=exclude) for v in valor]
                else:
                    resultado[rel.key] = valor.to_dict(exclude=exclude)

        return resultado

