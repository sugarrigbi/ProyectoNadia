#================LIBRERIAS================
import tkinter as tk                      
from tkinter import messagebox              
import re
from PIL import Image, ImageTk
from customtkinter import *
import json
from tkcalendar import DateEntry
#================ADMIN CREDENCIALES================
USUARIO_ADMIN = "Admin"
CONTRASENA_ADMIN = "1145224601Aa**"
#================VARIABLES================
usuarios = {}
contador = 0
max_intentos = 3
intentos_restantes = 3
ARCHIVO_USUARIOS = "usuarios.json"
ARCHIVO_PERSONAS = "Datos.json"
Mensajes = {
    True: {
        "usuario": {
            "longitud": "El nombre de usuario debe tener al menos 5 caracteres.",
            "existente": "Este usuario ya está registrado. Intente con otro nombre.",
            "correcto": "Usuario creado con éxito. Ahora puedes iniciar sesión.",
            "modificado": "Usuario modificado correctamente.",
            "no_encontrado": "Usuario no encontrado.",
            "eliminado": "Usuario eliminado correctamente.",
        },
        "contraseña": {
            "longitud": "ERROR: La contraseña debe tener al menos 8 caracteres.",
            "mayuscula": "ERROR: La contraseña debe contener al menos una mayúscula.",
            "numero": "ERROR: La contraseña debe contener al menos un número.",
            "especial": "ERROR: La contraseña debe contener al menos un carácter especial.",
            "modificada": "Contraseña modificada correctamente.",
            "incorrecta": "Contraseña incorrecta.",
        },
        "intentos": {
            "restantes": "Intentos restantes: {}",
            "agotados": "Has agotado todos los intentos.",
        },
        "confirmacion": {
            "eliminar_usuario": "¿Estás seguro de que deseas eliminar el usuario '{}'? (Esta acción no se puede deshacer)",
        },
        "login": {
            "exito": "Acceso concedido.",
            "exito_admin": "Acceso concedido Admin.",
        },
        "Datos Persona": {
            "obligatorio": "Los campos Primer Nombre, Primer Apellido y Cédula son obligatorios.",
            "cedula": "La cédula debe contener entre 8 y 10 dígitos numéricos.",
            "telefono": "El teléfono debe contener exactamente 10 dígitos numéricos.",
            "genero": "El género debe ser 'Masculino' o 'Femenino'.",
            "cedula_registrada": "La cédula ya está registrada.",
            "guardado": "PERSONA GUARDADA CORRECTAMENTE"
        }
    },
    False: {
        "usuario": {
            "longitud": "The username must be at least 5 characters long.",
            "existente": "This username is already taken. Please try another one.",
            "correcto": "User successfully created. You can now log in.",
            "modificado": "User successfully updated.",
            "no_encontrado": "User not found.",
            "eliminado": "User successfully deleted.",
        },
        "contraseña": {
            "longitud": "ERROR: Password must be at least 8 characters long.",
            "mayuscula": "ERROR: Password must contain at least one uppercase letter.",
            "numero": "ERROR: Password must contain at least one number.",
            "especial": "ERROR: Password must contain at least one special character.",
            "modificada": "Password successfully changed.",
            "incorrecta": "Incorrect password.",
        },
        "intentos": {
            "restantes": "Remaining attempts: {}",
            "agotados": "You have used all your attempts.",
        },
        "confirmacion": {
            "eliminar_usuario": "Are you sure you want to delete the user '{}'? (This action cannot be undone)",
        },
        "login": {
            "exito": "Access granted.",
            "exito_admin": "Access granted Admin.",
        },
        "Datos Persona": {
            "obligatorio": "First Name, Last Name, and ID are required fields.",
            "cedula": "The ID must contain between 8 and 10 numeric digits.",
            "telefono": "The phone number must contain exactly 10 numeric digits.",
            "genero": "Gender must be 'Male' or 'Female'.",
            "cedula_registrada": "This ID is already registered.",
            "guardado": "PERSON SAVED SUCCESSFULLY"
        }

    }
}
#================DEFINICIONES================
def obtener_fecha():
    print("Fecha seleccionada:", calendario.get_date())
