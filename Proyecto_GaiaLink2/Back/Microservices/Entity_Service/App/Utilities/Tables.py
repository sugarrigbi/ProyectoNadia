from sqlalchemy.inspection import inspect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Modelo_Base(db.Model):
    __abstract__ = True
    def to_dict(self):
        Resultado = {}
        for column in inspect(self).mapper.column_attrs:
            Valor = getattr(self, column.key)
            if isinstance(Valor, datetime):
                Valor = Valor.isoformat()
            Resultado[column.key] = Valor
        return Resultado