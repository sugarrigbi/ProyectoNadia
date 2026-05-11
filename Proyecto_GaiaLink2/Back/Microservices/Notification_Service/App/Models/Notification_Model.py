from App.Utilities.Tables import db, Modelo_Base

class Correo_Auditoria(Modelo_Base):
    __tablename__ = "Correo_Auditoria"

    ID = db.Column(db.Integer, primary_key=True)

    Accion = db.Column(db.String(100), nullable=False)
    Template = db.Column(db.String(100), nullable=False)
    Correo = db.Column(db.String(100), nullable=False)
    Fecha_Modificacion = db.Column(db.DateTime, server_default=db.func.now())