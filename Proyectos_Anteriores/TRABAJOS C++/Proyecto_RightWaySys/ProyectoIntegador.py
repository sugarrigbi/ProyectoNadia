#================================LIBRERIAS=========================================================================================================================
import tkinter as tk                      
from tkinter import ttk, messagebox              
import re
from PIL import Image, ImageTk
from customtkinter import *
from tkcalendar import DateEntry
import mysql.connector
from datetime import date, datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import uuid
import webbrowser
#================================ADMIN CREDENCIALES================================================================================================================
correo_emisor = "rightwaysys.contacto@gmail.com"
contraseña = "jfsm pdmy hmuj ollo"
correo_receptor1 = "rightwaysys.directivas@gmail.com"
fuente = "Bahnschrift SemiBold"
Contador = 0
Max_Intentos = 3
Intentos_Restantes = 3
token_recuperacion = None
correo_token = None
hora_token = None
Tipo_Documento_Valores2 = {
    "Cedula Ciudadania": "CC",
    "Cedula Extranjeria": "CE",
    "Pasaporte": "PA",
    "Registro Civil": "RC",
    "Tarjeta de identidad": "TI"
}
Tipo_Documento_Valores = {
    "CC": "Cedula Ciudadania",
    "CE": "Cedula Extranjeria",
    "PA": "Pasaporte",
    "RC": "Registro Civil",
    "TI": "Tarjeta de identidad"
}
Estados_Valores = {
    "Pendiente": "Caso_00",
    "Activo": "Caso_01",
    "Finalizado": "Caso_02",
    "Eliminado": "Caso_03",
    "Usuario Inactivo": "Usuario_00",
    "Usuario Activo": "usuario_01"
}
Estados_Valores2 = {
    "Caso_00": "Pendiente",
    "Caso_01": "Activo",
    "Caso_02": "Finalizado",
    "Caso_03": "Eliminado",
    "Usuario_00": "Usuario Inactivo",
    "usuario_01": "Usuario Activo"
}
Rol_Valores = {
    "Usuario": "Usu",
    "Administrador": "Admin"
}
Rol_Valores2 = {
    "Usu": "Usuario",
    "Admin": "Administrador"
}
Desastres_Valores = {
    "Incendio": "Incen",
    "Inundaciòn": "Inund",
    "Sismo-temblor": "Sismo",
    "Terremoto": "Terre"
}
Desastres_Valores2 = {
    "Incen": "Incendio",
    "Inund": "Inundaciòn",
    "Sismo": "Sismo-temblor",
    "Terre": "Terremoto"
}
Departamento_Valores = {
    "Cundinamarca": "001DEP"
}
Departamento_Valores2 = {
    "001DEP": "Cundinamarca"
}
#================================VENTANA=============================================================================================================
root = CTk()
root.title("Right Way Sys")
root.configure(fg_color="#2d3e50")
root.resizable(height = True, width = True)
set_appearance_mode("dark")
App_Ancho = 600
App_Alto = 600
Ventana_Ancho = root.winfo_screenwidth()
Ventana_Alto = root.winfo_screenheight()
Cordenada_X = (Ventana_Ancho // 2) - (App_Ancho // 2)
Cordenada_Y = (Ventana_Alto // 2) - (App_Alto // 2)
root.geometry(f"{App_Ancho}x{App_Alto}+{Cordenada_X}+{Cordenada_Y}")
#============IMAGENES============
lblimagen = Image.open("Logo Right Way System.png")
lblimagen = lblimagen.resize((140, 130))
imagenL = ImageTk.PhotoImage(lblimagen)
Imagen_Boton_Salir = Image.open("x.png")
Imagen_Boton_Volver = Image.open("Volver.png")
Imagen_Boton_Emergencia = Image.open("Emergencia.png")
Imagen_Boton_Login = Image.open("Login.png")
Imagen_Boton_Crear_Usuario = Image.open("Crear Usuario.png")
Imagen_Boton_Modificar_Contraseña = Image.open("Modificar Contraseña.png")
Imagen_Boton_Modificar_Usuario = Image.open("Modificar Usuario.png")
Imagen_Boton_Usuario_Casos = Image.open("Casos.png")
Imagen_Boton_Usuario_Cuenta = Image.open("Configuracion.png")
Imagen_Boton_Usuario_Cuenta_Modificar_Datos = Image.open("Contacto.png")
Imagen_Boton_Usuario_Datos_Documento = Image.open("Documento.png")
Imagen_Boton_Usuario_Datos_Correo = Image.open("Correo.png")
Imagen_Boton_Usuario_Datos_Telefono = Image.open("Contacto.png")
Imagen_Boton_Usuario_Datos_Direccion = Image.open("Direccion.png")
Imagen_Boton_Usuario_Buscar_Caso = Image.open("Buscar.png")
Imagen_Boton_Usuario_Crear_Caso = Image.open("Hoja.png")
Imagen_Boton_Admin_Entidad = Image.open("Entidad.png")
Imagen_Boton_Usuario_Datos = Image.open("Pagina.png")
Imagen_Boton_Whatsapp = Image.open("Robot.png")
#============DEFINICIONES====================
def Conexion_Base_De_Datos():
     global cursor, conexion
     try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Root",
            database="proyecto",
            port="3306"
        )
        cursor = conexion.cursor()
     except mysql.connector.Error as err:
          messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos:\n{err}")
          print(f"error: ",{err})
          exit()
def Cerrar_Base_De_Datos():
        conexion.rollback()
        cursor.close()
        conexion.close()
def cancelar_evento(event):
    return "break"
class Persona:
    def __init__(self, Usuario, Contraseña, Primer_Nombre, Segundo_Nombre, Primer_Apellido, Segundo_Apellido,
                 Documento, Tipo_Documento,Valor_Tipo_Documento, Fecha_Nacimiento, Edad, Direccion, Numero, Email, Ciudad, Departamento, Barrio, Localidad):
        self.Usuario = Usuario
        self.Contraseña = Contraseña
        self.Primer_Nombre = Primer_Nombre
        self.Segundo_Nombre = Segundo_Nombre
        self.Primer_Apellido = Primer_Apellido
        self.Segundo_Apellido = Segundo_Apellido
        self.Documento = Documento
        self.Tipo_Documento = Tipo_Documento
        self.Valor_Tipo_Documento = Valor_Tipo_Documento
        self.Fecha_Nacimiento = Fecha_Nacimiento
        self.Edad = Edad
        self.Direccion = Direccion
        self.Numero = Numero
        self.Email = Email
        self.Ciudad = Ciudad
        self.Departamento = Departamento
        self.Barrio = Barrio
        self.Localidad = Localidad
class Caso:
    def __init__(self, TipoDesastre, Fecha, Descripcion, Direccion, Afectados):
        self.TipoDesastre = TipoDesastre
        self.Fecha = Fecha
        self.Descripcion = Descripcion
        self.Direccion = Direccion
        self.Afectados = Afectados
def Funcion_Login():
     global Contador, Max_Intentos, Intentos_Restantes, Usuario
     Conexion_Base_De_Datos()
     Usuario = Entrada_Usuario.get()
     Contraseña = Entrada_Contraseña.get()
     if not all([Usuario, Contraseña]):
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        Cerrar_Base_De_Datos()
        return
     cursor.execute("SELECT * FROM tbl_usuario WHERE Nombre = %s", (Usuario,))
     resultado = cursor.fetchone()
     if not resultado:
          messagebox.showerror("Usuario no encontrado", "El nombre de usuario no existe.")
          return

     cursor.execute("SELECT * FROM tbl_usuario WHERE Nombre = %s", (Usuario,))
     resultado_Identificacion = cursor.fetchone()
     if not resultado_Identificacion:
        messagebox.showerror("Usuario no encontrado", "El nombre de usuario no existe.")
        Cerrar_Base_De_Datos()
        return
     Id_Usuario = resultado_Identificacion[0]

     cursor.execute("SELECT fk_estado FROM tbl_usuario WHERE Id_usuario = %s", (Id_Usuario,))
     resultado_estado = cursor.fetchone()
     if not resultado_estado:
        messagebox.showerror("Error", "No se encontró el Usuario.")
        Cerrar_Base_De_Datos()
        return
     Estado_Actual = resultado_estado[0]
     if Estado_Actual == "Usuario_00":
        messagebox.showerror("Usuario no encontrado", "El usuario no existe.")
        return
     else:
        cursor.execute("SELECT * FROM tbl_usuario WHERE Nombre = %s AND Contraseña = %s", (Usuario, Contraseña))
        resultado_login = cursor.fetchone()
        if resultado_login:
            cursor.execute("SELECT tbl_usuario.fk_rol From tbl_usuario WHERE tbl_usuario.Nombre = %s", (Usuario,))
            rol_resultado = cursor.fetchone()
            if rol_resultado:
                rol = rol_resultado[0]
                if rol == "Usu":
                    messagebox.showinfo("Acceso concedido", f"Bienvenido, {Usuario}.")
                    Cerrar_Base_De_Datos()
                    Contador = 0
                    Grafico_Usuario_Inicio()
                    return
                elif rol == "Admin":
                    messagebox.showinfo("Administrador", f"Bienvenido, {Usuario}.")
                    Cerrar_Base_De_Datos()
                    Contador = 0
                    Grafico_Admin_Inicio()
                    return
                else:
                    messagebox.showinfo("Error", "No se encontro el rol del usuario")
                    return
        else:
            messagebox.showerror("Contraseña incorrecta", "La contraseña no es correcta.")
            Contador += 1
            Intentos_Restantes = Max_Intentos - Contador
            Texto4.configure(text=f"Intentos restantes: {Intentos_Restantes}", font=(fuente, 35))
     Intentos_Restantes = Max_Intentos - Contador
     if Intentos_Restantes > 0:
        messagebox.showinfo("Intentos restantes", f"Te quedan {Intentos_Restantes} intento(s).")
     else:
        messagebox.showerror("Acceso denegado", "Has superado el número máximo de intentos.")
        Cerrar_Base_De_Datos()
        root.quit()
def Conseguir_Correo():
    global correo_receptor2
    cursor.execute("SELECT * FROM tbl_usuario WHERE Nombre = %s", (Usuario,))
    resultado = cursor.fetchone()
    if not resultado:
        messagebox.showerror("Usuario no encontrado", "El nombre de usuario no existe.")
        return
    id_usuario = resultado[0]

    cursor.execute("SELECT tbl_adic_persona.Email FROM tbl_adic_persona JOIN tbl_persona ON tbl_adic_persona.fk_persona = tbl_persona.Id_persona JOIN tbl_tipo_documento ON tbl_persona.fk_Tipo_documento = tbl_tipo_documento.Id_Documento JOIN tbl_usuario ON tbl_persona.fk_usuario = tbl_usuario.Id_usuario WHERE tbl_usuario.Id_usuario = %s", (id_usuario,))
    correo = cursor.fetchone()
    if not correo:
        messagebox.showerror("Correo no encontrado", "El correo no existe.")
        return
    correo_receptor2 = correo[0]
    print("Correo del usuario:", correo_receptor2)
def Funcion_Validar_Contraseña(Contraseña):
    if len(Contraseña) < 8:
        return "La contraseña debe tener mas de 8 caracteres"
    if not any(c.isupper() for c in Contraseña):
        return "La contraseña debe tener una mayuscula"
    if not any(c.isdigit() for c in Contraseña):
        return "la contraseña debe tener un numero"
    if not re.search(r'[/!@#$%^&*(),.?":{}|<>]', Contraseña):
        return "La contraseña debe tener un caracter especial"
    return None
def Funcion_Crear_Usuario():
     Conexion_Base_De_Datos()
     Usuario = Entrada_Usuario.get()
     Contraseña = Entrada_Contraseña.get()
     Primer_Nombre = Entrada_Primer_Nombre.get().strip().capitalize()
     Segundo_Nombre = Entrada_Segundo_Nombre.get().strip().capitalize()
     Primer_Apellido = Entrada_Primer_Apellido.get().strip().capitalize()
     Segundo_Apellido = Entrada_Segundo_Apellido.get().strip().capitalize()
     Documento = Entrada_Documento.get().strip()
     Tipo_Documento =Entrada_Tipo_Documento.get()
     Valor_Tipo_Documento = Tipo_Documento_Valores2.get(Tipo_Documento)
     Fecha_Nacimiento = Entrada_Fecha_Nacimento.get_date()
     Direccion = Entrada_Direccion.get()
     Numero = Entrada_Numero.get().strip()
     Email = Entrada_Email.get()
     Ciudad = Entrada_Ciudad.get().strip().capitalize()
     Departamento = Entrada_Departamento.get().strip().capitalize()
     Barrio = Entrada_Barrio.get().strip().capitalize()
     Localidad = Entrada_Localidad.get().strip().capitalize()
     hoy = date.today()
     Edad = hoy.year - Fecha_Nacimiento.year - ((hoy.month, hoy.day) < (Fecha_Nacimiento.month, Fecha_Nacimiento.day))
     if not all([Usuario, Contraseña, Primer_Nombre, Primer_Apellido, Documento, Valor_Tipo_Documento, Fecha_Nacimiento, Direccion, Numero, Email, Ciudad, Departamento, Barrio, Localidad]):
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        Cerrar_Base_De_Datos()
        return
     if not Documento.isdigit() or not (8 <= len(Documento) <= 10):
        messagebox.showerror("Error", "El documento debe tener entre 8 a 10 digitos")
        Cerrar_Base_De_Datos()
        return
     if not re.match(r"[^@]+@[^@]+\.[^@]+", Email):
        messagebox.showerror("Error", "Correo invalido")
        Cerrar_Base_De_Datos()
        return     
     if not Numero.isdigit() or len(Numero) != 10:
        messagebox.showerror("Error", "El telefono debe tener 10 digitos")
        Cerrar_Base_De_Datos()
        return
     cursor.execute("SELECT * FROM tbl_usuario WHERE Nombre = %s", (Usuario,))
     if cursor.fetchone():
        messagebox.showerror("Error", "El nuevo nombre de usuario ya está en uso.")
        Cerrar_Base_De_Datos()
        return
     cursor.execute("SELECT * FROM tbl_persona WHERE Id_Persona = %s", (Documento,))
     if cursor.fetchone():
        messagebox.showerror("Error", "El documento ya está registrado.")
        Cerrar_Base_De_Datos()
        return
     error = Funcion_Validar_Contraseña(Contraseña)
     if error:
        messagebox.showerror("Error de contraseña", error)
        Cerrar_Base_De_Datos()
        return
     persona = Persona(Usuario, Contraseña, Primer_Nombre, Segundo_Nombre, Primer_Apellido, Segundo_Apellido,
                  Documento, Tipo_Documento,Valor_Tipo_Documento, Fecha_Nacimiento, Edad, Direccion, Numero, Email,
                  Ciudad, Departamento, Barrio, Localidad)
     def generar_id(tabla, prefijo):
        cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
        resultado = cursor.fetchone()
        count = resultado[0] if resultado else 0
        return str(count + 1).zfill(3) + prefijo
     id_rol = "Usu"
     id_activo = "usuario_01"
     id_usuario = generar_id("tbl_usuario", "USU")
     id_barrio = generar_id("tbl_barrio", "BAR")
     id_ciudad = generar_id("tbl_ciudad", "CIU")
     id_departamento = generar_id("tbl_departamento", "DEP")
     id_localidad = generar_id("tbl_localidad", "LOC")
     id_adic_persona = generar_id("tbl_adic_persona", "PAD")

     try:
        if not conexion.in_transaction:
            conexion.start_transaction()

        cursor.execute("SELECT Id_dep FROM tbl_departamento WHERE Nom_departamento = %s", (persona.Departamento,))
        dep = cursor.fetchone()
        id_departamento = dep[0] if dep else generar_id("tbl_departamento", "DEP")
        if not dep:
            cursor.execute("INSERT INTO tbl_departamento (Id_dep, Nom_departamento) VALUES (%s, %s)",
                           (id_departamento, persona.Departamento))

        cursor.execute("SELECT Id_ciudad FROM tbl_ciudad WHERE Nom_ciudad = %s", (persona.Ciudad,))
        c = cursor.fetchone()
        id_ciudad = c[0] if c else generar_id("tbl_ciudad", "CIU")
        if not c:
            cursor.execute("INSERT INTO tbl_ciudad (Id_ciudad, Nom_ciudad, Fk_Dep) VALUES (%s, %s, %s)",
                           (id_ciudad, persona.Ciudad, id_departamento))

        cursor.execute("SELECT Id_local FROM tbl_localidad WHERE Localidad = %s", (persona.Localidad,))
        l = cursor.fetchone()
        id_localidad = l[0] if l else generar_id("tbl_localidad", "LOC")
        if not l:
            cursor.execute("INSERT INTO tbl_localidad (Id_local, Localidad, fk_ciudad) VALUES (%s, %s, %s)",
                           (id_localidad, persona.Localidad, id_ciudad))

        cursor.execute("SELECT Id_barrio FROM tbl_barrio WHERE Barrio = %s AND fk_local = %s", (persona.Barrio, id_localidad))
        b = cursor.fetchone()
        id_barrio = b[0] if b else generar_id("tbl_barrio", "BAR")
        if not b:
            cursor.execute("INSERT INTO tbl_barrio (Id_barrio, Barrio, fk_local) VALUES (%s, %s, %s)",
                           (id_barrio, persona.Barrio, id_localidad))
            
        cursor.execute("SELECT Id_Documento FROM tbl_tipo_documento WHERE Id_Documento = %s", (persona.Valor_Tipo_Documento,))
        tipo_doc = cursor.fetchone()
        id_tipo_documento = persona.Valor_Tipo_Documento 
        if not tipo_doc:
            cursor.execute("INSERT INTO tbl_tipo_documento (Id_Documento, Tipo_documento) VALUES (%s, %s)",
                   (id_tipo_documento, persona.Tipo_Documento))

        id_usuario = generar_id("tbl_usuario", "USU")
        cursor.execute("INSERT INTO tbl_usuario (Id_usuario, Nombre, Contraseña, fk_rol, fk_estado) VALUES (%s, %s, %s, %s, %s)", 
                       (id_usuario, persona.Usuario, persona.Contraseña, id_rol, id_activo))

        cursor.execute("INSERT INTO tbl_persona (Id_Persona, Pri_Nom, Seg_Nom, Pri_Ape, Seg_Ape, fk_Tipo_documento, Fecha_nacimiento, fk_Usuario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                       (persona.Documento, persona.Primer_Nombre, persona.Segundo_Nombre, persona.Primer_Apellido, persona.Segundo_Apellido, persona.Valor_Tipo_Documento, persona.Fecha_Nacimiento, id_usuario))

        cursor.execute("INSERT INTO tbl_adic_persona (Id_Adic_Persona, Edad, Dirección, Num_Contact, Email, fk_persona, fk_dir) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                       (id_adic_persona, persona.Edad, persona.Direccion, persona.Numero, persona.Email, persona.Documento, id_barrio)) 

        conexion.commit()
        messagebox.showinfo("Éxito", "Usuario y datos asociados creados correctamente.")
     except mysql.connector.Error as err:
        conexion.rollback()
        messagebox.showerror("Error", f"Ocurrió un error al guardar los datos: {err}")
     finally:
        mensaje = MIMEMultipart()
        mensaje["From"] = correo_emisor
        mensaje["To"] = Email
        mensaje["Subject"] = f"Estimado/a {Usuario}"
        cuerpo = "Queremos informarte que tu usuario ha sido creado exitosamente en nuestro sistema.\nSi no fuiste tú quien realizó este registro, por favor comunícate de inmediato con nuestro equipo de soporte para garantizar la seguridad de tu cuenta\nSi necesitas ayuda adicional, no dudes en escribirnos\nSi necesitas asistencia adicional, no dudes en escribirnos.\n\nAtentamente,El equipo de soporte de Right way sys"
        mensaje.attach(MIMEText(cuerpo, "plain"))
        try:
            servidor = smtplib.SMTP("smtp.gmail.com", 587)
            servidor.starttls()
            servidor.login(correo_emisor, contraseña)
            servidor.sendmail(correo_emisor, Email, mensaje.as_string())
            servidor.quit()
            print(f"Correo del usuario: {Email}")
            print("Correo enviado exitosamente")
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
        Cerrar_Base_De_Datos()
        Grafico_Inicio()
def Funcion_Recuperar_Contraseña():
    global Usuario, token_recuperacion, correo_token, hora_token
    Conexion_Base_De_Datos()
    Usuario = Entrada_Usuario.get()
    cursor.execute("SELECT * FROM tbl_usuario WHERE Nombre = %s", (Usuario,))
    resultado = cursor.fetchone()
    if not resultado:
          messagebox.showerror("Usuario no encontrado", "El nombre de usuario no existe.")
          return
    id_usuario = resultado[0]

    cursor.execute("SELECT tbl_adic_persona.Email FROM tbl_usuario  JOIN tbl_persona ON tbl_persona.fk_usuario = tbl_usuario.Id_usuario JOIN tbl_adic_persona ON tbl_adic_persona.fk_persona = tbl_persona.Id_Persona WHERE tbl_usuario.Nombre = %s", (Usuario,))
    resultado_correo = cursor.fetchone()
    if not resultado_correo:
          messagebox.showerror("Correo no encontrado", "El correo no existe.")
          return
    correo = resultado_correo[0]
    Cerrar_Base_De_Datos()

    token_recuperacion = str(uuid.uuid4())[:8] 
    correo_token = correo
    hora_token = datetime.now()

    mensaje = MIMEMultipart()
    mensaje["From"] = correo_emisor
    mensaje["To"] = correo
    mensaje["Subject"] = "Código de recuperación"
    cuerpo = f"Tu código para recuperar la contraseña es: {token_recuperacion}\nEste código es válido por 10 minutos\nRecuerda no compartirlo con nadie\nAtentamente,El equipo de Right way sys"
    mensaje.attach(MIMEText(cuerpo, "plain"))
    Grafico_Recuperar_Contraseña2()
    try:
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(correo_emisor, contraseña)
        servidor.sendmail(correo_emisor, correo, mensaje.as_string())
        servidor.quit()
        messagebox.showinfo("Éxito", "Se envió un token al correo.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al enviar el correo: {e}")
def Funcion_Validar_Token_Cambiar():
    global token_recuperacion, correo_token, hora_token
    Conexion_Base_De_Datos()
    if not token_recuperacion or not correo_token or not hora_token:
        messagebox.showerror("Error", "Primero solicita el código de recuperación.")
        return
    token_usuario = Entrada_UUID.get()
    nueva = Entrada_Contraseña_Nueva.get()
    if not token_usuario or not nueva:
        messagebox.showerror("Error", "todos los campos son obligatorios.")
        return
    if token_usuario != token_recuperacion:
        messagebox.showerror("Error", "Token incorrecto.")
        return
    if datetime.now() > hora_token + timedelta(minutes=10):
        messagebox.showerror("Error", "El token ha expirado.")
        return
    error = Funcion_Validar_Contraseña(nueva)
    if error:
        messagebox.showerror("Error", error)
        return
    cursor.execute("SELECT id_usuario FROM tbl_usuario WHERE Nombre = %s", (Usuario,))
    resultado_usuario = cursor.fetchone()
    if not resultado_usuario:
        messagebox.showerror("Error", "No se encontró el usuario.")
        Cerrar_Base_De_Datos()
        return
    id_usuario = resultado_usuario[0]
    cursor.execute("UPDATE tbl_usuario SET Contraseña = %s WHERE Id_usuario = %s", (nueva, id_usuario))
    conexion.commit()
    Cerrar_Base_De_Datos()
    token_recuperacion = None
    correo_token = None
    hora_token = None
    messagebox.showinfo("Éxito", "La contraseña ha sido actualizada.")
    Grafico_Inicio()
def Funcion_Crear_Usuario2():
     Conexion_Base_De_Datos()
     Usuario = Entrada_Usuario.get()
     Contraseña = Entrada_Contraseña.get()
     Primer_Nombre = Entrada_Primer_Nombre.get().strip().capitalize()
     Segundo_Nombre = Entrada_Segundo_Nombre.get().strip().capitalize()
     Primer_Apellido = Entrada_Primer_Apellido.get().strip().capitalize()
     Segundo_Apellido = Entrada_Segundo_Apellido.get().strip().capitalize()
     Documento = Entrada_Documento.get().strip()
     Tipo_Documento =Entrada_Tipo_Documento.get()
     Valor_Tipo_Documento = Tipo_Documento_Valores2.get(Tipo_Documento)
     Fecha_Nacimiento = Entrada_Fecha_Nacimento.get_date()
     Direccion = Entrada_Direccion.get()
     Numero = Entrada_Numero.get().strip()
     Email = Entrada_Email.get()
     Ciudad = Entrada_Ciudad.get().strip().capitalize()
     Departamento = Entrada_Departamento.get().strip().capitalize()
     Barrio = Entrada_Barrio.get().strip().capitalize()
     Localidad = Entrada_Localidad.get().strip().capitalize()
     hoy = date.today()
     Edad = hoy.year - Fecha_Nacimiento.year - ((hoy.month, hoy.day) < (Fecha_Nacimiento.month, Fecha_Nacimiento.day))
     if not all([Usuario, Contraseña, Primer_Nombre, Primer_Apellido, Documento, Valor_Tipo_Documento, Fecha_Nacimiento, Edad, Direccion, Numero, Email, Ciudad, Departamento, Barrio, Localidad]):
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        Cerrar_Base_De_Datos()
        return
     if not Documento.isdigit() or not (8 <= len(Documento) <= 10):
        messagebox.showerror("Error", "El documento debe tener entre 8 a 10 digitos")
        Cerrar_Base_De_Datos()
        return
     if not re.match(r"[^@]+@[^@]+\.[^@]+", Email):
        messagebox.showerror("Error", "Correo invalido")
        Cerrar_Base_De_Datos()
        return     
     if not Numero.isdigit() or len(Numero) != 10:
        messagebox.showerror("Error", "El telefono debe tener 10 digitos")
        Cerrar_Base_De_Datos()
        return
     cursor.execute("SELECT * FROM tbl_usuario WHERE Nombre = %s", (Usuario,))
     if cursor.fetchone():
        messagebox.showerror("Error", "El nuevo nombre de usuario ya está en uso.")
        Cerrar_Base_De_Datos()
        return
     cursor.execute("SELECT * FROM tbl_persona WHERE Id_Persona = %s", (Documento,))
     if cursor.fetchone():
        messagebox.showerror("Error", "El documento ya está registrado.")
        Cerrar_Base_De_Datos()
        return
     error = Funcion_Validar_Contraseña(Contraseña)
     if error:
        messagebox.showerror("Error de contraseña", error)
        Cerrar_Base_De_Datos()
        return
     persona = Persona(Usuario, Contraseña, Primer_Nombre, Segundo_Nombre, Primer_Apellido, Segundo_Apellido,
                  Documento, Tipo_Documento,Valor_Tipo_Documento, Fecha_Nacimiento, Edad, Direccion, Numero, Email,
                  Ciudad, Departamento, Barrio, Localidad)
     def generar_id(tabla, prefijo):
        cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
        resultado = cursor.fetchone()
        count = resultado[0] if resultado else 0
        return str(count + 1).zfill(3) + prefijo
     id_rol = "Usu"
     id_activo = "usuario_01"
     id_usuario = generar_id("tbl_usuario", "USU")
     id_barrio = generar_id("tbl_barrio", "BAR")
     id_ciudad = generar_id("tbl_ciudad", "CIU")
     id_departamento = generar_id("tbl_departamento", "DEP")
     id_localidad = generar_id("tbl_localidad", "LOC")
     id_adic_persona = generar_id("tbl_adic_persona", "PAD")

     try:
        if not conexion.in_transaction:
            conexion.start_transaction()

        cursor.execute("SELECT Id_dep FROM tbl_departamento WHERE Nom_departamento = %s", (persona.Departamento,))
        dep = cursor.fetchone()
        id_departamento = dep[0] if dep else generar_id("tbl_departamento", "DEP")
        if not dep:
            cursor.execute("INSERT INTO tbl_departamento (Id_dep, Nom_departamento) VALUES (%s, %s)",
                           (id_departamento, persona.Departamento))

        cursor.execute("SELECT Id_ciudad FROM tbl_ciudad WHERE Nom_ciudad = %s", (persona.Ciudad,))
        c = cursor.fetchone()
        id_ciudad = c[0] if c else generar_id("tbl_ciudad", "CIU")
        if not c:
            cursor.execute("INSERT INTO tbl_ciudad (Id_ciudad, Nom_ciudad, Fk_Dep) VALUES (%s, %s, %s)",
                           (id_ciudad, persona.Ciudad, id_departamento))

        cursor.execute("SELECT Id_local FROM tbl_localidad WHERE Localidad = %s", (persona.Localidad,))
        l = cursor.fetchone()
        id_localidad = l[0] if l else generar_id("tbl_localidad", "LOC")
        if not l:
            cursor.execute("INSERT INTO tbl_localidad (Id_local, Localidad, fk_ciudad) VALUES (%s, %s, %s)",
                           (id_localidad, persona.Localidad, id_ciudad))

        cursor.execute("SELECT Id_barrio FROM tbl_barrio WHERE Barrio = %s AND fk_local = %s", (persona.Barrio, id_localidad))
        b = cursor.fetchone()
        id_barrio = b[0] if b else generar_id("tbl_barrio", "BAR")
        if not b:
            cursor.execute("INSERT INTO tbl_barrio (Id_barrio, Barrio, fk_local) VALUES (%s, %s, %s)",
                           (id_barrio, persona.Barrio, id_localidad))
            
        cursor.execute("SELECT Id_Documento FROM tbl_tipo_documento WHERE Id_Documento = %s", (persona.Valor_Tipo_Documento,))
        tipo_doc = cursor.fetchone()
        id_tipo_documento = persona.Valor_Tipo_Documento 
        if not tipo_doc:
            cursor.execute("INSERT INTO tbl_tipo_documento (Id_Documento, Tipo_documento) VALUES (%s, %s)",
                   (id_tipo_documento, persona.Tipo_Documento))

        id_usuario = generar_id("tbl_usuario", "USU")
        cursor.execute("INSERT INTO tbl_usuario (Id_usuario, Nombre, Contraseña, fk_rol, fk_estado) VALUES (%s, %s, %s, %s, %s)", 
                       (id_usuario, persona.Usuario, persona.Contraseña, id_rol, id_activo))

        cursor.execute("INSERT INTO tbl_persona (Id_Persona, Pri_Nom, Seg_Nom, Pri_Ape, Seg_Ape, fk_Tipo_documento, Fecha_nacimiento, fk_Usuario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                       (persona.Documento, persona.Primer_Nombre, persona.Segundo_Nombre, persona.Primer_Apellido, persona.Segundo_Apellido, persona.Valor_Tipo_Documento, persona.Fecha_Nacimiento, id_usuario))

        cursor.execute("INSERT INTO tbl_adic_persona (Id_Adic_Persona, Edad, Dirección, Num_Contact, Email, fk_persona, fk_dir) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                       (id_adic_persona, persona.Edad, persona.Direccion, persona.Numero, persona.Email, persona.Documento, id_barrio)) 

        conexion.commit()
        messagebox.showinfo("Éxito", "Usuario y datos asociados creados correctamente.")
     except mysql.connector.Error as err:
        conexion.rollback()
        messagebox.showerror("Error", f"Ocurrió un error al guardar los datos: {err}")
     finally:
        mensaje = MIMEMultipart()
        mensaje["From"] = correo_emisor
        mensaje["To"] = Email
        mensaje["Subject"] = f"Estimado/a {Usuario}"
        cuerpo = "Queremos informarte que tu usuario ha sido creado exitosamente en nuestro sistema.\nSi no fuiste tú quien realizó este registro, por favor comunícate de inmediato con nuestro equipo de soporte para garantizar la seguridad de tu cuenta\nSi necesitas ayuda adicional, no dudes en escribirnos\nSi necesitas asistencia adicional, no dudes en escribirnos.\n\nAtentamente,El equipo de soporte de Right way sys"
        mensaje.attach(MIMEText(cuerpo, "plain"))
        try:
            servidor = smtplib.SMTP("smtp.gmail.com", 587)
            servidor.starttls()
            servidor.login(correo_emisor, contraseña)
            servidor.sendmail(correo_emisor, Email, mensaje.as_string())
            servidor.quit()
            print(f"Correo del usuario: {Email}")
            print("Correo enviado exitosamente")
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
        Cerrar_Base_De_Datos()
        Grafico_Admin_Usuarios()
def Funcion_Crear_Caso():
     Conexion_Base_De_Datos()
     TipoDesastre = Entrada_Caso_TipoDesastre.get()
     Fecha = Entrada_Caso_Fecha.get_date()
     Descripcion = Entrada_Caso_Descripcion.get("1.0", "end").strip()
     Direccion = Entrada_Caso_Direccion.get()
     Afectados = Entrada_Caso_Personas.get()

     if not all([TipoDesastre, Fecha, Descripcion, Direccion, Afectados]):
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        Cerrar_Base_De_Datos()
        return
     caso = Caso(TipoDesastre, Fecha, Descripcion, Direccion, Afectados)
     def generar_id(tabla, prefijo, longitud):
        cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
        resultado = cursor.fetchone()
        count = resultado[0] if resultado else 0
        return str(count + 1).zfill(longitud) + prefijo
     id_Caso_desastre = generar_id("tbl_caso", "CAD", longitud=3)
     radicado = generar_id("tbl_num_caso", "R", longitud=6)
     id_entidad = generar_id("tbl_num_caso", "NUC", longitud=3)
     id_caso = "Caso"
     if TipoDesastre == "Incendio":
         id_desastre = "Incen"
     elif TipoDesastre == "Inundaciòn":
         id_desastre = "Inund"
     elif TipoDesastre == "Sismo-temblor":
         id_desastre = "Sismo"
     elif TipoDesastre == "Terremoto":
         id_desastre = "Terre"

     cursor.execute("SELECT id_usuario FROM tbl_usuario WHERE Nombre = %s", (Usuario,))
     resultado_usuario = cursor.fetchone()
     if not resultado_usuario:
        messagebox.showerror("Error", "No se encontró el usuario.")
        Cerrar_Base_De_Datos()
        return
     id_usuario = resultado_usuario[0]
     id_departamento = "001DEP"
     id_estado = "Caso_00"
     try:
        if not conexion.in_transaction:
            conexion.start_transaction()

        cursor.execute("INSERT INTO tbl_caso (Id_Caso_Desastre, Fecha, Descripción, Personas_Afectadas, Fk_Usuario, Fk_Desastre, Fk_Dep, Fk_Tipo_Caso, Fk_Estado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
                       (id_Caso_desastre, caso.Fecha, caso.Descripcion, caso.Afectados, id_usuario, id_desastre, id_departamento, id_caso, id_estado))

        cursor.execute("INSERT INTO tbl_num_caso (Id_num_caso, Radicado, Fk_Caso) VALUES (%s, %s, %s)", 
                       (id_entidad, radicado, id_Caso_desastre)) 

        conexion.commit()
        messagebox.showinfo("Éxito", f"Caso y datos asociados creados correctamente.\n Numero de radicado: {radicado}")
     except mysql.connector.Error as err:
        conexion.rollback()
        messagebox.showerror("Error", f"Ocurrió un error al guardar los datos: {err}")
     finally:
        Conseguir_Correo()
        mensaje = MIMEMultipart()
        mensaje["From"] = correo_emisor
        mensaje["To"] = f"{correo_receptor1}, {correo_receptor2}"
        mensaje["Subject"] = f"Confirmación de Generación de Caso: {radicado}"
        cuerpo = f"Estimado/a {Usuario},\nTe confirmamos que tu solicitud ha sido recibida correctamente. Un ticket ha sido generado con el ID: {radicado}. Nuestro equipo está trabajando en tu solicitud y te contactará en breve para resolver tu problema.\nSi necesitas más detalles sobre el estado de tu ticket, puedes seguirlo a través de nuestro sistema o contactar a soporte.\nGracias por confiar en nosotros.\nAtentamente,\nEl equipo de soporte de Right way sys"
        mensaje.attach(MIMEText(cuerpo, "plain"))
        try:
            servidor = smtplib.SMTP("smtp.gmail.com", 587)
            servidor.starttls()
            servidor.login(correo_emisor, contraseña)
            servidor.sendmail(correo_emisor, [correo_receptor1, correo_receptor2], mensaje.as_string())
            servidor.quit()
            print("Correo enviado exitosamente")
        except Exception as e:
            print(f"Error al enviar el correo: {e}")        
        cursor.execute("SELECT tbl_usuario.fk_rol From tbl_usuario WHERE tbl_usuario.Nombre = %s", (Usuario,))
        rol_resultado = cursor.fetchone()
        if rol_resultado:
            rol = rol_resultado[0]
            if rol == "Usu":
                Cerrar_Base_De_Datos()
                Contador = 0
                Grafico_Usuario_Casos()
                return
            elif rol == "Admin":
                Cerrar_Base_De_Datos()
                Contador = 0
                Grafico_Admin_Casos()
                return
            else:
                Cerrar_Base_De_Datos()
                messagebox.showinfo("Error", "No se encontro el rol del usuario")
                return     
def Funcion_Buscar_Caso2():
    global Radicado, Radicado_Fecha, Radicado_Descripcion, Radicado_Personas, Radicado_Usuario, Radicado_Desastre, Radicado_Departamento, Radicado_Tipo, Radicado_Estado
    Conexion_Base_De_Datos()
    Radicado = Entrada_Caso_Radicado.get()
    if not Radicado:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        try:
            if conexion and conexion.is_connected():
                Cerrar_Base_De_Datos()
        except:
            pass
        return
    try:
        cursor.execute("SELECT id_usuario, fk_rol FROM tbl_usuario WHERE Nombre = %s", (Usuario,))
        resultado_usuario = cursor.fetchone()
        if not resultado_usuario:
            messagebox.showerror("Error", "No se encontró el usuario.")
            return
        id_usuario, rol = resultado_usuario
        cursor.execute("SELECT tbl_caso.Fk_Estado FROM tbl_num_caso JOIN tbl_caso ON tbl_num_caso.Fk_Caso = tbl_caso.Id_Caso_Desastre WHERE tbl_num_caso.Radicado = %s", (Radicado,))
        resultado_estado = cursor.fetchone()
        if not resultado_estado:
            messagebox.showerror("Error", "No se encontró el estado del de radicado.")
            Cerrar_Base_De_Datos()
            return
        Estado_Actual = resultado_estado[0]
        if Estado_Actual == "Caso_03":
            messagebox.showerror("Error", "El numero de radicado no existe.")
            return
        cursor.execute("SELECT radicado FROM tbl_num_caso WHERE Radicado = %s", (Radicado,))
        if not cursor.fetchone():
            messagebox.showerror("Error", "No se encontró el número de radicado.")
            return

        if not conexion.in_transaction:
            conexion.start_transaction()
        query = """
            SELECT 
                tbl_caso.Fecha,
                tbl_caso.Descripción,
                tbl_caso.Personas_Afectadas,
                tbl_usuario.Nombre,
                tbl_desastre.Desastre,
                tbl_departamento.Nom_departamento,
                tbl_tipo_caso.Tipo_Caso,
                tbl_estado.Estado
            FROM tbl_caso
            JOIN tbl_usuario ON tbl_caso.Fk_Usuario = tbl_usuario.Id_Usuario
            JOIN tbl_desastre ON tbl_caso.Fk_Desastre = tbl_desastre.Id_Desastre
            JOIN tbl_departamento ON tbl_caso.Fk_Dep = tbl_departamento.Id_dep
            JOIN tbl_tipo_caso ON tbl_caso.Fk_Tipo_Caso = tbl_tipo_caso.Id_caso
            JOIN tbl_estado ON tbl_caso.Fk_Estado = tbl_estado.Id_estado
            JOIN tbl_num_caso ON tbl_caso.Id_Caso_Desastre = tbl_num_caso.Fk_Caso
            WHERE tbl_num_caso.Radicado = %s
        """
        cursor.execute(query, (Radicado,))
        resultado = cursor.fetchone()
        if not resultado:
            messagebox.showerror("Error", "No se encontraron los datos del caso.")
            return
        fecha, descripcion, personas, usuario, desastre, departamento, tipo, estado = resultado
        Radicado_Fecha = fecha.strftime("%d/%m/%Y") if fecha else ""
        Radicado_Descripcion = descripcion
        Radicado_Personas = personas
        Radicado_Usuario = usuario
        Radicado_Desastre = desastre
        Radicado_Departamento = departamento
        Radicado_Tipo = tipo
        Radicado_Estado = estado

        conexion.commit()
        messagebox.showinfo("Éxito", f"Caso encontrado.\n Número de radicado: {Radicado}")
        Contador = 0
        if rol == "Usu":
            Grafico_Usuario_Casos_Buscar_2()
        elif rol == "Admin":
            Grafico_Admin_Modificar_Casos()
        else:
            messagebox.showerror("Error", "Rol del usuario desconocido.")

    except mysql.connector.Error as err:
        try:
            if conexion and conexion.is_connected() and conexion.in_transaction:
                conexion.rollback()
        except:
            print("No se pudo hacer rollback: conexión cerrada.")
        messagebox.showerror("Error", f"Ocurrió un error al consultar los datos: {err}")

    finally:
        try:
            if conexion and conexion.is_connected():
                Cerrar_Base_De_Datos()
        except:
            print("No se pudo cerrar la conexión: ya se había cerrado.")
def Funcion_Buscar_Caso():
    global Radicado, Radicado_Fecha, Radicado_Descripcion, Radicado_Personas, Radicado_Usuario, Radicado_Desastre, Radicado_Departamento, Radicado_Tipo, Radicado_Estado
    Conexion_Base_De_Datos()
    Radicado = Entrada_Caso_Radicado.get()
    if not Radicado:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        try:
            if conexion and conexion.is_connected():
                Cerrar_Base_De_Datos()
        except:
            pass
        return
    try:
        cursor.execute("SELECT id_usuario, fk_rol FROM tbl_usuario WHERE Nombre = %s", (Usuario,))
        resultado_usuario = cursor.fetchone()
        if not resultado_usuario:
            messagebox.showerror("Error", "No se encontró el usuario.")
            return
        id_usuario, rol = resultado_usuario
        cursor.execute("SELECT tbl_caso.Fk_Estado FROM tbl_num_caso JOIN tbl_caso ON tbl_num_caso.Fk_Caso = tbl_caso.Id_Caso_Desastre WHERE tbl_num_caso.Radicado = %s", (Radicado,))
        resultado_estado = cursor.fetchone()
        if not resultado_estado:
            messagebox.showerror("Error", "No se encontró el estado del de radicado.")
            Cerrar_Base_De_Datos()
            return
        Estado_Actual = resultado_estado[0]
        if Estado_Actual == "Caso_03":
            messagebox.showerror("Error", "El numero de radicado no existe.")
            return
        cursor.execute("SELECT radicado FROM tbl_num_caso WHERE Radicado = %s", (Radicado,))
        if not cursor.fetchone():
            messagebox.showerror("Error", "No se encontró el número de radicado.")
            return

        if not conexion.in_transaction:
            conexion.start_transaction()
        query = """
            SELECT 
                tbl_caso.Fecha,
                tbl_caso.Descripción,
                tbl_caso.Personas_Afectadas,
                tbl_usuario.Nombre,
                tbl_desastre.Desastre,
                tbl_departamento.Nom_departamento,
                tbl_tipo_caso.Tipo_Caso,
                tbl_estado.Estado
            FROM tbl_caso
            JOIN tbl_usuario ON tbl_caso.Fk_Usuario = tbl_usuario.Id_Usuario
            JOIN tbl_desastre ON tbl_caso.Fk_Desastre = tbl_desastre.Id_Desastre
            JOIN tbl_departamento ON tbl_caso.Fk_Dep = tbl_departamento.Id_dep
            JOIN tbl_tipo_caso ON tbl_caso.Fk_Tipo_Caso = tbl_tipo_caso.Id_caso
            JOIN tbl_estado ON tbl_caso.Fk_Estado = tbl_estado.Id_estado
            JOIN tbl_num_caso ON tbl_caso.Id_Caso_Desastre = tbl_num_caso.Fk_Caso
            WHERE tbl_num_caso.Radicado = %s
        """
        cursor.execute(query, (Radicado,))
        resultado = cursor.fetchone()
        if not resultado:
            messagebox.showerror("Error", "No se encontraron los datos del caso.")
            return
        fecha, descripcion, personas, usuario, desastre, departamento, tipo, estado = resultado
        Radicado_Fecha = fecha.strftime("%d/%m/%Y") if fecha else ""
        Radicado_Descripcion = descripcion
        Radicado_Personas = personas
        Radicado_Usuario = usuario
        Radicado_Desastre = desastre
        Radicado_Departamento = departamento
        Radicado_Tipo = tipo
        Radicado_Estado = estado

        conexion.commit()
        messagebox.showinfo("Éxito", f"Caso encontrado.\n Número de radicado: {Radicado}")
        Contador = 0
        if rol == "Usu":
            Grafico_Usuario_Casos_Buscar_2()
        elif rol == "Admin":
            Grafico_Admin_Casos_Buscar_2()
        else:
            messagebox.showerror("Error", "Rol del usuario desconocido.")

    except mysql.connector.Error as err:
        try:
            if conexion and conexion.is_connected() and conexion.in_transaction:
                conexion.rollback()
        except:
            print("No se pudo hacer rollback: conexión cerrada.")
        messagebox.showerror("Error", f"Ocurrió un error al consultar los datos: {err}")

    finally:
        try:
            if conexion and conexion.is_connected():
                Cerrar_Base_De_Datos()
        except:
            print("No se pudo cerrar la conexión: ya se había cerrado.")
def Funcion_Buscar_Usuario():
    global Identificacion, Busqueda_Documento, Busqueda_Edad, Busqueda_TipoDocumento, Busqueda_PrimerNombre, Busqueda_SegundoNombre, Busqueda_PrimerApellido, Busqueda_SegundoApellido, Busqueda_NombreUsuario, Busqueda_RolUsuario, Busqueda_EstadoUsuario, Busqueda_Departamento, Busqueda_Ciudad, Busqueda_Localidad, Busqueda_Barrio, Busqueda_Direccion, Busqueda_FechaNacimento, Busqueda_Busqueda_Edad, Busqueda_Telefono, Busqueda_Email
    Conexion_Base_De_Datos()
    Identificacion = Entrada_Usuario_Identificacion.get()
    if not Identificacion:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        try:
            if conexion and conexion.is_connected():
                Cerrar_Base_De_Datos()
        except:
            pass
        return
    try:
        cursor.execute("SELECT fk_usuario FROM tbl_persona WHERE Id_Persona = %s", (Identificacion,))
        resultado_usuario = cursor.fetchone()
        if not resultado_usuario:
            messagebox.showerror("Error", "No se encontró el usuario.")
            return
        id_usuario = resultado_usuario[0]

        cursor.execute("SELECT fk_estado FROM tbl_usuario WHERE Id_usuario = %s", (id_usuario,))
        resultado_estado = cursor.fetchone()
        if not resultado_estado:
            messagebox.showerror("Error", "No se encontró el Usuario.")
            Cerrar_Base_De_Datos()
            return
        Estado_Actual = resultado_estado[0]
        if Estado_Actual == "Usuario_00":
            messagebox.showerror("Usuario no encontrado", "El usuario no existe.")
            return

        if not conexion.in_transaction:
            conexion.start_transaction()
        cursor.execute("""
                SELECT 
                    tbl_persona.Id_Persona,
                    tbl_persona.fk_Tipo_documento,
                    tbl_persona.Pri_Nom,
                    tbl_persona.Seg_Nom,
                    tbl_persona.Pri_Ape,
                    tbl_persona.Seg_Ape,
                    tbl_usuario.Nombre,
                    tbl_usuario.fk_rol,
                    tbl_usuario.fk_estado,
                    tbl_departamento.Nom_departamento,
                    tbl_ciudad.Nom_ciudad,
                    tbl_localidad.Localidad,
                    tbl_barrio.Barrio,
                    tbl_adic_persona.Dirección,
                    tbl_persona.Fecha_nacimiento,
                    tbl_adic_persona.Edad,
                    tbl_adic_persona.Num_Contact,
                    tbl_adic_persona.Email
                FROM tbl_adic_persona 
                JOIN tbl_persona ON tbl_adic_persona.fk_persona = tbl_persona.Id_persona
                JOIN tbl_tipo_documento ON tbl_persona.fk_Tipo_documento = tbl_tipo_documento.Id_Documento 
                JOIN tbl_usuario ON tbl_persona.fk_usuario = tbl_usuario.Id_usuario 
                JOIN tbl_barrio ON tbl_adic_persona.fk_dir = tbl_barrio.Id_barrio
                JOIN tbl_localidad ON tbl_barrio.fk_local = tbl_localidad.Id_local
                JOIN tbl_ciudad ON tbl_localidad.fk_ciudad = tbl_ciudad.Id_ciudad
                JOIN tbl_departamento ON tbl_ciudad.Fk_Dep = tbl_departamento.Id_dep
                WHERE tbl_usuario.Id_usuario = %s
                """, (id_usuario,))
        resultado = cursor.fetchone()
        if not resultado:
            messagebox.showerror("Error", "No se encontraron los datos del usuario.")
            return
        
        Documento, TipoDocumento, PrimerNombre, SegundoNombre, PrimerApellido, SegundoApellido, NombreUsuario, RolUsuario, EstadoUsuario, Departamento, Ciudad, Localidad, Barrio, Direccion, FechaNacimento, Edad, Telefono, Email = resultado
        Busqueda_Documento = Documento
        Busqueda_TipoDocumento = Tipo_Documento_Valores.get(TipoDocumento)
        Busqueda_PrimerNombre = PrimerNombre
        Busqueda_SegundoNombre = SegundoNombre
        Busqueda_PrimerApellido = PrimerApellido
        Busqueda_SegundoApellido = SegundoApellido
        Busqueda_NombreUsuario = NombreUsuario
        Busqueda_RolUsuario = Rol_Valores2.get(RolUsuario, "Rol desconocido")
        Busqueda_EstadoUsuario = Estados_Valores2.get(EstadoUsuario, "Estado desconocido")
        Busqueda_Departamento = Departamento
        Busqueda_Ciudad = Ciudad
        Busqueda_Localidad = Localidad
        Busqueda_Barrio = Barrio
        Busqueda_Direccion = Direccion
        Busqueda_FechaNacimento = FechaNacimento.strftime("%d/%m/%Y") if FechaNacimento else ""
        Busqueda_Edad = Edad
        Busqueda_Telefono = Telefono
        Busqueda_Email = Email

        conexion.commit()
        messagebox.showinfo("Éxito", f"Usuario encontrado.\n Número de Identificacion: {Identificacion}")
        Contador = 0
        Grafico_Admin_Usuarios_Buscar_2()
    except mysql.connector.Error as err:
        try:
            if conexion and conexion.is_connected() and conexion.in_transaction:
                conexion.rollback()
        except:
            print("No se pudo hacer rollback: conexión cerrada.")
        messagebox.showerror("Error", f"Ocurrió un error al consultar los datos: {err}")

    finally:
        try:
            if conexion and conexion.is_connected():
                Cerrar_Base_De_Datos()
        except:
            print("No se pudo cerrar la conexión: ya se había cerrado.")
def Funcion_Pagina():
    global Busqueda2_Documento, Busqueda2_Edad, Busqueda2_TipoDocumento, Busqueda2_PrimerNombre, Busqueda2_SegundoNombre, Busqueda2_PrimerApellido, Busqueda2_SegundoApellido, Busqueda2_NombreUsuario, Busqueda2_RolUsuario, Busqueda2_EstadoUsuario, Busqueda2_Departamento, Busqueda2_Ciudad, Busqueda2_Localidad, Busqueda2_Barrio, Busqueda2_Direccion, Busqueda2_FechaNacimento, Busqueda2_Busqueda2_Edad, Busqueda2_Telefono, Busqueda2_Email
    Conexion_Base_De_Datos()

    try:
        cursor.execute("SELECT * FROM tbl_usuario WHERE Nombre = %s", (Usuario,))
        resultado = cursor.fetchone()
        if not resultado:
            messagebox.showerror("Usuario no encontrado", "El nombre de usuario no existe.")
            return
        id_usuario = resultado[0]
        if not conexion.in_transaction:
            conexion.start_transaction()
        cursor.execute("""
                SELECT 
                    tbl_persona.Id_Persona,
                    tbl_persona.fk_Tipo_documento,
                    tbl_persona.Pri_Nom,
                    tbl_persona.Seg_Nom,
                    tbl_persona.Pri_Ape,
                    tbl_persona.Seg_Ape,
                    tbl_usuario.Nombre,
                    tbl_usuario.fk_rol,
                    tbl_usuario.fk_estado,
                    tbl_departamento.Nom_departamento,
                    tbl_ciudad.Nom_ciudad,
                    tbl_localidad.Localidad,
                    tbl_barrio.Barrio,
                    tbl_adic_persona.Dirección,
                    tbl_persona.Fecha_nacimiento,
                    tbl_adic_persona.Edad,
                    tbl_adic_persona.Num_Contact,
                    tbl_adic_persona.Email
                FROM tbl_adic_persona 
                JOIN tbl_persona ON tbl_adic_persona.fk_persona = tbl_persona.Id_persona
                JOIN tbl_tipo_documento ON tbl_persona.fk_Tipo_documento = tbl_tipo_documento.Id_Documento 
                JOIN tbl_usuario ON tbl_persona.fk_usuario = tbl_usuario.Id_usuario 
                JOIN tbl_barrio ON tbl_adic_persona.fk_dir = tbl_barrio.Id_barrio
                JOIN tbl_localidad ON tbl_barrio.fk_local = tbl_localidad.Id_local
                JOIN tbl_ciudad ON tbl_localidad.fk_ciudad = tbl_ciudad.Id_ciudad
                JOIN tbl_departamento ON tbl_ciudad.Fk_Dep = tbl_departamento.Id_dep
                WHERE tbl_usuario.Id_usuario = %s
                """, (id_usuario,))
        resultado = cursor.fetchone()
        if not resultado:
            messagebox.showerror("Error", "No se encontraron los datos del usuario.")
            return
        
        Documento, TipoDocumento, PrimerNombre, SegundoNombre, PrimerApellido, SegundoApellido, NombreUsuario, RolUsuario, EstadoUsuario, Departamento, Ciudad, Localidad, Barrio, Direccion, FechaNacimento, Edad, Telefono, Email = resultado
        Busqueda2_Documento = Documento
        Busqueda2_TipoDocumento = Tipo_Documento_Valores.get(TipoDocumento)
        Busqueda2_PrimerNombre = PrimerNombre
        Busqueda2_SegundoNombre = SegundoNombre
        Busqueda2_PrimerApellido = PrimerApellido
        Busqueda2_SegundoApellido = SegundoApellido
        Busqueda2_NombreUsuario = NombreUsuario
        Busqueda2_RolUsuario = Rol_Valores2.get(RolUsuario, "Rol desconocido")
        Busqueda2_EstadoUsuario = Estados_Valores2.get(EstadoUsuario, "Estado desconocido")
        Busqueda2_Departamento = Departamento
        Busqueda2_Ciudad = Ciudad
        Busqueda2_Localidad = Localidad
        Busqueda2_Barrio = Barrio
        Busqueda2_Direccion = Direccion
        Busqueda2_FechaNacimento = FechaNacimento.strftime("%d/%m/%Y") if FechaNacimento else ""
        Busqueda2_Edad = Edad
        Busqueda2_Telefono = Telefono
        Busqueda2_Email = Email

        conexion.commit()
        Contador = 0
        Grafico_Pagina()
    except mysql.connector.Error as err:
        try:
            if conexion and conexion.is_connected() and conexion.in_transaction:
                conexion.rollback()
        except:
            print("No se pudo hacer rollback: conexión cerrada.")
        messagebox.showerror("Error", f"Ocurrió un error al consultar los datos: {err}")

    finally:
        try:
            if conexion and conexion.is_connected():
                Cerrar_Base_De_Datos()
        except:
            print("No se pudo cerrar la conexión: ya se había cerrado.")
def Funcion_Buscar_Entidades():
    try:
        Conexion_Base_De_Datos()
        cursor.execute("""
            SELECT 
                tbl_entidad.Id_entidad, 
                tbl_entidad.Nombre_Entidad, 
                tbl_entidad.Descripción AS Descripcion_Entidad, 
                tbl_entidad.fk_desastre, 
                tbl_adic_entidad.Id_Adic_Entidad, 
                tbl_adic_entidad.Direccion, 
                tbl_adic_entidad.Num_Contact, 
                tbl_adic_entidad.web_site, 
                tbl_adic_entidad.Descripción AS Descripcion_Adicional
            FROM tbl_entidad
            LEFT JOIN tbl_adic_entidad ON tbl_entidad.Id_entidad = tbl_adic_entidad.fk_entidad
        """)
        resultados = cursor.fetchall()

        ventana = CTkToplevel()
        ventana.title("Listado de Entidades")
        ventana.geometry("1220x580")
        ventana.resizable(False, False)
        ventana.config(background="#2d3e50")
        ventana.lift()
        ventana.focus_force()
        ventana.grab_set()
        ancho, alto = 1200, 580
        x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (ventana.winfo_screenheight() // 2) - (alto // 2)
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

        barra_superior = CTkFrame(ventana, height=40, fg_color="#2d3e50", border_color="#2d3e50")
        barra_superior.pack(fill="x", padx=20, pady=(10, 0))

        Boton_Salir = CTkButton(barra_superior, width=30, height=35, text="", corner_radius= 8, fg_color="#ff1919", hover_color="#be0000", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Salir, size=(22, 22)), command=ventana.destroy) 
        Boton_Salir.pack(side="left", padx=10, pady=5)

        contenedor = CTkFrame(ventana, corner_radius=15)
        contenedor.pack(padx=20, pady=20, fill="both", expand=True)

        columnas = (
            "ID Entidad", "Nombre", "Descripción Ent", "Desastre",
            "ID Adicional", "Dirección", "Teléfono", "Web", "Descripción Adic"
        )

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#2d3e50",
                        foreground="black",
                        rowheight=30,
                        fieldbackground="#f0f0f0",
                        font=(fuente, 10))
        style.configure("Treeview.Heading",
                        background="#12bfbf",
                        foreground="white",
                        font=(fuente, 11, "bold"))
        style.map('Treeview', background=[('selected', '#16e3e3')])

        tabla = ttk.Treeview(contenedor, columns=columnas, show="headings", height=15)

        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, anchor="center", width=120)

        scroll = ttk.Scrollbar(contenedor, orient="vertical", command=tabla.yview)
        tabla.configure(yscrollcommand=scroll.set)

        tabla.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        for i, fila in enumerate(resultados):
            tabla.insert("", tk.END, values=fila, tags=('evenrow' if i % 2 == 0 else 'oddrow',))

        tabla.tag_configure('evenrow', background="#f9f9f9")
        tabla.tag_configure('oddrow', background="#e6e6e6")

    except mysql.connector.Error as error:
        messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos:\n{error}")
def Funcion_Modificar_Contraseña():
    global Contador, Max_Intentos, Intentos_Restantes
    Conexion_Base_De_Datos()
    Contraseña = Entrada_Contraseña.get()
    Nueva_Contraseña = Entrada_Contraseña_Nueva.get()
    if not all([ Contraseña, Nueva_Contraseña]):
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        Cerrar_Base_De_Datos()
        return
    try: 
     cursor.execute("SELECT * FROM tbl_usuario WHERE Nombre = %s", (Usuario,))
     resultado = cursor.fetchone()
     if not resultado:
          messagebox.showerror("Usuario no encontrado", "El nombre de usuario no existe.")
          return
     id_usuario = resultado[0]
     cursor.execute("SELECT * FROM tbl_usuario WHERE Nombre = %s AND Contraseña = %s", (Usuario, Contraseña))
     resultado_contraseña = cursor.fetchone()
     if not resultado_contraseña:
        Contador += 1
        Intentos_Restantes = Max_Intentos - Contador
        if Intentos_Restantes > 0:
            messagebox.showerror("Contraseña incorrecta", f"La contraseña es incorrecta. Intentos restantes: {Intentos_Restantes}")
        else:
            messagebox.showerror("Acceso denegado", "Has superado el número máximo de intentos.")
            root.quit()
        return
     Funcion_Validar_Contraseña(Nueva_Contraseña)
     respuesta = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas modificar la contraseña?")
     if respuesta:
        cursor.execute("UPDATE tbl_usuario SET Contraseña = %s WHERE Id_usuario = %s", (Nueva_Contraseña, id_usuario))
        conexion.commit()
        messagebox.showinfo("Éxito", "Contraseña modificada correctamente.")
        Contador = 0
        Grafico_Usuario_Inicio()
     else:
        messagebox.showinfo("Cancelado", "La modificación de la contraseña ha sido cancelada.")
        Grafico_Usuario_Inicio()
    except mysql.connector.Error as err:
        conexion.rollback()
        messagebox.showerror("Error", f"Error al modificar la contraseña: {err}")
    finally:
        Conseguir_Correo()
        mensaje = MIMEMultipart()
        mensaje["From"] = correo_emisor
        mensaje["To"] = correo_receptor2
        mensaje["Subject"] = f"Estimado/a {Usuario}"
        cuerpo = "Queremos informarte que tu contraseña ha sido cambiada exitosamente en nuestro sistema.\nSi no realizaste este cambio, te pedimos que te pongas en contacto con nuestro soporte técnico\nlo más pronto posible para asegurar la seguridad de tu cuenta.\nSi necesitas asistencia adicional, no dudes en escribirnos.\n\nAtentamente,El equipo de soporte de Right way sys"
        mensaje.attach(MIMEText(cuerpo, "plain"))
        try:
            servidor = smtplib.SMTP("smtp.gmail.com", 587)
            servidor.starttls()
            servidor.login(correo_emisor, contraseña)
            servidor.sendmail(correo_emisor, correo_receptor2, mensaje.as_string())
            servidor.quit()
            print("Correo enviado exitosamente")
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
        Cerrar_Base_De_Datos()
def Funcion_Cargar_Contactos_Usuario():
    global Email_Original, Telefono_Original, Direccion_Original, TipoDocumento_Original, id_persona, id_usuario
    Conexion_Base_De_Datos()

    cursor.execute("SELECT * FROM tbl_usuario WHERE Nombre = %s", (Usuario,))
    resultado = cursor.fetchone()
    if not resultado:
        messagebox.showerror("Usuario no encontrado", "El nombre de usuario no existe.")
        return
    id_usuario = resultado[0]

    cursor.execute("SELECT Id_Persona FROM tbl_persona WHERE fk_usuario = %s", (id_usuario,))
    resultado2 = cursor.fetchone()
    if not resultado2:
        messagebox.showerror("Persona no encontrada", "El número de la persona no existe.")
        return
    id_persona = resultado2[0]

    cursor.execute("SELECT tbl_adic_persona.Email, tbl_adic_persona.Num_Contact, tbl_adic_persona.Dirección, tbl_tipo_documento.Tipo_documento FROM tbl_adic_persona JOIN tbl_persona ON tbl_adic_persona.fk_persona = tbl_persona.Id_persona JOIN tbl_tipo_documento ON tbl_persona.fk_Tipo_documento = tbl_tipo_documento.Id_Documento JOIN tbl_usuario ON tbl_persona.fk_usuario = tbl_usuario.Id_usuario WHERE tbl_usuario.Id_usuario = %s", (id_usuario,))
    datos = cursor.fetchone()
    if not datos:
        messagebox.showerror("Datos no encontrados", "Los datos no existen.")
        return
    Email_Original, Telefono_Original, Direccion_Original, TipoDocumento_Original = datos

    Cerrar_Base_De_Datos()
def Funcion_Cargar_Datos_Casos():
    global Estado_Original, Fecha_Formateada, Fecha_Original, Descripcion_Original, Afectados_Original, Desastre_Original, Departamento_Original, Tipo_Original, Desastre_Convertido, Estado_Convertido, Departamento_Convertido
    Conexion_Base_De_Datos()
    cursor.execute("SELECT tbl_caso.Fk_Estado FROM tbl_num_caso JOIN tbl_caso ON tbl_num_caso.Fk_Caso = tbl_caso.Id_Caso_Desastre WHERE tbl_num_caso.Radicado = %s", (Radicado,))
    resultado_estado = cursor.fetchone()
    if not resultado_estado:
        messagebox.showerror("Error", "No se encontró el estado del de radicado.")
        Cerrar_Base_De_Datos()
        return
    Estado_Actual = resultado_estado[0]
    if Estado_Actual == "Caso_03":
        messagebox.showerror("Error", "El numero de radicado no existe.")
        return
    cursor.execute("SELECT tbl_caso.Fk_Estado, tbl_caso.Fecha, tbl_caso.Descripción, tbl_caso.Personas_Afectadas, tbl_caso.Fk_Desastre, tbl_caso.Fk_Dep, tbl_caso.Fk_Tipo_Caso FROM tbl_caso JOIN tbl_num_caso ON tbl_caso.Id_Caso_Desastre = tbl_num_caso.Fk_Caso WHERE tbl_num_caso.Radicado = %s", (Radicado,))
    datos = cursor.fetchone()
    if not datos:
        messagebox.showerror("Datos no encontrados", "Los datos no existen.")
        return
    Estado_Original, Fecha_Original, Descripcion_Original, Afectados_Original, Desastre_Original, Departamento_Original, Tipo_Original = datos
    Desastre_Convertido = Desastres_Valores2.get(Desastre_Original)
    Estado_Convertido = Estados_Valores2.get(Estado_Original)
    Departamento_Convertido = Departamento_Valores2.get(Departamento_Original)
    Fecha_Formateada = Fecha_Original.strftime("%d/%m/%Y")
    Cerrar_Base_De_Datos()
def Funcion_Cargar_Datos_Usuarios():
    global Identificacion, Documento_Normal, TipoDocumento_Convertido, PrimerNombre_Normal, SegundoNombre_Normal, PrimerApellido_Normal, SegundoApellido_Normal, NombreUsuario_Normal, RolUsuario_Normal, EstadoUsuario_Normal, Departamento_Normal, Ciudad_Normal, Localidad_Normal, Barrio_Normal, Direccion_Normal, FechaNacimento_Normal, Edad_Normal, Telefono_Normal, Email_Normal, Rol_Convertido, Estado_Convertido, Nacimiento_Formateada
    Conexion_Base_De_Datos()
    Identificacion = Entrada_Usuario_Identificacion.get()
    cursor.execute("SELECT tbl_usuario.Id_usuario FROM tbl_usuario JOIN tbl_persona ON tbl_persona.fk_usuario = tbl_usuario.Id_usuario WHERE tbl_persona.Id_Persona = %s", (Identificacion,))
    resultado = cursor.fetchone()
    if not resultado:
        messagebox.showerror("Usuario no encontrado", "La identificación no existe.")
        return
    id_usuario = resultado[0]
    cursor.execute("SELECT fk_estado FROM tbl_usuario WHERE Id_usuario = %s", (id_usuario,))
    resultado_estado = cursor.fetchone()
    if not resultado_estado:
        messagebox.showerror("Error", "No se encontró el Usuario.")
        Cerrar_Base_De_Datos()
        return
    Estado_Actual = resultado_estado[0]
    if Estado_Actual == "Usuario_00":
        messagebox.showerror("Usuario no encontrado", "El usuario no existe.")
        Cerrar_Base_De_Datos()
        return
    cursor.execute("""
                SELECT 
                    tbl_persona.Id_Persona,
                    tbl_persona.fk_Tipo_documento,
                    tbl_persona.Pri_Nom,
                    tbl_persona.Seg_Nom,
                    tbl_persona.Pri_Ape,
                    tbl_persona.Seg_Ape,
                    tbl_usuario.Nombre,
                    tbl_usuario.fk_rol,
                    tbl_usuario.fk_estado,
                    tbl_departamento.Nom_departamento,
                    tbl_ciudad.Nom_ciudad,
                    tbl_localidad.Localidad,
                    tbl_barrio.Barrio,
                    tbl_adic_persona.Dirección,
                    tbl_persona.Fecha_nacimiento,
                    tbl_adic_persona.Edad,
                    tbl_adic_persona.Num_Contact,
                    tbl_adic_persona.Email
                FROM tbl_adic_persona 
                JOIN tbl_persona ON tbl_adic_persona.fk_persona = tbl_persona.Id_persona
                JOIN tbl_tipo_documento ON tbl_persona.fk_Tipo_documento = tbl_tipo_documento.Id_Documento 
                JOIN tbl_usuario ON tbl_persona.fk_usuario = tbl_usuario.Id_usuario 
                JOIN tbl_barrio ON tbl_adic_persona.fk_dir = tbl_barrio.Id_barrio
                JOIN tbl_localidad ON tbl_barrio.fk_local = tbl_localidad.Id_local
                JOIN tbl_ciudad ON tbl_localidad.fk_ciudad = tbl_ciudad.Id_ciudad
                JOIN tbl_departamento ON tbl_ciudad.Fk_Dep = tbl_departamento.Id_dep
                WHERE tbl_usuario.Id_usuario = %s
                """, (id_usuario,))
    datos = cursor.fetchone()
    if not datos:
        messagebox.showerror("Datos no encontrados", "Los datos no existen.")
        return
    if datos:
      messagebox.showinfo("Éxito", f"Usuario encontrado.\n Numero de usuario: {id_usuario}")
    Documento_Normal, TipoDocumento_Normal, PrimerNombre_Normal, SegundoNombre_Normal, PrimerApellido_Normal, SegundoApellido_Normal, NombreUsuario_Normal, RolUsuario_Normal, EstadoUsuario_Normal, Departamento_Normal, Ciudad_Normal, Localidad_Normal, Barrio_Normal, Direccion_Normal, FechaNacimento_Normal, Edad_Normal, Telefono_Normal, Email_Normal = datos
    Estado_Convertido = Estados_Valores2.get(EstadoUsuario_Normal)
    Rol_Convertido = Rol_Valores2.get(RolUsuario_Normal)
    Nacimiento_Formateada = FechaNacimento_Normal.strftime("%d/%m/%Y")
    TipoDocumento_Convertido = Tipo_Documento_Valores.get(TipoDocumento_Normal)

    Cerrar_Base_De_Datos()
    Grafico_Admin_Modificar_Usuarios()
def Funcion_Modificar_Contactos_Usuario():
    global Contador, Max_Intentos, Intentos_Restantes
    Conexion_Base_De_Datos()
    Correo_Listo = Entrada_Usuario_Datos_Correo.get()
    Telefono_Listo = Entrada_Usuario_Datos_Telefono.get()
    Direccion_Listo = Entrada_Usuario_Datos_Direccion.get()
    Tipo_Listo = Entrada_Usuario_Datos_Tipo.get()
    Tipo_Convertido = Tipo_Documento_Valores2.get(Tipo_Listo)
    Contraseña = Entrada_Contraseña.get()
    if not all([Correo_Listo, Telefono_Listo, Direccion_Listo, Tipo_Convertido, Contraseña]):
        messagebox.showerror("Error", "Todos los campos deben estar rellenados")
        Cerrar_Base_De_Datos()
        return
    if not re.match(r"[^@]+@[^@]+\.[^@]+", Correo_Listo):
        messagebox.showerror("Error", "Correo inválido")
        Cerrar_Base_De_Datos()
        return
    if not Telefono_Listo.isdigit() or len(Telefono_Listo) != 10:
        messagebox.showerror("Error", "El teléfono debe tener 10 dígitos")
        Cerrar_Base_De_Datos()
        return
    cursor.execute("SELECT * FROM tbl_usuario WHERE Nombre = %s AND Contraseña = %s", (Usuario, Contraseña))
    resultado_contraseña = cursor.fetchone()
    if not resultado_contraseña:
        Contador += 1
        Intentos_Restantes = Max_Intentos - Contador
        if Intentos_Restantes > 0:
            messagebox.showerror("Contraseña incorrecta", f"La contraseña es incorrecta. Intentos restantes: {Intentos_Restantes}")
            return
        else:
            messagebox.showerror("Acceso denegado", "Has superado el número máximo de intentos.")
            root.quit()
    try:
        if not conexion.in_transaction:
            conexion.start_transaction()

        cursor.execute("UPDATE tbl_adic_persona SET Email = %s WHERE fk_persona = %s", (Correo_Listo, id_persona))
        cursor.execute("UPDATE tbl_adic_persona SET Num_Contact = %s WHERE fk_persona = %s", (Telefono_Listo, id_persona))
        cursor.execute("UPDATE tbl_adic_persona SET Dirección = %s WHERE fk_persona = %s", (Direccion_Listo, id_persona))
        cursor.execute("UPDATE tbl_persona SET fk_Tipo_documento = %s WHERE fk_usuario = %s", (Tipo_Convertido, id_usuario))

        conexion.commit()
        messagebox.showinfo("Éxito", "Usuario y datos asociados actualizados correctamente.")
    except mysql.connector.Error as err:
        conexion.rollback()
        messagebox.showerror("Error", f"Ocurrió un error al guardar los datos: {err}")
    finally:
        Conseguir_Correo()
        mensaje = MIMEMultipart()
        mensaje["From"] = correo_emisor
        mensaje["To"] = correo_receptor2
        mensaje["Subject"] = f"Estimado/a {Usuario}"
        cuerpo = "Queremos informarte que tus datos han sido cambiados exitosamente en nuestro sistema.\nSi no realizaste este cambio, te pedimos que te pongas en contacto con nuestro soporte técnico\nlo más pronto posible para asegurar la seguridad de tu cuenta.\nSi necesitas asistencia adicional, no dudes en escribirnos.\n\nAtentamente,El equipo de soporte de Right way sys"
        mensaje.attach(MIMEText(cuerpo, "plain"))
        try:
            servidor = smtplib.SMTP("smtp.gmail.com", 587)
            servidor.starttls()
            servidor.login(correo_emisor, contraseña)
            servidor.sendmail(correo_emisor, correo_receptor2, mensaje.as_string())
            servidor.quit()
            print("Correo enviado exitosamente")
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
        Entrada_Usuario_Datos_Correo.place_forget()
        Entrada_Usuario_Datos_Correo_Check.place_forget()
        Entrada_Usuario_Datos_Telefono.place_forget()
        Entrada_Usuario_Datos_Telefono_Check.place_forget()
        Entrada_Usuario_Datos_Direccion.place_forget()
        Entrada_Usuario_Datos_Direccion_Check.place_forget()
        Entrada_Usuario_Datos_Tipo.place_forget()
        Entrada_Usuario_Datos_Tipo_Check.place_forget()
        Boton_Funcion_Modificar_Datos_Usuario.place_forget()
        Boton_Salir.place_forget()
        Grafico_Usuario_Cuenta()
        Cerrar_Base_De_Datos()
def Funcion_Modificar_Datos_Usuarios():
    global Contador, Max_Intentos, Intentos_Restantes
    Conexion_Base_De_Datos()

    Documento_Normal = Entrada_Usuario_Modificar_Documento.get()
    TipoIdentificacion_Medio = Entrada_Usuario_Modificar_TipoIdentificacion.get()
    TipoIdentificacion_Normal = Tipo_Documento_Valores2.get(TipoIdentificacion_Medio)
    PrimerNombre_Normal = Entrada_Usuario_Modificar_PrimerNombre.get()
    SegundoNombre_Normal = Entrada_Usuario_Modificar_SegundoNombre.get()
    PrimerApellido_Normal = Entrada_Usuario_Modificar_PrimerApellido.get()
    SegundoApellido_Normal = Entrada_Usuario_Modificar_SegundoApellido.get()
    NombreUsuario_Normal = Entrada_Usuario_Modificar_NombreUsuario.get()
    RolUsuario_Medio = Entrada_Usuario_Modificar_RolUsuario.get()
    EstadoUsuario_Medio = Entrada_Usuario_Modificar_EstadoUsuario.get()
    Departamento_Normal = Entrada_Usuario_Modificar_Departamento_Normal.get()
    RolUsuario_Normal = Rol_Valores.get(RolUsuario_Medio)
    EstadoUsuario_Normal = Estados_Valores.get(EstadoUsuario_Medio)
    Ciudad_Normal = Entrada_Usuario_Modificar_Ciudad.get()
    Localidad_Normal = Entrada_Usuario_Modificar_Localidad.get()
    Barrio_Normal = Entrada_Usuario_Modificar_Barrio.get()
    Direccion_Normal = Entrada_Usuario_Modificar_Direccion.get()
    Nacimiento_Normal = Entrada_Caso_Nacimiento.get_date()
    Telefono_Normal = Entrada_Usuario_Modificar_Telefono.get()
    Email_Normal = Entrada_Usuario_Modificar_Email.get()
    Contraseña = Entrada_Contraseña.get()

    if not all([Documento_Normal, PrimerNombre_Normal , SegundoNombre_Normal , PrimerApellido_Normal , SegundoApellido_Normal , NombreUsuario_Normal , Ciudad_Normal , Localidad_Normal , Barrio_Normal , Direccion_Normal , Telefono_Normal , Email_Normal , Contraseña]):
        messagebox.showerror("Error", "Todos los campos deben estar rellenados")
        Cerrar_Base_De_Datos()
        return
    if not Documento_Normal.isdigit() or not (8 <= len(Documento_Normal) <= 10):
        messagebox.showerror("Error", "El documento debe tener entre 8 a 10 digitos")
        Cerrar_Base_De_Datos()
        return
    if not re.match(r"[^@]+@[^@]+\.[^@]+", Email_Normal):
        messagebox.showerror("Error", "Correo inválido")
        Cerrar_Base_De_Datos()
        return
    if not Telefono_Normal.isdigit() or len(Telefono_Normal) != 10:
        messagebox.showerror("Error", "El teléfono debe tener 10 dígitos")
        Cerrar_Base_De_Datos()
        return
    cursor.execute("SELECT tbl_usuario.Id_usuario FROM tbl_usuario JOIN tbl_persona ON tbl_persona.fk_usuario = tbl_usuario.Id_usuario WHERE tbl_persona.Id_Persona = %s", (Identificacion,))
    resultado = cursor.fetchone()
    if not resultado:
        messagebox.showerror("Usuario no encontrado", "La identificación no existe.")
        return
    id_usuario = resultado[0]
    cursor.execute("SELECT Id_Persona FROM tbl_persona WHERE fk_usuario = %s", (id_usuario,))
    resultado2 = cursor.fetchone()
    if not resultado2:
        messagebox.showerror("Persona no encontrada", "El número de la persona no existe.")
        return
    id_persona = resultado2[0]
    cursor.execute("SELECT Id_barrio FROM tbl_barrio WHERE Barrio = %s", (Barrio_Normal,))
    resultado_barrio = cursor.fetchone()
    if not resultado_barrio:
        messagebox.showerror("Error", f"El barrio '{Barrio_Normal}' no existe en la base de datos.")
        Cerrar_Base_De_Datos()
        return
    id_barrio = resultado_barrio[0]

    cursor.execute("SELECT Id_local FROM tbl_localidad WHERE Localidad = %s", (Localidad_Normal,))
    resultado_localidad = cursor.fetchone()
    if not resultado_localidad:
        messagebox.showerror("Error", f"La localidad '{Localidad_Normal}' no existe en la base de datos.")
        Cerrar_Base_De_Datos()
        return
    id_localidad = resultado_localidad[0]

    cursor.execute("SELECT Id_ciudad FROM tbl_ciudad WHERE Nom_ciudad = %s", (Ciudad_Normal,))
    resultado_ciudad = cursor.fetchone()
    if not resultado_ciudad:
        messagebox.showerror("Error", f"La ciudad '{Ciudad_Normal}' no existe en la base de datos.")
        Cerrar_Base_De_Datos()
        return
    id_ciudad = resultado_ciudad[0]

    cursor.execute("SELECT * FROM tbl_usuario WHERE Nombre = %s AND Contraseña = %s", (Usuario, Contraseña))
    resultado_contraseña = cursor.fetchone()
    if not resultado_contraseña:
        Contador += 1
        Intentos_Restantes = Max_Intentos - Contador
        if Intentos_Restantes > 0:
            messagebox.showerror("Contraseña incorrecta", f"La contraseña es incorrecta. Intentos restantes: {Intentos_Restantes}")
            return
        else:
            messagebox.showerror("Acceso denegado", "Has superado el número máximo de intentos.")
            root.quit()
    try:
        if not conexion.in_transaction:
            conexion.start_transaction()
        cursor.execute("UPDATE tbl_usuario SET Nombre = %s, Contraseña = %s, fk_estado = %s, fk_rol = %s WHERE Id_usuario = %s",(NombreUsuario_Normal, Contraseña, EstadoUsuario_Normal, RolUsuario_Normal, id_usuario))

        cursor.execute("UPDATE tbl_persona SET fk_Tipo_documento = %s, Id_Persona = %s, Pri_Nom = %s, Seg_Nom = %s, Pri_Ape = %s, Seg_Ape = %s, Fecha_nacimiento = %s WHERE fk_usuario = %s",(TipoIdentificacion_Normal, Documento_Normal, PrimerNombre_Normal, SegundoNombre_Normal, PrimerApellido_Normal, SegundoApellido_Normal, Nacimiento_Normal, id_usuario))

        cursor.execute("UPDATE tbl_adic_persona SET Email = %s, Num_Contact = %s, Dirección = %s, fk_dir = %s WHERE fk_persona = %s",(Email_Normal, Telefono_Normal, Direccion_Normal, id_barrio, id_persona))

        conexion.commit()   
        messagebox.showinfo("Éxito", "Usuario y datos asociados actualizados correctamente.")
    except mysql.connector.Error as err:
        conexion.rollback()
        messagebox.showerror("Error", f"Ocurrió un error al guardar los datos: {err}")
    finally:
        Olvidar_Lugares()
        Entrada_Usuario_Modificar_Documento.place_forget()
        Entrada_Usuario_Modificar_Documento_Check.place_forget()
        Entrada_Usuario_Modificar_TipoIdentificacion.place_forget()
        Entrada_Usuario_Modificar_TipoIdentificacion_Check.place_forget()
        Entrada_Usuario_Modificar_PrimerNombre.place_forget()
        Entrada_Usuario_Modificar_PrimerNombre_Check.place_forget()
        Entrada_Usuario_Modificar_SegundoNombre.place_forget()
        Entrada_Usuario_Modificar_SegundoNombre_Check.place_forget()
        Entrada_Usuario_Modificar_PrimerApellido.place_forget()
        Entrada_Usuario_Modificar_PrimerApellido_Check.place_forget()
        Entrada_Usuario_Modificar_SegundoApellido.place_forget()
        Entrada_Usuario_Modificar_SegundoApellido_Check.place_forget()
        Entrada_Usuario_Modificar_NombreUsuario.place_forget()
        Entrada_Usuario_Modificar_NombreUsuario_Check.place_forget()
        Entrada_Usuario_Modificar_RolUsuario.place_forget()
        Entrada_Usuario_Modificar_RolUsuario_Check.place_forget()
        Entrada_Usuario_Modificar_EstadoUsuario.place_forget()
        Entrada_Usuario_Modificar_EstadoUsuario_Check.place_forget()
        Entrada_Usuario_Modificar_Departamento_Normal.place_forget()
        Entrada_Usuario_Modificar_Departamento_Normal_Check.place_forget()
        Entrada_Usuario_Modificar_Ciudad.place_forget()
        Entrada_Usuario_Modificar_Ciudad_Check.place_forget()
        Entrada_Usuario_Modificar_Localidad.place_forget()
        Entrada_Usuario_Modificar_Localidad_Check.place_forget()
        Entrada_Usuario_Modificar_Barrio.place_forget()
        Entrada_Usuario_Modificar_Barrio_Check.place_forget()
        Entrada_Usuario_Modificar_Direccion.place_forget()
        Entrada_Usuario_Modificar_Direccion_Check.place_forget()
        Entrada_Caso_Nacimiento.place_forget()
        Entrada_Caso_Nacimiento_Check.place_forget()
        Entrada_Usuario_Modificar_Telefono.place_forget()
        Entrada_Usuario_Modificar_Telefono_Check.place_forget()
        Entrada_Usuario_Modificar_Email.place_forget()
        Entrada_Usuario_Modificar_Email_Check.place_forget()
        Boton_Funcion_Modificar_Datos_Usuario.place_forget()
        Boton_Admin_Volver3.place_forget()
        Boton_Salir.place_forget()
        Grafico_Admin_Usuarios()
        Cerrar_Base_De_Datos()
def Funcion_Modificar_Datos_Casos():
    global Contador, Max_Intentos, Intentos_Restantes
    Conexion_Base_De_Datos()
    Departamento_Medio = Entrada_Caso_Departamento.get()
    Departamento_Listo = Departamento_Valores.get(Departamento_Medio)
    Descripcion_Listo = Entrada_Caso_Descripcion2.get()
    Fecha_Listo = Entrada_Caso_Fecha.get_date()
    Afectados_Listo = Entrada_Caso_Afectados.get()
    Estado_Mitad = Entrada_Caso_Estado.get()
    Estado_Listo = Estados_Valores.get(Estado_Mitad)
    Desastre_Mitad = Entrada_Caso_Desastre.get()
    Desastre_Listo = Desastres_Valores.get(Desastre_Mitad)
    Tipo_Listo = Entrada_Caso_Tipo.get()
    Contraseña = Entrada_Contraseña.get()
    if not all([Contraseña]):
        messagebox.showerror("Error", "la contraseña es obligatoria")
        Cerrar_Base_De_Datos()
        return
    if not all([Entrada_Caso_Descripcion2.get(), Entrada_Caso_Fecha.get()]):
        messagebox.showerror("Error", "Todos los campos deben estar rellenados")
        Cerrar_Base_De_Datos()
        return
    cursor.execute("SELECT * FROM tbl_usuario WHERE Nombre = %s AND Contraseña = %s", (Usuario, Contraseña))
    resultado_contraseña = cursor.fetchone()
    if not resultado_contraseña:
        Contador += 1
        Intentos_Restantes = Max_Intentos - Contador
        if Intentos_Restantes > 0:
            messagebox.showerror("Contraseña incorrecta", f"La contraseña es incorrecta. Intentos restantes: {Intentos_Restantes}")
            return
        else:
            messagebox.showerror("Acceso denegado", "Has superado el número máximo de intentos.")
            root.quit()
    try:
        if not conexion.in_transaction:
            conexion.start_transaction()

        cursor.execute("UPDATE tbl_caso JOIN tbl_num_caso ON tbl_caso.Id_Caso_Desastre = tbl_num_caso.Fk_Caso SET Fk_Estado = %s WHERE Radicado = %s", (Estado_Listo, Radicado))
        cursor.execute("UPDATE tbl_caso JOIN tbl_num_caso ON tbl_caso.Id_Caso_Desastre = tbl_num_caso.Fk_Caso SET Fecha = %s WHERE Radicado = %s", (Fecha_Listo, Radicado))
        cursor.execute("UPDATE tbl_caso JOIN tbl_num_caso ON tbl_caso.Id_Caso_Desastre = tbl_num_caso.Fk_Caso SET Descripción = %s WHERE Radicado = %s", (Descripcion_Listo, Radicado))
        cursor.execute("UPDATE tbl_caso JOIN tbl_num_caso ON tbl_caso.Id_Caso_Desastre = tbl_num_caso.Fk_Caso SET Personas_Afectadas = %s WHERE Radicado = %s", (Afectados_Listo, Radicado))
        cursor.execute("UPDATE tbl_caso JOIN tbl_num_caso ON tbl_caso.Id_Caso_Desastre = tbl_num_caso.Fk_Caso SET Fk_Desastre = %s WHERE Radicado = %s", (Desastre_Listo, Radicado))
        cursor.execute("UPDATE tbl_caso JOIN tbl_num_caso ON tbl_caso.Id_Caso_Desastre = tbl_num_caso.Fk_Caso SET Fk_Dep = %s WHERE Radicado = %s", (Departamento_Listo, Radicado))
        cursor.execute("UPDATE tbl_caso JOIN tbl_num_caso ON tbl_caso.Id_Caso_Desastre = tbl_num_caso.Fk_Caso SET Fk_Tipo_Caso = %s WHERE Radicado = %s", (Tipo_Listo, Radicado))

        conexion.commit()
        messagebox.showinfo("Éxito", "Usuario y datos asociados actualizados correctamente.")
    except mysql.connector.Error as err:
        conexion.rollback()
        messagebox.showerror("Error", f"Ocurrió un error al guardar los datos: {err}")
        return
    finally:
        Entrada_Caso_Departamento.place_forget()
        Entrada_Caso_Descripcion2.place_forget()
        Entrada_Caso_Fecha.place_forget()
        Entrada_Caso_Departamento.place_forget()
        Entrada_Caso_Estado.place_forget()
        Entrada_Caso_Desastre.place_forget()
        Entrada_Caso_Tipo.place_forget()
        Entrada_Caso_Departamento_Check.place_forget()
        Entrada_Caso_Descripcion2_Check.place_forget()
        Entrada_Caso_Fecha_Check.place_forget()
        Entrada_Caso_Departamento_Check.place_forget()
        Entrada_Caso_Estado_Check.place_forget()
        Entrada_Caso_Desastre_Check.place_forget()
        Entrada_Caso_Afectados.place_forget()
        Entrada_Caso_Afectados_Check.place_forget()
        Entrada_Caso_Tipo_Check.place_forget()
        Boton_Funcion_Modificar_Datos_Caso.place_forget()
        Boton_Admin_Volver2.place_forget()
        Boton_Salir.place_forget()
        Grafico_Admin_Casos()
        Cerrar_Base_De_Datos()
def Funcion_Cargar_GPS():
    Conexion_Base_De_Datos()
    cursor.execute("SELECT Barrio FROM tbl_barrio")
    lista_barrios = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT Localidad FROM tbl_localidad")
    lista_localidades = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT Nom_ciudad FROM tbl_ciudad")
    lista_ciudades = [row[0] for row in cursor.fetchall()]

    Cerrar_Base_De_Datos()

    return lista_barrios, lista_localidades, lista_ciudades
def Funcion_Eliminar_Datos_Casos():
    global Contador, Max_Intentos
    Conexion_Base_De_Datos()
    Estado = "Caso_03"
    Contraseña = Entrada_Contraseña.get()
    Radicado = Entrada_Caso_Radicado.get()
    cursor.execute("SELECT radicado FROM tbl_num_caso WHERE Radicado = %s", (Radicado,))
    resultado_radicado = cursor.fetchone()
    if not resultado_radicado:
        messagebox.showerror("Error", "No se encontró el numero de radicado.")
        Cerrar_Base_De_Datos()
        return
    cursor.execute("SELECT * FROM tbl_usuario WHERE Nombre = %s AND Contraseña = %s", (Usuario, Contraseña))
    resultado_contraseña = cursor.fetchone()
    if not resultado_contraseña:
        Contador += 1
        Intentos_Restantes = Max_Intentos - Contador
        if Intentos_Restantes > 0:
            messagebox.showerror("Contraseña incorrecta", f"La contraseña es incorrecta. Intentos restantes: {Intentos_Restantes}")
            return
        else:
            messagebox.showerror("Acceso denegado", "Has superado el número máximo de intentos.")
            root.quit()
    cursor.execute("SELECT tbl_caso.Fk_Estado FROM tbl_num_caso JOIN tbl_caso ON tbl_num_caso.Fk_Caso = tbl_caso.Id_Caso_Desastre WHERE tbl_num_caso.Radicado = %s", (Radicado,))
    resultado_estado = cursor.fetchone()
    if not resultado_estado:
        messagebox.showerror("Error", "No se encontró el estado del de radicado.")
        Cerrar_Base_De_Datos()
        return
    Estado_Actual = resultado_estado[0]
    if Estado_Actual == "Caso_03":
        messagebox.showerror("Error", "El numero de radicado no existe.")
        return
    confirmar = messagebox.askyesno("Confirmar eliminación", f"¿Estás seguro que deseas eliminar el caso con radicado {Radicado}?")
    if not confirmar:
        messagebox.showinfo("Cancelado", "La operación fue cancelada.")
        Cerrar_Base_De_Datos()
        return
    try:
        if not conexion.in_transaction:
            conexion.start_transaction()

        cursor.execute("UPDATE tbl_caso JOIN tbl_num_caso ON tbl_caso.Id_Caso_Desastre = tbl_num_caso.Fk_Caso SET Fk_Estado = %s WHERE Radicado = %s", (Estado, Radicado))

        conexion.commit()
        messagebox.showinfo("Éxito", "Caso y datos asociados actualizados correctamente.")
        Contador = 0
    except mysql.connector.Error as err:
        conexion.rollback()
        messagebox.showerror("Error", f"Ocurrió un error al guardar los datos: {err}")
        return
    finally:
        Grafico_Admin_Casos()
        Cerrar_Base_De_Datos()
def Funcion_Eliminar_Usuario():
    global Contador, Max_Intentos
    Conexion_Base_De_Datos()
    Estado = "Usuario_00"
    Contraseña = Entrada_Contraseña.get()
    Identificacion = Entrada_Usuario_Identificacion.get()

    cursor.execute("SELECT Pri_Nom FROM tbl_persona WHERE Id_Persona = %s", (Identificacion,))
    resultado_Nombre = cursor.fetchone()
    if not resultado_Nombre:
        messagebox.showerror("Error", "No se encontró el numero de Identificacion.")
        Cerrar_Base_De_Datos()
        return
    Nombre = resultado_Nombre[0]

    cursor.execute("SELECT fk_Usuario FROM tbl_persona WHERE Id_Persona = %s", (Identificacion,))
    resultado_Identificacion = cursor.fetchone()
    if not resultado_Identificacion:
        messagebox.showerror("Error", "No se encontró el numero de Identificacion.")
        Cerrar_Base_De_Datos()
        return
    Id_Usuario = resultado_Identificacion[0]

    cursor.execute("SELECT fk_estado FROM tbl_usuario WHERE Id_usuario = %s", (Id_Usuario,))
    resultado_estado = cursor.fetchone()
    if not resultado_estado:
        messagebox.showerror("Error", "No se encontró el numero de Identificacion.")
        Cerrar_Base_De_Datos()
        return
    Estado_Actual = resultado_estado[0]

    cursor.execute("SELECT * FROM tbl_usuario WHERE Nombre = %s AND Contraseña = %s", (Usuario, Contraseña))
    resultado_contraseña = cursor.fetchone()
    if not resultado_contraseña:
        Contador += 1
        Intentos_Restantes = Max_Intentos - Contador
        if Intentos_Restantes > 0:
            messagebox.showerror("Contraseña incorrecta", f"La contraseña es incorrecta. Intentos restantes: {Intentos_Restantes}")
            return
        else:
            messagebox.showerror("Acceso denegado", "Has superado el número máximo de intentos.")
            root.quit()
    if Estado_Actual == "Usuario_00":
        messagebox.showerror("Error", "El numero de identificacion no existe.")
        return
    confirmar = messagebox.askyesno("Confirmar eliminación", f"¿Estás seguro que deseas eliminar el usuario con identificacion {Identificacion}?")
    if not confirmar:
        messagebox.showinfo("Cancelado", "La operación fue cancelada.")
        Cerrar_Base_De_Datos()
        return
    try:
        if not conexion.in_transaction:
            conexion.start_transaction()

        cursor.execute("UPDATE tbl_usuario SET fk_estado = %s WHERE Id_usuario = %s", (Estado, Id_Usuario))
        conexion.commit()
        messagebox.showinfo("Éxito", "Usuario y datos asociados actualizados correctamente.")
        Contador = 0
    except mysql.connector.Error as err:
        conexion.rollback()
        messagebox.showerror("Error", f"Ocurrió un error al guardar los datos: {err}")
        return
    finally:
        cursor.execute("SELECT tbl_adic_persona.Email FROM tbl_adic_persona JOIN tbl_persona ON tbl_adic_persona.fk_persona = tbl_persona.Id_persona JOIN tbl_tipo_documento ON tbl_persona.fk_Tipo_documento = tbl_tipo_documento.Id_Documento JOIN tbl_usuario ON tbl_persona.fk_usuario = tbl_usuario.Id_usuario WHERE tbl_usuario.Id_usuario = %s", (Id_Usuario,))
        resultado_Correo = cursor.fetchone()
        if not resultado_Correo:
            messagebox.showerror("Error", "No se encontró el numero de Identificacion.")
            Cerrar_Base_De_Datos()
            return
        Correo = resultado_Correo[0]
        mensaje = MIMEMultipart()
        mensaje["From"] = correo_emisor
        mensaje["To"] = Correo
        mensaje["Subject"] = f"Estimado/a {Nombre}"
        cuerpo = f"Queremos informarte que un administrador ha eliminado tu usuario con identificación {Identificacion} de nuestro sistema.\nSi no fuiste tú quien solicitó esta acción, por favor comunícate de inmediato con nuestro equipo de soporte para garantizar la seguridad de tu cuenta.\nSi necesitas asistencia adicional, no dudes en escribirnos.\n\nAtentamente,El equipo de soporte de Right way sys"
        mensaje.attach(MIMEText(cuerpo, "plain"))
        try:
            servidor = smtplib.SMTP("smtp.gmail.com", 587)
            servidor.starttls()
            servidor.login(correo_emisor, contraseña)
            servidor.sendmail(correo_emisor, Correo, mensaje.as_string())
            servidor.quit()
            print(f"Correo del usuario: {Correo}")
            print("Correo enviado exitosamente")
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
        Grafico_Admin_Usuarios()
        Cerrar_Base_De_Datos()
def Olvidar_Lugares():
# Botones generales y usuario
    Boton_Salir.place_forget()
    Boton_Funcion_Buscar_Caso2.place_forget()
    Boton_Funcion_Modificar_Datos_Usuario.place_forget()
    Boton_Funcion_Buscar_Usuario2.place_forget()
    Boton_Usuario_Casos_Grafico_Buscar.place_forget()
    Boton_Usuario_Volver.place_forget()
    Boton_Volver.place_forget()
    Boton_Funcion_Recuperar_Contraseña.place_forget()
    Boton_Inicio_Login.place_forget()
    Boton_Inicio_Crear_Usuario.place_forget()
    Boton_Funcion_Crear_Usuario2.place_forget()
    Boton_Funcion_Buscar_Usuario.place_forget()
    Boton_Funcion_Eliminar_Caso.place_forget()
    Boton_Funcion_Eliminar_Usuario.place_forget()
    Boton_Inicio_Recuperar.place_forget()
    Boton_Funcion_Login.place_forget()
    Boton_Funcion_Crear_Usuario.place_forget()
    Boton_Usuario_Casos.place_forget()
    Boton_Funcion_Buscar_Caso.place_forget()
    Boton_Usuario_Cuenta.place_forget()
    Boton_Funcion_Crear_Caso.place_forget()
    Boton_Usuario_Casos_Grafico_Volver_Buscar.place_forget()
    Boton_Funcion_Modificar_Datos_Usuario5.place_forget()
    Boton_Usuario_Casos_Grafico_Crear.place_forget()
    Boton_Usuario_Cuenta_Modificar_Contraseña.place_forget()
    Boton_Usuario_Cuenta_Modificar_Datos.place_forget()
    Boton_Funcion_Cuenta_Modificar_Contraseña.place_forget()
    Boton_Usuario_Casos_Volver.place_forget()
    Boton_Pagina.place_forget()
    Boton_Funcion_Recuperar_Contraseña2.place_forget()

# Botones Admin generales
    Boton_Admin_Usuarios.place_forget()
    Boton_Admin_Casos.place_forget()
    Boton_Admin_Entidades.place_forget()
    Boton_Admin_Volver.place_forget()
    Boton_Admin_Volver_Casos.place_forget()
    Boton_Admin_Volver_Usuarios.place_forget()
    Boton_Funcion_Modificar_Datos_Caso.place_forget()

# Botones Admin gráficos
    Boton_Admin_Grafico_Usuarios_Buscar.place_forget()
    Boton_Admin_Grafico_Usuarios_Crear.place_forget()
    Boton_Admin_Grafico_Usuarios_Modificar.place_forget()
    Boton_Admin_Grafico_Usuarios_Eliminar.place_forget()
    Boton_Admin_Grafico_Casos_Buscar.place_forget()
    Boton_Admin_Grafico_Casos_Crear.place_forget()
    Boton_Admin_Grafico_Casos_Modificar.place_forget()
    Boton_Admin_Grafico_Casos_Eliminar.place_forget()

# Entradas
    Entrada_UUID.place_forget()
    Entrada_Caso_Radicado.place_forget()
    Entrada_Usuario_Identificacion.place_forget()
    Entrada_Usuario.place_forget()
    Entrada_Contraseña.place_forget()
    Entrada_Contraseña_Nueva.place_forget()
    Entrada_Primer_Nombre.place_forget()
    Entrada_Segundo_Nombre.place_forget()
    Entrada_Primer_Apellido.place_forget()
    Entrada_Segundo_Apellido.place_forget()
    Entrada_Documento.place_forget()
    Entrada_Tipo_Documento.place_forget()
    Entrada_Fecha_Nacimento.place_forget()
    Entrada_Direccion.place_forget()
    Entrada_Numero.place_forget()
    Entrada_Email.place_forget()
    Entrada_Ciudad.place_forget()
    Entrada_Departamento.place_forget()
    Entrada_Barrio.place_forget()
    Entrada_Localidad.place_forget()
    Entrada_Usuario_Nueva.place_forget()

# Entradas tipo Text y Combobox específicos
    Entrada_Caso_Descripcion.place_forget()
    Entrada_Caso_Personas.place_forget()
    Entrada_Caso_Direccion.place_forget()
    Entrada_Caso_Fecha.place_forget()
    Entrada_Caso_TipoDesastre.place_forget()

# Imágenes
    Imagen_Grafico_Usuario_Datos_Documento.place_forget()
    Imagen_Grafico_Usuario_Datos_Correo.place_forget()
    Imagen_Grafico_Usuario_Datos_Telefono.place_forget()
    Imagen_Grafico_Usuario_Datos_Direccion.place_forget()
    Imagen_Grafico_Login_Usuario.place_forget()
    Imagen_Grafico_Login_Contraseña.place_forget()
    Imagen_Grafico_Modificar_Contraseña.place_forget()

# Textos (labels, mensajes, etc)
    Texto1.place_forget()
    Texto2.place_forget()
    Texto3.place_forget()
    Texto4.place_forget()
    Texto5.place_forget()
    Texto6.place_forget()
    Texto7.place_forget()
    Texto8.place_forget()
    Texto9.place_forget()
    Texto10.place_forget()
    Texto11.place_forget()
    Texto12.place_forget()
    Texto13.place_forget()
    Texto14.place_forget()
    Texto15.place_forget()
    Texto16.place_forget()
    Texto17.place_forget()
    Texto18.place_forget()
    Texto19.place_forget()
    Texto20.place_forget()
    Texto21.place_forget()
    Texto22.place_forget()
    Texto23.place_forget()
    Texto24.place_forget()
    Texto25.place_forget()
    Texto26.place_forget()
    Texto27.place_forget()
    Texto28.place_forget()
    Texto29.place_forget()
    Texto30.place_forget()
    Texto31.place_forget()
    Texto32.place_forget()
    Texto33.place_forget()
    Texto34.place_forget()
    Texto35.place_forget()
    Texto36.place_forget()
    Texto37.place_forget()
    Texto38.place_forget()

# Limpieza de campos (delete y set)
    Entrada_Caso_Direccion.delete(0, END)
    Entrada_Caso_Radicado.delete(0, END)
    Entrada_Contraseña_Nueva.delete(0, END)
    Entrada_Usuario_Nueva.delete(0, END)
    Entrada_Primer_Nombre.delete(0, END)
    Entrada_Usuario_Identificacion.delete(0, END)
    Entrada_Segundo_Nombre.delete(0, END)
    Entrada_Primer_Apellido.delete(0, END)
    Entrada_Segundo_Apellido.delete(0, END)
    Entrada_Documento.delete(0, END)
    Entrada_Email.delete(0, END)
    Entrada_Ciudad.delete(0, END)
    Entrada_Localidad.delete(0, END)
    Entrada_Barrio.delete(0, END)
    Entrada_Direccion.delete(0, END)
    Entrada_Numero.delete(0, END)
    Entrada_Usuario.delete(0, END)
    Entrada_Contraseña.delete(0, END)
    Entrada_Tipo_Documento.set("Seleccion")
    Entrada_Departamento.set("Seleccion")
    Entrada_Caso_Descripcion.delete("1.0", "end")
    Entrada_Caso_Personas.set("Seleccion")
    Entrada_Caso_TipoDesastre.set("Seleccion")
def Grafico_Inicio():
    Olvidar_Lugares()
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Inicio_Login.place(relx=0.5, rely=0.49, anchor="center")
    Boton_Inicio_Crear_Usuario.place(relx=0.5, rely=0.63, anchor="center")
    Boton_Inicio_Recuperar.place(relx=0.5, rely=0.77, anchor="center")
    Texto1.configure(text="RIGHT WAY", text_color="white", font=(fuente, 55))
    Texto2.configure(text="SYS", text_color="white", font=(fuente, 55))
    Texto1.place(relx=0.5, rely=0.22, anchor="center")
    Texto2.place(relx=0.5, rely=0.34, anchor="center")
def Grafico_Emergencia():
    root2 = CTkToplevel()
    root2.title("Right Way Sys")
    App_Ancho = 600
    App_Alto = 600
    Ventana_Ancho = root.winfo_screenwidth()
    Ventana_Alto = root.winfo_screenheight()
    Cordenada_X = (Ventana_Ancho // 2) - (App_Ancho // 2)
    Cordenada_Y = (Ventana_Alto // 2) - (App_Alto // 2)
    root2.geometry(f"{App_Ancho}x{App_Alto}+{Cordenada_X}+{Cordenada_Y}")
    root2.config(background="#2d3e50")
    root2.resizable(height = True, width = True)
    root2.lift()
    root2.focus_force()
    root2.grab_set()
    Boton_Salir2 = CTkButton(root2, width=60, height=60, text="", corner_radius= 8, fg_color="#ff1919", hover_color="#be0000", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Salir, size=(40, 40)), command=root2.destroy) 
    Boton_Salir2.place(relx=0.015, rely=0.015, anchor="nw")
    TextoRoot1 = CTkLabel(root2, font=(fuente, 30), text="Contactos de Emergencia", anchor='center', bg_color ="#2d3e50")
    TextoRoot1.place(relx=0.5, rely=0.1, anchor="center")
    TextoRoot2 = CTkLabel(root2, font=(fuente, 18), text="\nEmergencias generales: 123\nPolicía Nacional: 112\nBomberos: 119\nAmbulancias: 125\nCruz Roja Colombiana: 132\nDefensa Civil: 144\nGAULA - Antisecuestro y Antiextorsión: 165\nPolicía de Tránsito: 127\nAtención a Desastres: 111\nLínea Púrpura (violencia de género): 155\nApoyo emocional (El poder de ser escuchado): 106\nICBF - Protección a menores: 141\nLínea psicoactiva (consumo de sustancias): 018000112439\nSecretaría de la Mujer - Atención psicológica: 7491027\nSecretaría de la Mujer - Atención psicológica (móvil): 3227203450", anchor='center', bg_color ="#2d3e50")
    TextoRoot2.place(relx=0.5, rely=0.54, anchor="center")

    def abrir_whatsapp():
        numero = "14155238886"
        mensaje = "Hola"
        enlace = f"https://wa.me/{numero}?text={mensaje.replace(' ', '%20')}"
        webbrowser.open(enlace)

    Boton_Whatsapp = CTkButton(root2, image=CTkImage(dark_image=Imagen_Boton_Whatsapp, size=(50, 50)), hover_color="#2d3e50", text="", width=40, height=40, bg_color="#2d3e50", fg_color="#2d3e50", command=abrir_whatsapp)
    Boton_Whatsapp.place(relx=0.99, rely=0.01, anchor="ne")

    root2.mainloop()
def Grafico_Pagina():
    root3 = CTkToplevel()
    root3.title("Right Way Sys")
    App_Ancho = 600
    App_Alto = 600
    Ventana_Ancho = root.winfo_screenwidth()
    Ventana_Alto = root.winfo_screenheight()
    Cordenada_X = (Ventana_Ancho // 2) - (App_Ancho // 2)
    Cordenada_Y = (Ventana_Alto // 2) - (App_Alto // 2)
    root3.geometry(f"{App_Ancho}x{App_Alto}+{Cordenada_X}+{Cordenada_Y}")
    root3.config(background="#2d3e50")
    root3.resizable(height = True, width = True)
    root3.lift()
    root3.focus_force()
    root3.grab_set()
    Boton_Salir3 = CTkButton(root3, width=60, height=60, text="", corner_radius= 8, fg_color="#ff1919", hover_color="#be0000", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Salir, size=(40, 40)), command=root3.destroy) 
    Boton_Salir3.place(relx=0.015, rely=0.015, anchor="nw")

    Texto38 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text="Usuario", font=(fuente, 45))
    Texto1 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text=f"{Usuario}", font=(fuente, 45))
    Texto2 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text="ID", font=(fuente, 17))
    Texto3 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text="Tipo ID", font=(fuente, 17))
    Texto4 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text="Primer Nombre", font=(fuente, 17))
    Texto5 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text="Segundo Nombre", font=(fuente, 17))
    Texto6 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text="Primer Apellido", font=(fuente, 17))
    Texto7 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text="Segundo Apellido", font=(fuente, 17))
    Texto8 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text="Usuario", font=(fuente, 17))
    Texto9 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text="Rol", font=(fuente, 17))
    Texto10 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text="Estado", font=(fuente, 17))
    Texto11 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text="Departamento", font=(fuente, 17))
    Texto12 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text="Ciudad", font=(fuente, 17))
    Texto13 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text="Localidad", font=(fuente, 17))
    Texto14 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text="Barrio", font=(fuente, 17))
    Texto15 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text="Direccion", font=(fuente, 17))
    Texto16 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text="Fecha Nacimiento", font=(fuente, 17))
    Texto17 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text="Edad", font=(fuente, 17))
    Texto18 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text="Correo", font=(fuente, 17))
    Texto19 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text="Telefono", font=(fuente, 17))

    Texto20 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text=f"{Busqueda2_Documento}", font=(fuente, 18, "bold"))
    Texto21 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text=f"{Busqueda2_TipoDocumento}", font=(fuente, 18, "bold"))
    Texto22 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text=f"{Busqueda2_PrimerNombre}", font=(fuente, 18, "bold"))
    Texto23 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text=f"{Busqueda2_SegundoNombre}", font=(fuente, 18, "bold"))
    Texto24 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text=f"{Busqueda2_PrimerApellido}", font=(fuente, 18, "bold"))
    Texto25 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text=f"{Busqueda2_SegundoApellido}", font=(fuente, 18, "bold"))
    Texto26 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text=f"{Busqueda2_NombreUsuario}", font=(fuente, 18, "bold"))
    Texto27 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text=f"{Busqueda2_RolUsuario}", font=(fuente, 18, "bold"))
    Texto28 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text=f"{Busqueda2_EstadoUsuario}", font=(fuente, 18, "bold"))
    Texto29 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text=f"{Busqueda2_Departamento}", font=(fuente, 18, "bold"))
    Texto30 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text=f"{Busqueda2_Ciudad}", font=(fuente, 18, "bold"))
    Texto31 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text=f"{Busqueda2_Localidad}", font=(fuente, 18, "bold"))
    Texto32 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text=f"{Busqueda2_Barrio}", font=(fuente, 18, "bold"))
    Texto33 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text=f"{Busqueda2_Direccion}", font=(fuente, 18, "bold"))
    Texto34 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text=f"{Busqueda2_FechaNacimento}", font=(fuente, 18, "bold"))
    Texto35 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text=f"{Busqueda2_Edad}", font=(fuente, 18, "bold"))
    Texto36 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text=f"{Busqueda2_Email}", font=(fuente, 18, "bold"))
    Texto37 = CTkLabel(root3, anchor='center', bg_color ="#2d3e50", text=f"{Busqueda2_Telefono}", font=(fuente, 18, "bold"))

    Texto1.place(relx=0.5, rely=0.15, anchor="center")
    Texto38.place(relx=0.5, rely=0.04, anchor="center")
    Texto2.place(relx=0.15, rely=0.23, anchor="center")
    Texto3.place(relx=0.38, rely=0.23, anchor="center")
    Texto4.place(relx=0.61, rely=0.23, anchor="center")
    Texto5.place(relx=0.85, rely=0.23, anchor="center")
    Texto6.place(relx=0.15, rely=0.36, anchor="center")
    Texto7.place(relx=0.38, rely=0.36, anchor="center")
    Texto8.place(relx=0.61, rely=0.36, anchor="center")
    Texto9.place(relx=0.85, rely=0.36, anchor="center")
    Texto10.place(relx=0.15, rely=0.49, anchor="center")
    Texto11.place(relx=0.38, rely=0.49, anchor="center")
    Texto12.place(relx=0.61, rely=0.49, anchor="center")
    Texto13.place(relx=0.85, rely=0.49, anchor="center")
    Texto14.place(relx=0.15, rely=0.62, anchor="center")
    Texto15.place(relx=0.38, rely=0.62, anchor="center")
    Texto16.place(relx=0.61, rely=0.62, anchor="center")
    Texto17.place(relx=0.85, rely=0.62, anchor="center")
    Texto18.place(relx=0.5, rely=0.75, anchor="center")
    Texto19.place(relx=0.5, rely=0.88, anchor="center")

    Texto20.place(relx=0.15, rely=0.28, anchor="center")
    Texto21.place(relx=0.38, rely=0.28, anchor="center")
    Texto22.place(relx=0.61, rely=0.28, anchor="center")
    Texto23.place(relx=0.85, rely=0.28, anchor="center")
    Texto24.place(relx=0.15, rely=0.41, anchor="center")
    Texto25.place(relx=0.38, rely=0.41, anchor="center")
    Texto26.place(relx=0.61, rely=0.41, anchor="center")
    Texto27.place(relx=0.85, rely=0.41, anchor="center")
    Texto28.place(relx=0.15, rely=0.54, anchor="center")
    Texto29.place(relx=0.38, rely=0.54, anchor="center")
    Texto30.place(relx=0.61, rely=0.54, anchor="center")
    Texto31.place(relx=0.85, rely=0.54, anchor="center")
    Texto32.place(relx=0.15, rely=0.67, anchor="center")
    Texto33.place(relx=0.38, rely=0.67, anchor="center")
    Texto34.place(relx=0.61, rely=0.67, anchor="center")
    Texto35.place(relx=0.85, rely=0.67, anchor="center")
    Texto36.place(relx=0.5, rely=0.80, anchor="center")
    Texto37.place(relx=0.5, rely=0.93, anchor="center")
    root3.mainloop()
