import customtkinter as ctk
from tkinter import filedialog
import threading
import asyncio
import discord
import aiohttp

#=========================================
#          CONFIGURACION DEL BOT
#=========================================

AVATAR_BOT = "INSERTAR LINK"
NOMBRE_BOT = "Moon-Bot"
COLOR_BOT = "0x4509B3"
WEBHOOKS_URLS = {
    "#《🌙》CHAT-SOCIAL ": "INSERTAR LINK",
    "#《🎮》COMANDOS": "INSERTAR LINK",
    "#《😆》MEMES": "INSERTAR LINK",
    "#《⚡》TODO": "INSERTAR LINK",
    "#《1️⃣》COUNTER": "INSERTAR LINK",
    "#《🌈》COLORES": "INSERTAR LINK",
    "#《👋》BIENVENIDA": "INSERTAR LINK",
    "#《📜》REGLAS": "INSERTAR LINK",
    "#《🎫》TICKETS": "INSERTAR LINK",
    "#《💡》IDEAS": "INSERTAR LINK",
    "#《🖼️》MEDIA": "INSERTAR LINK",
    "#《🎧》AUDIO": "INSERTAR LINK",
    "#《🎬》VIDEO": "INSERTAR LINK",
    "#《🙋》SOBRE-MI": "INSERTAR LINK",
    "#《🤳》SELFIES": "INSERTAR LINK",
    "#《🎮》TUS-HOBBYS": "INSERTAR LINK",
    "#《❤️》TUS-GUSTOS": "INSERTAR LINK",
    "#《🎨》DIBUJOS": "INSERTAR LINK",
    "#《✨》ANIMACIONES": "INSERTAR LINK",
    "#《🛠️》MODS CONSULTA": "INSERTAR LINK",
    "#《🆕》NEW MODS": "INSERTAR LINK",
    "#《📜》REGISTROS": "INSERTAR LINK",
    "#《🐢》CARL": "INSERTAR LINK",
    "#《🤝》ALIANZA": "INSERTAR LINK",
    "#《📖》SOBRE ALIANZA": "INSERTAR LINK",
    "#《💬》DEBATES": "INSERTAR LINK",
    "#《⚠️》QUEJAS": "INSERTAR LINK"
}

async def Enviar_Embed(Titulo, Descripcion, Url, Color, Imagen_Input=""):
    Texto = discord.Embed(
        title=Titulo,
        description=Descripcion,
        color=discord.Color(Color)
    )
    Imagen = Imagen_Input
    if Imagen != "":
        Texto.set_image(url=Imagen)

    async with aiohttp.ClientSession() as Sesion:
        Webhook = discord.Webhook.from_url(
            Url,
            session=Sesion
        )
        await Webhook.send(
            embed=Texto,
            username=NOMBRE_BOT,
            avatar_url=AVATAR_BOT,
            allowed_mentions=discord.AllowedMentions(
                everyone=True
            )
        )
        return "--Embed enviado correctamente--"
    
async def Enviar_Mensaje(Url, Mensaje):
    async with aiohttp.ClientSession() as Sesion:
        Webhook = discord.Webhook.from_url(
            Url,
            session=Sesion
        )        
        await Webhook.send(
            content=Mensaje,
            username=NOMBRE_BOT,
            avatar_url=AVATAR_BOT,
            allowed_mentions=discord.AllowedMentions(
                everyone=True        
            )
        )
        return "--Mensaje enviado correctamente--"

async def Enviar_Hilo(Url, Titulo, Descripcion):
    async with aiohttp.ClientSession() as Sesion:
        Webhook = discord.Webhook.from_url(
            Url,
            session=Sesion
        )
        try:
            await Webhook.send(
                thread_name=Titulo,
                content=Descripcion,
                username=NOMBRE_BOT,
                avatar_url=AVATAR_BOT,
                allowed_mentions=discord.AllowedMentions(
                    everyone=True        
                )            
            )       
            return "--Hilo enviado correctamente--" 
        except discord.HTTPException as e:
            if e.code == 220003:
                return "--Error este canal no es un Foro--"
            else:
                return f"--Error al enviar: {e.text}--"                    
    
