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

    def to_dict(self, exclude=None):
        resultado = {
            "ID": self.ID,
            "Nombre": self.Nombre, 
            "Localidad": {
                "ID": self.localidad.ID,
                "Nombre": self.localidad.Nombre,
                "Ciudad": {
                    "ID": self.localidad.ciudad.ID,
                    "Nombre": self.localidad.ciudad.Nombre,
                    "Departamento": {
                        "ID": self.localidad.ciudad.departamento.ID,
                        "Nombre": self.localidad.ciudad.departamento.Nombre                        
                    }                    
                }       
            }
        }

        return resultado
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

    usuario = db.relationship("Usuario", back_populates="persona")
    barrio = db.relationship("Barrio")
    tipo_documento = db.relationship("Tipo_Documento")
class Persona_Auditoria(Modelo_Base):
    __tablename__ = "Persona_Auditoria"

    ID = db.Column(db.Integer, primary_key=True)

    Accion = db.Column(db.String(100), nullable=False)
    Fecha_Modificacion = db.Column(db.DateTime, server_default=db.func.now())

    Modificado_Por = db.Column(db.Integer,db.ForeignKey("Usuario.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
    Persona_ID = db.Column(db.Integer,db.ForeignKey("Persona.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False) 
class Usuario(Modelo_Base):
    __tablename__ = "Usuario"
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(50), nullable=False, unique=True)
    Correo = db.Column(db.String(100), nullable=False, unique=True)
    Contraseña = db.Column(db.String(255), nullable=False)
    Intentos_Fallidos = db.Column(db.Integer, nullable=False, default=0)
    Bloqueado_Hasta = db.Column(db.DateTime, nullable=True)
    Creado_En = db.Column(db.DateTime, server_default=db.func.now())
    Ultimo_Ingreso = db.Column(db.DateTime, server_default=db.func.now())
    Autenticador = db.Column(db.Boolean, nullable=False, default=False)

    Estado_Usuario_ID = db.Column(db.Integer,db.ForeignKey("Estado_Usuario.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
    estado_usuario = db.relationship("Estado_Usuario")

    Rol_ID = db.Column(db.Integer,db.ForeignKey("Rol.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
    rol = db.relationship("Rol")

    persona = db.relationship("Persona", back_populates="usuario", uselist=False)

    def to_dict(self, exclude=None):
        resultado = {
            "ID": self.ID,
            "Nombre": self.Nombre,
            "Correo": self.Correo,
            "Estado_Usuario_ID": self.Estado_Usuario_ID,
            "Rol_ID": self.Rol_ID,
            "Persona": {
                "ID": self.persona.ID,
                "Documento": self.persona.Documento,
                "Primer_Nombre": self.persona.Primer_Nombre,
                "Segundo_Nombre": self.persona.Segundo_Nombre,
                "Primer_Apellido": self.persona.Primer_Apellido,
                "Segundo_Apellido": self.persona.Segundo_Apellido           
            }
        }
        return resultado
    def to_dict2(self, exclude=None):
        resultado = {
            "ID": self.ID,
            "Nombre": self.Nombre,
            "Persona": {
                "Primer_Nombre": self.persona.Primer_Nombre,
                "Segundo_Nombre": self.persona.Segundo_Nombre,
                "Primer_Apellido": self.persona.Primer_Apellido,
                "Segundo_Apellido": self.persona.Segundo_Apellido           
            }
        }
        return resultado    
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

    ID = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50), nullable=False, unique=True)
    Creado_En = db.Column(db.DateTime, server_default=db.func.now())

    Permisos = db.relationship("RolAPermiso", back_populates="Rol_Permiso")
class Estado_Usuario(Modelo_Base):
    __tablename__ = "Estado_Usuario"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(50), nullable=False, unique=True)
    Creado_En = db.Column(db.DateTime, server_default=db.func.now())
class Tipo_Documento(Modelo_Base):
    __tablename__ = "Tipo_Documento"

    ID = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50), nullable=False, unique=True)
    Abreviatura = db.Column(db.String(10), nullable=False, unique=True)
    Creado_En = db.Column(db.DateTime, server_default=db.func.now())    
class Permiso(Modelo_Base):
    __tablename__ = "Permiso"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Permiso = db.Column(db.String(50), unique=True, nullable=False)
    Creado_En = db.Column(db.DateTime, server_default=db.func.now())

    Roles = db.relationship("RolAPermiso", back_populates="Permiso_Rol")
class RolAPermiso(Modelo_Base):
    __tablename__ = "Rol_a_Permiso"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Rol_ID = db.Column(db.Integer, db.ForeignKey("Rol.ID", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    Permiso_ID = db.Column(db.Integer, db.ForeignKey("Permiso.ID", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    Creado_En = db.Column(db.DateTime, server_default=db.func.now())

    Rol_Permiso = db.relationship("Rol", back_populates="Permisos")
    Permiso_Rol = db.relationship("Permiso", back_populates="Roles")
    def to_dict(self, exclude=None):
        resultado = {
            "Nombre": self.Permiso_Rol.Permiso
        }
        return resultado  
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
    Anterior = db.Column(db.Text, nullable=False)
    Modificado_Por = db.Column(db.Integer,db.ForeignKey("Usuario.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False,index=True)
    Fecha_Modificacion = db.Column(db.DateTime, default=datetime.utcnow)
    Entidad_ID = db.Column(db.Integer,db.ForeignKey("Entidad.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False,index=True)