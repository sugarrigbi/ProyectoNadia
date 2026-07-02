from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
import re

def Cargar_Template(Ruta, **Variables):

    Ruta_Real = os.path.join(os.path.dirname(__file__), "Templates", f"{Ruta}.html")

    with open(Ruta_Real, "r", encoding="utf-8") as File:
        Html = File.read()
    Html = re.sub(r"\[\[(\w+)\]\]", r"{\1}", Html)
    return Html.format(**Variables)
def Enviar_Correo(Template, Data, Correo, Asunto):
    Msg = MIMEMultipart("alternative")

    Msg["From"] = os.getenv("BOT_EMAIL")
    Msg["To"] = Correo
    Msg["Subject"] = Asunto

    Html = Cargar_Template(Template, **Data)
    Msg.attach(MIMEText(Html, "html"))

    Server = smtplib.SMTP("smtp.gmail.com", 587)
    Server.starttls()
    
    Server.login(os.getenv("BOT_EMAIL"), os.getenv("BOT_PASSWORD"))

    Server.sendmail(os.getenv("BOT_EMAIL"), Correo, Msg.as_string())
    Server.quit()