async def Enviar_Archivo(Url, Mensaje, Ruta_Archivo):
    async with aiohttp.ClientSession() as Sesion:
        Webhook = discord.Webhook.from_url(
            Url,
            session=Sesion
        )
        if Ruta_Archivo == "":
            return "--Error archivo no seleccionado--"
        try:
            await Webhook.send(
                file=discord.File(Ruta_Archivo),
                content=Mensaje,
                username=NOMBRE_BOT,
                avatar_url=AVATAR_BOT,
                allowed_mentions=discord.AllowedMentions(
                    everyone=True        
                )            
            )       
            return "--Archivo enviado con exito--" 
        except FileNotFoundError:
            return "--Error archivo no enviado--"
        
async def Editar_Embed(Url, Id_Mensaje, Titulo_Nuevo, Descripcion_Nuevo, Color_Nuevo, Imagen_Input=""):
    Embed_Nuevo = discord.Embed(
        title=Titulo_Nuevo,
        description=Descripcion_Nuevo,
        color=discord.Color(Color_Nuevo)
    )
    Imagen = Imagen_Input
    if Imagen != "":
        Embed_Nuevo.set_image(url=Imagen)    
    async with aiohttp.ClientSession() as Sesion:
        Webhook = discord.Webhook.from_url(
            Url,
            session=Sesion
        )
        try:
            await Webhook.edit_message(
                Id_Mensaje,
                embed=Embed_Nuevo,
                allowed_mentions=discord.AllowedMentions(
                    everyone=True        
                )               
            )
        except discord.NotFound:
            return "--Error Embed no encontrado--"
        return "--Embed editado correctamente--"
    
async def Editar_Mensaje(Url, Id_Mensaje, Mensaje_Nuevo):
    async with aiohttp.ClientSession() as Sesion:
        Webhook = discord.Webhook.from_url(
            Url,
            session=Sesion
        )    
        try:    
            await Webhook.edit_message(
                Id_Mensaje,
                content=Mensaje_Nuevo,
            )
        except discord.NotFound:
            return "--Error Mensaje no encontrado--"            
        return "--Mensaje editado correctamente--"

async def Editar_Hilo(Url, Id_Mensaje, Id_Hilo, Contenido_Nuevo):
    async with aiohttp.ClientSession() as Sesion:
        Webhook = discord.Webhook.from_url(
            Url,
            session=Sesion
        )     
        try:   
            await Webhook.edit_message(
                Id_Mensaje,
                content=Contenido_Nuevo,
                thread=discord.Object(id=Id_Hilo)
            )
        except discord.NotFound:
            return "--Error Mensaje no encontrado--"          
        return "--Hilo editado correctamente--"

async def Borrar_Mensaje(Url, Id_Mensaje):
    async with aiohttp.ClientSession() as Sesion:
        Webhook = discord.Webhook.from_url(
            Url,
            session=Sesion
        )
        try:
            await Webhook.delete_message(Id_Mensaje)
            return "--Mensaje eliminado correctamente--"
        except discord.NotFound:
            return "--Error No se encontró ese mensaje--"        

async def Enviar_TTS(Url, Mensaje):
    async with aiohttp.ClientSession() as Sesion:
        Webhook = discord.Webhook.from_url(
            Url,
            session=Sesion
        )
        await Webhook.send(
            content=Mensaje,
            username=NOMBRE_BOT,
            avatar_url=AVATAR_BOT,
            tts=True,
            allowed_mentions=discord.AllowedMentions(
                everyone=True
            )
        )
        return "--Mensaje TTS enviado correctamente--"

#=========================================
#        CONFIGURACION DEL TKINTER
#=========================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

