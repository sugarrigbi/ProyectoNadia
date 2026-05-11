from App.Models.Notification_Model import Correo_Auditoria as Tabla_Auditoria
from App.Utilities.Mailer import Enviar_Correo
from App.Utilities.Tables import db


class Email_Service:
    @staticmethod
    def Envio(Template, Data, Correo, Asunto):
        try:
            Enviar_Correo(Template, Data, Correo, Asunto)

            Auditoria = Tabla_Auditoria(Accion="Correo enviado", Template=Template, Correo=Correo)
            db.session.add(Auditoria)
            db.session.commit()

            return {"Message": "Correo enviado"}
        except Exception as e:
            return {"Error": str(e)}
        