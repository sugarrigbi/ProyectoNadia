from sqlalchemy.inspection import inspect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Modelo_Base(db.Model):
    __abstract__ = True

    def to_dict(self):
        Resultado = {}
        for Columna in inspect(self).mapper.column_attrs:
            Valor = getattr(self, Columna.key)
            if isinstance(Valor, datetime):
                Valor = Valor.isoformat()
            Resultado[Columna.key] = Valor
        return Resultado