COLOR_ACENTO = "#6322AD"
COLOR_ACENTO_HOVER = "#2E114F"
COLOR_FONDO_CARD = "#1E1E2E"
FUENTE_TITULO = ("Segoe UI", 28, "bold")
FUENTE_SUBTITULO = ("Segoe UI", 15)
FUENTE_LABEL = ("Segoe UI", 15, "bold")
FUENTE_BOTON = ("Segoe UI", 13)

ACCIONES = ["Enviar Embed", "Enviar Texto", "Enviar Hilo", "Enviar Archivo", "Editar Embed", "Editar Mensaje", "Editar Hilo", "Borrar Mensaje", "Mensaje TTS"]

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Discord Webhook")
        self.geometry("820x820")
        self.resizable(False, False)
        self.Ruta_Lista = ""

        self.Crear_Emcabezado()
        self.Crear_Selector_Canal()
        self.Crear_Acciones()

        self.Card_Contenido = ctk.CTkFrame(self, corner_radius=15, fg_color=COLOR_FONDO_CARD)
        self.Card_Contenido.pack(pady=(10, 5), padx=25, fill="both", expand=True) 

        self.Crear_Boton_Enviar()
        self.Crear_Texto_Estado()

        self.Cambiar_Accion("Enviar Embed")       
#=========================================
#            INICIO CANALES
#=========================================
    def Crear_Emcabezado(self):
        Header = ctk.CTkFrame(self, fg_color="transparent")
        Header.pack(pady=(5, 5), padx=25, fill="x")

        ctk.CTkLabel(Header, text="Panel de Webhooks", font=FUENTE_TITULO).pack()
        ctk.CTkLabel(Header, text="Desarrollado por Sugarrigbi© Todos los derechos reservados", font=FUENTE_SUBTITULO).pack(pady=(0, 0))

    def Crear_Selector_Canal(self):
        Card = ctk.CTkFrame(self, corner_radius=15, fg_color=COLOR_FONDO_CARD)
        Card.pack(pady=5, padx=25, fill="x")

        ctk.CTkLabel(Card, text="Elegir Canal:", font=FUENTE_LABEL).pack(anchor="w", padx=20, pady=(5, 5))

        self.Combo_Canal = ctk.CTkComboBox(
            Card,
            values=list(WEBHOOKS_URLS.keys()),
            height=36,
            corner_radius=10,
            button_color=COLOR_ACENTO,
            border_color=COLOR_ACENTO,
            button_hover_color=COLOR_ACENTO_HOVER,
            dropdown_hover_color=COLOR_ACENTO_HOVER,
            dropdown_font=FUENTE_SUBTITULO,
            font=FUENTE_SUBTITULO
        )
        self.Combo_Canal.set(list(WEBHOOKS_URLS.keys())[0])
        self.Combo_Canal.pack(anchor="w", padx=20, pady=(0, 15), fill="x")

    def Crear_Acciones(self):
        Grid = ctk.CTkFrame(self, fg_color=COLOR_FONDO_CARD, corner_radius=15)
        Grid.pack(pady=5, padx=25, fill="x")
        ctk.CTkLabel(Grid, text="Elige una accion:", font=FUENTE_LABEL).pack(anchor="w", padx=20, pady=(5, 0))

        Grid2 = ctk.CTkFrame(Grid, fg_color="transparent")
        Grid2.pack(pady=(0, 10), padx=20, fill="x")

        self.Botones_Accion = {}

        for i, Nombre in enumerate(ACCIONES):
            Fila = i // 3 + 1
            Columna = i % 3

            Boton = ctk.CTkButton(
                Grid2,
                text=Nombre,
                height=32,
                corner_radius=8,
                font=FUENTE_BOTON,
                fg_color=COLOR_ACENTO, 
                hover_color=COLOR_ACENTO_HOVER,                
                command=lambda Valor=Nombre: self.Cambiar_Accion(Valor)
            )
            Boton.grid(row=Fila, column=Columna, padx=3, pady=3, sticky="ew")
            Grid2.grid_columnconfigure(Columna, weight=1)
            self.Botones_Accion[Nombre] = Boton

    def Cambiar_Accion(self, Nombre):
        self.Accion_Actual = Nombre

        for Nombre_Boton, Boton in self.Botones_Accion.items():
            if Nombre_Boton == Nombre:
                Boton.configure(fg_color=COLOR_ACENTO, hover_color=COLOR_ACENTO_HOVER)
            else:
                Boton.configure(fg_color="gray25", hover_color="gray35")

        for Widget in self.Card_Contenido.winfo_children():
            Widget.destroy()

        if Nombre == "Enviar Embed":
            self.Vista_Enviar_Embed()
        elif Nombre == "Enviar Texto":
            self.Vista_Enviar_Texto()
        elif Nombre == "Enviar Hilo":
            self.Vista_Enviar_Hilo()
        elif Nombre == "Enviar Archivo":
            self.Vista_Enviar_Archivo()
        elif Nombre == "Editar Embed":
            self.Vista_Editar_Embed()
        elif Nombre == "Editar Mensaje":
            self.Vista_Editar_Mensaje()
        elif Nombre == "Editar Hilo":
            self.Vista_Editar_Hilo()
        elif Nombre == "Borrar Mensaje":
            self.Vista_Borrar_Mensaje()
        elif Nombre == "Mensaje TTS":
            self.Vista_Mensaje_TTS()
