from App.Utilities.Tables import db, Modelo_Base
from datetime import datetime

#USUARIOS
class Usuario(Modelo_Base):
    __tablename__ = "Usuario"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)

    Nombre = db.Column(db.String(50), nullable=False, unique=True)
    Correo = db.Column(db.String(100), nullable=False, unique=True)
    Contraseña = db.Column(db.String(255), nullable=False)
    Intentos_Fallidos = db.Column(db.Integer, nullable=False, default=0)
    Bloqueado_Hasta = db.Column(db.DateTime, nullable=True)
    Creado_En = db.Column(db.DateTime, server_default=db.func.now())
    Autenticador = db.Column(db.Boolean, nullable=False, default=False)
    Autenticador_Secreto = db.Column(db.String(255), nullable=True)

    Estado_Usuario_ID = db.Column(db.Integer,db.ForeignKey("Estado_Usuario.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
    estado_usuario = db.relationship("Estado_Usuario")
    Rol_ID = db.Column(db.Integer,db.ForeignKey("Rol.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
    rol = db.relationship("Rol")
class Usuario_Auditoria(Modelo_Base):
    __tablename__ = "Usuario_Auditoria"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Accion = db.Column(db.String(100), nullable=False)
    Fecha_Modificacion = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    Usuario_ID = db.Column(db.Integer, db.ForeignKey("Usuario.ID", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    usuario = db.relationship("Usuario", foreign_keys=[Usuario_ID], backref="auditorias_realizadas")
    Modificado_Por = db.Column(db.Integer, db.ForeignKey("Usuario.ID", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    modificado_por = db.relationship("Usuario", foreign_keys=[Modificado_Por], backref="auditorias_modificadas")
class Rol(Modelo_Base):
    __tablename__ = "Rol"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(50), nullable=False, unique=True)
    Creado_En = db.Column(db.DateTime, server_default=db.func.now())
class Estado_Usuario(Modelo_Base):
    __tablename__ = "Estado_Usuario"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(50), nullable=False, unique=True)
    Creado_En = db.Column(db.DateTime, server_default=db.func.now())
#ENTIDAD
class EstadoEntidad(Modelo_Base):
    __tablename__ = "Estado_Entidad"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(50), unique=True, nullable=False)
    Creado_En = db.Column(db.DateTime, default=datetime.utcnow)

    entidades = db.relationship("Entidad", backref="estado_entidad", lazy=True)
class Incidente(Modelo_Base):
    __tablename__ = "Incidente"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Incidente = db.Column(db.String(40), nullable=False)

    Prioridad_ID = db.Column(db.Integer,db.ForeignKey("Prioridad.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
    entidades = db.relationship("Entidad", backref="incidente", lazy=True)
class Entidad(Modelo_Base):
    __tablename__ = "Entidad"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)

    Nombre = db.Column(db.String(50), nullable=False)
    Direccion = db.Column(db.String(70), nullable=False)
    Telefono = db.Column(db.String(15), nullable=False)
    Website = db.Column(db.String(50), nullable=False)
    Descripcion = db.Column(db.String(255), nullable=False)

    Incidente_ID = db.Column(db.Integer,db.ForeignKey("Incidente.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False,index=True)
    Estado_Entidad_ID = db.Column(db.Integer,db.ForeignKey("Estado_Entidad.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False,index=True)
    auditorias = db.relationship("EntidadAuditoria", backref="entidad", lazy=True)
class EntidadAuditoria(Modelo_Base):
    __tablename__ = "Entidad_Auditoria"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)

    Accion = db.Column(db.String(100), nullable=False)

    Modificado_Por = db.Column(db.Integer,db.ForeignKey("Usuario.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False,index=True)
    Fecha_Modificacion = db.Column(db.DateTime, default=datetime.utcnow)
    Entidad_ID = db.Column(db.Integer,db.ForeignKey("Entidad.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False,index=True)