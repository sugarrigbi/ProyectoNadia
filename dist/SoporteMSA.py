import win32com.client
import time
import os
from datetime import datetime
import tkinter as tk
from tkinter import scrolledtext
from tkinter import simpledialog

#===== GUI=====
root = tk.Tk()
root.title("Monitor de Correos")
root.geometry("700x500")
root.configure(bg="#f0f4f7")

text_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', font=("Consolas", 10))
text_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

def log(msg):
    text_log.configure(state='normal')
    text_log.insert(tk.END, msg + "\n")
    text_log.see(tk.END)
    text_log.configure(state='disabled')

def print(*args, **kwargs):
    msg = " ".join(str(a) for a in args)
    log(msg)

def iniciar():
    global running
    running = True
    btn_iniciar.config(state='disabled')
    Enviar_Correos()

def cerrar():
    global running
    running = False
    root.destroy()

Outlook = win32com.client.Dispatch("Outlook.Application")
namespace = Outlook.GetNamespace("MAPI")

buzon = namespace.Folders["soportemsa@mectronics.co"]
inbox = buzon.Folders["Bandeja de entrada"]
soporte = inbox.Folders["11-Soporte"]
mensajes = soporte.Items
inicio = datetime.now()

running = False
CORREO_ENVIO = "practicante.tecnologia@mectronics.co"
FIRMA_HTML = "Kevin (practicante.tecnologia@mectronics.co).htm"

print("⏳ Script iniciado. Esperando correos nuevos...")

def obtener_cuenta(correo):
    for cuenta in Outlook.Session.Accounts:
        if cuenta.SmtpAddress.lower() == correo.lower():
            return cuenta
    return None

def cargar_firma(nombre_firma):
    ruta = os.path.join(os.environ["APPDATA"], "Microsoft", "Signatures", nombre_firma)
    with open(ruta, "r", encoding="latin-1") as f:
        return f.read()

cuenta_envio = obtener_cuenta(CORREO_ENVIO)
firma_html = cargar_firma(FIRMA_HTML)

def Enviar_Correos():
    if not running:
        return    
    mensajes = soporte.Items
    mensajes.Sort("[ReceivedTime]", True)
    for mensaje in mensajes:
        try:
            if mensaje.Class != 43:
                continue            
            recibido = mensaje.ReceivedTime.replace(tzinfo=None)
            if (recibido > inicio and mensaje.Categories and "Tecnología" in mensaje.Categories and mensaje.FlagStatus == 0):
                print("📩 Nuevo correo:", mensaje.Subject)
                print("De:", mensaje.SenderName)
                print("Asunto:", mensaje.Subject)
                ticket = simpledialog.askstring("Número de ticket", f"Asignar ticket para:\n{mensaje.Subject}")
                if not ticket:
                    ticket = "SIN_TICKET"
                mail = Outlook.CreateItem(0)
                mail.SendUsingAccount = cuenta_envio
                mail.To = mensaje.SenderEmailAddress
                mail.Subject = "RE: " + mensaje.Subject
                mail.HTMLBody = f"""
                <p>Buen día<br>
                Cordial saludo</p>
                <p>La novedad se está gestionando bajo el número de ticket
                <b>NO. {ticket}</b></p>
                <p>Si tiene alguna inquietud no dude en comunicarla.</p>
                <br>
                """+ mail.HTMLBody
                mail.Send()
                mensaje.FlagStatus = 1
                mensaje.Save()
                print("✅ Respondido desde practicante.tecnologia")
        except Exception as e:
            print("❌ Error:", e)
    print("Esperando Correo nuevo...")
    root.after(5000, Enviar_Correos)

btn_iniciar = tk.Button(root, text="Iniciar código", font=("Arial", 14, "bold"), bg="#4caf50", fg="white", command=iniciar)
btn_cerrar = tk.Button(root, text="Cerrar", font=("Arial", 14, "bold"),bg="#f44336", fg="white",command=cerrar)
btn_cerrar.pack(pady=10)
btn_iniciar.pack(pady=10)

root.mainloop()