def Grafico_Login():
    Olvidar_Lugares()
    Texto1.configure(text="LOGIN", font=(fuente, 55))
    Texto2.configure(text="Usuario", font=(fuente, 26))
    Texto3.configure(text="Contraseña", font=(fuente, 26))
    Texto4.configure(text=f"Intentos restantes: {Intentos_Restantes}", font=(fuente, 26))
    Texto1.place(relx=0.5, rely=0.23, anchor="center")
    Texto2.place(relx=0.5, rely=0.37, anchor="center")
    Texto3.place(relx=0.5, rely=0.52, anchor="center")
    Texto4.place(relx=0.015, rely=0.99, anchor="sw")

    Entrada_Usuario.place(relx=0.5, rely=0.43, anchor="center")
    Entrada_Contraseña.place(relx=0.5, rely=0.59, anchor="center")
    
    Imagen_Grafico_Login_Usuario.place(relx=0.34, rely=0.43, anchor="center")
    Imagen_Grafico_Login_Contraseña.place(relx=0.34, rely=0.59, anchor="center")

    Boton_Funcion_Login.place(relx=0.5, rely=0.76, anchor="center")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Volver.place(relx=0.105, rely=0.015, anchor="nw")
def Grafico_Crear_Usuario():
    Olvidar_Lugares()
    Texto1.configure(text="CREAR USUARIO", font=(fuente, 45))
    Texto2.configure(text="Primer Nombre", font=(fuente, 18))
    Texto3.configure(text="Segundo Nombre", font=(fuente, 18))
    Texto4.configure(text="Primer Apellido", font=(fuente, 18))
    Texto5.configure(text="Segundo Apellido", font=(fuente, 18))
    Texto6.configure(text="Tipo de documento", font=(fuente, 18))
    Texto7.configure(text="ID", font=(fuente, 18))
    Texto8.configure(text="Fecha de Nacimiento", font=(fuente, 18))
    Texto9.configure(text="Correo", font=(fuente, 18))
    Texto10.configure(text="Departamento", font=(fuente, 18))
    Texto11.configure(text="Ciudad", font=(fuente, 18))
    Texto12.configure(text="Localidad", font=(fuente, 18))
    Texto13.configure(text="Barrio", font=(fuente, 18))
    Texto14.configure(text="Direccion", font=(fuente, 18))
    Texto15.configure(text="Telefono", font=(fuente, 18))
    Texto16.configure(text="Usuario", font=(fuente, 18))
    Texto17.configure(text="Contraseña", font=(fuente, 18))
    Texto1.place(relx=0.5, rely=0.13, anchor="center")
    Texto2.place(relx=0.15, rely=0.27, anchor="center")
    Texto3.place(relx=0.38, rely=0.27, anchor="center")
    Texto4.place(relx=0.61, rely=0.27, anchor="center")
    Texto5.place(relx=0.85, rely=0.27, anchor="center")
    Texto6.place(relx=0.15, rely=0.42, anchor="center")
    Texto7.place(relx=0.38, rely=0.42, anchor="center")
    Texto8.place(relx=0.61, rely=0.42, anchor="center")
    Texto9.place(relx=0.85, rely=0.42, anchor="center")
    Texto10.place(relx=0.15, rely=0.57, anchor="center")
    Texto11.place(relx=0.38, rely=0.57, anchor="center")
    Texto12.place(relx=0.61, rely=0.57, anchor="center")
    Texto13.place(relx=0.85, rely=0.57, anchor="center")
    Texto14.place(relx=0.15, rely=0.72, anchor="center")
    Texto15.place(relx=0.38, rely=0.72, anchor="center")
    Texto16.place(relx=0.61, rely=0.72, anchor="center")
    Texto17.place(relx=0.85, rely=0.72, anchor="center")

    Entrada_Primer_Nombre.place(relx=0.15, rely=0.33, anchor="center")
    Entrada_Segundo_Nombre.place(relx=0.38, rely=0.33, anchor="center")
    Entrada_Primer_Apellido.place(relx=0.61, rely=0.33, anchor="center")
    Entrada_Segundo_Apellido.place(relx=0.85, rely=0.33, anchor="center")
    Entrada_Tipo_Documento.place(relx=0.15, rely=0.48, anchor="center")
    Entrada_Documento.place(relx=0.38, rely=0.48, anchor="center")
    Entrada_Fecha_Nacimento.place(relx=0.61, rely=0.48, anchor="center")
    Entrada_Email.place(relx=0.85, rely=0.48, anchor="center")
    Entrada_Departamento.place(relx=0.15, rely=0.63, anchor="center")
    Entrada_Ciudad.place(relx=0.38, rely=0.63, anchor="center")
    Entrada_Localidad.place(relx=0.61, rely=0.63, anchor="center")
    Entrada_Barrio.place(relx=0.85, rely=0.63, anchor="center")
    Entrada_Direccion.place(relx=0.15, rely=0.78, anchor="center")
    Entrada_Numero.place(relx=0.38, rely=0.78, anchor="center")
    Entrada_Contraseña.place(relx=0.85, rely=0.78, anchor="center")
    Entrada_Usuario.place(relx=0.61, rely=0.78, anchor="center")

    Boton_Funcion_Crear_Usuario.place(relx=0.5, rely=0.9, anchor="center")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Volver.place(relx=0.105, rely=0.015, anchor="nw")