#=========================================
#            VISTAS ACCIONES
#=========================================
    def Vista_Enviar_Embed(self):
        ctk.CTkLabel(self.Card_Contenido, text="Título", font=FUENTE_LABEL).pack(anchor="w", padx=18, pady=(5, 5))
        self.Embed_Titulo = ctk.CTkEntry(self.Card_Contenido, height=36, corner_radius=10)
        self.Embed_Titulo.pack(padx=18, fill="x")

        ctk.CTkLabel(self.Card_Contenido, text="Descripción", font=FUENTE_LABEL).pack(anchor="w", padx=18, pady=(5, 5))
        self.Embed_Descripcion = ctk.CTkTextbox(self.Card_Contenido, height=80, corner_radius=10)
        self.Embed_Descripcion.pack(padx=18, fill="x")

        ctk.CTkLabel(self.Card_Contenido, text="Imagen (opcional)", font=FUENTE_LABEL).pack(anchor="w", padx=18, pady=(5, 5))
        self.Embed_Imagen = ctk.CTkEntry(self.Card_Contenido, height=36, corner_radius=10, placeholder_text="URL de la imagen")
        self.Embed_Imagen.pack(padx=18, pady=(0, 10), fill="x")

        ctk.CTkLabel(self.Card_Contenido, text="Color (opcional)", font=FUENTE_LABEL).pack(anchor="w", padx=18, pady=(5, 5))
        self.Embed_Color = ctk.CTkEntry(self.Card_Contenido, height=36, corner_radius=10, placeholder_text="Color en HEX")
        self.Embed_Color.pack(padx=18, pady=(0, 10), fill="x")        

    def Vista_Enviar_Texto(self):
        ctk.CTkLabel(self.Card_Contenido, text="Mensaje", font=FUENTE_LABEL).pack(anchor="w", padx=18, pady=(18, 4))
        self.Texto_Mensaje = ctk.CTkTextbox(self.Card_Contenido, height=220, corner_radius=10)
        self.Texto_Mensaje.pack(padx=18, pady=(0, 18), fill="x")

    def Vista_Enviar_Hilo(self):
        ctk.CTkLabel(self.Card_Contenido, text="Título del hilo", font=FUENTE_LABEL).pack(anchor="w", padx=18, pady=(18, 4))
        self.Hilo_Titulo = ctk.CTkEntry(self.Card_Contenido, height=36, corner_radius=10)
        self.Hilo_Titulo.pack(padx=18, fill="x")

        ctk.CTkLabel(self.Card_Contenido, text="Contenido", font=FUENTE_LABEL).pack(anchor="w", padx=18, pady=(14, 4))
        self.Hilo_Descripcion = ctk.CTkTextbox(self.Card_Contenido, height=140, corner_radius=10)
        self.Hilo_Descripcion.pack(padx=18, pady=(0, 18), fill="x")

    def Vista_Enviar_Archivo(self):
        ctk.CTkLabel(self.Card_Contenido, text="Ruta del archivo", font=FUENTE_LABEL).pack(anchor="w", padx=18, pady=(18, 4))
        self.Archivo_Ruta = ctk.CTkButton(self.Card_Contenido, command=self.Buscar_Archivo, text="Subir Archivo", height=37, corner_radius=12, font=FUENTE_LABEL, fg_color=COLOR_ACENTO,  hover_color=COLOR_ACENTO_HOVER, width=150)
        self.Archivo_Ruta.pack(anchor="w", padx=18)

        self.Label_Ruta = ctk.CTkLabel(self.Card_Contenido, text="", font=FUENTE_LABEL)
        self.Label_Ruta.pack(padx=18,pady=(7, 0), anchor="w")

        ctk.CTkLabel(self.Card_Contenido, text="Mensaje (opcional)", font=FUENTE_LABEL).pack(anchor="w", padx=18, pady=(7, 4))
        self.Archivo_Mensaje = ctk.CTkEntry(self.Card_Contenido, height=36, corner_radius=10)
        self.Archivo_Mensaje.pack(padx=18, pady=(0, 18), fill="x")

    def Vista_Editar_Embed(self):
        ctk.CTkLabel(self.Card_Contenido, text="ID del mensaje", font=FUENTE_LABEL).pack(anchor="w", padx=18, pady=(2, 2))
        self.Embed_Editar_Id = ctk.CTkEntry(self.Card_Contenido, height=36, corner_radius=10)
        self.Embed_Editar_Id.pack(padx=18, fill="x")

        ctk.CTkLabel(self.Card_Contenido, text="Nuevo Titulo", font=FUENTE_LABEL).pack(anchor="w", padx=18, pady=(2, 2))
        self.Embed_Editar_Titulo = ctk.CTkEntry(self.Card_Contenido, height=36, corner_radius=10)
        self.Embed_Editar_Titulo.pack(padx=18, fill="x")

        ctk.CTkLabel(self.Card_Contenido, text="Nuevo contenido", font=FUENTE_LABEL).pack(anchor="w", padx=18, pady=(2, 2))
        self.Embed_Editar_Contenido = ctk.CTkTextbox(self.Card_Contenido, height=60, corner_radius=10)
        self.Embed_Editar_Contenido.pack(padx=18, pady=(2, 2), fill="x")        

        ctk.CTkLabel(self.Card_Contenido, text="Nueva imagen (opcional)", font=FUENTE_LABEL).pack(anchor="w", padx=18, pady=(2, 2))
        self.Embed_Editar_Imagen = ctk.CTkEntry(self.Card_Contenido, height=36, corner_radius=10)
        self.Embed_Editar_Imagen.pack(padx=18, fill="x")

        ctk.CTkLabel(self.Card_Contenido, text="Nuevo color (opcional)", font=FUENTE_LABEL).pack(anchor="w", padx=18, pady=(2, 2))
        self.Embed_Editar_Color = ctk.CTkEntry(self.Card_Contenido, height=36, corner_radius=10)
        self.Embed_Editar_Color.pack(padx=18, fill="x", pady=(0, 7))        

    def Vista_Editar_Mensaje(self):
        ctk.CTkLabel(self.Card_Contenido, text="ID del mensaje", font=FUENTE_LABEL).pack(anchor="w", padx=18, pady=(2, 2))
        self.Mensaje_Editar_Id = ctk.CTkEntry(self.Card_Contenido, height=36, corner_radius=10)
        self.Mensaje_Editar_Id.pack(padx=18, fill="x")

        ctk.CTkLabel(self.Card_Contenido, text="Nuevo contenido", font=FUENTE_LABEL).pack(anchor="w", padx=18, pady=(2, 2))
        self.Mensaje_Editar_Contenido = ctk.CTkTextbox(self.Card_Contenido, height=140, corner_radius=10)
        self.Mensaje_Editar_Contenido.pack(padx=18, pady=(2, 2), fill="x")        

    def Vista_Editar_Mensaje(self):
        ctk.CTkLabel(self.Card_Contenido, text="ID del mensaje", font=FUENTE_LABEL).pack(anchor="w", padx=18, pady=(2, 2))
        self.Mensaje_Editar_Id = ctk.CTkEntry(self.Card_Contenido, height=36, corner_radius=10)
        self.Mensaje_Editar_Id.pack(padx=18, fill="x")

        ctk.CTkLabel(self.Card_Contenido, text="Nuevo contenido", font=FUENTE_LABEL).pack(anchor="w", padx=18, pady=(2, 2))
        self.Mensaje_Editar_Contenido = ctk.CTkTextbox(self.Card_Contenido, height=140, corner_radius=10)
        self.Mensaje_Editar_Contenido.pack(padx=18, pady=(2, 2), fill="x")        

    def Vista_Editar_Hilo(self):
        ctk.CTkLabel(self.Card_Contenido, text="ID del mensaje", font=FUENTE_LABEL).pack(anchor="w", padx=18, pady=(2, 2))
        self.Hilo_Editar_Id_Mensaje = ctk.CTkEntry(self.Card_Contenido, height=36, corner_radius=10)
        self.Hilo_Editar_Id_Mensaje.pack(padx=18, fill="x")

        ctk.CTkLabel(self.Card_Contenido, text="ID del hilo", font=FUENTE_LABEL).pack(anchor="w", padx=18, pady=(2, 2))
        self.Hilo_Editar_Id_Hilo = ctk.CTkEntry(self.Card_Contenido, height=36, corner_radius=10)
        self.Hilo_Editar_Id_Hilo.pack(padx=18, fill="x")

        ctk.CTkLabel(self.Card_Contenido, text="Nuevo contenido", font=FUENTE_LABEL).pack(anchor="w", padx=18, pady=(2, 2))
        self.Hilo_Editar_Contenido = ctk.CTkTextbox(self.Card_Contenido, height=140, corner_radius=10)
        self.Hilo_Editar_Contenido.pack(padx=18, pady=(2, 2), fill="x")

    def Vista_Borrar_Mensaje(self):
        ctk.CTkLabel(self.Card_Contenido, text="ID del mensaje a borrar", font=FUENTE_LABEL).pack(anchor="w", padx=18, pady=(6, 6))
        self.Borrar_Id = ctk.CTkEntry(self.Card_Contenido, height=36, corner_radius=10)
        self.Borrar_Id.pack(padx=18, pady=(0, 18), fill="x")

    def Vista_Mensaje_TTS(self):
        ctk.CTkLabel(self.Card_Contenido, text="Mensaje (se lee en voz alta)", font=FUENTE_LABEL).pack(anchor="w", padx=18, pady=(6, 6))
        self.Tts_Mensaje = ctk.CTkTextbox(self.Card_Contenido, height=220, corner_radius=10)
        self.Tts_Mensaje.pack(padx=18, pady=(0, 18), fill="x")        
