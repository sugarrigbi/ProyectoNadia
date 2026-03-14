from App.Utilities.Mailer import Enviar_Email

class Email_Service:

    @staticmethod
    def Send(Correo, Asunto, Mensaje):

        try:

            Enviar_Email(Correo, Asunto, Mensaje)

            return {"Message": "Correo enviado"}

        except Exception as e:

            return {"Error": str(e)}