def Grafico_Usuario_Inicio():
    Olvidar_Lugares()
    Texto1.configure(text="Bienvenido", font=(fuente, 50))
    Texto1.place(relx=0.5, rely=0.25, anchor="center")
    Texto2.configure(text=f"{Usuario}", font=(fuente, 50))
    Texto2.place(relx=0.5, rely=0.37, anchor="center")

    Boton_Usuario_Casos.place(relx=0.5, rely=0.59, anchor="center")
    Boton_Usuario_Cuenta.place(relx=0.5, rely=0.73, anchor="center")
    Boton_Pagina.place(relx=0.99, rely=0.01, anchor="ne")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Volver.place(relx=0.105, rely=0.015, anchor="nw")
def Grafico_Usuario_Cuenta():
    Olvidar_Lugares()
    Texto1.configure(text="Configuracion de", font=(fuente, 50))
    Texto1.place(relx=0.5, rely=0.25, anchor="center")
    Texto2.configure(text="la cuenta", font=(fuente, 50))
    Texto2.place(relx=0.5, rely=0.37, anchor="center")

    Boton_Usuario_Cuenta_Modificar_Contraseña.place(relx=0.5, rely=0.59, anchor="center")
    Boton_Usuario_Cuenta_Modificar_Datos.place(relx=0.5, rely=0.73, anchor="center")
    Boton_Pagina.place(relx=0.99, rely=0.01, anchor="ne")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Usuario_Volver.place(relx=0.105, rely=0.015, anchor="nw")
