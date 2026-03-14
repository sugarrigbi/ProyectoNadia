from App.Utilities.Tables import db, Modelo_Base
from datetime import datetime

#FORMULARIOS
class Tipo_Formulario(Modelo_Base):
    __tablename__ = "Tipo_Formulario"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(50), nullable=False)
    Creado_En = db.Column(db.DateTime, default=datetime.utcnow)
    calificanos = db.relationship("Calificanos", backref="tipo_formulario", lazy=True)
    ayuda = db.relationship("Ayuda", backref="tipo_formulario", lazy=True)
    contactanos = db.relationship("Contactanos", backref="tipo_formulario", lazy=True)
class Calificanos(Modelo_Base):
    __tablename__ = "Calificanos"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)

    Pregunta1 = db.Column(db.String(100), nullable=False)
    Pregunta2 = db.Column(db.String(100), nullable=False)
    Pregunta3 = db.Column(db.String(100), nullable=False)
    Pregunta4 = db.Column(db.String(100), nullable=False)

    Creado_En = db.Column(db.DateTime, default=datetime.utcnow)

    Tipo_Formulario_ID = db.Column(db.Integer,db.ForeignKey("Tipo_Formulario.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False,index=True,default=1)
class Ayuda(Modelo_Base):
    __tablename__ = "Ayuda"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(50), nullable=False)
    Correo = db.Column(db.String(200), nullable=False)
    Soporte = db.Column(db.String(255), nullable=False)
    Creado_En = db.Column(db.DateTime, default=datetime.utcnow)
    Tipo_Formulario_ID = db.Column(db.Integer,db.ForeignKey("Tipo_Formulario.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False,index=True,default=2)
class Contactanos(Modelo_Base):
    __tablename__ = "Contactanos"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)

    Nombre = db.Column(db.String(50), nullable=False)
    Telefono = db.Column(db.String(12), nullable=False)
    Correo = db.Column(db.String(100), nullable=False)
    Mensaje = db.Column(db.String(255), nullable=False)
    Creado_En = db.Column(db.DateTime, default=datetime.utcnow)

    Tipo_Formulario_ID = db.Column(db.Integer,db.ForeignKey("Tipo_Formulario.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False,index=True,default=3)
