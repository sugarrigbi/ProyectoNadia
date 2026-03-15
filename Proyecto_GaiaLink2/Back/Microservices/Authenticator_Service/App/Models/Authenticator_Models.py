from App.Utilities.Tables import db, Modelo_Base
from datetime import datetime

class Rol(Modelo_Base):
    __tablename__ = "Rol"

    ID = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50), nullable=False, unique=True)
    Creado_En = db.Column(db.DateTime, server_default=db.func.now())
class Estado_Usuario(Modelo_Base):
    __tablename__ = "Estado_Usuario"

    ID = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50), nullable=False, unique=True)
    Creado_En = db.Column(db.DateTime, server_default=db.func.now())
class Estado_Dispositivo(Modelo_Base):
    __tablename__ = "Estado_Dispositivo"

    ID = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50), nullable=False, unique=True)
    Creado_En = db.Column(db.DateTime, server_default=db.func.now())
class Usuario(Modelo_Base):
    __tablename__ = "Usuario"

    ID = db.Column(db.Integer, primary_key=True)

    Nombre = db.Column(db.String(50), nullable=False, unique=True)
    Correo = db.Column(db.String(100), nullable=False, unique=True)
    Contraseña = db.Column(db.String(255), nullable=False)

    Intentos_Fallidos = db.Column(db.Integer, default=0)
    Bloqueado_Hasta = db.Column(db.DateTime)

    Creado_En = db.Column(db.DateTime, server_default=db.func.now())
    Actualizado_En = db.Column(db.DateTime, onupdate=db.func.now())

    Autenticador = db.Column(db.Boolean, default=False)
    Autenticador_Secreto = db.Column(db.String(255))

    Estado_Usuario_ID = db.Column(db.Integer,db.ForeignKey("Estado_Usuario.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False,default=1)
    Rol_ID = db.Column(db.Integer,db.ForeignKey("Rol.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False,default=2)

    estado = db.relationship("Estado_Usuario")
    rol = db.relationship("Rol")
class Usuario_Auditoria(Modelo_Base):
    __tablename__ = "Usuario_Auditoria"

    ID = db.Column(db.Integer, primary_key=True)

    Accion = db.Column(db.String(100), nullable=False)
    Fecha_Modificacion = db.Column(db.DateTime, server_default=db.func.now())

    Modificado_Por = db.Column(db.Integer,db.ForeignKey("Usuario.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
    Usuario_ID = db.Column(db.Integer,db.ForeignKey("Usuario.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
class Dispositivos(Modelo_Base):
    __tablename__ = "Dispositivos"

    ID = db.Column(db.Integer, primary_key=True)

    IP = db.Column(db.String(15), nullable=False)
    Token = db.Column(db.String(255), nullable=False, unique=True)

    Navegador = db.Column(db.String(120), nullable=False)
    Sistema = db.Column(db.String(50), nullable=False)
    Dispositivo = db.Column(db.String(120), nullable=False)

    Fecha_Conexion = db.Column(db.DateTime, server_default=db.func.now())
    Ultimo_Uso = db.Column(db.DateTime, nullable=False)

    Estado_Dispositivo_ID = db.Column(db.Integer,db.ForeignKey("Estado_Dispositivo.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False, default=1)
    Usuario_ID = db.Column(db.Integer,db.ForeignKey("Usuario.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)

    estado = db.relationship("Estado_Dispositivo")
    usuario = db.relationship("Usuario")
class Dispositivos_Auditoria(Modelo_Base):
    __tablename__ = "Dispositivos_Auditoria"

    ID = db.Column(db.Integer, primary_key=True)

    Accion = db.Column(db.String(100), nullable=False)
    Fecha_Modificacion = db.Column(db.DateTime, server_default=db.func.now())

    Modificado_Por = db.Column(db.Integer,db.ForeignKey("Usuario.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
    Dispositivos_ID = db.Column(db.Integer,db.ForeignKey("Dispositivos.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)    