#=========================================
#            BOTONES ACCIONES
#=========================================
    def Buscar_Archivo(self):
        self.Ruta_Lista = filedialog.askopenfilename(title="Selecciona un archivo")
        if self.Ruta_Lista:
            self.Label_Ruta.configure(text=self.Ruta_Lista, text_color="#1D8EDE")            

    def Crear_Boton_Enviar(self):
        self.Boton_Enviar = ctk.CTkButton(
            self, 
            text="Enviar", 
            height=44, 
            corner_radius=12,
            font=FUENTE_LABEL,
            fg_color=COLOR_ACENTO, 
            hover_color=COLOR_ACENTO_HOVER,
            command=self.Click_Enviar            
        )
        self.Boton_Enviar.pack(pady=(10, 0), padx=250, fill="x")

    def Crear_Texto_Estado(self):
        self.Label_Estado = ctk.CTkLabel(self, text="", font=FUENTE_LABEL)
        self.Label_Estado.pack(pady=(7, 7))

    def Click_Enviar(self):
        Canal = self.Combo_Canal.get()
        Url_Webhook = WEBHOOKS_URLS.get(Canal)

        if self.Accion_Actual == "Enviar Embed":
            Titulo = self.Embed_Titulo.get()
            Descripcion = self.Embed_Descripcion.get("1.0", "end").strip()
            Imagen = self.Embed_Imagen.get()
            Color = self.Embed_Color.get()
            if Color == "":
                ColorF = int(COLOR_BOT, 16)   
            else:
                try:
                    ColorF = int(Color, 16)    
                except ValueError:
                    self.Label_Estado.configure(text="--El Color no esta en Hex--", text_color="#DE4A4A")            
                    return                
                ColorF = int(Color, 16)         

            Respuesta = asyncio.run(Enviar_Embed(Titulo, Descripcion, Url_Webhook, Color=ColorF,Imagen_Input=Imagen))
            self.Label_Estado.configure(text=Respuesta, text_color="#4ADE80")

            self.Embed_Titulo.delete(0, "end")
            self.Embed_Descripcion.delete("1.0", "end")
            self.Embed_Imagen.delete(0, "end")
            self.Embed_Color.delete(0, "end")

        elif self.Accion_Actual == "Enviar Texto":
            Mensaje = self.Texto_Mensaje.get("1.0", "end")

            Respuesta = asyncio.run(Enviar_Mensaje(Url_Webhook, Mensaje))
            self.Label_Estado.configure(text=Respuesta, text_color="#4ADE80")
            
            self.Texto_Mensaje.delete("1.0", "end")

        elif self.Accion_Actual == "Enviar Hilo":
            Titulo = self.Hilo_Titulo.get()
            Descripcion = self.Hilo_Descripcion.get("1.0", "end")

            Respuesta = asyncio.run(Enviar_Hilo(Url_Webhook, Titulo, Descripcion))
            if "--Error" in Respuesta:
                self.Label_Estado.configure(text=Respuesta, text_color="#DE4A4A")
            else:
                self.Label_Estado.configure(text=Respuesta, text_color="#4ADE80")

            self.Hilo_Titulo.delete(0, "end")
            self.Hilo_Descripcion.delete("1.0", "end")            

        elif self.Accion_Actual == "Enviar Archivo":
            Ruta = self.Ruta_Lista
            Mensaje = self.Archivo_Mensaje.get()

            Respuesta = asyncio.run(Enviar_Archivo(Url_Webhook, Mensaje, Ruta))
            if "--Error" in Respuesta:
                self.Label_Estado.configure(text=Respuesta, text_color="#DE4A4A")
            else:
                self.Label_Estado.configure(text=Respuesta, text_color="#4ADE80")
                self.Ruta_Lista = ""

            self.Label_Ruta.configure(text="")            
            self.Archivo_Mensaje.delete(0, "end")        

        elif self.Accion_Actual == "Editar Embed":
            Id = self.Embed_Editar_Id.get()
            if not Id.isdigit():
                self.Label_Estado.configure(text="--El ID debe ser un número válido--", text_color="#DE4A4A")
                return

            Titulo = self.Embed_Editar_Titulo.get()
            Contenido = self.Embed_Editar_Contenido.get("1.0", "end").strip()
            Imagen = self.Embed_Editar_Imagen.get()

            Color = self.Embed_Editar_Color.get()
            if Color == "":
                ColorF = int(COLOR_BOT, 16)   
            else:
                try:
                    ColorF = int(Color, 16)    
                except ValueError:
                    self.Label_Estado.configure(text="--El Color no esta en Hex--", text_color="#DE4A4A")            
                    return                
                ColorF = int(Color, 16)             

            Respuesta = asyncio.run(Editar_Embed(Url_Webhook, Id, Titulo, Contenido, ColorF, Imagen))
            if "--Error" in Respuesta:
                self.Label_Estado.configure(text=Respuesta, text_color="#DE4A4A")
            else:
                self.Label_Estado.configure(text=Respuesta, text_color="#4ADE80")

            self.Embed_Editar_Id.delete(0, "end")
            self.Embed_Editar_Titulo.delete(0, "end")
            self.Embed_Editar_Imagen.delete(0, "end")
            self.Embed_Editar_Color.delete(0, "end")
            self.Embed_Editar_Contenido.delete("1.0", "end")            

        elif self.Accion_Actual == "Editar Mensaje":
            Id = self.Mensaje_Editar_Id.get()
            if not Id.isdigit():
                self.Label_Estado.configure(text="--El ID debe ser un número válido--", text_color="#DE4A4A")
                return            
            Mensaje = self.Mensaje_Editar_Contenido.get("1.0", "end").strip()

            Respuesta = asyncio.run(Editar_Mensaje(Url_Webhook, Id, Mensaje))
            if "--Error" in Respuesta:
                self.Label_Estado.configure(text=Respuesta, text_color="#DE4A4A")
            else:
                self.Label_Estado.configure(text=Respuesta, text_color="#4ADE80") 

            self.Mensaje_Editar_Id.delete(0, "end")
            self.Mensaje_Editar_Contenido.delete("1.0", "end")                              

        elif self.Accion_Actual == "Editar Hilo":
            Id_Mensaje = self.Hilo_Editar_Id_Mensaje.get()
            Id_Hilo = self.Hilo_Editar_Id_Hilo.get()
            if not Id_Mensaje.isdigit():
                self.Label_Estado.configure(text="--El ID del mensaje debe ser un número válido--",text_color="#DE4A4A")
                return
            if not Id_Hilo.isdigit():
                self.Label_Estado.configure(text="--El ID del hilo debe ser un número válido--",text_color="#DE4A4A")
                return

            Contenido = self.Hilo_Editar_Contenido.get("1.0", "end").strip()

            Respuesta = asyncio.run(Editar_Hilo(Url_Webhook,int(Id_Mensaje),int(Id_Hilo),Contenido))

            if "--Error" in Respuesta:
                self.Label_Estado.configure(text=Respuesta, text_color="#DE4A4A")
            else:
                self.Label_Estado.configure(text=Respuesta, text_color="#4ADE80")

            self.Hilo_Editar_Id_Mensaje.delete(0, "end")
            self.Hilo_Editar_Id_Hilo.delete(0, "end")
            self.Hilo_Editar_Contenido.delete("1.0", "end")

        elif self.Accion_Actual == "Borrar Mensaje":
            Id_Mensaje = self.Borrar_Id.get()
            if not Id_Mensaje.isdigit():
                self.Label_Estado.configure(text="--El ID del mensaje debe ser un número válido--",text_color="#DE4A4A")
                return            
            
            Respuesta = asyncio.run(Borrar_Mensaje(Url_Webhook, int(Id_Mensaje)))
            if "--Error" in Respuesta:
                self.Label_Estado.configure(text=Respuesta, text_color="#DE4A4A")
            else:
                self.Label_Estado.configure(text=Respuesta, text_color="#4ADE80")            
            
            self.Id_Mensaje.delete(0, "end")

        elif self.Accion_Actual == "Mensaje TTS":
            Mensaje = self.Tts_Mensaje.get("1.0", "end")

            Respuesta = asyncio.run(Enviar_TTS(Url_Webhook, Mensaje))
            self.Label_Estado.configure(text=Respuesta, text_color="#4ADE80")
            
            self.Texto_Mensaje.delete("1.0", "end")

if __name__ == "__main__":
    App().mainloop()