def Grafico_Usuario_Cuenta_Modificar_contraseña():
    Olvidar_Lugares()
    Texto1.configure(text="Modificar", font=(fuente, 55))
    Texto2.configure(text="contraseña", font=(fuente, 55))
    Texto3.configure(text="Contraseña", font=(fuente, 22))
    Texto4.configure(text="Nueva Contraseña", font=(fuente, 22))
    Texto5.configure(text=f"Intentos restantes: {Intentos_Restantes}", font=(fuente, 26))

    Texto1.place(relx=0.5, rely=0.15, anchor="center")
    Texto2.place(relx=0.5, rely=0.26, anchor="center")

    Texto3.place(relx=0.5, rely=0.37, anchor="center")
    Texto4.place(relx=0.5, rely=0.52, anchor="center")

    Texto5.place(relx=0.015, rely=0.99, anchor="sw")

    Entrada_Contraseña.place(relx=0.5, rely=0.43, anchor="center")
    Entrada_Contraseña_Nueva.place(relx=0.5, rely=0.59, anchor="center")

    Imagen_Grafico_Login_Contraseña.place(relx=0.33, rely=0.42, anchor="center")
    Imagen_Grafico_Modificar_Contraseña.place(relx=0.33, rely=0.58, anchor="center")
    Boton_Pagina.place(relx=0.99, rely=0.01, anchor="ne")
    Boton_Funcion_Cuenta_Modificar_Contraseña.place(relx=0.5, rely=0.76, anchor="center")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Usuario_Cuenta_Volver.place(relx=0.105, rely=0.015, anchor="nw")
