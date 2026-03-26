from App.Utilities.Tables import db, Modelo_Base
from datetime import datetime
import json

#CASOS
class Caso(Modelo_Base):
    __tablename__ = "Caso"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Creacion = db.Column(db.DateTime, default=datetime.utcnow)
    Nombre = db.Column(db.String(100), nullable=False)
    Descripcion = db.Column(db.String(255), nullable=False)
    Afectados = db.Column(db.Integer, nullable=False)
    Direccion = db.Column(db.String(60), nullable=False)
    Caso_Asociado = db.Column(db.String(10), nullable=False, default="SI")
    Actualizado_En = db.Column(db.DateTime, onupdate=db.func.now())
    Usuario_Creador_ID = db.Column(db.Integer, db.ForeignKey("Usuario.ID", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    Usuario_Asociado_ID = db.Column(db.Integer, db.ForeignKey("Usuario.ID", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    Incidente_ID = db.Column(db.Integer, db.ForeignKey("Incidente.ID", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    Estado_Caso_ID = db.Column(db.Integer, db.ForeignKey("Estado_Caso.ID", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    Prioridad_ID = db.Column(db.Integer, db.ForeignKey("Prioridad.ID", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    Barrio_ID = db.Column(db.Integer, db.ForeignKey("Barrio.ID", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)

    usuario_creador = db.relationship("Usuario", foreign_keys=[Usuario_Creador_ID], backref="casos_creados")
    usuario_asociado = db.relationship("Usuario", foreign_keys=[Usuario_Asociado_ID], backref="casos_asociados")
    incidente = db.relationship("Incidente", backref="casos")
    estado = db.relationship("Estado_Caso", backref="casos")
    prioridad = db.relationship("Prioridad", backref="casos")
    barrio = db.relationship("Barrio", backref="casos")
class Caso_Auditoria(Modelo_Base):
    __tablename__ = "Caso_Auditoria"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Accion = db.Column(db.String(100), nullable=False)
    Anterior = db.Column(db.Text, nullable=False)
    Fecha_Modificacion = db.Column(db.DateTime, default=datetime.utcnow)

    Caso_ID = db.Column(db.Integer,db.ForeignKey("Caso.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
    caso = db.relationship("Caso", backref="auditorias")
    Modificado_Por = db.Column(db.Integer,db.ForeignKey("Usuario.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
    usuario = db.relationship("Usuario")

    def to_dict(self, exclude=None):
        resultado = {
            "Accion": self.Accion,
            "Caso_ID": self.Caso_ID,
            "Fecha_Modificacion": self.Fecha_Modificacion.strftime("%Y-%m-%d %H:%M:%S"),
            "ID": self.ID,
            "Modificado_Por": {
                "ID": self.usuario.persona.ID,
                "Documento": self.usuario.persona.Documento,
                "Primer_Nombre": self.usuario.persona.Primer_Nombre,
                "Segundo_Nombre": self.usuario.persona.Segundo_Nombre,
                "Primer_Apellido": self.usuario.persona.Primer_Apellido,
                "Segundo_Apellido": self.usuario.persona.Segundo_Apellido                     
            }
        }
        return resultado
    def to_dict2(self, exclude=None):
        anterior_dict = json.loads(self.Anterior)
        resultado = {
            "Accion": self.Accion,
            "Anterior": {
                "Estado": anterior_dict.get("estado", {}).get("Nombre")
            },
            "Caso_ID": self.Caso_ID,
            "Mod_Fecha": self.Fecha_Modificacion.strftime("%Y-%m-%d"),
            "Mod_Hora": self.Fecha_Modificacion.strftime("%H:%M:%S"),
            "ID": self.ID,
            "Modificado_Por": {
                "ID": self.usuario.persona.ID,
                "Documento": self.usuario.persona.Documento,
                "Primer_Nombre": self.usuario.persona.Primer_Nombre,
                "Segundo_Nombre": self.usuario.persona.Segundo_Nombre,
                "Primer_Apellido": self.usuario.persona.Primer_Apellido,
                "Segundo_Apellido": self.usuario.persona.Segundo_Apellido                     
            }
        }
        return resultado        
class Radicado_Caso(Modelo_Base):
    __tablename__ = "Radicado_Caso"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Radicado = db.Column(db.String(40), nullable=False, unique=True)

    Caso_ID = db.Column(db.Integer,db.ForeignKey("Caso.ID", ondelete="RESTRICT", onupdate="CASCADE"),nullable=False)
    caso = db.relationship("Caso", backref="radicados")
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
class Caso_Discusion(Modelo_Base):
    __tablename__ = "Caso_Discusion"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Caso_ID = db.Column(db.Integer, db.ForeignKey("Caso.ID", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    Usuario_ID = db.Column(db.Integer, db.ForeignKey("Usuario.ID", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    Mensaje = db.Column(db.Text, nullable=False)
    Creado_En = db.Column(db.DateTime, default=datetime.utcnow)

    caso = db.relationship("Caso", backref="discusiones")
    usuario = db.relationship("Usuario", backref="discusiones")
    def to_dict(self, exclude=None):
        if exclude is None:
            exclude = []
        resultado = {
            "Caso_ID": self.Caso_ID,
            "Creado_En": self.Creado_En,
            "ID": self.ID,
            "Mensaje": self.Mensaje,  
            "Nombre": self.usuario.Nombre,
            "Persona": {
                "ID": self.usuario.persona.ID,
                "Documento": self.usuario.persona.Documento,
                "Primer_Nombre": self.usuario.persona.Primer_Nombre,
                "Segundo_Nombre": self.usuario.persona.Segundo_Nombre,
                "Primer_Apellido": self.usuario.persona.Primer_Apellido,
                "Segundo_Apellido": self.usuario.persona.Segundo_Apellido           
            }    
        }
        return resultado    
class Casos_a_Casos(Modelo_Base):
    __tablename__ = "Casos_a_Casos"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Caso_Principal_ID = db.Column(db.Integer, db.ForeignKey("Caso.ID", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    Caso_Asociado_ID = db.Column(db.Integer, db.ForeignKey("Caso.ID", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    Tipo_Relacion_ID = db.Column(db.Integer, db.ForeignKey("Tipo_Relacion.ID", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    Creado_En = db.Column(db.DateTime, default=datetime.utcnow)

    caso_principal = db.relationship("Caso", foreign_keys=[Caso_Principal_ID], backref="casos_asociados")
    caso_asociado = db.relationship("Caso", foreign_keys=[Caso_Asociado_ID], backref="casos_principales")
    tipo_relacion = db.relationship("Tipo_Relacion", backref="casos_relacionados")

    def to_dict(self, exclude=None):
        resultado = {
            "ID": self.ID,
            "Caso_Principal_ID": self.Caso_Principal_ID,
            "Creado_En": self.Creado_En,
            "Caso_Asociado_ID": {
                "ID": self.caso_asociado.ID,
                "Radicado": self.caso_asociado.radicados[0].Radicado,
                "Nombre": self.caso_asociado.Nombre,
                "Actualizado": self.caso_asociado.Actualizado_En,
                "Estado": self.caso_asociado.estado.Nombre
            },
            "Tipo_Relacion_ID": self.tipo_relacion.Nombre,
            "Tipo_Relacion_ID_ID": self.tipo_relacion.ID
        }
        return resultado
    def to_dict2(self, exclude=None):
        resultado = {
            "ID": self.ID,
            "Caso_Principal_ID": self.Caso_Principal_ID,
            "Creado_En": self.Creado_En,
            "Caso_Asociado_ID": self.caso_asociado.ID,
            "Tipo_Relacion_ID": self.tipo_relacion.Nombre,
            "Tipo_Relacion_ID_ID": self.tipo_relacion.ID
        }
        return resultado    
class Tipo_Relacion(Modelo_Base):
    __tablename__ = "Tipo_Relacion"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(50), unique=True, nullable=False)
    Creado_En = db.Column(db.DateTime, default=datetime.utcnow)
class Estado_Caso(Modelo_Base):
    __tablename__ = "Estado_Caso"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(50), unique=True, nullable=False)
    Creado_En = db.Column(db.DateTime, default=datetime.utcnow)
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
#USUARIOS
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
    Autenticador = db.Column(db.Boolean, nullable=False, default=False)
    Autenticador_Secreto = db.Column(db.String(255), nullable=True)

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