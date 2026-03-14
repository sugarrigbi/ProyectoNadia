import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL = "bot.gaialink@gmail.com"
PASSWORD = "sizv jqee ojco ixqc"


def Enviar_Email(destino, asunto, mensaje):

    msg = MIMEMultipart()

    msg["From"] = EMAIL
    msg["To"] = destino
    msg["Subject"] = asunto

    msg.attach(MIMEText(mensaje, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(EMAIL, PASSWORD)

    server.sendmail(EMAIL, destino, msg.as_string())

    server.quit()