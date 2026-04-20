from App.Models.Account_Model import Dispositivos as Tabla_Dispositivos, Dispositivos_Auditoria as Tabla_Auditoria, Usuario as Tabla_Usuario, RolAPermiso as Tabla_Permiso, Persona as Tabla_Persona
from App.Utilities.Tables import db
import requests
from datetime import datetime
import pytz

bogota_tz = pytz.timezone("America/Bogota")

class Account_Service:
    @staticmethod
    def Read_Devices(User_ID):
        if not User_ID:
            return "Auth"
        
        Usuario_Validar = Tabla_Usuario.query.get(User_ID)
        Permisos = Tabla_Permiso.query.filter(Tabla_Permiso.Rol_ID == Usuario_Validar.Rol_ID).all()
        Nombres = [P.to_dict()["Nombre"] for P in Permisos]
        if "dispositivo_ver" in Nombres:
            Dispositivos = Tabla_Dispositivos.query.filter(Tabla_Dispositivos.Usuario_ID == Usuario_Validar.ID, Tabla_Dispositivos.Estado_Dispositivo_ID != 3).order_by(Tabla_Dispositivos.Ultimo_Uso.desc()).all()
            return Dispositivos
        else:
            return "Auth"
    @staticmethod
    def Delete_Device(User_ID, Device_ID):
        if not User_ID:
            return "Auth"
        
        Usuario_Validar = Tabla_Usuario.query.get(User_ID)
        Permisos = Tabla_Permiso.query.filter(Tabla_Permiso.Rol_ID == Usuario_Validar.Rol_ID).all()
        Nombres = [P.to_dict()["Nombre"] for P in Permisos]
        if "dispositivo_eliminar" in Nombres:
            Dispositivo = Tabla_Dispositivos.query.get(Device_ID)
            if not Dispositivo:
                return False
            Dispositivo.Estado_Dispositivo_ID = 3
            db.session.commit()
            Persona = Tabla_Persona.query.filter(Tabla_Persona.Usuario_ID == Usuario_Validar.ID).first()
            Persona_json = Persona.to_dict()
            Dispositivo_json = Dispositivo.to_dict()
            requests.post("http://127.0.0.1:5007/email",
                json={
                    "Template": "Eliminar_Dispositivo",
                    "Datos": {
                        "Nombre": Persona_json["Primer_Nombre"]+" "+Persona_json["Primer_Apellido"],
                        "Fecha": datetime.now(bogota_tz).replace(tzinfo=None).strftime("%d/%m/%Y %H:%M"),
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
    def Obtener_Mfa(User_ID):
        if not User_ID:
            return "Auth"
        
        Usuario_Validar = Tabla_Usuario.query.get(User_ID)
        if not Usuario_Validar:
            return "Auth"
        return Usuario_Validar.Autenticador