def Grafico_Usuario_Modificar_Datos():
    global Entrada_Usuario_Datos_Correo, Entrada_Usuario_Datos_Correo_Check, Entrada_Usuario_Datos_Telefono, Entrada_Usuario_Datos_Telefono_Check, Entrada_Usuario_Datos_Direccion, Entrada_Usuario_Datos_Direccion_Check, Entrada_Usuario_Datos_Tipo, Entrada_Usuario_Datos_Tipo_Check
    Olvidar_Lugares()
    Funcion_Cargar_Contactos_Usuario()
    Texto1.configure(text="Seleccione una casilla", font=(fuente, 35))
    Texto1.place(relx=0.5, rely=0.10, anchor="center")
    Texto2.configure(text="para modificar ese dato", font=(fuente, 35))
    Texto2.place(relx=0.5, rely=0.20, anchor="center")
    Texto3.configure(text="Tipo Documento:", font=(fuente, 20))
    Texto3.place(relx=0.22, rely=0.30, anchor="center")
    Texto4.configure(text="Correo:", font=(fuente, 20))
    Texto4.place(relx=0.70, rely=0.30, anchor="center")
    Texto5.configure(text="Telefono:", font=(fuente, 20))
    Texto5.place(relx=0.22, rely=0.50, anchor="center")
    Texto6.configure(text="Direccion:", font=(fuente, 20))
    Texto6.place(relx=0.70, rely=0.50, anchor="center")
    Texto7.configure(text="Contraseña:", font=(fuente, 20))
    Texto7.place(relx=0.5, rely=0.65, anchor="center")
    Email_Var = tk.StringVar(value=Email_Original)
    Entrada_Usuario_Datos_Correo = CTkEntry(root, text_color="#828282", textvariable=Email_Var, state="disabled", font=(fuente, 15), width=160, height=17, fg_color="#555555", bg_color ="#2d3e50", corner_radius=20)
    Entrada_Usuario_Datos_Correo.place(relx=0.70, rely=0.35, anchor="center") 
    Email_Check_Var = tk.BooleanVar(value=False)
    Entrada_Usuario_Datos_Correo_Check = CTkCheckBox(root, text="", variable=Email_Check_Var, command=lambda: (Entrada_Usuario_Datos_Correo.configure(state="normal" if Email_Check_Var.get() else "disabled"), Email_Var.set(Email_Var.get() if Email_Check_Var.get() else Email_Original), Entrada_Usuario_Datos_Correo.configure(text_color="white" if Email_Check_Var.get() else "#828282")))
    Entrada_Usuario_Datos_Correo_Check.place(relx=0.94, rely=0.35, anchor="center") 
    Boton_Pagina.place(relx=0.99, rely=0.01, anchor="ne")
    Telefono_Var = tk.StringVar(value=Telefono_Original)
    Entrada_Usuario_Datos_Telefono = CTkEntry(root, text_color="#828282", textvariable=Telefono_Var, state="disabled", font=(fuente, 15), width=160, height=17, fg_color="#555555", bg_color ="#2d3e50", corner_radius=20)
    Entrada_Usuario_Datos_Telefono.place(relx=0.22, rely=0.55, anchor="center")
    Telefono_Check_Var = tk.BooleanVar(value=False)
    Entrada_Usuario_Datos_Telefono_Check = CTkCheckBox(root, text="", variable=Telefono_Check_Var, command=lambda: (Entrada_Usuario_Datos_Telefono.configure(state="normal" if Telefono_Check_Var.get() else "disabled"), Telefono_Var.set(Telefono_Var.get() if Telefono_Check_Var.get() else Telefono_Original), Entrada_Usuario_Datos_Telefono.configure(text_color="white" if Telefono_Check_Var.get() else "#828282")))
    Entrada_Usuario_Datos_Telefono_Check.place(relx=0.46, rely=0.55, anchor="center")

    Direccion_Var = tk.StringVar(value=Direccion_Original)
    Entrada_Usuario_Datos_Direccion = CTkEntry(root, text_color="#828282", textvariable=Direccion_Var, state="disabled", font=(fuente, 15), width=160, height=17, fg_color="#555555", bg_color ="#2d3e50", corner_radius=20)
    Entrada_Usuario_Datos_Direccion.place(relx=0.70, rely=0.55, anchor="center")
    Direccion_Check_Var = tk.BooleanVar(value=False)
    Entrada_Usuario_Datos_Direccion_Check = CTkCheckBox(root, text="", variable=Direccion_Check_Var, command=lambda: (Entrada_Usuario_Datos_Direccion.configure(state="normal" if Direccion_Check_Var.get() else "disabled"), Direccion_Var.set(Direccion_Var.get() if Direccion_Check_Var.get() else Direccion_Original), Entrada_Usuario_Datos_Direccion.configure(text_color="white" if Direccion_Check_Var.get() else "#828282")))
    Entrada_Usuario_Datos_Direccion_Check.place(relx=0.94, rely=0.55, anchor="center") 

    TipoDocumento_Var = tk.StringVar(value=TipoDocumento_Original)
    Entrada_Usuario_Datos_Tipo = CTkOptionMenu(root, text_color="#828282", values=["Cedula Ciudadania","Cedula Extranjeria", "Pasaporte", "Tarjeta de identidad"], corner_radius=32, fg_color="#555555", button_color="#404040", dropdown_fg_color="#555555", bg_color ="#2d3e50", font=(fuente, 15), width=120, height=15, anchor="w", variable=TipoDocumento_Var, state="disabled")
    Entrada_Usuario_Datos_Tipo.place(relx=0.22, rely=0.35, anchor="center")
    Tipo_Check_Var = tk.BooleanVar(value=False)
    Entrada_Usuario_Datos_Tipo_Check = CTkCheckBox(root, text="", variable=Tipo_Check_Var, command=lambda: (Entrada_Usuario_Datos_Tipo.configure(state="normal" if Tipo_Check_Var.get() else "disabled"), TipoDocumento_Var.set(TipoDocumento_Var.get() if Tipo_Check_Var.get() else TipoDocumento_Original), Entrada_Usuario_Datos_Tipo.configure(text_color="white" if Tipo_Check_Var.get() else "#828282")))
    Entrada_Usuario_Datos_Tipo_Check.place(relx=0.469, rely=0.35, anchor="center")  

    Entrada_Contraseña.place(relx=0.5, rely=0.70, anchor="center")
    def salir():
        Entrada_Usuario_Datos_Correo.place_forget()
        Entrada_Usuario_Datos_Correo_Check.place_forget()
        Entrada_Usuario_Datos_Telefono.place_forget()
        Entrada_Usuario_Datos_Telefono_Check.place_forget()
        Entrada_Usuario_Datos_Direccion.place_forget()
        Entrada_Usuario_Datos_Direccion_Check.place_forget()
        Entrada_Usuario_Datos_Tipo.place_forget()
        Entrada_Usuario_Datos_Tipo_Check.place_forget()
        Boton_Usuario_Volver2.place_forget()
        Boton_Funcion_Modificar_Datos_Usuario.place_forget()
        Boton_Salir.place_forget()
        Grafico_Usuario_Cuenta()
    Boton_Usuario_Volver2 = CTkButton(root, width=30, height=35, text="", corner_radius= 8, fg_color="#ff7b19", hover_color="#cf5800", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Volver, size=(22, 22)), command=salir)
    Boton_Funcion_Modificar_Datos_Usuario.place(relx=0.5, rely=0.83, anchor="center")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Usuario_Volver2.place(relx=0.105, rely=0.015, anchor="nw")
def Grafico_Usuario_Casos():
    Olvidar_Lugares()
    Texto1.configure(text="Seleccione una", font=(fuente, 55))
    Texto1.place(relx=0.5, rely=0.15, anchor="center")
    Texto2.configure(text="opcion", font=(fuente, 55))
    Texto2.place(relx=0.5, rely=0.26, anchor="center")
    Boton_Pagina.place(relx=0.99, rely=0.01, anchor="ne")
    Boton_Usuario_Casos_Grafico_Crear.place(relx=0.5, rely=0.59, anchor="center")
    Boton_Usuario_Casos_Grafico_Buscar.place(relx=0.5, rely=0.73, anchor="center")

    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Usuario_Volver.place(relx=0.105, rely=0.015, anchor="nw")
def Grafico_Usuario_Casos_Crear():
    Olvidar_Lugares()
    Texto1.configure(text="Crear Caso", font=(fuente, 45))
    Texto2.configure(text="Tipo Desastre", font=(fuente, 22))
    Texto3.configure(text="Fecha Caso", font=(fuente, 22))
    Texto4.configure(text="Direccion Caso", font=(fuente, 22))
    Texto6.configure(text="Personas Afectadas", font=(fuente, 22))
    Texto5.configure(text="Descripcion Caso", font=(fuente, 22))
    Boton_Pagina.place(relx=0.99, rely=0.01, anchor="ne")
    Texto1.place(relx=0.5, rely=0.15, anchor="center")

    Texto2.place(relx=0.33, rely=0.24, anchor="center")
    Texto3.place(relx=0.66, rely=0.24, anchor="center")
    Texto4.place(relx=0.33, rely=0.36, anchor="center")
    Texto6.place(relx=0.66, rely=0.36, anchor="center")

    Texto5.place(relx=0.5, rely=0.49, anchor="center")

    Entrada_Caso_TipoDesastre.place(relx=0.33, rely=0.30, anchor="center")
    Entrada_Caso_Fecha.place(relx=0.66, rely=0.30, anchor="center")
    Entrada_Caso_Direccion.place(relx=0.33, rely=0.42, anchor="center")
    Entrada_Caso_Personas.place(relx=0.66, rely=0.42, anchor="center")

    Entrada_Caso_Descripcion.place(relx=0.5, rely=0.65, anchor="center")

    Boton_Funcion_Crear_Caso.place(relx=0.5, rely=0.85, anchor="center")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Usuario_Casos_Volver.place(relx=0.105, rely=0.015, anchor="nw")
def Grafico_Usuario_Casos_Buscar():
    Olvidar_Lugares()
    Texto1.configure(text="Buscar Caso", font=(fuente, 45))
    Texto2.configure(text="Ingrese el numero de radicado:", font=(fuente, 30))
    Texto1.place(relx=0.5, rely=0.15, anchor="center")
    Texto2.place(relx=0.5, rely=0.4, anchor="center")
    Boton_Pagina.place(relx=0.99, rely=0.01, anchor="ne")
    Boton_Funcion_Buscar_Caso.place(relx=0.5, rely=0.75, anchor="center")
    Entrada_Caso_Radicado.place(relx=0.5, rely=0.47, anchor="center")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Usuario_Casos_Volver.place(relx=0.105, rely=0.015, anchor="nw")
def Grafico_Usuario_Casos_Buscar_2():
    Olvidar_Lugares()
    Texto1.configure(text=f"Caso {Radicado}", font=(fuente, 45))

    Texto2.configure(text="Fecha:", font=(fuente, 22))
    Texto3.configure(text="Descripcion:", font=(fuente, 22))
    Texto4.configure(text="Afectados:", font=(fuente, 22))
    Texto5.configure(text="Usuario:", font=(fuente, 22))
    Texto6.configure(text="Desastre:", font=(fuente, 22))
    Texto7.configure(text="Departamento:", font=(fuente, 22))
    Texto8.configure(text="Tipo:", font=(fuente, 22))
    Texto9.configure(text="Estado:", font=(fuente, 22))
    Boton_Pagina.place(relx=0.99, rely=0.01, anchor="ne")
    Texto10.configure(text=f"{Radicado_Fecha}", font=(fuente, 18, "bold"))
    Texto11.configure(text=f"{Radicado_Descripcion}", font=(fuente, 18, "bold"))
    Texto12.configure(text=f"{Radicado_Personas}", font=(fuente, 18, "bold"))
    Texto13.configure(text=f"{Radicado_Usuario}", font=(fuente, 18, "bold"))
    Texto14.configure(text=f"{Radicado_Desastre}", font=(fuente, 18, "bold"))
    Texto15.configure(text=f"{Radicado_Departamento}", font=(fuente, 18, "bold"))
    Texto16.configure(text=f"{Radicado_Tipo}", font=(fuente, 18, "bold"))
    Texto17.configure(text=f"{Radicado_Estado}", font=(fuente, 18, "bold"))

    Texto1.place(relx=0.5, rely=0.15, anchor="center")

    Texto2.place(relx=0.15, rely=0.38, anchor="center")
    Texto3.place(relx=0.38, rely=0.38, anchor="center")
    Texto4.place(relx=0.61, rely=0.38, anchor="center")
    Texto5.place(relx=0.85, rely=0.38, anchor="center")
    Texto6.place(relx=0.15, rely=0.57, anchor="center")
    Texto7.place(relx=0.38, rely=0.57, anchor="center")
    Texto8.place(relx=0.61, rely=0.57, anchor="center")
    Texto9.place(relx=0.85, rely=0.57, anchor="center")
    Texto10.place(relx=0.15, rely=0.44, anchor="center")
    Texto11.place(relx=0.38, rely=0.44, anchor="center")
    Texto12.place(relx=0.61, rely=0.44, anchor="center")
    Texto13.place(relx=0.85, rely=0.44, anchor="center")
    Texto14.place(relx=0.15, rely=0.63, anchor="center")
    Texto15.place(relx=0.38, rely=0.63, anchor="center")
    Texto16.place(relx=0.61, rely=0.63, anchor="center")
    Texto17.place(relx=0.85, rely=0.63, anchor="center")

    Boton_Usuario_Casos_Grafico_Volver_Buscar.place(relx=0.5, rely=0.85, anchor="center")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Usuario_Casos_Volver.place(relx=0.105, rely=0.015, anchor="nw")
def Grafico_Admin_Inicio():
    Olvidar_Lugares()
    Usuario = "ADMIN"
    Texto1.configure(text="Bienvenido", font=(fuente, 50))
    Texto1.place(relx=0.5, rely=0.20, anchor="center")
    Texto2.configure(text=f"{Usuario}", font=(fuente, 50))
    Texto2.place(relx=0.5, rely=0.33, anchor="center")

    Boton_Admin_Usuarios.place(relx=0.5, rely=0.49, anchor="center")
    Boton_Admin_Casos.place(relx=0.5, rely=0.63, anchor="center")
    Boton_Admin_Entidades.place(relx=0.5, rely=0.77, anchor="center")

    Texto_Admin.place(relx=0.015, rely=0.935, anchor="nw")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Volver.place(relx=0.105, rely=0.015, anchor="nw")
