from App.Utilities.Mailer import Enviar_Correo

class Email_Service:
    @staticmethod
    def Envio(Template, Data, Correo, Asunto):
        try:
            Enviar_Correo(Template, Data, Correo, Asunto)
            return {"Message": "Correo enviado"}
        except Exception as e:
            return {"Error": str(e)}