def cargar_usuarios():
    try:
        with open(ARCHIVO_USUARIOS, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
def cargar_personas():
    try:
        with open(ARCHIVO_PERSONAS, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
def guardar_usuarios():
    with open(ARCHIVO_USUARIOS, "w") as archivo:
        json.dump(usuarios, archivo, indent=4)
def guardar_personas(datos):
    with open(ARCHIVO_PERSONAS, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)
def cargar_imagen():
    global imagenL
    Imagen_Fondo = Image.open(r"C:\Users\SALA B307\Pictures\WhatsApp Image 2025-04-09 at 8.32.16 AM.jpeg").convert("RGBA")
    Imagen_Fondo = Imagen_Fondo.resize((777, 939))
    r, g, b, a = Imagen_Fondo.split()
    a = a.point(lambda p: p * 0.3)
    Imagen_Fondo = Image.merge("RGBA", (r, g, b, a))
    imagenL = ImageTk.PhotoImage(Imagen_Fondo)
usuarios = cargar_usuarios()
def validar_contraseña(contraseña):
    idioma = Idioma_var.get()
    if len(contraseña) < 8:
        return Mensajes[idioma]["contraseña"]["longitud"]
    if not any(c.isupper() for c in contraseña):
        return Mensajes[idioma]["contraseña"]["mayuscula"]
    if not any(c.isdigit() for c in contraseña):
        return Mensajes[idioma]["contraseña"]["numero"]
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', contraseña):
        return Mensajes[idioma]["contraseña"]["especial"]
    return None
def crear_usuario():
    idioma = Idioma_var.get()
    usuario = Entrada_usuario.get()
    contraseña = Entrada_contraseña.get()
    if len(usuario) < 5:
        messagebox.showerror("Error", Mensajes[idioma]["usuario"]["longitud"])
        return
    error = validar_contraseña(contraseña)
    if error:
        messagebox.showerror("Error", error)
        return
    if usuario in usuarios:
        messagebox.showwarning("Error", Mensajes[idioma]["usuario"]["existente"])
    else:
        usuarios[usuario] = contraseña
        guardar_usuarios()
        messagebox.showinfo("Éxito", Mensajes[idioma]["usuario"]["correcto"])
def modificar_usuario():
    global contador, max_intentos, intentos_restantes

    idioma = Idioma_var.get()
    usuario_actual = Entrada_usuario.get()
    contraseña_actual = Entrada_contraseña.get()
    nuevo_usuario = Entrada_nuevo_usuario.get()
    if usuario_actual not in usuarios:
        messagebox.showerror("Error", Mensajes[idioma]["usuario"]["no_encontrado"])
        return
    if usuarios[usuario_actual] != contraseña_actual:
        messagebox.showerror("Error", Mensajes[idioma]["contraseña"]["incorrecta"])
        contador += 1
        intentos_restantes = max_intentos - contador
        if intentos_restantes > 0:
            messagebox.showinfo("Info", Mensajes[idioma]["intentos"]["restantes"].format(intentos_restantes))
            Texto_Intentos_Restantes.config(text=Mensajes[idioma]["intentos"]["restantes"].format(intentos_restantes))
        else:
            messagebox.showerror("Error", Mensajes[idioma]["intentos"]["agotados"])
            root.quit()
        return
    if len(nuevo_usuario) < 5:
        messagebox.showerror("Error", Mensajes[idioma]["usuario"]["longitud"])
        return
    usuarios[nuevo_usuario] = usuarios.pop(usuario_actual)
    guardar_usuarios()
    messagebox.showinfo("Éxito", Mensajes[idioma]["usuario"]["modificado"])
def modificar_contraseña():
    global contador, max_intentos, intentos_restantes

    idioma = Idioma_var.get()
    usuario = Entrada_usuario.get()
    contraseña_actual = Entrada_contraseña.get()
    nueva_contraseña = Entrada_nueva_contraseña.get()
    if usuario not in usuarios:
        messagebox.showerror("Error", Mensajes[idioma]["usuario"]["no_encontrado"])
        return
    if usuarios[usuario] != contraseña_actual:
        messagebox.showerror("Error", Mensajes[idioma]["contraseña"]["incorrecta"])
        contador += 1
        intentos_restantes = max_intentos - contador
        if intentos_restantes > 0:
            messagebox.showinfo("Info", Mensajes[idioma]["intentos"]["restantes"].format(intentos_restantes))
            Texto_Intentos_Restantes.config(text=Mensajes[idioma]["intentos"]["restantes"].format(intentos_restantes))
        else:
            messagebox.showerror("Error", Mensajes[idioma]["intentos"]["agotados"])
            root.quit()
        return
    error = validar_contraseña(nueva_contraseña)
    if error:
        messagebox.showerror("Error", error)
        return
    usuarios[usuario] = nueva_contraseña
    guardar_usuarios()
    messagebox.showinfo("Éxito", Mensajes[idioma]["contraseña"]["modificada"])
def borrar_usuario():
    global contador, max_intentos, intentos_restantes

    idioma = Idioma_var.get()
    usuario = Entrada_usuario.get()
    contraseña = Entrada_contraseña.get()
    if usuario not in usuarios:
        messagebox.showerror("Error", Mensajes[idioma]["usuario"]["no_encontrado"])
        return
    if usuarios[usuario] != contraseña:
        messagebox.showerror("Error", Mensajes[idioma]["contraseña"]["incorrecta"])
        contador += 1
        intentos_restantes = max_intentos - contador
        if intentos_restantes > 0:
            messagebox.showinfo("Info", Mensajes[idioma]["intentos"]["restantes"].format(intentos_restantes))
            Texto_Intentos_Restantes.config(text=Mensajes[idioma]["intentos"]["restantes"].format(intentos_restantes))
        else:
            messagebox.showerror("Error", Mensajes[idioma]["intentos"]["agotados"])
            root.quit()
        return
    confirmacion = messagebox.askyesno(Mensajes[idioma]["confirmacion"]["titulo"],Mensajes[idioma]["confirmacion"]["borrar_usuario"].format(usuario)
    )
    if confirmacion:
        del usuarios[usuario]
        guardar_usuarios()
        messagebox.showinfo("Éxito", Mensajes[idioma]["usuario"]["eliminado"])
        Limpiar_Entradas()
def Ventana_Admin():
    ventana_admin = CTk.Tomle
    ventana_admin.title = "SAPO"
    ventana_admin.geometry("100x100")
def login():
    global contador, max_intentos, intentos_restantes

    idioma = Idioma_var.get()
    usuario = Entrada_usuario.get()
    contraseña = Entrada_contraseña.get()
    if usuario == USUARIO_ADMIN and contraseña == CONTRASENA_ADMIN:
        messagebox.showinfo("Éxito", Mensajes[idioma]["login"]["exito_admin"])
        Ventana_Admin()
        return
    if usuario not in usuarios:
        messagebox.showerror("Error", Mensajes[idioma]["usuario"]["no_encontrado"])
        return
    if usuarios[usuario] != contraseña:
        messagebox.showerror("Error", Mensajes[idioma]["contraseña"]["incorrecta"])
        contador += 1
        intentos_restantes = max_intentos - contador
        if intentos_restantes > 0:
            messagebox.showinfo("Info", Mensajes[idioma]["intentos"]["restantes"].format(intentos_restantes))
            Texto_Intentos_Restantes.config(text=Mensajes[idioma]["intentos"]["restantes"].format(intentos_restantes))
        else:
            messagebox.showerror("Error", Mensajes[idioma]["intentos"]["agotados"])
            root.quit()
        return
    if usuario in usuarios and usuarios[usuario] == contraseña:
        messagebox.showinfo("Éxito", Mensajes[idioma]["login"]["exito"])
        Ingresar_Datos()
def Olvidar_Lugares():
    Texto_Nueva_Contraseña.place_forget()
    Texto_Nuevo_Usuario.place_forget()
    Entrada_nueva_contraseña.place_forget()
    Entrada_nuevo_usuario.place_forget()
    Boton_Usuario_Mod.place_forget()
    Boton_Contraseña_Mod.place_forget()
    Boton_Crear.place_forget()
    Texto_Usuario.place_forget()
    Texto_Contraseña.place_forget()
    Boton_Sesion.place_forget()
    Boton_Salir.place_forget()
    Boton_Eliminar.place_forget()
    Entrada_contraseña.place_forget()
    Entrada_usuario.place_forget()
    texto.place_forget()
    Boton_Ingresar.place_forget()
    Boton_Crear_Usuario.place_forget()
    Boton_Modificar_Contraseña.place_forget()
    Boton_Modificar_Usuario.place_forget()
    Boton_Eliminar_Usuario.place_forget()
    Boton_Volver.place_forget()
    Switch_Ingresar_Sistema.place_forget()
    Switch_Crear_Usuario.place_forget()
    Switch_Modificar_Contraseña.place_forget()
    Switch_Modificar_Usuario.place_forget()
    Switch_Eliminar_Usuario.place_forget()
    Switch_Volver_Inicio.place_forget()
    Texto_Intentos_Restantes.place_forget()
def Limpiar_Entradas():
    global contador, max_intentos, intentos_restantes
    Entrada_usuario.delete(0, tk.END)
    Entrada_contraseña.delete(0, tk.END)
    Entrada_nuevo_usuario.delete(0, tk.END)
    Entrada_nueva_contraseña.delete(0, tk.END)
def Ingresar_Sistema():
    Olvidar_Lugares()
    Limpiar_Entradas()
    texto.configure(text="INICIO DE SESION" if Idioma_var.get() else "LOGIN", font=("Century", 30))
    texto.place(relx=0.5, rely=0.2, anchor="center")
    Entrada_contraseña.place(relx=0.8, rely=0.4, anchor="center")
    Entrada_usuario.place(relx=0.2, rely=0.4, anchor="center")
    Texto_Usuario.place(relx=0.2, rely=0.35, anchor="center")
    Texto_Usuario.configure(text = "Ingrese su usuario:" if Idioma_var.get() else "Enter your user:")
    Texto_Contraseña.place(relx=0.8, rely=0.35, anchor="center")
    Texto_Contraseña.configure(text = "Ingrese su contraseña:" if Idioma_var.get() else "Enter your password:")
    Boton_Sesion.place(relx=0.2, rely=0.5, anchor="center")
    Boton_Sesion.configure(text="Iniciar Sesion" if Idioma_var.get() else "Login")
    Boton_Salir.place(relx=0.8, rely=0.5, anchor="center")
    Boton_Salir.configure(text="Salir" if Idioma_var.get() else "Close")
    Boton_Volver.place(relx=0.5, rely=0.7, anchor="center")
    Boton_Volver.configure(text="Volver al menu inicial" if Idioma_var.get() else "Return to the start menu")
    Switch_Ingresar_Sistema.place(relx=0.885, rely=0.97, anchor="center")
    Texto_Intentos_Restantes.place(relx=0.156, rely=0.97, anchor="center")
    Texto_Intentos_Restantes.config(text=f"Intentos Restantes: {intentos_restantes}" if Idioma_var.get() else f"Remaining attempts: {intentos_restantes}")
def Crear_Usuario():
    Olvidar_Lugares()
    Limpiar_Entradas()
    texto.configure(text="CREAR USUARIO"if Idioma_var.get() else "CREATE USER", font=("Century", 30))
    texto.place(relx=0.5, rely=0.2, anchor="center")
    Entrada_contraseña.place(relx=0.8, rely=0.4, anchor="center")
    Entrada_usuario.place(relx=0.2, rely=0.4, anchor="center")
    Texto_Usuario.place(relx=0.2, rely=0.35, anchor="center")
    Texto_Usuario.configure(text = "Ingrese su usuario:" if Idioma_var.get() else "Enter your user:")
    Texto_Contraseña.place(relx=0.8, rely=0.35, anchor="center")
    Texto_Contraseña.configure(text = "Ingrese su contraseña:" if Idioma_var.get() else "Enter your password:")
    Boton_Crear.place(relx=0.2, rely=0.5, anchor="center")
    Boton_Crear.configure(text="Crear Usuario"if Idioma_var.get() else "Create User")
    Boton_Salir.place(relx=0.8, rely=0.5, anchor="center")
    Boton_Salir.configure(text="Salir" if Idioma_var.get() else "Close")
    Boton_Volver.place(relx=0.5, rely=0.7, anchor="center")
    Boton_Volver.configure(text="Volver al menu inicial" if Idioma_var.get() else "Return to the start menu")
    Switch_Crear_Usuario.place(relx=0.885, rely=0.97, anchor="center")
def Modificar_Usuario():
    Olvidar_Lugares()
    Limpiar_Entradas()
    texto.configure(text="MODIFICAR USUARIO"if Idioma_var.get() else "MODIFY USER", font=("Century", 30))
    texto.place(relx=0.5, rely=0.2, anchor="center")
    Entrada_nuevo_usuario.place(relx=0.5, rely=0.52, anchor="center")
    Entrada_usuario.place(relx=0.2, rely=0.4, anchor="center")
    Entrada_contraseña.place(relx=0.8, rely=0.4, anchor="center")
    Texto_Usuario.place(relx=0.2, rely=0.35, anchor="center")
    Texto_Usuario.configure(text = "Ingrese su usuario:" if Idioma_var.get() else "Enter your user:")
    Texto_Nuevo_Usuario.place(relx=0.5, rely=0.47, anchor="center")
    Texto_Nuevo_Usuario.configure(text = "Ingrese su nuevo usuario:" if Idioma_var.get() else "Enter your new user:")
    Texto_Contraseña.place(relx=0.8, rely=0.35, anchor="center")
    Texto_Contraseña.configure(text = "Ingrese su contraseña:" if Idioma_var.get() else "Enter your password:")
    Boton_Usuario_Mod.place(relx=0.2, rely=0.6, anchor="center")
    Boton_Usuario_Mod.configure(text="Modificar Usuario" if Idioma_var.get() else "Modify User")
    Boton_Salir.place(relx=0.8, rely=0.6, anchor="center")
    Boton_Salir.configure(text="Salir" if Idioma_var.get() else "Close")
    Boton_Volver.place(relx=0.5, rely=0.7, anchor="center")
    Boton_Volver.configure(text="Volver al menu inicial" if Idioma_var.get() else "Return to start menu")
    Switch_Modificar_Usuario.place(relx=0.885, rely=0.97, anchor="center")
    Texto_Intentos_Restantes.place(relx=0.156, rely=0.97, anchor="center")
    Texto_Intentos_Restantes.config(text=f"Intentos Restantes: {intentos_restantes}" if Idioma_var.get() else f"Remaining attempts: {intentos_restantes}")
def Modificar_Contraseña():
    Olvidar_Lugares()
    Limpiar_Entradas()
    texto.configure(text="MODIFICAR CONTRASEÑA"if Idioma_var.get() else "MODIFY USER", font=("Century", 30))
    texto.place(relx=0.5, rely=0.2, anchor="center")
    Entrada_nueva_contraseña.place(relx=0.5, rely=0.52, anchor="center")
    Entrada_contraseña.place(relx=0.8, rely=0.4, anchor="center")
    Entrada_usuario.place(relx=0.2, rely=0.4, anchor="center")
    Texto_Contraseña.place(relx=0.8, rely=0.35, anchor="center")
    Texto_Contraseña.configure(text = "Ingrese su contraseña:" if Idioma_var.get() else "Enter your password:")
    Texto_Usuario.place(relx=0.2, rely=0.35, anchor="center")
    Texto_Usuario.configure(text = "Ingrese su usuario:" if Idioma_var.get() else "Enter your user:")
    Texto_Nueva_Contraseña.place(relx=0.5, rely=0.47, anchor="center")
    Texto_Nueva_Contraseña.configure(text = "Ingrese su nueva contraseña:" if Idioma_var.get() else "Enter your new password:")
    Boton_Contraseña_Mod.place(relx=0.2, rely=0.6, anchor="center")
    Boton_Contraseña_Mod.configure(text="Modificar Contraseña" if Idioma_var.get() else "Modify Password")
    Boton_Salir.place(relx=0.8, rely=0.6, anchor="center")
    Boton_Salir.configure(text="Salir" if Idioma_var.get() else "Close")
    Boton_Volver.place(relx=0.5, rely=0.7, anchor="center")
    Boton_Volver.configure(text="Volver al menu inicial" if Idioma_var.get() else "Return to the start menu")
    Switch_Modificar_Contraseña.place(relx=0.885, rely=0.97, anchor="center")
    Texto_Intentos_Restantes.place(relx=0.156, rely=0.97, anchor="center")
    Texto_Intentos_Restantes.config(text=f"Intentos Restantes: {intentos_restantes}" if Idioma_var.get() else f"Remaining attempts: {intentos_restantes}")
def Eliminar_Usuario():
    Olvidar_Lugares()
    Limpiar_Entradas()
    texto.configure(text="ELIMINAR USUARIO" if Idioma_var.get() else "DELETE USER", font=("Century", 30))
    texto.place(relx=0.5, rely=0.2, anchor="center")
    Entrada_contraseña.place(relx=0.8, rely=0.4, anchor="center")
    Entrada_usuario.place(relx=0.2, rely=0.4, anchor="center")
    Texto_Contraseña.place(relx=0.8, rely=0.35, anchor="center")
    Texto_Contraseña.configure(text = "Ingrese su contraseña:" if Idioma_var.get() else "Enter your password:")
    Texto_Usuario.place(relx=0.2, rely=0.35, anchor="center")
    Texto_Usuario.configure(text = "Ingrese su usuario:" if Idioma_var.get() else "Enter your user:")
    Boton_Eliminar.place(relx=0.2, rely=0.5, anchor="center")
    Boton_Eliminar.configure(text="Borrar Usuario" if Idioma_var.get() else "Delete User")
    Boton_Salir.place(relx=0.8, rely=0.5, anchor="center")
    Boton_Salir.configure(text="Salir" if Idioma_var.get() else "Close")
    Boton_Volver.place(relx=0.5, rely=0.7, anchor="center")
    Boton_Volver.configure(text="Volver al menu inicial" if Idioma_var.get() else "Return to the start menu")
    Switch_Eliminar_Usuario.place(relx=0.885, rely=0.97, anchor="center")
    Texto_Intentos_Restantes.place(relx=0.156, rely=0.97, anchor="center")
    Texto_Intentos_Restantes.config(text=f"Intentos Restantes: {intentos_restantes}" if Idioma_var.get() else f"Remaining attempts: {intentos_restantes}")
def Volver_Inicio():
    Olvidar_Lugares()
    Limpiar_Entradas()
    texto.configure(text="Bienvenido a Gaialink" if Idioma_var.get() else "Welcome to Gaialink", font=("Century", 50))
    texto.place(relx=0.5, rely=0.15, anchor="center")
    Boton_Ingresar.place(relx=0.5, rely=0.3, anchor="center")
    Boton_Ingresar.configure(text="Inicio de Sesion"if Idioma_var.get() else "Login")
    Boton_Crear_Usuario.place(relx=0.5, rely=0.4, anchor="center")
    Boton_Crear_Usuario.configure(text="Crear Usuarios"if Idioma_var.get() else "Create Users")
    Boton_Modificar_Contraseña.place(relx=0.5, rely=0.5, anchor="center")
    Boton_Modificar_Contraseña.configure(text="Modificar Contraseñas"if Idioma_var.get() else "Modify Passwords")
    Boton_Modificar_Usuario.place(relx=0.5, rely=0.6, anchor="center")
    Boton_Modificar_Usuario.configure(text="Modificar Usuarios"if Idioma_var.get() else "Modify Users")
    Boton_Eliminar_Usuario.place(relx=0.5, rely=0.7, anchor="center")
    Boton_Eliminar_Usuario.configure(text="Eliminar Usuarios"if Idioma_var.get() else "Delete Users")
    Boton_Salir.place(relx=0.5, rely=0.8, anchor="center")
    Boton_Salir.configure(text="Salir" if Idioma_var.get() else "Close")
    Switch_Volver_Inicio.place(relx=0.885, rely=0.97, anchor="center")
def Leer_Datos():
    idioma = Idioma_var.get()
    Primer_Nombre = Entrada_Primer_Nombre.get().strip()
    Segundo_Nombre = Entrada_Segundo_Nombre.get().strip()
    Primer_Apellido = Entrada_Primer_Apellido.get().strip()
    Segundo_Apellido = Entrada_Segundo_Apellido.get().strip()
    Telefono = Entrada_Telefono.get().strip()
    Cedula = Entrada_Cedula .get().strip()
    Correo = Entrada_Correo.get().strip()
    Direccion = Entrada_Direccion.get().strip()
    Genero = Entrada_Genero.get().strip().capitalize()
    Fecha_Nacimiento = calendario.get_date()
    Situacion = Entrada_Situacion.get("1.0", "end").strip()

    if not Primer_Nombre or not Primer_Apellido or not Cedula:
        messagebox.showerror("Error", Mensajes[idioma]["Datos Persona"]["obligatorio"])
        return
    if not Cedula.isdigit() or not (8 <= len(Cedula) <= 10):
        messagebox.showerror("Error", Mensajes[idioma]["Datos Persona"]["cedula"])
        return
    if not Telefono.isdigit() or len(Telefono) != 10:
        messagebox.showerror("Error", Mensajes[idioma]["Datos Persona"]["telefono"])
        return

    Personas = cargar_personas()
    if not isinstance(Personas, list):
        Personas = []
    for persona in Personas:
        if persona.get("Cedula") == Cedula:
            messagebox.showerror("Error", Mensajes[idioma]["Datos Persona"]["cedula_registrada"])
            return

    Datos_Persona = {
        "Primer Nombre": Primer_Nombre,
        "Segundo Nombre": Segundo_Nombre,
        "Primer Apellido": Primer_Apellido,
        "Segundo Apellido": Segundo_Apellido,
        "Telefono": Telefono,
        "Cedula": Cedula,
        "Correo": Correo,
        "Direccion": Direccion,
        "Genero": Genero,
        "Fecha de Nacimiento": str(Fecha_Nacimiento),
        "Situacion": Situacion,
    }

    Personas.append(Datos_Persona)
    guardar_personas(Personas)
    messagebox.showinfo("Éxito", Mensajes[idioma]["Datos Persona"]["guardado"])
def Ingresar_Datos():
    Olvidar_Lugares()
    Limpiar_Entradas()
    Entrada_Primer_Nombre.place(relx=0.1, rely=0.1, anchor="w")
    Entrada_Segundo_Nombre.place(relx=0.1, rely=0.2, anchor="w")
    Entrada_Primer_Apellido.place(relx=0.1, rely=0.3, anchor="w")
    Entrada_Segundo_Apellido.place(relx=0.1, rely=0.4, anchor="w")
    Entrada_Telefono.place(relx=0.1, rely=0.5, anchor="w")
    Entrada_Cedula.place(relx=0.55, rely=0.1, anchor="w")
    Entrada_Correo.place(relx=0.55, rely=0.2, anchor="w")
    Entrada_Direccion.place(relx=0.55, rely=0.3, anchor="w")
    Entrada_Genero.place(relx=0.55, rely=0.4, anchor="w")
    calendario.place(relx=0.55, rely=0.5, anchor="w")
    Entrada_Situacion.place(relx=0.38, rely=0.7, anchor="w")
    Texto_Entrada_Primer_Nombre.configure(text="Ingrese su primer nombre:" if Idioma_var.get() else "Enter your first name:")
    Texto_Entrada_Segundo_Nombre.configure(text="Ingrese su segundo nombre:" if Idioma_var.get() else "Enter your second name:")
    Texto_Entrada_Primer_Apellido.configure(text="Ingrese su primer apellido:" if Idioma_var.get() else "Enter your first surname:")
    Texto_Entrada_Segundo_Apellido.configure(text="Ingrese su segundo apellido:" if Idioma_var.get() else "Enter your second surname:")
    Texto_Entrada_Telefono.configure(text="Ingrese su teléfono:" if Idioma_var.get() else "Enter your phone number:")
    Texto_Entrada_Cedula.configure(text="Ingrese su cédula:" if Idioma_var.get() else "Enter your ID:")
    Texto_Entrada_Correo.configure(text="Ingrese su correo:" if Idioma_var.get() else "Enter your email:")
    Texto_Entrada_Direccion.configure(text="Ingrese su dirección:" if Idioma_var.get() else "Enter your address:")
    Texto_Entrada_Genero.configure(text="Seleccione su género:" if Idioma_var.get() else "Select your gender:")
    Texto_Entrada_Fecha_Nacimiento.configure(text="Ingrese su fecha de nacimiento:" if Idioma_var.get() else "Enter your birth date:")
    Texto_Entrada_Situacion.configure(text="Ingrese su situación:" if Idioma_var.get() else "Enter your situation:")
    Texto_Entrada_Primer_Nombre.place(relx=0.1, rely=0.05, anchor="w")
    Texto_Entrada_Segundo_Nombre.place(relx=0.1, rely=0.15, anchor="w")
    Texto_Entrada_Primer_Apellido.place(relx=0.1, rely=0.25, anchor="w")
    Texto_Entrada_Segundo_Apellido.place(relx=0.1, rely=0.35, anchor="w")
    Texto_Entrada_Telefono.place(relx=0.1, rely=0.45, anchor="w")
    Texto_Entrada_Cedula.place(relx=0.55, rely=0.05, anchor="w")
    Texto_Entrada_Correo.place(relx=0.55, rely=0.15, anchor="w")
    Texto_Entrada_Direccion.place(relx=0.55, rely=0.25, anchor="w")
    Texto_Entrada_Genero.place(relx=0.55, rely=0.35, anchor="w")
    Texto_Entrada_Fecha_Nacimiento.place(relx=0.55, rely=0.45, anchor="w")
    Texto_Entrada_Situacion.place(relx=0.35, rely=0.555, anchor="w")
    Switch_Ingresar_Datos.place(relx=0.885, rely=0.97, anchor="center")
    Boton_Crear_Persona.place(relx=0.5, rely=0.9, anchor="center")
    Boton_Crear_Persona.configure(text="Crear Persona" if Idioma_var.get() else "Create Person")
    Boton_Salir2.configure(text="Salir" if Idioma_var.get() else "Close")
    Boton_Salir2.place(relx=0.15, rely=0.97, anchor="center")
#================CREAR_VENTANA================
root = CTk()
root.title("Login Gaialink")
root.geometry("950x980")
root.resizable(height = True, width = True)
root.configure(fg_color="#f4f4f4")
#================CREAR_IMAGEN_FONDO================
cargar_imagen()
lblimagen = tk.Label(root, image=imagenL)
lblimagen.place(relx=0.5, rely=0.485, anchor="center")
#================TEXTOS_OPCIONES================
Texto_Usuario = tk.Label(root, text="Ingrese su usuario:", font=("Century", 20), anchor='center', bd=1, relief="solid")
Texto_Intentos_Restantes = tk.Label(root, font=("Century", 20), anchor='center', bg="#277cd6", fg="white")
Texto_Contraseña = tk.Label(root, text="Ingrese su contraseña:", font=("Century", 20), anchor='center', bd=1, relief="solid")
Texto_Nuevo_Usuario = tk.Label(root, text="Nuevo Usuario:", font=("Century", 20), anchor='center', bd=1, relief="solid")
Texto_Nueva_Contraseña = tk.Label(root, text="Nueva Contraseña:", font=("Century", 20), anchor='center', bd=1, relief="solid")
Texto_Entrada_Primer_Nombre = tk.Label(root, text="Ingrese su primer nombre:", font=("Century", 20), anchor='center', bd=1, relief="solid")
Texto_Entrada_Segundo_Nombre = tk.Label(root, text="Ingrese su segundo nombre:", font=("Century", 20), anchor='center', bd=1, relief="solid")
Texto_Entrada_Primer_Apellido = tk.Label(root, text="Ingrese su primer apellido:", font=("Century", 20), anchor='center', bd=1, relief="solid")
Texto_Entrada_Segundo_Apellido = tk.Label(root, text="Ingrese su segundo apellido:", font=("Century", 20), anchor='center', bd=1, relief="solid")
Texto_Entrada_Telefono = tk.Label(root, text="Ingrese su telefono:", font=("Century", 20), anchor='center', bd=1, relief="solid")
Texto_Entrada_Cedula = tk.Label(root, text="Ingrese su cedula:", font=("Century", 20), anchor='center', bd=1, relief="solid")
Texto_Entrada_Correo = tk.Label(root, text="Ingrese su correo:", font=("Century", 20), anchor='center', bd=1, relief="solid")
Texto_Entrada_Direccion = tk.Label(root, text="Ingrese su direccion:", font=("Century", 20), anchor='center', bd=1, relief="solid")
Texto_Entrada_Genero = tk.Label(root, text="Ingrese su genero:", font=("Century", 20), anchor='center', bd=1, relief="solid")
Texto_Entrada_Fecha_Nacimiento = tk.Label(root, text="Ingrese su fecha de nacimiento:", font=("Century", 20), anchor='center', bd=1, relief="solid")
Texto_Entrada_Situacion = tk.Label(root, text="Ingrese su situacion:", font=("Century", 20), anchor='center', bd=1, relief="solid")
#================ENTRADAS_DE_DATOS================
Entrada_usuario = CTkEntry(root, font=("Century", 20), width=200, height=30, fg_color="#e1e0e0", text_color="black")
Entrada_contraseña = CTkEntry(root, show="*", font=("Century", 20), width=200, height=30, fg_color="#e1e0e0", text_color="black")
Entrada_nuevo_usuario = CTkEntry(root, font=("Century", 20), width=200, height=30, fg_color="#e1e0e0", text_color="black")
Entrada_nueva_contraseña = CTkEntry(root, show="*", font=("Century", 20), width=200, height=30, fg_color="#e1e0e0", text_color="black")
Entrada_Primer_Nombre = CTkEntry(root, font=("Century", 20), width=200, height=30, fg_color="#e1e0e0", text_color="black")
Entrada_Segundo_Nombre = CTkEntry(root, font=("Century", 20), width=200, height=30, fg_color="#e1e0e0", text_color="black")
Entrada_Primer_Apellido = CTkEntry(root, font=("Century", 20), width=200, height=30, fg_color="#e1e0e0", text_color="black")
Entrada_Segundo_Apellido = CTkEntry(root, font=("Century", 20), width=200, height=30, fg_color="#e1e0e0", text_color="black")
Entrada_Telefono = CTkEntry(root, font=("Century", 20), width=200, height=30, fg_color="#e1e0e0", text_color="black")
Entrada_Cedula = CTkEntry(root, font=("Century", 20), width=200, height=30, fg_color="#e1e0e0", text_color="black")
Entrada_Correo = CTkEntry(root, font=("Century", 20), width=200, height=30, fg_color="#e1e0e0", text_color="black")
Entrada_Direccion = CTkEntry(root, font=("Century", 20), width=200, height=30, fg_color="#e1e0e0", text_color="black")
Entrada_Genero = CTkSegmentedButton(root, bg_color="transparent", fg_color="#277cd6", border_width=3, font=("Century", 25), values=["M", "F"])
calendario = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
Entrada_Situacion = CTkTextbox(root, font=("Century", 20), width=200, height=200, fg_color="#e1e0e0", text_color="black")
#================BOTONES_OPCIONES===============
Boton_Crear = CTkButton(root, height=40, corner_radius= 80, bg_color="transparent", fg_color="#277cd6", hover_color="#0ca518", border_color="#013b79", border_width=3, font=("Century", 25), command=crear_usuario)
Boton_Volver = CTkButton(root, height=40, corner_radius= 80, bg_color="transparent", fg_color="#277cd6", hover_color="#faa300", border_color="#013b79", border_width=3, font=("Century", 25), command=Volver_Inicio)
Boton_Ingresar = CTkButton(root, height=40, corner_radius= 80, bg_color="transparent", fg_color="#277cd6", hover_color="#faa300", border_color="#013b79", border_width=3, font=("Century", 25), command=Ingresar_Sistema)
Boton_Crear_Usuario = CTkButton(root, height=40, corner_radius= 80, bg_color="transparent", fg_color="#277cd6", hover_color="#faa300", border_color="#013b79", border_width=3, font=("Century", 25), command=Crear_Usuario)
Boton_Modificar_Contraseña = CTkButton(root, height=40, corner_radius= 80, bg_color="transparent", fg_color="#277cd6", hover_color="#faa300", border_color="#013b79", border_width=3, font=("Century", 25), command=Modificar_Contraseña)
Boton_Modificar_Usuario = CTkButton(root, height=40, corner_radius= 80, bg_color="transparent", fg_color="#277cd6", hover_color="#faa300", border_color="#013b79", border_width=3, font=("Century", 25), command=Modificar_Usuario)
Boton_Eliminar_Usuario = CTkButton(root, height=40, corner_radius= 80, bg_color="transparent", fg_color="#277cd6", hover_color="#faa300", border_color="#013b79", border_width=3, font=("Century", 25), command=Eliminar_Usuario)
Boton_Usuario_Mod = CTkButton(root, height=40, corner_radius= 80, bg_color="transparent", fg_color="#277cd6", hover_color="#0ca518", border_color="#013b79", border_width=3, font=("Century", 25), command=modificar_usuario)
Boton_Contraseña_Mod = CTkButton(root, height=40, corner_radius= 80, bg_color="transparent", fg_color="#277cd6", hover_color="#0ca518", border_color="#013b79", border_width=3, font=("Century", 25), command=modificar_contraseña)
Boton_Sesion = CTkButton(root, height=40, corner_radius= 80, bg_color="transparent", fg_color="#277cd6", hover_color="#0ca518", border_color="#013b79", border_width=3, font=("Century", 25), command=login)
Boton_Salir = CTkButton(root, height=40, corner_radius= 100, bg_color="transparent", fg_color="#277cd6", hover_color="#de0017", border_color="#013b79", border_width=3, font=("Century", 25), command=root.quit)
Boton_Salir2 = CTkButton(root, height=40, corner_radius= 100, bg_color="transparent", fg_color="#277cd6", hover_color="#de0017", border_color="#013b79", border_width=3, font=("Century", 25), command=root.quit)
Boton_Eliminar = CTkButton(root, height=40, corner_radius= 80, bg_color="transparent", fg_color="#277cd6", hover_color="#de0017", border_color="#013b79", border_width=3, font=("Century", 25), command=borrar_usuario)
Boton_Crear_Persona = CTkButton(root, height=40, corner_radius= 80, bg_color="transparent", fg_color="#277cd6", hover_color="#0ca518", border_color="#013b79", border_width=3, font=("Century", 25), command=Leer_Datos)
Boton_Calendario = CTkButton(root, height=40, corner_radius= 80, bg_color="transparent", fg_color="#277cd6", hover_color="#0ca518", border_color="#013b79", border_width=3, font=("Century", 25), command=obtener_fecha)
#================SWITH================
Idioma_var = tk.BooleanVar(value=True)
Switch_Ingresar_Sistema = CTkSwitch(root, text="Español / English", onvalue=False, offvalue=True, variable=Idioma_var, font=("Century", 20), button_hover_color="#faa300", bg_color="#277cd6", width=200, height=30, border_color="#013b79", button_color="#00254b",progress_color="#08c302", command=Ingresar_Sistema)
Switch_Crear_Usuario = CTkSwitch(root, text="Español / English", onvalue=False, offvalue=True, variable=Idioma_var, font=("Century", 20), button_hover_color="#faa300", bg_color="#277cd6", width=200, height=30, border_color="#013b79", button_color="#00254b",progress_color="#08c302", command=Crear_Usuario)
Switch_Modificar_Contraseña = CTkSwitch(root, text="Español / English", onvalue=False, offvalue=True, variable=Idioma_var, font=("Century", 20), button_hover_color="#faa300", bg_color="#277cd6", width=200, height=30, border_color="#013b79", button_color="#00254b",progress_color="#08c302", command=Modificar_Contraseña)
Switch_Modificar_Usuario = CTkSwitch(root, text="Español / English", onvalue=False, offvalue=True, variable=Idioma_var, font=("Century", 20), button_hover_color="#faa300", bg_color="#277cd6", width=200, height=30, border_color="#013b79", button_color="#00254b",progress_color="#08c302", command=Modificar_Usuario)
Switch_Eliminar_Usuario = CTkSwitch(root, text="Español / English", onvalue=False, offvalue=True, variable=Idioma_var, font=("Century", 20), button_hover_color="#faa300", bg_color="#277cd6", width=200, height=30, border_color="#013b79", button_color="#00254b",progress_color="#08c302", command=Eliminar_Usuario)
Switch_Volver_Inicio = CTkSwitch(root, text="Español / English", onvalue=False, offvalue=True, variable=Idioma_var, font=("Century", 20), button_hover_color="#faa300", bg_color="#277cd6", width=200, height=30, border_color="#013b79", button_color="#00254b",progress_color="#08c302", command=Volver_Inicio)
Switch_Ingresar_Datos = CTkSwitch(root, text="Español / English", onvalue=False, offvalue=True, variable=Idioma_var, font=("Century", 20), button_hover_color="#faa300", bg_color="#277cd6", width=200, height=30, border_color="#013b79", button_color="#00254b",progress_color="#08c302", command=Ingresar_Datos)
#================INICIO_CODIGO================
texto = tk.Label(root, text="", font=("Century", 38), bd=2, relief="solid")
texto.place(relx=0.3, rely=0.1, anchor='center')
Copyright = tk.Label(root, text="© Gaialink Todos los derechos reservados", font=("Century", 15), anchor='center', fg="#a9a9a9")
Copyright.place(relx=0.53, rely=0.98, anchor='center')


Volver_Inicio()

root.mainloop()