def Grafico_Admin_Casos():
    Olvidar_Lugares()
    Texto1.configure(text="Casos", font=(fuente, 50))
    Texto1.place(relx=0.5, rely=0.20, anchor="center")

    Boton_Admin_Grafico_Casos_Buscar.place(relx=0.5, rely=0.40, anchor="center")
    Boton_Admin_Grafico_Casos_Crear.place(relx=0.5, rely=0.53, anchor="center")
    Boton_Admin_Grafico_Casos_Modificar.place(relx=0.5, rely=0.66, anchor="center")
    Boton_Admin_Grafico_Casos_Eliminar.place(relx=0.5, rely=0.79, anchor="center")

    Texto_Admin.place(relx=0.015, rely=0.935, anchor="nw")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Admin_Volver.place(relx=0.105, rely=0.015, anchor="nw")
def Grafico_Admin_Casos_Buscar():
    Olvidar_Lugares()
    Texto1.configure(text="Buscar Caso", font=(fuente, 45))
    Texto2.configure(text="Ingrese el numero de radicado:", font=(fuente, 30))
    Texto1.place(relx=0.5, rely=0.15, anchor="center")
    Texto2.place(relx=0.5, rely=0.4, anchor="center")
    Texto_Admin.place(relx=0.015, rely=0.935, anchor="nw")
    Boton_Funcion_Buscar_Caso.place(relx=0.5, rely=0.75, anchor="center")
    Entrada_Caso_Radicado.place(relx=0.5, rely=0.47, anchor="center")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Admin_Volver_Casos.place(relx=0.105, rely=0.015, anchor="nw")
def Grafico_Admin_Casos_Buscar_2():
    Olvidar_Lugares()
    Texto1.configure(text=f"Caso {Radicado}", font=(fuente, 45))

    Texto2.configure(text="Fecha:", font=(fuente, 22))
    Texto3.configure(text="Descripcion:", font=(fuente, 22))
    Texto4.configure(text="Afectados:", font=(fuente, 22))
    Texto5.configure(text="Usuario:", font=(fuente, 22))
    Texto6.configure(text="Desastre:", font=(fuente, 22))
    Texto7.configure(text="Departamento:", font=(fuente, 22))
    Texto8.configure(text="Tipo:", font=(fuente, 22))
    Texto9.configure(text="Estado:", font=(fuente, 22))

    Texto10.configure(text=f"{Radicado_Fecha}", font=(fuente, 18, "bold"))
    Texto11.configure(text=f"{Radicado_Descripcion}", font=(fuente, 18, "bold"))
    Texto12.configure(text=f"{Radicado_Personas}", font=(fuente, 18, "bold"))
    Texto13.configure(text=f"{Radicado_Usuario}", font=(fuente, 18, "bold"))
    Texto14.configure(text=f"{Radicado_Desastre}", font=(fuente, 18, "bold"))
    Texto15.configure(text=f"{Radicado_Departamento}", font=(fuente, 18, "bold"))
    Texto16.configure(text=f"{Radicado_Tipo}", font=(fuente, 18, "bold"))
    Texto17.configure(text=f"{Radicado_Estado}", font=(fuente, 18, "bold"))

    Texto1.place(relx=0.5, rely=0.15, anchor="center")

    Texto2.place(relx=0.15, rely=0.38, anchor="center")
    Texto3.place(relx=0.38, rely=0.38, anchor="center")
    Texto4.place(relx=0.61, rely=0.38, anchor="center")
    Texto5.place(relx=0.85, rely=0.38, anchor="center")
    Texto6.place(relx=0.15, rely=0.57, anchor="center")
    Texto7.place(relx=0.38, rely=0.57, anchor="center")
    Texto8.place(relx=0.61, rely=0.57, anchor="center")
    Texto9.place(relx=0.85, rely=0.57, anchor="center")
    Texto10.place(relx=0.15, rely=0.44, anchor="center")
    Texto11.place(relx=0.38, rely=0.44, anchor="center")
    Texto12.place(relx=0.61, rely=0.44, anchor="center")
    Texto13.place(relx=0.85, rely=0.44, anchor="center")
    Texto14.place(relx=0.15, rely=0.63, anchor="center")
    Texto15.place(relx=0.38, rely=0.63, anchor="center")
    Texto16.place(relx=0.61, rely=0.63, anchor="center")
    Texto17.place(relx=0.85, rely=0.63, anchor="center")
    Texto_Admin.place(relx=0.015, rely=0.935, anchor="nw")
    Boton_Usuario_Casos_Grafico_Volver_Buscar.place(relx=0.5, rely=0.85, anchor="center")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Admin_Volver_Casos.place(relx=0.105, rely=0.015, anchor="nw")
def Grafico_Admin_Casos_Crear():
    Olvidar_Lugares()
    Texto1.configure(text="Crear Caso", font=(fuente, 45))
    Texto2.configure(text="Tipo Desastre", font=(fuente, 22))
    Texto3.configure(text="Fecha Caso", font=(fuente, 22))
    Texto4.configure(text="Direccion Caso", font=(fuente, 22))
    Texto6.configure(text="Personas Afectadas", font=(fuente, 22))
    Texto5.configure(text="Descripcion Caso", font=(fuente, 22))

    Texto1.place(relx=0.5, rely=0.15, anchor="center")

    Texto2.place(relx=0.33, rely=0.24, anchor="center")
    Texto3.place(relx=0.66, rely=0.24, anchor="center")
    Texto4.place(relx=0.33, rely=0.36, anchor="center")
    Texto6.place(relx=0.66, rely=0.36, anchor="center")

    Texto5.place(relx=0.5, rely=0.49, anchor="center")

    Entrada_Caso_TipoDesastre.place(relx=0.33, rely=0.30, anchor="center")
    Entrada_Caso_Fecha.place(relx=0.66, rely=0.30, anchor="center")
    Entrada_Caso_Direccion.place(relx=0.33, rely=0.42, anchor="center")
    Entrada_Caso_Personas.place(relx=0.66, rely=0.42, anchor="center")

    Entrada_Caso_Descripcion.place(relx=0.5, rely=0.65, anchor="center")

    Texto_Admin.place(relx=0.015, rely=0.935, anchor="nw")
    Boton_Funcion_Crear_Caso.place(relx=0.5, rely=0.85, anchor="center")
    Boton_Admin_Volver_Casos.place(relx=0.105, rely=0.015, anchor="nw")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
def Grafico_Admin_Modificar_Casos_Buscar():
    Olvidar_Lugares()
    Texto1.configure(text="Buscar Caso", font=(fuente, 45))
    Texto2.configure(text="Ingrese el numero de radicado:", font=(fuente, 30))
    Texto1.place(relx=0.5, rely=0.15, anchor="center")
    Texto2.place(relx=0.5, rely=0.4, anchor="center")
    Texto_Admin.place(relx=0.015, rely=0.935, anchor="nw")
    Boton_Funcion_Buscar_Caso2.place(relx=0.5, rely=0.75, anchor="center")
    Entrada_Caso_Radicado.place(relx=0.5, rely=0.47, anchor="center")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Admin_Volver_Casos.place(relx=0.105, rely=0.015, anchor="nw")
def Grafico_Admin_Modificar_Casos():
    global Boton_Admin_Volver2, Entrada_Caso_Departamento, Entrada_Caso_Departamento_Check, Entrada_Caso_Descripcion2, Entrada_Caso_Descripcion2_Check, Entrada_Caso_Fecha, Entrada_Caso_Fecha_Check, Entrada_Caso_Afectados, Entrada_Caso_Afectados_Check, Entrada_Caso_Estado, Entrada_Caso_Estado_Check, Entrada_Caso_Desastre, Entrada_Caso_Desastre_Check, Entrada_Caso_Estado, Entrada_Caso_Estado_Check, Entrada_Caso_Tipo, Entrada_Caso_Tipo_Check
    Olvidar_Lugares()
    Funcion_Cargar_Datos_Casos()
    Texto1.configure(text="Seleccione una casilla", font=(fuente, 35))
    Texto1.place(relx=0.5, rely=0.05, anchor="center")
    Texto2.configure(text="para modificar ese dato", font=(fuente, 35))
    Texto2.place(relx=0.5, rely=0.12, anchor="center")

    Texto3.configure(text="Tipo de Caso:", font=(fuente, 20))
    Texto3.place(relx=0.25, rely=0.20, anchor="center")

    Texto4.configure(text="Fecha del Caso:", font=(fuente, 20))
    Texto4.place(relx=0.75, rely=0.20, anchor="center")

    Texto5.configure(text="Desastre:", font=(fuente, 20))
    Texto5.place(relx=0.25, rely=0.33, anchor="center")

    Texto6.configure(text="Afectados:", font=(fuente, 20))
    Texto6.place(relx=0.75, rely=0.33, anchor="center")

    Texto7.configure(text="Estado del Caso:", font=(fuente, 20))
    Texto7.place(relx=0.25, rely=0.46, anchor="center")

    Texto8.configure(text="Descripción:", font=(fuente, 20))
    Texto8.place(relx=0.75, rely=0.46, anchor="center")

    Texto9.configure(text="Departamento:", font=(fuente, 20))
    Texto9.place(relx=0.5, rely=0.59, anchor="center")

    Texto10.configure(text="Contraseña:", font=(fuente, 20))
    Texto10.place(relx=0.5, rely=0.75, anchor="center")

    Tipo_Var = tk.StringVar(value=Tipo_Original)
    Entrada_Caso_Tipo = CTkOptionMenu(root, text_color="#828282", values=["Caso", "Ticket"], corner_radius=32, fg_color="#555555", button_color="#404040", dropdown_fg_color="#555555", bg_color="#2d3e50", font=(fuente, 15), width=160, height=17, anchor="w", variable=Tipo_Var, state="disabled")
    Entrada_Caso_Tipo.place(relx=0.25, rely=0.25, anchor="center")
    Tipo_Check_Var = tk.BooleanVar(value=False)
    Entrada_Caso_Tipo_Check = CTkCheckBox(root, text="", variable=Tipo_Check_Var, command=lambda: (Entrada_Caso_Tipo.configure(state="normal" if Tipo_Check_Var.get() else "disabled"), Tipo_Var.set(Tipo_Var.get() if Tipo_Check_Var.get() else Tipo_Original), Entrada_Caso_Tipo.configure(text_color="white" if Tipo_Check_Var.get() else "#828282")))
    Entrada_Caso_Tipo_Check.place(relx=0.47, rely=0.25, anchor="center")

    Desastre_Var = tk.StringVar(value=Desastre_Convertido)
    Entrada_Caso_Desastre = CTkOptionMenu(root, text_color="#828282", values=["Incendio", "Inundación", "Sismo-temblor", "Terremoto"], corner_radius=32, fg_color="#555555", button_color="#404040", dropdown_fg_color="#555555", bg_color="#2d3e50", font=(fuente, 15), width=160, height=17, anchor="w", variable=Desastre_Var, state="disabled")
    Entrada_Caso_Desastre.place(relx=0.25, rely=0.38, anchor="center")
    Desastre_Check_Var = tk.BooleanVar(value=False)
    Entrada_Caso_Desastre_Check = CTkCheckBox(root, text="", variable=Desastre_Check_Var, command=lambda: (Entrada_Caso_Desastre.configure(state="normal" if Desastre_Check_Var.get() else "disabled"), Desastre_Var.set(Desastre_Var.get() if Desastre_Check_Var.get() else Desastre_Convertido), Entrada_Caso_Desastre.configure(text_color="white" if Desastre_Check_Var.get() else "#828282")))
    Entrada_Caso_Desastre_Check.place(relx=0.47, rely=0.38, anchor="center")

    Estado_Var = tk.StringVar(value=Estado_Convertido)
    Entrada_Caso_Estado = CTkOptionMenu(root, text_color="#828282", values=["Pendiente", "Activo", "Finalizado"], corner_radius=32, fg_color="#555555", button_color="#404040", dropdown_fg_color="#555555", bg_color="#2d3e50", font=(fuente, 15), width=160, height=17, anchor="w", variable=Estado_Var, state="disabled")
    Entrada_Caso_Estado.place(relx=0.25, rely=0.51, anchor="center")
    Estado_Check_Var = tk.BooleanVar(value=False)
    Entrada_Caso_Estado_Check = CTkCheckBox(root, text="", variable=Estado_Check_Var, command=lambda: (Entrada_Caso_Estado.configure(state="normal" if Estado_Check_Var.get() else "disabled"), Estado_Var.set(Estado_Var.get() if Estado_Check_Var.get() else Estado_Convertido), Entrada_Caso_Estado.configure(text_color="white" if Estado_Check_Var.get() else "#828282")))
    Entrada_Caso_Estado_Check.place(relx=0.47, rely=0.51, anchor="center")

    Afectados_Var = tk.StringVar(value=Afectados_Original)
    Entrada_Caso_Afectados = CTkOptionMenu(root, text_color="#828282", values=["1", "2", "3", "4", "5", "6", "7", "8"], corner_radius=32, fg_color="#555555", button_color="#404040", dropdown_fg_color="#555555", bg_color="#2d3e50", font=(fuente, 15), width=160, height=17, anchor="w", variable=Afectados_Var, state="disabled")
    Entrada_Caso_Afectados.place(relx=0.75, rely=0.38, anchor="center")
    Afectados_Check_Var = tk.BooleanVar(value=False)
    Entrada_Caso_Afectados_Check = CTkCheckBox(root, text="", variable=Afectados_Check_Var, command=lambda: (Entrada_Caso_Afectados.configure(state="normal" if Afectados_Check_Var.get() else "disabled"), Afectados_Var.set(Afectados_Var.get() if Afectados_Check_Var.get() else Afectados_Original), Entrada_Caso_Afectados.configure(text_color="white" if Afectados_Check_Var.get() else "#828282")))
    Entrada_Caso_Afectados_Check.place(relx=0.97, rely=0.38, anchor="center")

    Fecha_Var = tk.StringVar(value=Fecha_Formateada)
    Entrada_Caso_Fecha = DateEntry(root, textvariable=Fecha_Var, state="disabled", selectmode='day', date_pattern='dd/mm/yyyy', locale='es_ES', background='#12bfbf', foreground='#828282', selectbackground='#5a64ff', selectforeground='white', weekendbackground='#d1d1d1', headersbackground='#049c9c', font=(fuente, 10))
    Entrada_Caso_Fecha.place(relx=0.75, rely=0.25, anchor="center")
    Fecha_Check_Var = tk.BooleanVar(value=False)
    Entrada_Caso_Fecha_Check = CTkCheckBox(root, text="", variable=Fecha_Check_Var, command=lambda: (Entrada_Caso_Fecha.configure(state="normal" if Fecha_Check_Var.get() else "disabled"), Fecha_Var.set(Fecha_Var.get() if Fecha_Check_Var.get() else Fecha_Formateada), Entrada_Caso_Fecha.configure(foreground="white" if Fecha_Check_Var.get() else "#828282")))
    Entrada_Caso_Fecha_Check.place(relx=0.97, rely=0.25, anchor="center")

    Descripcion_Var = tk.StringVar(value=Descripcion_Original)
    Entrada_Caso_Descripcion2 = CTkEntry(root, text_color="#828282", textvariable=Descripcion_Var, state="disabled", font=(fuente, 15), width=160, height=17, fg_color="#555555", bg_color="#2d3e50", corner_radius=20)
    Entrada_Caso_Descripcion2.place(relx=0.75, rely=0.51, anchor="center")
    Descripcion_Check_Var = tk.BooleanVar(value=False)
    Entrada_Caso_Descripcion2_Check = CTkCheckBox(root, text="", variable=Descripcion_Check_Var, command=lambda: (Entrada_Caso_Descripcion2.configure(state="normal" if Descripcion_Check_Var.get() else "disabled"), Descripcion_Var.set(Descripcion_Var.get() if Descripcion_Check_Var.get() else Descripcion_Original), Entrada_Caso_Descripcion2.configure(text_color="white" if Descripcion_Check_Var.get() else "#828282")))
    Entrada_Caso_Descripcion2_Check.place(relx=0.97, rely=0.51, anchor="center")

    Departamento_Var = tk.StringVar(value=Departamento_Convertido)
    Entrada_Caso_Departamento = CTkOptionMenu(root, text_color="#828282", values=["Cundinamarca"], corner_radius=32, fg_color="#555555", button_color="#404040", dropdown_fg_color="#555555", bg_color="#2d3e50", font=(fuente, 15), width=160, height=17, anchor="w", variable=Departamento_Var, state="disabled")
    Entrada_Caso_Departamento.place(relx=0.5, rely=0.65, anchor="center")
    Departamento_Check_Var = tk.BooleanVar(value=False)
    Entrada_Caso_Departamento_Check = CTkCheckBox(root, text="", variable=Departamento_Check_Var, command=lambda: (Entrada_Caso_Departamento.configure(state="normal" if Departamento_Check_Var.get() else "disabled"), Departamento_Var.set(Departamento_Var.get() if Departamento_Check_Var.get() else Departamento_Convertido), Entrada_Caso_Departamento.configure(text_color="white" if Departamento_Check_Var.get() else "#828282")))
    Entrada_Caso_Departamento_Check.place(relx=0.72, rely=0.65, anchor="center")
    Texto_Admin.place(relx=0.015, rely=0.935, anchor="nw")
    Entrada_Contraseña.place(relx=0.5, rely=0.80, anchor="center")

    def salir():
        Entrada_Caso_Departamento.place_forget()
        Entrada_Caso_Descripcion2.place_forget()
        Entrada_Caso_Fecha.place_forget()
        Entrada_Caso_Departamento.place_forget()
        Entrada_Caso_Estado.place_forget()
        Entrada_Caso_Desastre.place_forget()
        Entrada_Caso_Tipo.place_forget()
        Entrada_Caso_Afectados.place_forget()
        Entrada_Caso_Afectados_Check.place_forget()
        Entrada_Caso_Departamento_Check.place_forget()
        Entrada_Caso_Descripcion2_Check.place_forget()
        Entrada_Caso_Fecha_Check.place_forget()
        Entrada_Caso_Departamento_Check.place_forget()
        Entrada_Caso_Estado_Check.place_forget()
        Entrada_Caso_Desastre_Check.place_forget()
        Entrada_Caso_Tipo_Check.place_forget()
        Boton_Funcion_Modificar_Datos_Caso.place_forget()
        Boton_Admin_Volver2.place_forget()
        Boton_Salir.place_forget()
        Grafico_Admin_Casos()

    Boton_Admin_Volver2 = CTkButton(root, width=30, height=35, text="", corner_radius=8, fg_color="#ff7b19", hover_color="#cf5800", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Volver, size=(22, 22)), command=salir)
    Boton_Funcion_Modificar_Datos_Caso.place(relx=0.5, rely=0.89, anchor="center")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Admin_Volver2.place(relx=0.105, rely=0.015, anchor="nw")
def Grafico_Admin_Eliminar_Casos():
    Olvidar_Lugares()
    Texto1.configure(text="Eliminar Caso", font=(fuente, 45))
    Texto2.configure(text="Ingrese el numero de radicado:", font=(fuente, 30))
    Texto3.configure(text="Contraseña:", font=(fuente, 30))
    Texto1.place(relx=0.5, rely=0.15, anchor="center")
    Texto2.place(relx=0.5, rely=0.37, anchor="center")
    Texto3.place(relx=0.5, rely=0.53, anchor="center")
    Texto_Admin.place(relx=0.015, rely=0.935, anchor="nw")
    Boton_Funcion_Eliminar_Caso.place(relx=0.5, rely=0.75, anchor="center")
    Entrada_Contraseña.place(relx=0.5, rely=0.6, anchor="center")
    Entrada_Caso_Radicado.place(relx=0.5, rely=0.44, anchor="center")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Admin_Volver_Casos.place(relx=0.105, rely=0.015, anchor="nw")
def Grafico_Admin_Usuarios():
    Olvidar_Lugares()
    Texto1.configure(text="Usuarios", font=(fuente, 50))
    Texto1.place(relx=0.5, rely=0.20, anchor="center")

    Boton_Admin_Grafico_Usuarios_Buscar.place(relx=0.5, rely=0.40, anchor="center")
    Boton_Admin_Grafico_Usuarios_Crear.place(relx=0.5, rely=0.53, anchor="center")
    Boton_Admin_Grafico_Usuarios_Modificar.place(relx=0.5, rely=0.66, anchor="center")
    Boton_Admin_Grafico_Usuarios_Eliminar.place(relx=0.5, rely=0.79, anchor="center")

    Texto_Admin.place(relx=0.015, rely=0.935, anchor="nw")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Admin_Volver.place(relx=0.105, rely=0.015, anchor="nw")  
def Grafico_Admin_Usuarios_Crear():
    Olvidar_Lugares()
    Texto1.configure(text="CREAR USUARIO", font=(fuente, 45))
    Texto2.configure(text="Primer Nombre", font=(fuente, 18))
    Texto3.configure(text="Segundo Nombre", font=(fuente, 18))
    Texto4.configure(text="Primer Apellido", font=(fuente, 18))
    Texto5.configure(text="Segundo Apellido", font=(fuente, 18))
    Texto6.configure(text="Tipo de documento", font=(fuente, 18))
    Texto7.configure(text="ID", font=(fuente, 18))
    Texto8.configure(text="Fecha de Nacimiento", font=(fuente, 18))
    Texto9.configure(text="Correo", font=(fuente, 18))
    Texto10.configure(text="Departamento", font=(fuente, 18))
    Texto11.configure(text="Ciudad", font=(fuente, 18))
    Texto12.configure(text="Localidad", font=(fuente, 18))
    Texto13.configure(text="Barrio", font=(fuente, 18))
    Texto14.configure(text="Direccion", font=(fuente, 18))
    Texto15.configure(text="Telefono", font=(fuente, 18))
    Texto16.configure(text="Usuario", font=(fuente, 18))
    Texto17.configure(text="Contraseña", font=(fuente, 18))
    Texto1.place(relx=0.5, rely=0.13, anchor="center")
    Texto2.place(relx=0.15, rely=0.27, anchor="center")
    Texto3.place(relx=0.38, rely=0.27, anchor="center")
    Texto4.place(relx=0.61, rely=0.27, anchor="center")
    Texto5.place(relx=0.85, rely=0.27, anchor="center")
    Texto6.place(relx=0.15, rely=0.42, anchor="center")
    Texto7.place(relx=0.38, rely=0.42, anchor="center")
    Texto8.place(relx=0.61, rely=0.42, anchor="center")
    Texto9.place(relx=0.85, rely=0.42, anchor="center")
    Texto10.place(relx=0.15, rely=0.57, anchor="center")
    Texto11.place(relx=0.38, rely=0.57, anchor="center")
    Texto12.place(relx=0.61, rely=0.57, anchor="center")
    Texto13.place(relx=0.85, rely=0.57, anchor="center")
    Texto14.place(relx=0.15, rely=0.72, anchor="center")
    Texto15.place(relx=0.38, rely=0.72, anchor="center")
    Texto16.place(relx=0.61, rely=0.72, anchor="center")
    Texto17.place(relx=0.85, rely=0.72, anchor="center")

    Entrada_Primer_Nombre.place(relx=0.15, rely=0.33, anchor="center")
    Entrada_Segundo_Nombre.place(relx=0.38, rely=0.33, anchor="center")
    Entrada_Primer_Apellido.place(relx=0.61, rely=0.33, anchor="center")
    Entrada_Segundo_Apellido.place(relx=0.85, rely=0.33, anchor="center")
    Entrada_Tipo_Documento.place(relx=0.15, rely=0.48, anchor="center")
    Entrada_Documento.place(relx=0.38, rely=0.48, anchor="center")
    Entrada_Fecha_Nacimento.place(relx=0.61, rely=0.48, anchor="center")
    Entrada_Email.place(relx=0.85, rely=0.48, anchor="center")
    Entrada_Departamento.place(relx=0.15, rely=0.63, anchor="center")
    Entrada_Ciudad.place(relx=0.38, rely=0.63, anchor="center")
    Entrada_Localidad.place(relx=0.61, rely=0.63, anchor="center")
    Entrada_Barrio.place(relx=0.85, rely=0.63, anchor="center")
    Entrada_Direccion.place(relx=0.15, rely=0.78, anchor="center")
    Entrada_Numero.place(relx=0.38, rely=0.78, anchor="center")
    Entrada_Contraseña.place(relx=0.85, rely=0.78, anchor="center")
    Entrada_Usuario.place(relx=0.61, rely=0.78, anchor="center")

    Texto_Admin.place(relx=0.015, rely=0.935, anchor="nw")
    Boton_Funcion_Crear_Usuario2.place(relx=0.5, rely=0.9, anchor="center")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Admin_Volver_Usuarios.place(relx=0.105, rely=0.015, anchor="nw") 
def Grafico_Admin_Eliminar_Usuarios():
    Olvidar_Lugares()
    Texto1.configure(text="Eliminar Usuario:", font=(fuente, 45))
    Texto2.configure(text="Ingrese el numero de identificacion:", font=(fuente, 30))
    Texto3.configure(text="Contraseña:", font=(fuente, 30))
    Texto1.place(relx=0.5, rely=0.15, anchor="center")
    Texto2.place(relx=0.5, rely=0.37, anchor="center")
    Texto3.place(relx=0.5, rely=0.53, anchor="center")
    Texto_Admin.place(relx=0.015, rely=0.935, anchor="nw")
    Boton_Funcion_Eliminar_Usuario.place(relx=0.5, rely=0.75, anchor="center")
    Entrada_Contraseña.place(relx=0.5, rely=0.6, anchor="center")
    Entrada_Usuario_Identificacion.place(relx=0.5, rely=0.44, anchor="center")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Admin_Volver_Usuarios.place(relx=0.105, rely=0.015, anchor="nw")
def Grafico_Usuario_Admin_Buscar():
    Olvidar_Lugares()
    Texto1.configure(text="Buscar Usuario", font=(fuente, 45))
    Texto2.configure(text="Ingrese el numero de identificacion:", font=(fuente, 30))
    Texto1.place(relx=0.5, rely=0.15, anchor="center")
    Texto2.place(relx=0.5, rely=0.4, anchor="center")

    Texto_Admin.place(relx=0.015, rely=0.935, anchor="nw")
    Boton_Funcion_Buscar_Usuario.place(relx=0.5, rely=0.75, anchor="center")
    Entrada_Usuario_Identificacion.place(relx=0.5, rely=0.47, anchor="center")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Admin_Volver_Usuarios.place(relx=0.105, rely=0.015, anchor="nw")
