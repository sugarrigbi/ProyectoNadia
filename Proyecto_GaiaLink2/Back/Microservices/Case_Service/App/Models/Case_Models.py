from App.Utilities.Tables import db, Modelo_Base
from datetime import datetime

#CASOS
class Caso(Modelo_Base):
    __tablename__ = "Caso"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Creacion = db.Column(db.DateTime, default=datetime.utcnow)
    Descripcion = db.Column(db.String(255), nullable=False)
    Afectados = db.Column(db.Integer, nullable=False)
    Direccion = db.Column(db.String(60), nullable=False)
    Caso_Asociado = db.Column(db.String(10), nullable=False)

    Usuario_ID = db.Column(db.Integer,db.ForeignKey("Usuario.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
    usuario = db.relationship("Usuario", backref="casos")
    Incidente_ID = db.Column(db.Integer,db.ForeignKey("Incidente.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
    incidente = db.relationship("Incidente", backref="casos")
    Estado_Caso_ID = db.Column(db.Integer,db.ForeignKey("Estado_Caso.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
    estado_caso = db.relationship("Estado_Caso", backref="casos")
    Prioridad_ID = db.Column(db.Integer,db.ForeignKey("Prioridad.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
    prioridad = db.relationship("Prioridad", backref="casos")
    Barrio_ID = db.Column(db.Integer,db.ForeignKey("Barrio.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
    barrio = db.relationship("Barrio", backref="casos")
class Caso_Auditoria(Modelo_Base):
    __tablename__ = "Caso_Auditoria"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Accion = db.Column(db.String(100), nullable=False)
    Fecha_Modificacion = db.Column(db.DateTime, default=datetime.utcnow)

    Caso_ID = db.Column(db.Integer,db.ForeignKey("Caso.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
    caso = db.relationship("Caso", backref="auditorias")
    Modificado_Por = db.Column(db.Integer,db.ForeignKey("Usuario.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
    usuario = db.relationship("Usuario")
class Radicado_Caso(Modelo_Base):
    __tablename__ = "Radicado_Caso"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Radicado = db.Column(db.String(40), nullable=False, unique=True)

    Caso_ID = db.Column(db.Integer,db.ForeignKey("Caso.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
    caso = db.relationship("Caso", backref="radicados")
class Estado_Caso(Modelo_Base):
    __tablename__ = "Estado_Caso"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(50), nullable=False, unique=True)
    Creado_En = db.Column(db.DateTime, server_default=db.func.now())
class Prioridad(Modelo_Base):
    __tablename__ = "Prioridad"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Prioridad = db.Column(db.String(30), nullable=False)
class Incidente(Modelo_Base):
    __tablename__ = "Incidente"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Incidente = db.Column(db.String(40), nullable=False)

    Prioridad_ID = db.Column(db.Integer, db.ForeignKey("Prioridad.ID", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    prioridad = db.relationship("Prioridad", backref="incidentes")
#UBICACION
class Pais(Modelo_Base):
    __tablename__ = "Pais"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(70), nullable=False)
    Creado_En = db.Column(db.DateTime, server_default=db.func.now())

    departamentos = db.relationship("Departamento", backref="pais")
class Departamento(Modelo_Base):
    __tablename__ = "Departamento"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(70), nullable=False)
    Creado_En = db.Column(db.DateTime, server_default=db.func.now())

    Pais_ID = db.Column(db.Integer,db.ForeignKey("Pais.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
    ciudades = db.relationship("Ciudad", backref="departamento")
class Ciudad(Modelo_Base):
    __tablename__ = "Ciudad"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(70), nullable=False)
    Creado_En = db.Column(db.DateTime, server_default=db.func.now())

    Departamento_ID = db.Column(db.Integer,db.ForeignKey("Departamento.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
    localidades = db.relationship("Localidad", backref="ciudad")
class Localidad(Modelo_Base):
    __tablename__ = "Localidad"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(70), nullable=False)
    Creado_En = db.Column(db.DateTime, server_default=db.func.now())

    Ciudad_ID = db.Column(db.Integer,db.ForeignKey("Ciudad.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
    barrios = db.relationship("Barrio", backref="localidad")
class Barrio(Modelo_Base):
    __tablename__ = "Barrio"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(70), nullable=False)
    Creado_En = db.Column(db.DateTime, server_default=db.func.now())

    Localidad_ID = db.Column(db.Integer,db.ForeignKey("Localidad.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
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