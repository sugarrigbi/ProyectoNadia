#LIBRERIAS
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from time import strftime
from colorama import Fore, Style, init
display_time = strftime ('%H:%M:%S %p')

app = Flask(__name__)
@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get('Body', '').strip().lower()
    from_number = request.values.get('From', '')
    print(f"{Fore.MAGENTA}==================================={Fore.WHITE}")
    print(f"{Fore.GREEN}Hora: {Fore.CYAN}{display_time}{Fore.WHITE}")
    print(f"{Fore.GREEN}Desde: {Fore.CYAN}{from_number}{Fore.WHITE}")
    print(f"{Fore.GREEN}Mensaje: {Fore.CYAN}{incoming_msg}{Fore.WHITE}")
    print(f"{Fore.MAGENTA}==================================={Fore.WHITE}")    
    resp = MessagingResponse()
    msg = resp.message()
    if incoming_msg == "hola":
        msg.body("Bienvenido, soy RightwayBot Estas son las opciones de Right way sys para ti:\n1- Cómo funciona el aplicativo?\n2- Para qué sirve?\n3- Como puedo registrarme?\n4- Olvidé mi contraseña\n5- Cambiar contraseña\n6- Quiénes somos? \n7- Mesa de ayuda \n8- Contactos \n9- adios \n")
    elif incoming_msg == "adiós":
        msg.body("Adios, Te esperamos pronto, y recuerda siempre estare cuando me nesesites!")
    elif incoming_msg == "gracias":
        msg.body("De nada, siempre estoy cuando me Nesesitas")
    elif incoming_msg == "1":
        msg.body("Para usar el aplicativo libremente debes registrarte primero como usuario en la opción crear usuario, a partir de ahí podrás ingresar y crear casos con información del desastre natural ocurrido.")
    elif incoming_msg == "Cómo funciona el aplicativo?":
        msg.body("Para usar el aplicativo libremente debes registrarte primero como usuario en la opción crear usuario, a partir de ahí podrás ingresar y crear casos con información del desastre natural ocurrido.")
    elif incoming_msg == "2":
        msg.body("El aplicativo tiene como objetivo notificar casos de desastres naturales (incendios, inundaciones, terremotos o temblores) a las autoridades competentes en la región de Cundinamarca, agilizando la respuesta y mitigación de emergencias.")
    elif incoming_msg == "Para qué sirve?":
        msg.body("El aplicativo tiene como objetivo notificar casos de desastres naturales (incendios, inundaciones, terremotos o temblores) a las autoridades competentes en la región de Cundinamarca, agilizando la respuesta y mitigación de emergencias.")        
    elif incoming_msg == "3":
        msg.body("Ingresa al aplicativo, en la página de inicio da click en el botón de crear usuario, llena las casillas con la información personal solicitada y asigna un nombre de usuario y contraseña. Luego da click en crear usuario e ingresa con el usuario y contraseña creados")
    elif incoming_msg == "Como puedo registrarme?":
        msg.body("Ingresa al aplicativo, en la página de inicio da click en el botón de crear usuario, llena las casillas con la información personal solicitada y asigna un nombre de usuario y contraseña. Luego da click en crear usuario e ingresa con el usuario y contraseña creados")        
    elif incoming_msg == "4":
        msg.body("Para recuperar tu contraseña sigue las instrucciones:\n1. Ingresa al correo que ingresaste al registrar tu usuario por primera vez.\n2.Busca en tu bandeja de entrada un correo a nombre de right way sys , si no se encuentra allí revisa en el apartado de Spam.\n3.Una vez encuentres el correo busca en él tu información de registro de usuario, allí se encuentra el nombre de usuario y la contraseña guardada.\n4.Abre el aplicativo e inicia sesión con el usuario y contraseña dadas en el correo.\n5.Una vez ingreses asegúrate de cambiar la contraseña por una segura y fácil de recordar en el apartado configuración de cuenta.")
    elif incoming_msg == "Olvidé mi contraseña":
        msg.body("Para recuperar tu contraseña sigue las instrucciones:\n1. Ingresa al correo que ingresaste al registrar tu usuario por primera vez.\n2.Busca en tu bandeja de entrada un correo a nombre de right way sys, si no se encuentra allí revisa en el apartado de Spam.\n3.Una vez encuentres el correo busca en él tu información de registro de usuario, allí se encuentra el nombre de usuario y la contraseña guardada.\n4.Abre el aplicativo e inicia sesión con el usuario y contraseña dadas en el correo.\n5.Una vez ingreses asegúrate de cambiar la contraseña por una segura y fácil de recordar en el apartado configuración de cuenta.")
    elif incoming_msg == "Cambiar contraseña":
        msg.body("Ingresa con tu usuario y contraseña establecidos, ve a configuración de cuenta y da click en modificar contraseña, ingresa la contraseña actual y la nueva.")
    elif incoming_msg == "5":
        msg.body("Ingresa con tu usuario y contraseña establecidos, ve a configuración de cuenta y da click en modificar contraseña, ingresa la contraseña actual y la nueva.")
    elif incoming_msg == "Quiénes somos?":
        msg.body("En Right Way Sys somos un equipo dedicado al desarrollo de soluciones tecnológicas para la gestión de emergencias, enfocados en proteger a las comunidades de Cundinamarca mediante herramientas eficientes y accesibles.")
    elif incoming_msg == "6":
        msg.body("En Right Way Sys somos un equipo dedicado al desarrollo de soluciones tecnológicas para la gestión de emergencias, enfocados en proteger a las comunidades de Cundinamarca mediante herramientas eficientes y accesibles.")
    elif incoming_msg == "7":
        msg.body("Da click en el siguiente enlace: https://app.onedesk.com/app-od/es/o-yourorganization1747230203684/web-page-0?customerAccess")
    elif incoming_msg == "Mesa de ayuda":
        msg.body("Da click en el siguiente enlace: https://app.onedesk.com/app-od/es/o-yourorganization1747230203684/web-page-0?customerAccess")
    elif incoming_msg == "8":
        msg.body("Si deseas contactarnos directamente puedes hacerlo por los siguientes medios: Correo: rightwaysys.contacto@gmail.com.  Telefono: 322 7824460 - 310 3069581")
    elif incoming_msg == "Contactos":
        msg.body("Si deseas contactarnos directamente puedes hacerlo por los siguientes medios: Correo: rightwaysys.contacto@gmail.com.  Telefono: 322 7824460 - 310 3069581")
    elif incoming_msg == "9":
        msg.body("Adios, Te esperamos pronto, y recuerda siempre estare cuando me nesesites!")
    else:
        msg.body("Disculpa, no logro entender tu solicitud, Escribe ¨hola¨ para darte la lista de opciones")
    return str(resp)
if __name__ == "__main__":
    app.run(port=5000, debug=True)