def Grafico_Admin_Usuarios_Buscar_2():
    Olvidar_Lugares()

    Texto38.configure(text="Usuario", font=(fuente, 45))
    Texto1.configure(text=f"{Identificacion}", font=(fuente, 45))
    Texto2.configure(text="ID", font=(fuente, 17))
    Texto3.configure(text="Tipo ID", font=(fuente, 17))
    Texto4.configure(text="Primer Nombre", font=(fuente, 17))
    Texto5.configure(text="Segundo Nombre", font=(fuente, 17))
    Texto6.configure(text="Primer Apellido", font=(fuente, 17))
    Texto7.configure(text="Segundo Apellido", font=(fuente, 17))
    Texto8.configure(text="Usuario", font=(fuente, 17))
    Texto9.configure(text="Rol", font=(fuente, 17))
    Texto10.configure(text="Estado", font=(fuente, 17))
    Texto11.configure(text="Departamento", font=(fuente, 17))
    Texto12.configure(text="Ciudad", font=(fuente, 17))
    Texto13.configure(text="Localidad", font=(fuente, 17))
    Texto14.configure(text="Barrio", font=(fuente, 17))
    Texto15.configure(text="Direccion", font=(fuente, 17))
    Texto16.configure(text="Fecha Nacimiento", font=(fuente, 17))
    Texto17.configure(text="Edad", font=(fuente, 17))
    Texto18.configure(text="Correo", font=(fuente, 17))
    Texto19.configure(text="Telefono", font=(fuente, 17))

    Texto20.configure(text=f"{Busqueda_Documento}", font=(fuente, 18, "bold"))
    Texto21.configure(text=f"{Busqueda_TipoDocumento}", font=(fuente, 18, "bold"))
    Texto22.configure(text=f"{Busqueda_PrimerNombre}", font=(fuente, 18, "bold"))
    Texto23.configure(text=f"{Busqueda_SegundoNombre}", font=(fuente, 18, "bold"))
    Texto24.configure(text=f"{Busqueda_PrimerApellido}", font=(fuente, 18, "bold"))
    Texto25.configure(text=f"{Busqueda_SegundoApellido}", font=(fuente, 18, "bold"))
    Texto26.configure(text=f"{Busqueda_NombreUsuario}", font=(fuente, 18, "bold"))
    Texto27.configure(text=f"{Busqueda_RolUsuario}", font=(fuente, 18, "bold"))
    Texto28.configure(text=f"{Busqueda_EstadoUsuario}", font=(fuente, 18, "bold"))
    Texto29.configure(text=f"{Busqueda_Departamento}", font=(fuente, 18, "bold"))
    Texto30.configure(text=f"{Busqueda_Ciudad}", font=(fuente, 18, "bold"))
    Texto31.configure(text=f"{Busqueda_Localidad}", font=(fuente, 18, "bold"))
    Texto32.configure(text=f"{Busqueda_Barrio}", font=(fuente, 18, "bold"))
    Texto33.configure(text=f"{Busqueda_Direccion}", font=(fuente, 18, "bold"))
    Texto34.configure(text=f"{Busqueda_FechaNacimento}", font=(fuente, 18, "bold"))
    Texto35.configure(text=f"{Busqueda_Edad}", font=(fuente, 18, "bold"))
    Texto36.configure(text=f"{Busqueda_Email}", font=(fuente, 18, "bold"))
    Texto37.configure(text=f"{Busqueda_Telefono}", font=(fuente, 18, "bold"))

    Texto1.place(relx=0.5, rely=0.15, anchor="center")
    Texto38.place(relx=0.5, rely=0.04, anchor="center")
    Texto2.place(relx=0.15, rely=0.23, anchor="center")
    Texto3.place(relx=0.38, rely=0.23, anchor="center")
    Texto4.place(relx=0.61, rely=0.23, anchor="center")
    Texto5.place(relx=0.85, rely=0.23, anchor="center")
    Texto6.place(relx=0.15, rely=0.36, anchor="center")
    Texto7.place(relx=0.38, rely=0.36, anchor="center")
    Texto8.place(relx=0.61, rely=0.36, anchor="center")
    Texto9.place(relx=0.85, rely=0.36, anchor="center")
    Texto10.place(relx=0.15, rely=0.49, anchor="center")
    Texto11.place(relx=0.38, rely=0.49, anchor="center")
    Texto12.place(relx=0.61, rely=0.49, anchor="center")
    Texto13.place(relx=0.85, rely=0.49, anchor="center")
    Texto14.place(relx=0.15, rely=0.62, anchor="center")
    Texto15.place(relx=0.38, rely=0.62, anchor="center")
    Texto16.place(relx=0.61, rely=0.62, anchor="center")
    Texto17.place(relx=0.85, rely=0.62, anchor="center")
    Texto18.place(relx=0.5, rely=0.75, anchor="center")
    Texto19.place(relx=0.5, rely=0.88, anchor="center")

    Texto20.place(relx=0.15, rely=0.28, anchor="center")
    Texto21.place(relx=0.38, rely=0.28, anchor="center")
    Texto22.place(relx=0.61, rely=0.28, anchor="center")
    Texto23.place(relx=0.85, rely=0.28, anchor="center")
    Texto24.place(relx=0.15, rely=0.41, anchor="center")
    Texto25.place(relx=0.38, rely=0.41, anchor="center")
    Texto26.place(relx=0.61, rely=0.41, anchor="center")
    Texto27.place(relx=0.85, rely=0.41, anchor="center")
    Texto28.place(relx=0.15, rely=0.54, anchor="center")
    Texto29.place(relx=0.38, rely=0.54, anchor="center")
    Texto30.place(relx=0.61, rely=0.54, anchor="center")
    Texto31.place(relx=0.85, rely=0.54, anchor="center")
    Texto32.place(relx=0.15, rely=0.67, anchor="center")
    Texto33.place(relx=0.38, rely=0.67, anchor="center")
    Texto34.place(relx=0.61, rely=0.67, anchor="center")
    Texto35.place(relx=0.85, rely=0.67, anchor="center")
    Texto36.place(relx=0.5, rely=0.80, anchor="center")
    Texto37.place(relx=0.5, rely=0.93, anchor="center")

    Texto_Admin.place(relx=0.015, rely=0.935, anchor="nw")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Admin_Volver_Usuarios.place(relx=0.105, rely=0.015, anchor="nw")
def Grafico_Admin_Modificar_Usuarios_Buscar():
    Olvidar_Lugares()
    Texto1.configure(text="Buscar Usuario", font=(fuente, 45))
    Texto2.configure(text="Ingrese el numero de identificacion:", font=(fuente, 30))
    Texto1.place(relx=0.5, rely=0.15, anchor="center")
    Texto2.place(relx=0.5, rely=0.4, anchor="center")
    Texto_Admin.place(relx=0.015, rely=0.935, anchor="nw")
    Boton_Funcion_Buscar_Usuario2.place(relx=0.5, rely=0.75, anchor="center")
    Entrada_Usuario_Identificacion.place(relx=0.5, rely=0.47, anchor="center")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Admin_Volver_Usuarios.place(relx=0.105, rely=0.015, anchor="nw")
def Grafico_Admin_Modificar_Usuarios():
    global Boton_Admin_Volver3, Entrada_Usuario_Modificar_Documento, Entrada_Usuario_Modificar_Documento_Check, Entrada_Usuario_Modificar_TipoIdentificacion, Entrada_Usuario_Modificar_TipoIdentificacion_Check, Entrada_Usuario_Modificar_PrimerNombre, Entrada_Usuario_Modificar_PrimerNombre_Check, Entrada_Usuario_Modificar_SegundoNombre, Entrada_Usuario_Modificar_SegundoNombre_Check, Entrada_Usuario_Modificar_PrimerApellido, Entrada_Usuario_Modificar_PrimerApellido_Check, Entrada_Usuario_Modificar_SegundoApellido, Entrada_Usuario_Modificar_SegundoApellido_Check, Entrada_Usuario_Modificar_NombreUsuario, Entrada_Usuario_Modificar_NombreUsuario_Check, Entrada_Usuario_Modificar_RolUsuario, Entrada_Usuario_Modificar_RolUsuario_Check, Entrada_Usuario_Modificar_EstadoUsuario, Entrada_Usuario_Modificar_EstadoUsuario_Check, Entrada_Usuario_Modificar_Departamento_Normal, Entrada_Usuario_Modificar_Departamento_Normal_Check, Entrada_Usuario_Modificar_Ciudad, Entrada_Usuario_Modificar_Ciudad_Check, Entrada_Usuario_Modificar_Localidad, Entrada_Usuario_Modificar_Localidad_Check, Entrada_Usuario_Modificar_Barrio, Entrada_Usuario_Modificar_Barrio_Check, Entrada_Usuario_Modificar_Direccion, Entrada_Usuario_Modificar_Direccion_Check, Entrada_Caso_Nacimiento, Entrada_Caso_Nacimiento_Check, Entrada_Usuario_Modificar_Telefono, Entrada_Usuario_Modificar_Telefono_Check, Entrada_Usuario_Modificar_Email, Entrada_Usuario_Modificar_Email_Check 
    Olvidar_Lugares()
    lista_barrios, lista_localidades, lista_ciudades = Funcion_Cargar_GPS()
    Texto1.configure(text="Seleccione una casilla", font=(fuente, 35))
    Texto1.place(relx=0.5, rely=0.05, anchor="center")
    Texto38.configure(text="para modificar ese dato", font=(fuente, 35))
    Texto38.place(relx=0.5, rely=0.12, anchor="center")

    Texto2.configure(text="ID", font=(fuente, 15))
    Texto3.configure(text="Tipo ID", font=(fuente, 15))
    Texto4.configure(text="Primer Nombre", font=(fuente, 15))
    Texto5.configure(text="Segundo Nombre", font=(fuente, 15))
    Texto6.configure(text="Primer Apellido", font=(fuente, 15))
    Texto7.configure(text="Segundo Apellido", font=(fuente, 15))
    Texto8.configure(text="Usuario", font=(fuente, 15))
    Texto9.configure(text="Rol", font=(fuente, 15))
    Texto10.configure(text="Estado", font=(fuente, 15))
    Texto11.configure(text="Departamento", font=(fuente, 15))
    Texto12.configure(text="Ciudad", font=(fuente, 15))
    Texto13.configure(text="Localidad", font=(fuente, 15))
    Texto14.configure(text="Barrio", font=(fuente, 15))
    Texto15.configure(text="Direccion", font=(fuente, 15))
    Texto16.configure(text="Fecha Nacimiento", font=(fuente, 15))
    Texto17.configure(text="Telefono", font=(fuente, 15))
    Texto18.configure(text="Correo", font=(fuente, 15))
    Texto19.configure(text="Contraseña", font=(fuente, 15))
    Texto2.place(relx=0.15, rely=0.21, anchor="center")
    Texto3.place(relx=0.38, rely=0.21, anchor="center")
    Texto4.place(relx=0.61, rely=0.21, anchor="center")
    Texto5.place(relx=0.85, rely=0.21, anchor="center")
    Texto6.place(relx=0.15, rely=0.34, anchor="center")
    Texto7.place(relx=0.38, rely=0.34, anchor="center")
    Texto8.place(relx=0.61, rely=0.34, anchor="center")
    Texto9.place(relx=0.85, rely=0.34, anchor="center")
    Texto10.place(relx=0.15, rely=0.47, anchor="center")
    Texto11.place(relx=0.38, rely=0.47, anchor="center")
    Texto12.place(relx=0.61, rely=0.47, anchor="center")
    Texto13.place(relx=0.85, rely=0.47, anchor="center")
    Texto14.place(relx=0.15, rely=0.60, anchor="center")
    Texto15.place(relx=0.38, rely=0.60, anchor="center")
    Texto16.place(relx=0.61, rely=0.60, anchor="center")
    Texto17.place(relx=0.85, rely=0.60, anchor="center")
    Texto18.place(relx=0.265, rely=0.75, anchor="center")
    Texto19.place(relx=0.73, rely=0.75, anchor="center")

    Documento_Var = tk.StringVar(value=Documento_Normal)
    Entrada_Usuario_Modificar_Documento = CTkEntry(root, text_color="#828282", textvariable=Documento_Var, state="disabled", font=(fuente, 13), width=130, fg_color="#555555", bg_color ="#2d3e50", corner_radius=20)
    Entrada_Usuario_Modificar_Documento.place(relx=0.15, rely=0.25, anchor="center")
    Documento_Check_Var = tk.BooleanVar(value=False)
    Entrada_Usuario_Modificar_Documento_Check = CTkCheckBox(root, height=10, width=10, text="", variable=Documento_Check_Var, command=lambda: (Entrada_Usuario_Modificar_Documento.configure(state="normal" if Documento_Check_Var.get() else "disabled"), Documento_Var.set(Documento_Var.get() if Documento_Check_Var.get() else Documento_Normal), Entrada_Usuario_Modificar_Documento.configure(text_color="white" if Documento_Check_Var.get() else "#828282")))
    Entrada_Usuario_Modificar_Documento_Check.place(relx=0.15, rely=0.30, anchor="center")

    TipoIdentificacion = tk.StringVar(value=TipoDocumento_Convertido)
    Entrada_Usuario_Modificar_TipoIdentificacion = CTkOptionMenu(root, text_color="#828282", values=["Cedula Ciudadania","Cedula Extranjeria", "Pasaporte", "Tarjeta de identidad"], corner_radius=32, fg_color="#555555", button_color="#404040", dropdown_fg_color="#555555", bg_color="#2d3e50", font=(fuente, 12), width=100, anchor="w", variable=TipoIdentificacion, state="disabled")
    Entrada_Usuario_Modificar_TipoIdentificacion.place(relx=0.38, rely=0.25, anchor="center")
    TipoIdentificacion_Check_Var = tk.BooleanVar(value=False)
    Entrada_Usuario_Modificar_TipoIdentificacion_Check = CTkCheckBox(root, height=10, width=10, text="", variable=TipoIdentificacion_Check_Var, command=lambda: (Entrada_Usuario_Modificar_TipoIdentificacion.configure(state="normal" if TipoIdentificacion_Check_Var.get() else "disabled"), TipoIdentificacion.set(TipoIdentificacion.get() if TipoIdentificacion_Check_Var.get() else TipoDocumento_Convertido), Entrada_Usuario_Modificar_TipoIdentificacion.configure(text_color="white" if TipoIdentificacion_Check_Var.get() else "#828282")))
    Entrada_Usuario_Modificar_TipoIdentificacion_Check.place(relx=0.38, rely=0.30, anchor="center")

    PrimerNombre_Var = tk.StringVar(value=PrimerNombre_Normal)
    Entrada_Usuario_Modificar_PrimerNombre = CTkEntry(root, text_color="#828282", textvariable=PrimerNombre_Var, state="disabled", font=(fuente, 13), width=130, fg_color="#555555", bg_color ="#2d3e50", corner_radius=20)
    Entrada_Usuario_Modificar_PrimerNombre.place(relx=0.61, rely=0.25, anchor="center")
    PrimerNombre_Check_Var = tk.BooleanVar(value=False)
    Entrada_Usuario_Modificar_PrimerNombre_Check = CTkCheckBox(root, height=10, width=10, text="", variable=PrimerNombre_Check_Var, command=lambda: (Entrada_Usuario_Modificar_PrimerNombre.configure(state="normal" if PrimerNombre_Check_Var.get() else "disabled"), PrimerNombre_Var.set(PrimerNombre_Var.get() if PrimerNombre_Check_Var.get() else PrimerNombre_Normal), Entrada_Usuario_Modificar_PrimerNombre.configure(text_color="white" if PrimerNombre_Check_Var.get() else "#828282")))
    Entrada_Usuario_Modificar_PrimerNombre_Check.place(relx=0.61, rely=0.30, anchor="center")

    SegundoNombre_Var = tk.StringVar(value=SegundoNombre_Normal)
    Entrada_Usuario_Modificar_SegundoNombre = CTkEntry(root, text_color="#828282", textvariable=SegundoNombre_Var, state="disabled", font=(fuente, 13), width=130, fg_color="#555555", bg_color ="#2d3e50", corner_radius=20)
    Entrada_Usuario_Modificar_SegundoNombre.place(relx=0.85, rely=0.25, anchor="center")
    SegundoNombre_Check_Var = tk.BooleanVar(value=False)
    Entrada_Usuario_Modificar_SegundoNombre_Check = CTkCheckBox(root, height=10, width=10, text="", variable=SegundoNombre_Check_Var, command=lambda: (Entrada_Usuario_Modificar_SegundoNombre.configure(state="normal" if SegundoNombre_Check_Var.get() else "disabled"), SegundoNombre_Var.set(SegundoNombre_Var.get() if SegundoNombre_Check_Var.get() else SegundoNombre_Normal), Entrada_Usuario_Modificar_SegundoNombre.configure(text_color="white" if SegundoNombre_Check_Var.get() else "#828282")))
    Entrada_Usuario_Modificar_SegundoNombre_Check.place(relx=0.85, rely=0.30, anchor="center")

    PrimerApellido_Var = tk.StringVar(value=PrimerApellido_Normal)
    Entrada_Usuario_Modificar_PrimerApellido = CTkEntry(root, text_color="#828282", textvariable=PrimerApellido_Var, state="disabled", font=(fuente, 13), width=130, fg_color="#555555", bg_color ="#2d3e50", corner_radius=20)
    Entrada_Usuario_Modificar_PrimerApellido.place(relx=0.15, rely=0.38, anchor="center")
    PrimerApellido_Check_Var = tk.BooleanVar(value=False)
    Entrada_Usuario_Modificar_PrimerApellido_Check = CTkCheckBox(root, height=10, width=10, text="", variable=PrimerApellido_Check_Var, command=lambda: (Entrada_Usuario_Modificar_PrimerApellido.configure(state="normal" if PrimerApellido_Check_Var.get() else "disabled"), PrimerApellido_Var.set(PrimerApellido_Var.get() if PrimerApellido_Check_Var.get() else PrimerApellido_Normal), Entrada_Usuario_Modificar_PrimerApellido.configure(text_color="white" if PrimerApellido_Check_Var.get() else "#828282")))
    Entrada_Usuario_Modificar_PrimerApellido_Check.place(relx=0.15, rely=0.43, anchor="center")

    SegundoApellido_Var = tk.StringVar(value=SegundoApellido_Normal)
    Entrada_Usuario_Modificar_SegundoApellido = CTkEntry(root, text_color="#828282", textvariable=SegundoApellido_Var, state="disabled", font=(fuente, 13), width=130, fg_color="#555555", bg_color ="#2d3e50", corner_radius=20)
    Entrada_Usuario_Modificar_SegundoApellido.place(relx=0.38, rely=0.38, anchor="center")
    SegundoApellido_Check_Var = tk.BooleanVar(value=False)
    Entrada_Usuario_Modificar_SegundoApellido_Check = CTkCheckBox(root, height=10, width=10, text="", variable=SegundoApellido_Check_Var, command=lambda: (Entrada_Usuario_Modificar_SegundoApellido.configure(state="normal" if SegundoApellido_Check_Var.get() else "disabled"), SegundoApellido_Var.set(SegundoApellido_Var.get() if SegundoApellido_Check_Var.get() else SegundoApellido_Normal), Entrada_Usuario_Modificar_SegundoApellido.configure(text_color="white" if SegundoApellido_Check_Var.get() else "#828282")))
    Entrada_Usuario_Modificar_SegundoApellido_Check.place(relx=0.38, rely=0.43, anchor="center")

    NombreUsuario_Var = tk.StringVar(value=NombreUsuario_Normal)
    Entrada_Usuario_Modificar_NombreUsuario = CTkEntry(root, text_color="#828282", textvariable=NombreUsuario_Var, state="disabled", font=(fuente, 13), width=130, fg_color="#555555", bg_color ="#2d3e50", corner_radius=20)
    Entrada_Usuario_Modificar_NombreUsuario.place(relx=0.61, rely=0.38, anchor="center")
    NombreUsuario_Check_Var = tk.BooleanVar(value=False)
    Entrada_Usuario_Modificar_NombreUsuario_Check = CTkCheckBox(root, height=10, width=10, text="", variable=NombreUsuario_Check_Var, command=lambda: (Entrada_Usuario_Modificar_NombreUsuario.configure(state="normal" if NombreUsuario_Check_Var.get() else "disabled"), NombreUsuario_Var.set(NombreUsuario_Var.get() if NombreUsuario_Check_Var.get() else NombreUsuario_Normal), Entrada_Usuario_Modificar_NombreUsuario.configure(text_color="white" if NombreUsuario_Check_Var.get() else "#828282")))
    Entrada_Usuario_Modificar_NombreUsuario_Check.place(relx=0.61, rely=0.43, anchor="center")

    RolUsuario_Var = tk.StringVar(value=Rol_Convertido)
    Entrada_Usuario_Modificar_RolUsuario = CTkOptionMenu(root, text_color="#828282", values=["Usuario", "Administrador"], corner_radius=32, fg_color="#555555", button_color="#404040", dropdown_fg_color="#555555", bg_color="#2d3e50", font=(fuente, 12), width=100, anchor="w", variable=RolUsuario_Var, state="disabled")
    Entrada_Usuario_Modificar_RolUsuario.place(relx=0.85, rely=0.38, anchor="center")
    RolUsuario_Check_Var = tk.BooleanVar(value=False)
    Entrada_Usuario_Modificar_RolUsuario_Check = CTkCheckBox(root, height=10, width=10, text="", variable=RolUsuario_Check_Var, command=lambda: (Entrada_Usuario_Modificar_RolUsuario.configure(state="normal" if RolUsuario_Check_Var.get() else "disabled"), RolUsuario_Var.set(RolUsuario_Var.get() if RolUsuario_Check_Var.get() else Rol_Convertido), Entrada_Usuario_Modificar_RolUsuario.configure(text_color="white" if RolUsuario_Check_Var.get() else "#828282")))
    Entrada_Usuario_Modificar_RolUsuario_Check.place(relx=0.85, rely=0.43, anchor="center")

    EstadoUsuario_Var = tk.StringVar(value=Estado_Convertido)
    Entrada_Usuario_Modificar_EstadoUsuario = CTkOptionMenu(root, text_color="#828282", values=["Usuario Activo", "Usuario Inactivo"], corner_radius=32, fg_color="#555555", button_color="#404040", dropdown_fg_color="#555555", bg_color="#2d3e50", font=(fuente, 12), width=100, anchor="w", variable=EstadoUsuario_Var, state="disabled")
    Entrada_Usuario_Modificar_EstadoUsuario.place(relx=0.15, rely=0.51, anchor="center")
    EstadoUsuario_Check_Var = tk.BooleanVar(value=False)
    Entrada_Usuario_Modificar_EstadoUsuario_Check = CTkCheckBox(root, height=10, width=10, text="", variable=EstadoUsuario_Check_Var, command=lambda: (Entrada_Usuario_Modificar_EstadoUsuario.configure(state="normal" if EstadoUsuario_Check_Var.get() else "disabled"), EstadoUsuario_Var.set(EstadoUsuario_Var.get() if EstadoUsuario_Check_Var.get() else Estado_Convertido), Entrada_Usuario_Modificar_EstadoUsuario.configure(text_color="white" if EstadoUsuario_Check_Var.get() else "#828282")))
    Entrada_Usuario_Modificar_EstadoUsuario_Check.place(relx=0.15, rely=0.56, anchor="center")

    Departamento_Normal_Var = tk.StringVar(value=Departamento_Normal)
    Entrada_Usuario_Modificar_Departamento_Normal = CTkOptionMenu(root, text_color="#828282", values=["Cundinamarca"], corner_radius=32, fg_color="#555555", button_color="#404040", dropdown_fg_color="#555555", bg_color="#2d3e50", font=(fuente, 12), width=100, anchor="w", variable=Departamento_Normal_Var, state="disabled")
    Entrada_Usuario_Modificar_Departamento_Normal.place(relx=0.38, rely=0.51, anchor="center")
    Departamento_Normal_Check_Var = tk.BooleanVar(value=False)
    Entrada_Usuario_Modificar_Departamento_Normal_Check = CTkCheckBox(root, height=10, width=10, text="", variable=Departamento_Normal_Check_Var, command=lambda: (Entrada_Usuario_Modificar_Departamento_Normal.configure(state="normal" if Departamento_Normal_Check_Var.get() else "disabled"), Departamento_Normal_Var.set(Departamento_Normal_Var.get() if Departamento_Normal_Check_Var.get() else Departamento_Normal), Entrada_Usuario_Modificar_Departamento_Normal.configure(text_color="white" if Departamento_Normal_Check_Var.get() else "#828282")))
    Entrada_Usuario_Modificar_Departamento_Normal_Check.place(relx=0.38, rely=0.56, anchor="center")

    Ciudad_Var = tk.StringVar(value=Ciudad_Normal)
    Entrada_Usuario_Modificar_Ciudad = CTkOptionMenu(root, text_color="#828282", values=lista_ciudades, corner_radius=32, fg_color="#555555", button_color="#404040", dropdown_fg_color="#555555", bg_color="#2d3e50", font=(fuente, 12), width=100, anchor="w", variable=Ciudad_Var, state="disabled")
    Entrada_Usuario_Modificar_Ciudad.place(relx=0.61, rely=0.51, anchor="center")
    Ciudad_Check_Var = tk.BooleanVar(value=False)
    Entrada_Usuario_Modificar_Ciudad_Check = CTkCheckBox(root, height=10, width=10, text="", variable=Ciudad_Check_Var, command=lambda: (Entrada_Usuario_Modificar_Ciudad.configure(state="normal" if Ciudad_Check_Var.get() else "disabled"), Ciudad_Var.set(Ciudad_Var.get() if Ciudad_Check_Var.get() else Ciudad_Normal), Entrada_Usuario_Modificar_Ciudad.configure(text_color="white" if Ciudad_Check_Var.get() else "#828282")))
    Entrada_Usuario_Modificar_Ciudad_Check.place(relx=0.61, rely=0.56, anchor="center")

    Localidad_Var = tk.StringVar(value=Localidad_Normal)
    Entrada_Usuario_Modificar_Localidad = CTkOptionMenu(root, text_color="#828282", values=lista_localidades, corner_radius=32, fg_color="#555555", button_color="#404040", dropdown_fg_color="#555555", bg_color="#2d3e50", font=(fuente, 12), width=100, anchor="w", variable=Localidad_Var, state="disabled")
    Entrada_Usuario_Modificar_Localidad.place(relx=0.85, rely=0.51, anchor="center")
    Localidad_Check_Var = tk.BooleanVar(value=False)
    Entrada_Usuario_Modificar_Localidad_Check = CTkCheckBox(root, height=10, width=10, text="", variable=Localidad_Check_Var, command=lambda: (Entrada_Usuario_Modificar_Localidad.configure(state="normal" if Localidad_Check_Var.get() else "disabled"), Localidad_Var.set(Localidad_Var.get() if Localidad_Check_Var.get() else Localidad_Normal), Entrada_Usuario_Modificar_Localidad.configure(text_color="white" if Localidad_Check_Var.get() else "#828282")))
    Entrada_Usuario_Modificar_Localidad_Check.place(relx=0.85, rely=0.56, anchor="center")

    Barrio_Var = tk.StringVar(value=Barrio_Normal)
    Entrada_Usuario_Modificar_Barrio = CTkOptionMenu(root, text_color="#828282", values=lista_barrios, corner_radius=32, fg_color="#555555", button_color="#404040", dropdown_fg_color="#555555", bg_color="#2d3e50", font=(fuente, 12), width=100, anchor="w", variable=Barrio_Var, state="disabled")
    Entrada_Usuario_Modificar_Barrio.place(relx=0.15, rely=0.65, anchor="center")
    Barrio_Check_Var = tk.BooleanVar(value=False)
    Entrada_Usuario_Modificar_Barrio_Check = CTkCheckBox(root, height=10, width=10, text="", variable=Barrio_Check_Var, command=lambda: (Entrada_Usuario_Modificar_Barrio.configure(state="normal" if Barrio_Check_Var.get() else "disabled"), Barrio_Var.set(Barrio_Var.get() if Barrio_Check_Var.get() else Barrio_Normal), Entrada_Usuario_Modificar_Barrio.configure(text_color="white" if Barrio_Check_Var.get() else "#828282")))
    Entrada_Usuario_Modificar_Barrio_Check.place(relx=0.15, rely=0.71, anchor="center")

    Direccion_Var = tk.StringVar(value=Direccion_Normal)
    Entrada_Usuario_Modificar_Direccion = CTkEntry(root, text_color="#828282", textvariable=Direccion_Var, state="disabled", font=(fuente, 13), width=130, fg_color="#555555", bg_color ="#2d3e50", corner_radius=20)
    Entrada_Usuario_Modificar_Direccion.place(relx=0.38, rely=0.65, anchor="center")
    Direccion_Check_Var = tk.BooleanVar(value=False)
    Entrada_Usuario_Modificar_Direccion_Check = CTkCheckBox(root, height=10, width=10, text="", variable=Direccion_Check_Var, command=lambda: (Entrada_Usuario_Modificar_Direccion.configure(state="normal" if Direccion_Check_Var.get() else "disabled"), Direccion_Var.set(Direccion_Var.get() if Direccion_Check_Var.get() else Direccion_Normal), Entrada_Usuario_Modificar_Direccion.configure(text_color="white" if Direccion_Check_Var.get() else "#828282")))
    Entrada_Usuario_Modificar_Direccion_Check.place(relx=0.38, rely=0.71, anchor="center")

    Nacimiento_Var = tk.StringVar(value=Nacimiento_Formateada)
    Entrada_Caso_Nacimiento = DateEntry(root, textvariable=Nacimiento_Var, state="disabled", selectmode='day', date_pattern='dd/mm/yyyy', locale='es_ES', background='#12bfbf', foreground='#828282', selectbackground='#5a64ff', selectforeground='white', weekendbackground='#d1d1d1', headersbackground='#049c9c', font=(fuente, 10))
    Entrada_Caso_Nacimiento.place(relx=0.61, rely=0.65, anchor="center")
    Nacimiento_Check_Var = tk.BooleanVar(value=False)
    Entrada_Caso_Nacimiento_Check = CTkCheckBox(root, height=10, width=10, text="", variable=Nacimiento_Check_Var, command=lambda: (Entrada_Caso_Nacimiento.configure(state="normal" if Nacimiento_Check_Var.get() else "disabled"), Nacimiento_Var.set(Nacimiento_Var.get() if Nacimiento_Check_Var.get() else Nacimiento_Formateada), Entrada_Caso_Nacimiento.configure(foreground="white" if Nacimiento_Check_Var.get() else "#828282")))
    Entrada_Caso_Nacimiento_Check.place(relx=0.61, rely=0.71, anchor="center")

    Telefono_Var = tk.StringVar(value=Telefono_Normal)
    Entrada_Usuario_Modificar_Telefono = CTkEntry(root, text_color="#828282", textvariable=Telefono_Var, state="disabled", font=(fuente, 13), width=130, fg_color="#555555", bg_color ="#2d3e50", corner_radius=20)
    Entrada_Usuario_Modificar_Telefono.place(relx=0.85, rely=0.65, anchor="center")
    Telefono_Check_Var = tk.BooleanVar(value=False)
    Entrada_Usuario_Modificar_Telefono_Check = CTkCheckBox(root, height=10, width=10, text="", variable=Telefono_Check_Var, command=lambda: (Entrada_Usuario_Modificar_Telefono.configure(state="normal" if Telefono_Check_Var.get() else "disabled"), Telefono_Var.set(Telefono_Var.get() if Telefono_Check_Var.get() else Telefono_Normal), Entrada_Usuario_Modificar_Telefono.configure(text_color="white" if Telefono_Check_Var.get() else "#828282")))
    Entrada_Usuario_Modificar_Telefono_Check.place(relx=0.85, rely=0.71, anchor="center")

    Email_Var = tk.StringVar(value=Email_Normal)
    Entrada_Usuario_Modificar_Email = CTkEntry(root, text_color="#828282", textvariable=Email_Var, state="disabled", font=(fuente, 13), width=130, fg_color="#555555", bg_color ="#2d3e50", corner_radius=20)
    Entrada_Usuario_Modificar_Email.place(relx=0.265, rely=0.79, anchor="center")
    Email_Check_Var = tk.BooleanVar(value=False)
    Entrada_Usuario_Modificar_Email_Check = CTkCheckBox(root, height=10, width=10, text="", variable=Email_Check_Var, command=lambda: (Entrada_Usuario_Modificar_Email.configure(state="normal" if Email_Check_Var.get() else "disabled"), Email_Var.set(Email_Var.get() if Email_Check_Var.get() else Email_Normal), Entrada_Usuario_Modificar_Email.configure(text_color="white" if Email_Check_Var.get() else "#828282")))
    Entrada_Usuario_Modificar_Email_Check.place(relx=0.265, rely=0.84, anchor="center")

    Texto_Admin.place(relx=0.015, rely=0.935, anchor="nw")
    Entrada_Contraseña.place(relx=0.73, rely=0.80, anchor="center")

    def salir():
        Entrada_Usuario_Modificar_Documento.place_forget()
        Entrada_Usuario_Modificar_Documento_Check.place_forget()
        Entrada_Usuario_Modificar_TipoIdentificacion.place_forget()
        Entrada_Usuario_Modificar_TipoIdentificacion_Check.place_forget()
        Entrada_Usuario_Modificar_PrimerNombre.place_forget()
        Entrada_Usuario_Modificar_PrimerNombre_Check.place_forget()
        Entrada_Usuario_Modificar_SegundoNombre.place_forget()
        Entrada_Usuario_Modificar_SegundoNombre_Check.place_forget()
        Entrada_Usuario_Modificar_PrimerApellido.place_forget()
        Entrada_Usuario_Modificar_PrimerApellido_Check.place_forget()
        Entrada_Usuario_Modificar_SegundoApellido.place_forget()
        Entrada_Usuario_Modificar_SegundoApellido_Check.place_forget()
        Entrada_Usuario_Modificar_NombreUsuario.place_forget()
        Entrada_Usuario_Modificar_NombreUsuario_Check.place_forget()
        Entrada_Usuario_Modificar_RolUsuario.place_forget()
        Entrada_Usuario_Modificar_RolUsuario_Check.place_forget()
        Entrada_Usuario_Modificar_EstadoUsuario.place_forget()
        Entrada_Usuario_Modificar_EstadoUsuario_Check.place_forget()
        Entrada_Usuario_Modificar_Departamento_Normal.place_forget()
        Entrada_Usuario_Modificar_Departamento_Normal_Check.place_forget()
        Entrada_Usuario_Modificar_Ciudad.place_forget()
        Entrada_Usuario_Modificar_Ciudad_Check.place_forget()
        Entrada_Usuario_Modificar_Localidad.place_forget()
        Entrada_Usuario_Modificar_Localidad_Check.place_forget()
        Entrada_Usuario_Modificar_Barrio.place_forget()
        Entrada_Usuario_Modificar_Barrio_Check.place_forget()
        Entrada_Usuario_Modificar_Direccion.place_forget()
        Entrada_Usuario_Modificar_Direccion_Check.place_forget()
        Entrada_Caso_Nacimiento.place_forget()
        Entrada_Caso_Nacimiento_Check.place_forget()
        Entrada_Usuario_Modificar_Telefono.place_forget()
        Entrada_Usuario_Modificar_Telefono_Check.place_forget()
        Entrada_Usuario_Modificar_Email.place_forget()
        Entrada_Usuario_Modificar_Email_Check.place_forget()
        Boton_Funcion_Modificar_Datos_Caso.place_forget()
        Boton_Salir.place_forget()
        Boton_Funcion_Modificar_Datos_Usuario5.place_forget()
        Grafico_Admin_Usuarios()

    Boton_Admin_Volver3 = CTkButton(root, width=30, height=35, text="", corner_radius=8, fg_color="#ff7b19", hover_color="#cf5800", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Volver, size=(22, 22)), command=salir)
    Boton_Funcion_Modificar_Datos_Usuario5.place(relx=0.5, rely=0.92, anchor="center")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Admin_Volver3.place(relx=0.105, rely=0.015, anchor="nw")
