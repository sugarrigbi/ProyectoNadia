from App.Utilities.Tables import db, Modelo_Base
from datetime import datetime

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

    Pais_ID = db.Column(db.Integer,db.ForeignKey("Pais.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False, default=1)
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
class Tipo_Documento(Modelo_Base):
    __tablename__ = "Tipo_Documento"

    ID = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50), nullable=False, unique=True)
    Abreviatura = db.Column(db.String(10), nullable=False, unique=True)
    Creado_En = db.Column(db.DateTime, server_default=db.func.now())
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
class Persona(Modelo_Base):
    __tablename__ = "Persona"

    ID = db.Column(db.Integer, primary_key=True)

    Tipo_Documento_ID = db.Column(db.Integer,db.ForeignKey("Tipo_Documento.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
    Documento = db.Column(db.String(20), nullable=False)

    Primer_Nombre = db.Column(db.String(50), nullable=False)
    Segundo_Nombre = db.Column(db.String(50))

    Primer_Apellido = db.Column(db.String(50), nullable=False)
    Segundo_Apellido = db.Column(db.String(50))

    Direccion = db.Column(db.String(255), nullable=False)
    Telefono = db.Column(db.String(15), nullable=False)

    Terminos_Condiciones = db.Column(db.Boolean, nullable=False, default=1)

    Fecha_Nacimiento = db.Column(db.Date, nullable=False)

    Creado_En = db.Column(db.DateTime, server_default=db.func.now())
    Actualizado_En = db.Column(db.DateTime, onupdate=db.func.now())

    Usuario_ID = db.Column(db.Integer,db.ForeignKey("Usuario.ID", ondelete="RESTRICT", onupdate="CASCADE"),unique=True,nullable=False)

    Barrio_ID = db.Column(db.Integer,db.ForeignKey("Barrio.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)

    usuario = db.relationship("Usuario")
    barrio = db.relationship("Barrio")
    tipo_documento = db.relationship("Tipo_Documento")
class Persona_Auditoria(Modelo_Base):
    __tablename__ = "Persona_Auditoria"

    ID = db.Column(db.Integer, primary_key=True)

    Accion = db.Column(db.String(100), nullable=False)
    Fecha_Modificacion = db.Column(db.DateTime, server_default=db.func.now())

    Modificado_Por = db.Column(db.Integer,db.ForeignKey("Usuario.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
    Persona_ID = db.Column(db.Integer,db.ForeignKey("Persona.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)      
