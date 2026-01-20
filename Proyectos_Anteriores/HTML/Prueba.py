import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate, make_msgid

remitente = "bot@gaialink.online"
destinatario = "kevinanzgarz26@gmail.com"
contraseña = "1145224601Aa*"

def Prueba():
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = "Prueba de correo desde Python"
    mensaje['Date'] = formatdate(localtime=True)
    mensaje['Message-ID'] = make_msgid(domain="gaialink.online")

    cuerpo = "Hola, este es un correo de prueba."
    mensaje.attach(MIMEText(cuerpo, "plain"))

    try:
        servidor = smtplib.SMTP_SSL("gaialink.online", 465)
        servidor.login(remitente, contraseña)
        servidor.send_message(mensaje)
        servidor.quit()
        print("✅ Correo enviado correctamente")
    except Exception as e:
        print("❌ Error al enviar:", e)

Prueba()