def Grafico_Recuperar_Contraseña():
    Olvidar_Lugares()
    Texto1.configure(text="Recuperar", font=(fuente, 45))
    Texto2.configure(text="Ingrese el usuario:", font=(fuente, 30))
    Texto1.place(relx=0.5, rely=0.15, anchor="center")
    Texto2.place(relx=0.5, rely=0.4, anchor="center")
    Boton_Funcion_Recuperar_Contraseña.place(relx=0.5, rely=0.75, anchor="center")
    Entrada_Usuario.place(relx=0.5, rely=0.47, anchor="center")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Volver.place(relx=0.105, rely=0.015, anchor="nw")
def Grafico_Recuperar_Contraseña2():
    Olvidar_Lugares()
    Texto1.configure(text="Modificar", font=(fuente, 55))
    Texto2.configure(text="contraseña", font=(fuente, 55))
    Texto3.configure(text="Ingrese el UUID:", font=(fuente, 22))
    Texto4.configure(text="Nueva Contraseña", font=(fuente, 22))

    Texto1.place(relx=0.5, rely=0.15, anchor="center")
    Texto2.place(relx=0.5, rely=0.26, anchor="center")

    Texto3.place(relx=0.5, rely=0.37, anchor="center")
    Texto4.place(relx=0.5, rely=0.52, anchor="center")

    Entrada_UUID.place(relx=0.5, rely=0.43, anchor="center")
    Entrada_Contraseña_Nueva.place(relx=0.5, rely=0.59, anchor="center")

    Imagen_Grafico_Login_Contraseña.place(relx=0.33, rely=0.42, anchor="center")
    Imagen_Grafico_Modificar_Contraseña.place(relx=0.33, rely=0.58, anchor="center")

    Boton_Funcion_Recuperar_Contraseña2.place(relx=0.5, rely=0.76, anchor="center")
    Boton_Salir.place(relx=0.015, rely=0.015, anchor="nw")
    Boton_Volver.place(relx=0.105, rely=0.015, anchor="nw")
#=======FONDO==================================================
Imagen_Fondo = tk.Label(root, image=imagenL, bg="#2d3e50")
Imagen_Fondo.place(relx=1.01, rely=-0.01, anchor="ne")
#===========BOTONES====================================
Boton_Salir = CTkButton(root, width=30, height=35, text="", corner_radius= 8, fg_color="#ff1919", hover_color="#be0000", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Salir, size=(22, 22)), command=root.quit) 
Boton_Volver = CTkButton(root, width=30, height=35, text="", corner_radius= 8, fg_color="#ff7b19", hover_color="#cf5800", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Volver, size=(22, 22)), command=Grafico_Inicio)
Boton_Usuario_Volver = CTkButton(root, width=30, height=35, text="", corner_radius= 8, fg_color="#ff7b19", hover_color="#cf5800", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Volver, size=(22, 22)), command=Grafico_Usuario_Inicio)
Boton_Admin_Volver = CTkButton(root, width=30, height=35, text="", corner_radius= 8, fg_color="#ff7b19", hover_color="#cf5800", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Volver, size=(22, 22)), command=Grafico_Admin_Inicio)
Boton_Admin_Volver_Casos = CTkButton(root, width=30, height=35, text="", corner_radius= 8, fg_color="#ff7b19", hover_color="#cf5800", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Volver, size=(22, 22)), command=Grafico_Admin_Casos)
Boton_Admin_Volver_Usuarios = CTkButton(root, width=30, height=35, text="", corner_radius= 8, fg_color="#ff7b19", hover_color="#cf5800", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Volver, size=(22, 22)), command=Grafico_Admin_Usuarios)
Boton_Usuario_Casos_Volver = CTkButton(root, width=30, height=35, text="", corner_radius= 8, fg_color="#ff7b19", hover_color="#cf5800", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Volver, size=(22, 22)), command=Grafico_Usuario_Casos) 
Boton_Usuario_Cuenta_Volver = CTkButton(root, width=30, height=35, text="", corner_radius= 8, fg_color="#ff7b19", hover_color="#cf5800", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Volver, size=(22, 22)), command=Grafico_Usuario_Cuenta) 
Boton_Emergencia = CTkButton(root, image=CTkImage(dark_image=Imagen_Boton_Emergencia, size=(70, 70)), hover_color="#2d3e50", text="", width=40, height=40, bg_color="#2d3e50", fg_color="#2d3e50", command=Grafico_Emergencia)
Boton_Inicio_Login = CTkButton(root, width=300, height=70, text_color="white", text="Iniciar Sesion", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Login, size=(30, 40)), command=Grafico_Login)
Boton_Inicio_Recuperar = CTkButton(root, width=255, height=70, text_color="white", text="Recuperar Contraseña", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Modificar_Contraseña, size=(23, 43)), command=Grafico_Recuperar_Contraseña)
Boton_Inicio_Crear_Usuario = CTkButton(root, width=300, height=70, text_color="white", text=" Crear Usuario", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Crear_Usuario, size=(45, 45)), command=Grafico_Crear_Usuario) 
Boton_Funcion_Login = CTkButton(root, width=255, height=50, text_color="white", text="Iniciar Sesion", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Login, size=(33, 45)), command=Funcion_Login)
Boton_Funcion_Crear_Usuario = CTkButton(root, width=255, height=50, text_color="white", text=" Crear Usuario", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Crear_Usuario, size=(45, 45)), command=Funcion_Crear_Usuario) 
Boton_Usuario_Casos = CTkButton(root, width=265, height=70, text_color="white", text="Casos", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Casos, size=(40, 40)), command=Grafico_Usuario_Casos)
Boton_Usuario_Cuenta = CTkButton(root, width=255, height=70, text_color="white", text="Ajustes de Cuenta", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Cuenta, size=(40, 40)), command=Grafico_Usuario_Cuenta)
Boton_Funcion_Cuenta_Modificar_Contraseña = CTkButton(root, width=255, height=50, text_color="white", text="Modificar Contraseña", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Cuenta, size=(35, 35)), command=Funcion_Modificar_Contraseña)
Boton_Usuario_Cuenta_Modificar_Contraseña = CTkButton(root, width=255, height=70, text_color="white", text="Modificar Contraseña", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Modificar_Contraseña, size=(22, 50)), command=Grafico_Usuario_Cuenta_Modificar_contraseña)
Boton_Usuario_Cuenta_Modificar_Datos = CTkButton(root, width=280, height=70, text_color="white", text="Modificar Datos", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Cuenta_Modificar_Datos, size=(40, 40)), command=Grafico_Usuario_Modificar_Datos)
Boton_Usuario_Casos_Grafico_Crear = CTkButton(root, width=265, height=70, text_color="white", text="Crear Caso", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Crear_Caso, size=(40, 40)), command=Grafico_Usuario_Casos_Crear)
Boton_Funcion_Crear_Caso = CTkButton(root, width=255, height=50, text_color="white", text="Crear Caso", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Crear_Usuario, size=(45, 45)), command=Funcion_Crear_Caso)
Boton_Funcion_Buscar_Caso = CTkButton(root, width=255, height=50, text_color="white", text=" Buscar Caso", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Buscar_Caso, size=(45, 45)), command=Funcion_Buscar_Caso)
Boton_Funcion_Buscar_Caso2 = CTkButton(root, width=255, height=50, text_color="white", text=" Buscar Caso", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Buscar_Caso, size=(45, 45)), command=Funcion_Buscar_Caso2)
Boton_Funcion_Buscar_Usuario = CTkButton(root, width=255, height=50, text_color="white", text=" Buscar Usuario", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Buscar_Caso, size=(45, 45)), command=Funcion_Buscar_Usuario)
Boton_Funcion_Buscar_Usuario2 = CTkButton(root, width=255, height=50, text_color="white", text=" Buscar Usuario", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Buscar_Caso, size=(45, 45)), command=Funcion_Cargar_Datos_Usuarios)
Boton_Usuario_Casos_Grafico_Volver_Buscar = CTkButton(root, width=255, height=50, text_color="white", text="Volver a Buscar", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Buscar_Caso, size=(45, 45)), command=Grafico_Usuario_Casos_Buscar)
Boton_Usuario_Casos_Grafico_Buscar = CTkButton(root, width=265, height=70, text_color="white", text="Buscar Casos", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Buscar_Caso, size=(45, 45)), command=Grafico_Usuario_Casos_Buscar)
Boton_Funcion_Modificar_Datos_Usuario = CTkButton(root, width=255, height=50, text_color="white", text="Modificar Datos", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Cuenta, size=(35, 35)), command=Funcion_Modificar_Contactos_Usuario)
Boton_Admin_Usuarios = CTkButton(root, width=260, height=70, text_color="white", text="Usuarios", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Modificar_Usuario, size=(35, 40)), command=Grafico_Admin_Usuarios)
Boton_Admin_Casos = CTkButton(root, width=260, height=70, text_color="white", text="Casos", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Crear_Caso, size=(40, 40)), command=Grafico_Admin_Casos)
Boton_Admin_Entidades = CTkButton(root, width=260, height=70, text_color="white", text="Entidades", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Admin_Entidad, size=(45, 35)), command=Funcion_Buscar_Entidades)
Boton_Funcion_Eliminar_Caso = CTkButton(root, width=255, height=50, text_color="white", text=" Eliminar Caso", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Casos, size=(45, 40)), command=Funcion_Eliminar_Datos_Casos)
Boton_Funcion_Eliminar_Usuario = CTkButton(root, width=255, height=50, text_color="white", text=" Eliminar Usuario", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Casos, size=(45, 40)), command=Funcion_Eliminar_Usuario)
Boton_Funcion_Modificar_Datos_Caso = CTkButton(root, width=255, height=50, text_color="white", text="Modificar Datos", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Cuenta, size=(35, 35)), command=Funcion_Modificar_Datos_Casos)
Boton_Funcion_Modificar_Datos_Usuario5 = CTkButton(root, width=255, height=50, text_color="white", text="Modificar Usuario", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Cuenta, size=(35, 35)), command=Funcion_Modificar_Datos_Usuarios)
Boton_Admin_Grafico_Casos_Buscar = CTkButton(root, width=300, height=70, text_color="white", text="Buscar Caso", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Buscar_Caso, size=(45, 45)), command=Grafico_Admin_Casos_Buscar)
Boton_Admin_Grafico_Casos_Crear = CTkButton(root, width=300, height=70, text_color="white", text="Crear Caso", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Crear_Usuario, size=(45, 45)), command=Grafico_Admin_Casos_Crear)
Boton_Admin_Grafico_Casos_Modificar = CTkButton(root, width=300, height=70, text_color="white", text="Modificar Caso", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Cuenta, size=(45, 45)), command=Grafico_Admin_Modificar_Casos_Buscar)
Boton_Admin_Grafico_Casos_Eliminar = CTkButton(root, width=300, height=70, text_color="white", text="Eliminar Caso", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Salir, size=(37, 37)), command=Grafico_Admin_Eliminar_Casos)
Boton_Funcion_Crear_Usuario2 = CTkButton(root, width=255, height=50, text_color="white", text=" Crear Usuario", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Crear_Usuario, size=(45, 45)), command=Funcion_Crear_Usuario2) 
Boton_Funcion_Recuperar_Contraseña = CTkButton(root, width=255, height=50, text_color="white", text="Enviar UUID", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Modificar_Contraseña, size=(20, 30)), command=Funcion_Recuperar_Contraseña) 
Boton_Funcion_Recuperar_Contraseña2 = CTkButton(root, width=255, height=50, text_color="white", text="Recuperar Usuario", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Modificar_Contraseña, size=(20, 30)), command=Funcion_Validar_Token_Cambiar)  
Boton_Admin_Grafico_Usuarios_Buscar = CTkButton(root, width=300, height=70, text_color="white", text="Buscar Usuario", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Buscar_Caso, size=(45, 45)), command=Grafico_Usuario_Admin_Buscar)
Boton_Admin_Grafico_Usuarios_Crear = CTkButton(root, width=300, height=70, text_color="white", text="Crear Usuario", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Crear_Usuario, size=(45, 45)), command=Grafico_Admin_Usuarios_Crear)
Boton_Admin_Grafico_Usuarios_Modificar = CTkButton(root, width=300, height=70, text_color="white", text="Modificar Usuario", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Cuenta, size=(45, 45)), command=Grafico_Admin_Modificar_Usuarios_Buscar)
Boton_Admin_Grafico_Usuarios_Eliminar = CTkButton(root, width=300, height=70, text_color="white", text="Eliminar Usuario", font=(fuente, 25), corner_radius= 12, fg_color="#12bfbf", hover_color="#079696", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Salir, size=(37, 37)), command=Grafico_Admin_Eliminar_Usuarios)
Boton_Pagina = CTkButton(root, image=CTkImage(dark_image=Imagen_Boton_Usuario_Datos, size=(110, 110)), hover_color="#2d3e50", text="", width=110, height=110, bg_color="#2d3e50", fg_color="#2d3e50", command=Funcion_Pagina)

Imagen_Grafico_Usuario_Datos_Documento = CTkLabel(root, text="", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Datos_Documento, size=(42, 35)))
Imagen_Grafico_Usuario_Datos_Correo = CTkLabel(root, text="", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Datos_Correo, size=(42, 35)))
Imagen_Grafico_Usuario_Datos_Telefono = CTkLabel(root, text="", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Datos_Telefono, size=(35, 35)))
Imagen_Grafico_Usuario_Datos_Direccion = CTkLabel(root, text="", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Usuario_Datos_Direccion, size=(40, 40)))
Imagen_Grafico_Login_Usuario = CTkLabel(root, text="", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Modificar_Usuario, size=(33, 40)))
Imagen_Grafico_Login_Contraseña = CTkLabel(root, text="", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Modificar_Contraseña, size=(25, 50)))
Imagen_Grafico_Modificar_Contraseña = CTkLabel(root, text="", bg_color="#2d3e50", image=CTkImage(dark_image=Imagen_Boton_Login, size=(30, 40)))

Contenedor = CTkFrame(root, corner_radius=10)
Entrada_UUID = CTkEntry(root, font=(fuente, 13), width=120, height=8, fg_color="#555555", text_color="white", bg_color ="#2d3e50", corner_radius=20)
Entrada_Usuario_Identificacion = CTkEntry(root, font=(fuente, 13), width=120, height=8, fg_color="#555555", text_color="white", bg_color ="#2d3e50", corner_radius=20)
Entrada_Caso_TipoDesastre = CTkOptionMenu(root, values=["Incendio","Inundaciòn", "Sismo-temblor", "Terremoto"], corner_radius=32, fg_color="#555555", button_color="#404040", dropdown_fg_color="#555555", bg_color ="#2d3e50", font=(fuente, 13), width=120, height=15, anchor="w")
Entrada_Caso_Personas = CTkOptionMenu(root, values=["1","2","3","4","5","6","7","8"], corner_radius=32, fg_color="#555555", button_color="#404040", dropdown_fg_color="#555555", bg_color ="#2d3e50", font=(fuente, 13), width=120, height=15, anchor="w")
Entrada_Caso_Fecha = DateEntry(root,selectmode='day', year=2009, month=11, day=11, locale='es_ES', date_pattern='dd/mm/yyyy', background='#12bfbf', foreground='white', selectbackground='#5a64ff', selectforeground='white', weekendbackground='#d1d1d1', headersbackground='#049c9c', font=(fuente, 10))
Entrada_Caso_Descripcion = CTkTextbox(root, font=(fuente, 20), width=400, height=150, fg_color="#555555", border_color="#3d3c3c", border_width=2, text_color="white", corner_radius=15, bg_color="#2d3e50")
Entrada_Caso_Direccion = CTkEntry(root, font=(fuente, 13), width=120, height=8, fg_color="#555555", text_color="white", bg_color ="#2d3e50", corner_radius=20)
Entrada_Caso_Radicado = CTkEntry(root, font=(fuente, 13), width=120, height=8, fg_color="#555555", text_color="white", bg_color ="#2d3e50", corner_radius=20)
Entrada_Contraseña_Nueva = CTkEntry(root, show="*", font=(fuente, 13), width=120, height=8, fg_color="#555555", text_color="white", bg_color ="#2d3e50", corner_radius=20)
Entrada_Usuario_Nueva = CTkEntry(root, font=(fuente, 13), width=120, height=8, fg_color="#555555", text_color="white", bg_color ="#2d3e50", corner_radius=20)
Entrada_Primer_Nombre = CTkEntry(root, font=(fuente, 13), width=120, height=8, fg_color="#555555", text_color="white", bg_color ="#2d3e50", corner_radius=20)
Entrada_Segundo_Nombre = CTkEntry(root, font=(fuente, 13), width=120, height=8, fg_color="#555555", text_color="white", bg_color ="#2d3e50", corner_radius=20)
Entrada_Primer_Apellido = CTkEntry(root, font=(fuente, 13), width=120, height=8, fg_color="#555555", text_color="white", bg_color ="#2d3e50", corner_radius=20)
Entrada_Segundo_Apellido = CTkEntry(root, font=(fuente, 13), width=120, height=8, fg_color="#555555", text_color="white", bg_color ="#2d3e50", corner_radius=20)
Entrada_Tipo_Documento = CTkOptionMenu(root, values=["Cedula Ciudadania","Cedula Extranjeria", "Pasaporte", "Tarjeta de identidad"], corner_radius=32, fg_color="#555555", button_color="#404040", dropdown_fg_color="#555555", bg_color ="#2d3e50", font=(fuente, 13), width=120, height=15, anchor="w")
Entrada_Documento = CTkEntry(root, font=(fuente, 13), width=120, height=8, fg_color="#555555", text_color="white", bg_color ="#2d3e50", corner_radius=20)
Entrada_Fecha_Nacimento = DateEntry(root,selectmode='day', year=2009, month=11, day=11, locale='es_ES', date_pattern='dd/mm/yyyy', background='#12bfbf', foreground='white', selectbackground='#5a64ff', selectforeground='white', weekendbackground='#d1d1d1', headersbackground='#049c9c', font=(fuente, 10))
Entrada_Email = CTkEntry(root, font=(fuente, 13), width=120, height=8, fg_color="#555555", text_color="white", bg_color ="#2d3e50", corner_radius=20)
Entrada_Departamento = CTkOptionMenu(root, values=["Cundinamarca"], corner_radius=32, fg_color="#555555", button_color="#404040", dropdown_fg_color="#555555", bg_color ="#2d3e50", font=(fuente, 15), width=120, height=12, anchor="w")
Entrada_Ciudad = CTkEntry(root, font=(fuente, 13), width=120, height=8, fg_color="#555555", text_color="white", bg_color ="#2d3e50", corner_radius=20)
Entrada_Localidad = CTkEntry(root, font=(fuente, 13), width=120, height=8, fg_color="#555555", text_color="white", bg_color ="#2d3e50", corner_radius=20)
Entrada_Barrio = CTkEntry(root, font=(fuente, 13), width=120, height=8, fg_color="#555555", text_color="white", bg_color ="#2d3e50", corner_radius=20)
Entrada_Direccion = CTkEntry(root, font=(fuente, 13), width=120, height=8, fg_color="#555555", text_color="white", bg_color ="#2d3e50", corner_radius=20)
Entrada_Numero = CTkEntry(root, font=(fuente, 13), width=120, height=8, fg_color="#555555", text_color="white", bg_color ="#2d3e50", corner_radius=20)
Entrada_Usuario = CTkEntry(root, font=(fuente, 13), width=120, height=8, fg_color="#555555", text_color="white", bg_color ="#2d3e50", corner_radius=20)
Entrada_Contraseña = CTkEntry(root, show="*", font=(fuente, 13), width=120, height=8, fg_color="#555555", text_color="white", bg_color ="#2d3e50", corner_radius=20)

Texto1 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto2 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto3 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto4 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto5 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto6 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto7 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto8 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto9 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto10 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto11 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto12 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto13 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto14 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto15 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto16 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto17 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto18 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto19 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto20 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto21 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto22 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto23 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto24 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto25 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto26 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto27 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto28 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto29 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto30 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto31 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto32 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto33 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto34 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto35 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto36 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto37 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")
Texto38 = CTkLabel(root, text="", font=(fuente, 20), anchor='center', bg_color ="#2d3e50")

Texto_Admin = CTkLabel(root, text="Modo Administrador", font=(fuente, 16), anchor='center', bg_color ="#2d3e50")
#==============================================================================================
for entry in [Entrada_Contraseña, Entrada_Contraseña_Nueva]:
    entry.bind("<Control-v>", cancelar_evento)
for entry in [Entrada_Contraseña, Entrada_Contraseña_Nueva]:
    entry.bind("<Control-c>", cancelar_evento)
#==============================================================================================
Boton_Emergencia.place(relx=0.99, rely=0.99, anchor="se")
Grafico_Inicio()
root.mainloop()