import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.clock import Clock
from kivy.metrics import dp, sp
from kivy.core.window import Window
from kivy.network.urlrequest import UrlRequest  # Red nativa y segura para Android
import traceback

#=========================================
#          CONFIGURACION DEL BOT
#=========================================
AVATAR_BOT = "https://i.pinimg.com/1200x/7a/34/f5/7a34f5bf09e75b480306182a67a88031.jpg"
NOMBRE_BOT = "Moon-Bot"
COLOR_BOT_DEF = 4524467  # 0x4509B3 en entero

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

ACCIONES = ["Enviar Embed", "Enviar Texto", "Enviar Hilo", "Editar Embed", "Editar Mensaje", "Editar Hilo", "Borrar Mensaje", "Mensaje TTS"]

# Paleta Dark unificada
COLOR_BOTON_ACTIVO = (0.450, 0.156, 0.811, 1)  # Morado Eléctrico
COLOR_BOTON_OFF = (0.219, 0.219, 0.298, 1)     # Gris sutil pasivo
COLOR_CARD = (0.133, 0.133, 0.196, 1)         # Fondo de los campos
COLOR_TEXTO_MUTED = (0.643, 0.643, 0.756, 1)   # Etiquetas secundarias

class PanelWebhooks(BoxLayout):
    def __init__(self, **kwargs):
        super(PanelWebhooks, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(16)
        self.spacing = dp(12)
        self.Accion_Actual = "Enviar Embed"
        self.inputs = {}

        # Títulos fluidos
        self.add_widget(Label(text="Panel de Webhooks", font_size=sp(24), bold=True, size_hint=(1, None), height=dp(35)))
        self.add_widget(Label(text="Sugarrigbi© Todos los derechos reservados", font_size=sp(11), color=COLOR_TEXTO_MUTED, size_hint=(1, None), height=dp(15)))

        # Selector de canal
        self.add_widget(Label(text="Elegir Canal:", bold=True, font_size=sp(13), color=COLOR_TEXTO_MUTED, size_hint=(1, None), height=dp(20), halign="left", text_size=(Window.width - dp(32), None)))
        self.Combo_Canal = Spinner(
            text=list(WEBHOOKS_URLS.keys())[0],
            values=list(WEBHOOKS_URLS.keys()),
            size_hint=(1, None),
            height=dp(45),
            background_normal='',
            background_color=COLOR_BOTON_ACTIVO,
            font_size=sp(13)
        )
        self.add_widget(self.Combo_Canal)

        # Matriz de acciones
        self.add_widget(Label(text="Elige una acción:", bold=True, font_size=sp(13), color=COLOR_TEXTO_MUTED, size_hint=(1, None), height=dp(20)))
        self.Grid_Acciones = GridLayout(cols=3, spacing=dp(6), size_hint=(1, None), height=dp(110))
        self.Botones_Accion = {}
        for nombre in ACCIONES:
            btn = Button(text=nombre, font_size=sp(11), background_normal='', background_color=COLOR_BOTON_ACTIVO if nombre == self.Accion_Actual else COLOR_BOTON_OFF)
            btn.bind(on_press=lambda instance, n=nombre: self.Cambiar_Accion(n))
            self.Grid_Acciones.add_widget(btn)
            self.Botones_Accion[nombre] = btn
        self.add_widget(self.Grid_Acciones)

        # Zona central deslizable
        self.Scroll_Contenido = ScrollView(size_hint=(1, 1))
        self.Card_Contenido = BoxLayout(orientation='vertical', spacing=dp(10), size_hint_y=None)
        self.Card_Contenido.bind(minimum_height=self.Card_Contenido.setter('height'))
        self.Scroll_Contenido.add_widget(self.Card_Contenido)
        self.add_widget(self.Scroll_Contenido)

        # Botón de ejecución principal y respuesta
        self.Boton_Enviar = Button(text="Enviar", size_hint=(1, None), height=dp(50), background_normal='', background_color=COLOR_BOTON_ACTIVO, font_size=sp(16), bold=True)
        self.Boton_Enviar.bind(on_press=self.Click_Enviar)
        self.add_widget(self.Boton_Enviar)

        self.Label_Estado = Label(text="", size_hint=(1, None), height=dp(25), font_size=sp(13), color=(0.29, 0.87, 0.5, 1))
        self.add_widget(self.Label_Estado)

        self.Cambiar_Accion("Enviar Embed")

    def Cambiar_Accion(self, nombre):
        self.Accion_Actual = nombre
        self.Card_Contenido.clear_widgets()
        self.inputs.clear()

        for k, btn in self.Botones_Accion.items():
            btn.background_color = COLOR_BOTON_ACTIVO if k == nombre else COLOR_BOTON_OFF

        if nombre == "Enviar Embed":
            self.crear_label_input("Título", "Embed_Titulo")
            self.crear_label_input("Descripción", "Embed_Descripcion", multiline=True)
            self.crear_label_input("Imagen (URL opcional)", "Embed_Imagen")
            self.crear_label_input("Color (HEX opcional)", "Embed_Color")
        elif nombre == "Enviar Texto":
            self.crear_label_input("Mensaje", "Texto_Mensaje", multiline=True)
        elif nombre == "Enviar Hilo":
            self.crear_label_input("Título del hilo", "Hilo_Titulo")
            self.crear_label_input("Contenido", "Hilo_Descripcion", multiline=True)
        elif nombre == "Editar Embed":
            self.crear_label_input("ID del mensaje", "Embed_Editar_Id")
            self.crear_label_input("Nuevo Título", "Embed_Editar_Titulo")
            self.crear_label_input("Nuevo Contenido", "Embed_Editar_Contenido", multiline=True)
            self.crear_label_input("Nueva Imagen (URL)", "Embed_Editar_Imagen")
            self.crear_label_input("Nuevo Color (HEX)", "Embed_Editar_Color")
        elif nombre == "Editar Mensaje":
            self.crear_label_input("ID del mensaje", "Mensaje_Editar_Id")
            self.crear_label_input("Nuevo Contenido", "Mensaje_Editar_Contenido", multiline=True)
        elif nombre == "Editar Hilo":
            self.crear_label_input("ID del mensaje", "Hilo_Editar_Id_Mensaje")
            self.crear_label_input("ID del hilo", "Hilo_Editar_Id_Hilo")
            self.crear_label_input("Nuevo Contenido", "Hilo_Editar_Contenido", multiline=True)
        elif nombre == "Borrar Mensaje":
            self.crear_label_input("ID del mensaje a borrar", "Borrar_Id")
        elif nombre == "Mensaje TTS":
            self.crear_label_input("Mensaje (Voz alta)", "Tts_Mensaje", multiline=True)

    def crear_label_input(self, texto_label, clave, multiline=False):
        lbl = Label(text=texto_label, font_size=sp(13), color=COLOR_TEXTO_MUTED, size_hint=(1, None), height=dp(20), halign="left")
        lbl.bind(size=lambda s, w: setattr(lbl, 'text_size', (w[0], None)))
        self.Card_Contenido.add_widget(lbl)
        
        txt_input = TextInput(
            multiline=multiline, 
            size_hint=(1, None), 
            height=dp(90) if multiline else dp(40), 
            font_size=sp(14),
            background_normal='',
            background_color=COLOR_CARD,
            foreground_color=(1, 1, 1, 1),
            cursor_color=COLOR_BOTON_ACTIVO
        )
        self.Card_Contenido.add_widget(txt_input)
        self.inputs[clave] = txt_input

    def respuesta_exitosa(self, req, resultado):
        self.Label_Estado.text = "-- Acción ejecutada correctamente --"
        self.Label_Estado.color = (0.3, 0.9, 0.5, 1)
        for v in self.inputs.values(): v.text = ""

    def respuesta_fallida(self, req, error):
        self.Label_Estado.text = f"-- Error al enviar la solicitud --"
        self.Label_Estado.color = (0.9, 0.3, 0.3, 1)

    def Click_Enviar(self, instance):
        Canal = self.Combo_Canal.text
        Url_Webhook = WEBHOOKS_URLS.get(Canal)
        datos = {k: v.text.strip() for k, v in self.inputs.items()}
        
        base_payload = {"username": NOMBRE_BOT, "avatar_url": AVATAR_BOT, "allowed_mentions": {"everyone": True}}
        url_final = Url_Webhook
        metodo = "POST"

        if self.Accion_Actual == "Enviar Embed":
            color_hex = datos.get("Embed_Color", "")
            color_f = COLOR_BOT_DEF
            if color_hex:
                try: color_f = int(color_hex, 16)
                except ValueError:
                    self.Label_Estado.text = "-- Error: El color no está en Hex --"
                    self.Label_Estado.color = (0.9, 0.3, 0.3, 1)
                    return
            embed = {"title": datos.get("Embed_Titulo"), "description": datos.get("Embed_Descripcion"), "color": color_f}
            if datos.get("Embed_Imagen"): embed["image"] = {"url": datos.get("Embed_Imagen")}
            base_payload["embeds"] = [embed]

        elif self.Accion_Actual == "Enviar Texto":
            base_payload["content"] = datos.get("Texto_Mensaje")

        elif self.Accion_Actual == "Enviar Hilo":
            base_payload["content"] = datos.get("Hilo_Descripcion")
            base_payload["thread_name"] = datos.get("Hilo_Titulo")

        elif self.Accion_Actual == "Editar Embed":
            idx = datos.get("Embed_Editar_Id")
            if not idx.isdigit(): return
            metodo = "PATCH"
            url_final = f"{Url_Webhook}/messages/{idx}"
            color_hex = datos.get("Embed_Editar_Color", "")
            color_f = COLOR_BOT_DEF if not color_hex else int(color_hex, 16)
            embed = {"title": datos.get("Embed_Editar_Titulo"), "description": datos.get("Embed_Editar_Contenido"), "color": color_f}
            if datos.get("Embed_Editar_Imagen"): embed["image"] = {"url": datos.get("Embed_Editar_Imagen")}
            base_payload = {"embeds": [embed]}

        elif self.Accion_Actual == "Editar Mensaje":
            idx = datos.get("Mensaje_Editar_Id")
            if not idx.isdigit(): return
            metodo = "PATCH"
            url_final = f"{Url_Webhook}/messages/{idx}"
            base_payload = {"content": datos.get("Mensaje_Editar_Contenido")}

        elif self.Accion_Actual == "Editar Hilo":
            id_m = datos.get("Hilo_Editar_Id_Mensaje")
            id_h = datos.get("Hilo_Editar_Id_Hilo")
            if not id_m.isdigit() or not id_h.isdigit(): return
            metodo = "PATCH"
            url_final = f"{Url_Webhook}/messages/{id_m}?thread_id={id_h}"
            base_payload = {"content": datos.get("Hilo_Editar_Contenido")}

        elif self.Accion_Actual == "Borrar Mensaje":
            idx = datos.get("Borrar_Id")
            if not idx.isdigit(): return
            metodo = "DELETE"
            url_final = f"{Url_Webhook}/messages/{idx}"
            base_payload = None

        elif self.Accion_Actual == "Mensaje TTS":
            base_payload["content"] = datos.get("Tts_Mensaje")
            base_payload["tts"] = True

        self.Label_Estado.text = "Enviando..."
        self.Label_Estado.color = COLOR_TEXTO_MUTED

        headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        req_body = json.dumps(base_payload) if base_payload is not None else ""
        
        UrlRequest(
            url_final,
            req_body=req_body,
            req_headers=headers,
            method=metodo,
            on_success=self.respuesta_exitosa,
            on_failure=self.respuesta_fallida,
            on_error=self.respuesta_fallida
        )

class MainApp(App):
    def build(self):
        try:
            self.title = "Discord Webhook Panel"
            from kivy.utils import get_color_from_hex
            Window.clearcolor = get_color_from_hex('#121218')  # Fondo negro azulado limpio
            return PanelWebhooks()
        except Exception as e:
            # BLINDAJE ANTI-CRASH: Muestra el error exacto si falla al arrancar
            layout_err = BoxLayout(orientation='vertical', padding=dp(20))
            layout_err.add_widget(Label(text="Error detectado en la carga:", color=(1,0.3,0.3,1), size_hint_y=None, height=dp(40)))
            txt_err = TextInput(text=traceback.format_exc(), readonly=True, background_color=(0.1,0.1,0.15,1), foreground_color=(1,1,1,1))
            layout_err.add_widget(txt_err)
            return layout_err

if __name__ == "__main__":
    MainApp().run()
