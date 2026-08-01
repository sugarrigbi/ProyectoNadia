from App.Models.Account_Model import (
    Dispositivos as Tabla_Dispositivos, 
    Usuario as Tabla_Usuario, 
    RolAPermiso as Tabla_Permiso, 
    Persona as Tabla_Persona,
    Barrio as Tabla_Barrio,
    Localidad as Tabla_Localidad,
    Ciudad as Tabla_Ciudad,
    Departamento as Tabla_Departamento,
    Tipo_Documento as Tabla_Documento,
    Persona_Auditoria as Tabla_P_Auditoria,
    Dispositivos_Auditoria as Tabla_D_Auditoria,
    Usuario_Auditoria as Tabla_U_Auditoria
) 
from App.Utilities.Util import Actualizar_Persona, Validar_Contraseña, Crear_Hash, Validar_Pw
from App.Utilities.Tables import db
from datetime import datetime, date
import requests
import boto3
import pytz
import json
import os

timezone_tz = pytz.timezone(os.getenv("TIMEZONE"))

class Account_Service:
    @staticmethod
    def Delete_Device(User_ID, Device_ID):
        if not User_ID:
            return "Auth"
        
        Usuario_Validar = Tabla_Usuario.query.get(User_ID)
        if not Usuario_Validar:
            return "Auth"
        Permisos = Tabla_Permiso.query.filter(Tabla_Permiso.Rol_ID == Usuario_Validar.Rol_ID).all()
        Nombres = [P.to_dict()["Nombre"] for P in Permisos]
        if "dispositivo_eliminar" in Nombres:
            Dispositivo = Tabla_Dispositivos.query.get(Device_ID)
            if not Dispositivo:
                return False
            
            Disp_json = json.dumps(Dispositivo.to_dict(), default=str, ensure_ascii=False)
            Auditoria = Tabla_D_Auditoria(Accion="Dispositivo eliminado", Anterior=Disp_json, Modificado_Por=Usuario_Validar.ID, Dispositivos_ID=Dispositivo.ID)
            db.session.add(Auditoria)     

            Dispositivo.Estado_Dispositivo_ID = 3
            db.session.commit()
            Persona = Tabla_Persona.query.filter(Tabla_Persona.Usuario_ID == Usuario_Validar.ID).first()
            Persona_json = Persona.to_dict()
            Dispositivo_json = Dispositivo.to_dict()
            requests.post(os.getenv("EMAIL_SERVICE"),
                json={
                    "Template": "Eliminar_Dispositivo",
                    "Datos": {
                        "Nombre": Persona_json["Primer_Nombre"]+" "+Persona_json["Primer_Apellido"],
                        "Fecha": datetime.now(timezone_tz).replace(tzinfo=None).strftime("%d/%m/%Y %H:%M"),
                        "Dispositivo": Dispositivo_json["Dispositivo"],
                        "Navegador": Dispositivo_json["Sistema"],
                        "IP": Dispositivo_json["IP"]
                        },
                    "Correo": Usuario_Validar.to_dict()["Correo"],
                    "Asunto": "Eliminacion de dispositivo"
                }
            )
            return Dispositivo
        else:
            return "Auth"
    @staticmethod
    def Cambiar_Mfa(User_ID):
        if not User_ID:
            return "Auth"
        
        Usuario_Validar = Tabla_Usuario.query.get(User_ID)
        if not Usuario_Validar:
            return "Auth"

        if Usuario_Validar.Autenticador == 0:
            Usuario_Validar.Autenticador = 1
        elif Usuario_Validar.Autenticador == 1:
            Usuario_Validar.Autenticador = 0
        db.session.commit()
        return Usuario_Validar.Autenticador
    @staticmethod
    def Read_Data(User_ID):
        if not User_ID:
            return "Auth"
        
        Usuario = Tabla_Usuario.query.get(User_ID)
        if not Usuario:
            return "Auth"
        Permisos = Tabla_Permiso.query.filter(Tabla_Permiso.Rol_ID == Usuario.Rol_ID).all()
        Nombres = [P.to_dict()["Nombre"] for P in Permisos]
        if "cuenta_ver" in Nombres and "dispositivo_ver" in Nombres:
            Persona = Tabla_Persona.query.filter(Tabla_Persona.Usuario_ID == Usuario.ID).first()
            if not Persona:
                return "Auth"
            Dispositivos = Tabla_Dispositivos.query.filter(Tabla_Dispositivos.Usuario_ID == Usuario.ID, Tabla_Dispositivos.Estado_Dispositivo_ID != 3).order_by(Tabla_Dispositivos.Ultimo_Uso.desc()).all()
            Barrio = Tabla_Barrio.query.order_by(Tabla_Barrio.ID.asc()).all()
            Localidad = Tabla_Localidad.query.order_by(Tabla_Localidad.ID.asc()).all()
            Ciudad = Tabla_Ciudad.query.order_by(Tabla_Ciudad.ID.asc()).all()
            Departamento = Tabla_Departamento.query.order_by(Tabla_Departamento.ID.asc()).all()
            Tipos = Tabla_Documento.query.order_by(Tabla_Documento.ID.asc()).all()
            Datos = {
                "Barrios": [B.to_dict() for B in Barrio],
                "Localidades": [L.to_dict() for L in Localidad],
                "Ciudades": [C.to_dict() for C in Ciudad],
                "Departamentos": [D.to_dict() for D in Departamento],
                "Tipos": [T.to_dict() for T in Tipos]
            }
            return Persona, Dispositivos, Datos
        else:
            return "Auth"
    @staticmethod
    def Cambiar_Personal(User_ID, Data):
        if not User_ID:
            return "Auth"

        Usuario = Tabla_Usuario.query.get(User_ID)
        if not Usuario:
            return "Auth"
        Permisos = Tabla_Permiso.query.filter(Tabla_Permiso.Rol_ID == Usuario.Rol_ID).all()
        Nombres = [P.to_dict()["Nombre"] for P in Permisos]
        if "cuenta_modificar_propio" in Nombres:
            Persona = Tabla_Persona.query.filter(Tabla_Persona.Usuario_ID == Usuario.ID).first()
            if not Persona:
                return False
            if Data["Documento"] != Persona.Documento:
                Doc_Exi = Tabla_Persona.query.filter(Tabla_Persona.Documento == Data["Documento"]).first()
                if Doc_Exi:
                    return "Documento"
            
            Fecha = datetime.strptime(Data["Fecha_Nacimiento"], "%Y-%m-%d").date()
            Hoy = date.today()
            Edad = Hoy.year - Fecha.year - ((Hoy.month, Hoy.day) < (Fecha.month, Fecha.day))
            if Edad < 13 or Edad > 110:
                return "Edad"

            Actualizar_Persona(Persona, Data, Tabla_P_Auditoria, Usuario.ID)
            db.session.commit()
            requests.post(os.getenv("EMAIL_SERVICE"),
                json={
                    "Template": "Persona_Cambio",
                    "Datos": {
                        "Nombre": Persona.Primer_Nombre + " " + Persona.Primer_Apellido
                    },
                    "Correo": Usuario.Correo,
                    "Asunto": "Actualización de datos en tu cuenta"
                }
            ) 
            return Persona             
        else:
            return "Auth"
    @staticmethod
    def Cambiar_Ubicacion(User_ID, Data):
        if not User_ID:
            return "Auth"
        
        Usuario = Tabla_Usuario.query.get(User_ID)
        Permisos = Tabla_Permiso.query.filter(Tabla_Permiso.Rol_ID == Usuario.Rol_ID).all()
        Nombres = [P.to_dict()["Nombre"] for P in Permisos]
        if "cuenta_modificar_propio" in Nombres:
            Persona = Tabla_Persona.query.filter(Tabla_Persona.Usuario_ID == Usuario.ID).first()
            if not Persona:
                return None            
            Barrio_Ant = Tabla_Barrio.query.filter(Tabla_Barrio.ID == Persona.Barrio_ID).first()

            Departamento = Data["Departamento_Input"].capitalize().strip()
            Dep_Exi = Tabla_Departamento.query.filter(Tabla_Departamento.Nombre == Departamento, Tabla_Departamento.Pais_ID == 1).first()
            if not Dep_Exi:
                Dep_Exi = Tabla_Departamento(Nombre=Departamento, Pais_ID=1)
                db.session.add(Dep_Exi)
                db.session.flush()
            
            Ciudad = Data["Ciudad_Input"].capitalize().strip()
            Ciu_Exi = Tabla_Ciudad.query.filter(Tabla_Ciudad.Nombre == Ciudad, Tabla_Ciudad.Departamento_ID == Dep_Exi.ID).first()
            if not Ciu_Exi:
                Ciu_Exi = Tabla_Ciudad(Nombre=Ciudad, Departamento_ID=Dep_Exi.ID)
                db.session.add(Ciu_Exi)
                db.session.flush()

            Localidad = Data["Localidad_Input"].capitalize().strip()
            Loc_Exi = Tabla_Localidad.query.filter(Tabla_Localidad.Nombre == Localidad, Tabla_Localidad.Ciudad_ID == Ciu_Exi.ID).first()
            if not Loc_Exi:
                Loc_Exi = Tabla_Localidad(Nombre=Localidad, Ciudad_ID=Ciu_Exi.ID)
                db.session.add(Loc_Exi)
                db.session.flush()

            Barrio = Data["Barrio_Input"].capitalize().strip()
            Bar_Exi = Tabla_Barrio.query.filter(Tabla_Barrio.Nombre == Barrio, Tabla_Barrio.Localidad_ID == Loc_Exi.ID).first()
            if not Bar_Exi:
                Bar_Exi = Tabla_Barrio(Nombre=Barrio, Localidad_ID=Loc_Exi.ID)
                db.session.add(Bar_Exi)
                db.session.flush()
            
            Persona.Barrio_ID = Bar_Exi.ID

            Anterior = json.dumps(Barrio_Ant.to_dict(), default=str, ensure_ascii=False)
            Auditoria = Tabla_P_Auditoria(Accion="Ubicacion modificada", Anterior=Anterior, Modificado_Por=Usuario.ID, Persona_ID=Usuario.ID)
            db.session.add(Auditoria) 

            db.session.commit()

            return Persona
        else:
            return "Auth"
    @staticmethod
    def Cambiar_Contraseña(User_ID, Device_ID, Data):
        if not User_ID:
            return "Auth"
        
        Usuario = Tabla_Usuario.query.get(User_ID)
        if not Usuario:
            return "Auth"
        Permisos = Tabla_Permiso.query.filter(Tabla_Permiso.Rol_ID == Usuario.Rol_ID).all()
        Nombres = [P.to_dict()["Nombre"] for P in Permisos]
        if "cuenta_modificar_propio" in Nombres:
            if not Validar_Pw(Data["Contraseña_Actual"], Usuario.Contraseña):
                return "La contraseña actual es incorrecta"
            Persona = Tabla_Persona.query.filter(Tabla_Persona.Usuario_ID == Usuario.ID).first()
            if not Persona:
                return False
            Contraseña_Nueva = Data["Contraseña_Nueva"].strip()

            if Data["Contraseña_Nueva2"] != Contraseña_Nueva:
                return "Las contraseñas no coinciden"
            Error = Validar_Contraseña(Contraseña_Nueva, Persona.Documento)
            if Error:
                return Error   
            if Contraseña_Nueva == Data["Contraseña_Actual"]:
                return "No se permite reutilizar contraseñas anteriores"

            Hash = Crear_Hash(Contraseña_Nueva)
            Usuario.Contraseña = Hash
            Dispositivos = Tabla_Dispositivos.query.filter(Tabla_Dispositivos.Usuario_ID == Usuario.ID, Tabla_Dispositivos.Token != Device_ID).all()
            for D in Dispositivos:
                D_json = json.dumps(D.to_dict(), default=str, ensure_ascii=False)
                Auditoria = Tabla_D_Auditoria(Accion="Dispositivo eliminado", Anterior=D_json, Modificado_Por=Usuario.ID, Dispositivos_ID=D.ID)
                db.session.add(Auditoria)
                D.Estado_Dispositivo_ID = 3
            Auditoria = Tabla_U_Auditoria(Accion="Cambio de contraseña",Anterior="None",Modificado_Por=Usuario.ID,Usuario_ID=Usuario.ID)
            db.session.add(Auditoria)
            db.session.commit()           

            requests.post(os.getenv("EMAIL_SERVICE"),
                json={
                    "Template": "Cambio_Contraseña",
                    "Datos": {
                        "Nombre": Persona.Primer_Nombre + " " + Persona.Primer_Apellido
                    },
                    "Correo": Usuario.Correo,
                    "Asunto": "Cambio de Contraseña"
                }
            )
            return "Correcto"
        else:
            return "Auth"
    @staticmethod
    def Cambiar_Imagen(User_ID, Archivo):
        if not User_ID:
            return "Auth"
        
        Usuario = Tabla_Usuario.query.get(User_ID)
        if not Usuario:
            return False
        Permisos = Tabla_Permiso.query.filter(Tabla_Permiso.Rol_ID == Usuario.Rol_ID).all()
        Nombres = [P.to_dict()["Nombre"] for P in Permisos]
        if "cuenta_modificar_propio" in Nombres:
            if not Archivo:
                return False
            if os.path.splitext(Archivo.filename)[1] not in [".png", ".jpg", ".jpeg"]:
                return "el archivo no tiene el formato requerido"
            if len(Archivo.read()) / 1024 > 5120:
                return "El archivo supera el tamaño maximo"
            Archivo.seek(0)

            Nombre_Nuevo = Usuario.Nombre + os.path.splitext(Archivo.filename)[1]
            Usuario.Nombre_Imagen = Nombre_Nuevo
            db.session.commit()
            S3 = boto3.client(
                "s3", 
                aws_access_key_id=os.getenv("AWS_ACCESS_KEY"), 
                aws_secret_access_key=os.getenv("AWS_SECRET_KEY"), 
                region_name=os.getenv("AWS_REGION")
            )

            S3.upload_fileobj(Archivo, os.getenv("AWS_BUCKET"), Nombre_Nuevo, ExtraArgs={"ContentType": Archivo.mimetype})
            return Nombre_Nuevo
        else:
            return "Auth"
    @staticmethod
    def Eliminar_Imagen(User_ID):
        if not User_ID:
            return "Auth"
        
        Usuario = Tabla_Usuario.query.get(User_ID)
        if not Usuario:
            return False
        Permisos = Tabla_Permiso.query.filter(Tabla_Permiso.Rol_ID == Usuario.Rol_ID).all()
        Nombres = [P.to_dict()["Nombre"] for P in Permisos]
        if "cuenta_modificar_propio" in Nombres:
            S3 = boto3.client(
                "s3", 
                aws_access_key_id=os.getenv("AWS_ACCESS_KEY"), 
                aws_secret_access_key=os.getenv("AWS_SECRET_KEY"), 
                region_name=os.getenv("AWS_REGION")
            )            
            if Usuario.Nombre_Imagen:
                S3.delete_object(Bucket=os.getenv("AWS_BUCKET"), Key=Usuario.Nombre_Imagen)
                Usuario.Nombre_Imagen = None
                db.session.commit()
            return "Correcto"
        else:
            return "Auth" 
    @staticmethod
    def Delete_All_Device(User_ID):
        if not User_ID:
            return "Auth"
        
        Usuario_Validar = Tabla_Usuario.query.get(User_ID)
        if not Usuario_Validar:
            return "Auth"
        Permisos = Tabla_Permiso.query.filter(Tabla_Permiso.Rol_ID == Usuario_Validar.Rol_ID).all()
        Nombres = [P.to_dict()["Nombre"] for P in Permisos]
        if "dispositivo_eliminar" in Nombres:
            Dispositivos = Tabla_Dispositivos.query.filter(Tabla_Dispositivos.Usuario_ID == Usuario_Validar.ID).all()
            for D in Dispositivos:
                D_json = json.dumps(D.to_dict(), default=str, ensure_ascii=False)
                Auditoria = Tabla_D_Auditoria(Accion="Dispositivo eliminado", Anterior=D_json, Modificado_Por=Usuario_Validar.ID, Dispositivos_ID=D.ID)
                db.session.add(Auditoria)
                D.Estado_Dispositivo_ID = 3
            db.session.commit()
            return "Correcto"
        else:
            return "Auth"
    @staticmethod
    def Delete_Account(User_ID):    
        if not User_ID:
            return "Auth"
        
        Usuario = Tabla_Usuario.query.get(User_ID)
        if not Usuario:
            return False
        Permisos = Tabla_Permiso.query.filter(Tabla_Permiso.Rol_ID == Usuario.Rol_ID).all()
        Nombres = [P.to_dict()["Nombre"] for P in Permisos]
        if "cuenta_modificar_propio" in Nombres:
            Usuario_json = json.dumps(Usuario.to_dict(), default=str, ensure_ascii=False)
            Dispositivos = Tabla_Dispositivos.query.filter(Tabla_Dispositivos.Usuario_ID == Usuario.ID).all()
            for D in Dispositivos:
                D.Estado_Dispositivo_ID = 3
            Usuario.Estado_Usuario_ID = 5
            Auditoria = Tabla_U_Auditoria(Accion="Eliminacion de cuenta",Anterior=Usuario_json,Modificado_Por=Usuario.ID,Usuario_ID=Usuario.ID)
            db.session.add(Auditoria)
            db.session.commit()
            return "Correcto"
        else:
            return "Auth"                            