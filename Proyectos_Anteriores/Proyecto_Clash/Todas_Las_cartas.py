import unicodedata
from Clase import *
from customtkinter import *
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox

class Carta_Tropa():
    def __init__(self, Nombre_Español, Nombre_Ingles, Coste, Calidad, Velocidad, Objetivo, Vida, Daño):
        self.Nombre_Español = Nombre_Español
        self.Nombre_Ingles = Nombre_Ingles
        self.Coste = Coste
        self.Calidad = Calidad
        self.Velocidad = Velocidad
        self.Objetivo = Objetivo
        self.Vida = Vida
        self.Daño = Daño

class Carta_Hechizo():
    def __init__(self, Nombre_Español, Nombre_Ingles, Coste, Calidad, Objetivo, Daño):
        self.Nombre_Español = Nombre_Español
        self.Nombre_Ingles = Nombre_Ingles
        self.Coste = Coste
        self.Calidad = Calidad
        self.Objetivo = Objetivo
        self.Daño = Daño

class Carta_Estructura():
    def __init__(self, Nombre_Español, Nombre_Ingles, Coste, Calidad, Objetivo, Vida, Daño, Generacion):
        self.Nombre_Español = Nombre_Español
        self.Nombre_Ingles = Nombre_Ingles
        self.Coste = Coste
        self.Calidad = Calidad
        self.Objetivo = Objetivo
        self.Vida = Vida
        self.Daño = Daño
        self.Generacion = Generacion
#1 de Elixir
Esqueletos = Carta_Tropa("Esqueletos", "Skeletons", 1, "Comun", "Rapido", "Terrestre", 81, 81)
Espíritu_Eléctrico = Carta_Tropa("Espíritu Eléctrico", "Electro Spirit", 1, "Comun", "Muy Rapido", "Terrestre y Aereo", 230, 99)
Espíritu_De_Fuego = Carta_Tropa("Espíritu De Fuego", "Fire Spirit", 1, "Comun", "Muy Rapido", "Terrestre y Aereo", 230, 207)
Espíritu_De_Hielo = Carta_Tropa("Espíritu De Hielo", "Ice Spirit", 1, "Comun", "Muy Rapido", "Terrestre y Aereo", 230, 110)
Espíritu_Sanador = Carta_Tropa("Espíritu Sanador", "Heal Spirit", 1, "Especial", "Muy Rapido", "Terrestre y Aereo", 230, 110)
#2 de Elixir
Duendes = Carta_Tropa("Duendes", "Goblins", 2, "Comun", "Muy Rapido", "Terrestre", 202, 120)
Duendes_Con_Lanza = Carta_Tropa("Duendes Con Lanza", "Spear Goblins", 2, "Comun", " Muy Rapido", "Terrestre y Aereo", 133, 81)
Bombardero = Carta_Tropa("Bombardero", "Bomber", 2, "Comun", "Medio", "Terrestre", 332, 225)
Murcielagos = Carta_Tropa("Murcielagos", "Bats", 2, "Comun", "Muy Rapido", "Terrestre y Aereo", 81, 81)
Descarga = Carta_Hechizo("Descarga", "Zap", 2, "Comun", "Terrestre y Aereo", 192)
Bola_De_Nieve = Carta_Hechizo("Bola De Nieve", "Snowball", 2, "Comun", "Terrestre y Aereo", 179)
Berserker = Carta_Tropa("Berserker", "Berserker", 2, "Comun", "Rapido", "Terrestre", 896, 102)
Golem_De_Hielo = Carta_Tropa("Golem De Hielo", "Ice Golem", 2, "Especial", "Lento", "Estructuras", 1318, 84)
Arbusto_Sospechoso = Carta_Tropa("Arbusto Sospechoso", "Suspicious Bush", 2, "Especial", "Medio", "Estructuras", 227, 81)
Barril_De_Barbaro = Carta_Hechizo("Barril De Barbaro", "Barbarian Barrel", 2, "Epica", "Terrestre", 240)
Rompemuros = Carta_Tropa("Rompemuros", "Wall Breakers", 2, "Epica", "Muy Rapido", "Terrestre", 391, 330)
Maldicion_de_Duendes = Carta_Hechizo("Maldicion de Duendes", "Goblin Curse", 2, "Epica", "Terrestre y Aereo", 180)
Furia = Carta_Hechizo("Furia", "Rage", 2, "Epica", "Terrestre y Aereo", 895)
Tronco = Carta_Hechizo("Tronco", "The Log", 2, "Legendaria", "Terrestre", 266)
#3 de Elixir
Arqueras = Carta_Tropa("Arqueras", "Archers", 3, "Comun", "Medio", "Terrestre y Aereo", 304, 112)
Flechas = Carta_Hechizo("Flechas", "Arrows", 3, "Comun", "Terrestre y Aereo", 366)
Caballero = Carta_Tropa("Caballero", "Knight", 3, "Comun", "Medio", "Terrestre", 1766, 202)
Esbirros = Carta_Tropa("Esbirros", "Minions", 3, "Comun", "Rapido", "Terrestre y Aereo", 230, 117)
Cañón = Carta_Estructura("Cañón", "Cannon", 3, "Comun", "Terrestre", 824, 212, 0)
Pandilla_De_Duendes = Carta_Tropa("Pandilla De Duendes", "Goblin Gang", 3, "Comun", "Muy Rapido", "Terrestre y Aereo", 202, 120)
Barril_De_Esqueletos = Carta_Tropa("Barril De Esqueletos", "Skeleton Barrel", 3, "Comun", "Rapido", "Estructura", 532, 145)
Lanza_Fuegos = Carta_Tropa("Lanza Fuegos", "Firecracker", 3, "Comun", "Rapido", "Terrestre y Aereo", 304, 320)
Paquete_Real = Carta_Hechizo("Paquete Real", "Royal Delivery", 3, "Comun", "Terrestre y Aerea", 437)
Lapida = Carta_Estructura("Lapida", "Tombstone", 3, "Especial", "Terrestre", 529, 81, "Esqueletos")
Megaesbirro = Carta_Tropa("Megaesbirro", "Mega Minion", 3, "Especial", "Media", "Terrestre y Aereo", 837, 312)
Lanza_Dardos = Carta_Tropa("Lanza Dardos", "Dart Goblin", 3, "Especial", "Muy Rapido", "Terrestre y Aereo", 261, 156)
Terremoto = Carta_Hechizo("Terremoto", "Earthquake", 3, "Especial", "Terrestre", 243)
Golem_De_Elixir = Carta_Tropa("Golem De Elixir", "Elixir Golem", 3, "Especial", "Lento", "Estructuras", 1569, 253)
Barril_De_Duendes = Carta_Hechizo("Barril De Duendes", "Goblin_Barrel", 3, "Epica", "Estructuras", "?")
Guardias = Carta_Tropa("Guardias", "Guards", 3, "Epica", "Rapido", "Terrestre", 117, 256)
Ejército_De_Esqueletos = Carta_Tropa("Ejército De Esqueletos", "Skeleton Army", 3, "Epica", "Rapido", "Terrestre", 81, 81)
Clon = Carta_Hechizo("Clon", "Clon", 3, "Epica", "Tropas Propias", "?")
Tornado = Carta_Hechizo("Tornado", "Tornado", 3, "Epica", "Terrestre y Aereo", 84)
Vacio = Carta_Hechizo("Vacio", "Void", 3, "Epica", "Terrestre y Aereo", 960)
Minero = Carta_Tropa("Minero", "Miner", 3, "Legendaria", "Rapido", "Terrestre", 1210, 194)
Princesa = Carta_Tropa("Princesa", "Princess", 3, "Legendaria", "Medio", "Terrestre y Aereo", 261, 168)
Mago_De_Hielo = Carta_Tropa("Mago De Hielo", "Ice Wizard", 3, "Legendaria", "Medio", "Terrestre Y Aereo", 688, 89)
Fantasma_Real = Carta_Tropa("Fantasma Real", "Royal_Ghost", 3, "Legendaria", "Rapido", "Terrestre", 1210, 261)
Bandida = Carta_Tropa("Bandida", "Bandit", 3, "Legendaria", "Rapido", "Terrestre", 906, 194)
Pescador = Carta_Tropa("Pescador", "Fisherman", 3, "Legendaria", "Medio", "Terrestre y Aereo", 870, 194)
Principito = Carta_Tropa("Principito", "Little Prince", 3, "Campeon", "Medio", "Terrestre y Aereo", 698, 102)
#4 de Elixir
Dragones_Esqueleto = Carta_Tropa("Dragones Esqueleto", "Skeleton Dragons", 4, "Comun", "Rapido", "Terrestre y Aereo", 560, 161)
Mortero = Carta_Estructura("Mortero", "Mortar", 4, "Comun", "Terrestre", 1369, 266, 0)
Tesla = Carta_Estructura("Tesla", "Tesla", 4, "Comun", "Terrestre y Aereo", 1152, 220, 0)
Bola_De_Fuego = Carta_Hechizo("Bola_De_Fuego", "Fireball", 4, "Especial", "Terrestre y Aereo", 688)
Mini_Pekka = Carta_Tropa("Mini P.E.K.K.A", "Mini P.E.K.K.A", 4, "Especial", "Rapido", "Terrestre", 1428, 755)
Mosquetera = Carta_Tropa("Mosquetera", "Musketeer", 4, "Especial", "Medio", "Terrestre y Aereo", 721, 217)
Jaula_Del_Forzudo = Carta_Estructura("Jaula Del Forzudo", "Goblin Cage", 4, "Especial", "Terrestre", 780, 212, "Forzudo")
Choza_De_Duendes = Carta_Estructura("Choza De Duendes", "Goblin Hut", 4, "Especial", "Terrestre y Aereo", 1305, 81, "Duendes Con Lanza")
Valquiria = Carta_Tropa("Valquiria", "Valkyrie", 4, "Especial", "Medio", "Terrestre", 1907, 266)
Ariete = Carta_Tropa("Ariete", "Battle Ram", 4, "Especial", "Medio", "Estructuras", 967, 286)
Torre_Bombardera = Carta_Estructura("Torre Bombardera", "Bomb Tower", 4, "Especial", "Terrestre", 1356, 222, "Bomba")
Maquina_Voladora = Carta_Tropa("Maquina Voladora", "Flying Machine", 4, "Especial", "Rapido", "Terrestre y Aereo", 614, 171)
Monta_Puercos = Carta_Tropa("Monta Puercos", "Hog Rider", 4, "Especial", "Muy Rapido", "Estructuras", 1697, 317)
Sanadora = Carta_Tropa("Sanadora", "Battle_Healer", 4, "Especial", "Medio", "Terrestre", 1717, 148)
Horno = Carta_Tropa("Horno", "Furnace", 4, "Especial", "Lento", "Terrestre y Aereo", 896, 135)
Electrocutadores = Carta_Tropa("Electrocutadores", "Zappies", 4, "Especial", "Medio", "Terrestre y Aereo", 529, 117)
Duende_Demoledor = Carta_Tropa("Duende Demoledor", "Goblin Demolisher", 4, "Especial", "Medio", "Terrestre", 1300, 186)
Bebe_Dragon = Carta_Tropa("Bebe Dragon", "Baby Dragon", 4, "Epica", "Rapido", "Terrestre y Aereo", 1152, 161)
Principe_Oscuro = Carta_Tropa("Principe Oscuro", "Dark_Prince", 4, "Epica", "Medio", "Terrestre", 1200, 248)
Hielo = Carta_Hechizo("Hielo", "Ice", 4, "Epica", "Terrestre y Aereo", 115)
Veneno = Carta_Hechizo("Veneno", "Poison", 4, "Epica", "Terrestre y Aereo", 736)
Gigante_Runica = Carta_Tropa("Gigante Runica", "Rune Giant", 4, "Epica", "Medio", "Estructura", 2662, 120)
Cazador = Carta_Tropa("Cazador", "Hunter", 4, "Epica", "Medio", "Terrestre y Aereo", 885, 832)
Excavadora = Carta_Estructura("Excavadora", "Goblin Drill", 4, "Epica", "Estructura", 1313, 120, "Duendes")
Mago_Eléctrico = Carta_Tropa("Mago Eléctrico ", "Electro Wizard", 4, "Legendaria", "Rapido", "Terrestre y Aereo", 714, 235)
Dragón_Infernal = Carta_Tropa("Dragón Infernal", "Inferno Dragon", 4, "Legendaria", "Medio", "Terrestre y Aereo", 1295, 35)
Fenix = Carta_Tropa("Fenix", "Phoenix", 4, "Legendaria", "Medio", "Terrestre y Aereo", 1052, 217)
Arquero_Mágico = Carta_Tropa("Arquero Mágico", "Magic Archer", 4, "Legendaria", "Medio", "Terrestre y Aereo", 529, 133)
Leñador = Carta_Tropa("Leñador", "Lumberjack", 4, "Legendaria", "Muy Rapido", "Terrestre", 1282, 256)
Bruja_Nocturna = Carta_Tropa("Bruja Nocturna", "Night Witch", 4, "Legendaria", "Medio", "Terrestre", 906, 314)
Bruja_Madre = Carta_Tropa("Bruja Madre", "Mother Witch", 4, "Legendaria", "Medio", "Terrestre y Aereo", 529, 133)
Caballero_Dorado = Carta_Tropa("Caballero Dorado ", "Golden Knight", 4, "Campeon", "Medio", "Terrestre", 1799, 161)
Rey_Esqueleto = Carta_Tropa("Rey Esqueleto", "Skeleton King", 4, "Campeon", "Medio", "Terrestre", 2298, 204)
Gran_Minero  = Carta_Tropa("Gran Minero", "Mighty Miner", 4, "Campeon", "Medio", "Terrestre", 2250, 40)
#5 de Elixir
Barbaros = Carta_Tropa("Barbaros", "Barbarians", 5, "Comun", "Medio", "Terrestre", 670, 192)
Horda_De_Esbirros = Carta_Tropa("Horda De Esbirros", "Skeletons", 5, "Comun", "Rapido", "Terrestre y Aereo", 230, 117)
Pillos = Carta_Tropa("Pillos", "Rascals", 5, "Comun", "Medio", "Terrestre y Aereo", 1940, 204)
Gigante = Carta_Tropa("Gigante", "Giant", 5, "Especial", "Lento", "Estructuras", 4090, 253)
Torre_Infernal = Carta_Estructura("Torre Infernal", "Inferno Tower", 5, "Especial", "Terrestre y Aereo", 1748, 43, 0)
Mago = Carta_Tropa("Mago", "Wizard", 5, "Especial", "Medio", "Terrestre y Aereo", 755, 281)
Cerdos_Reales = Carta_Tropa("Cerdos Reales", "Royal Hogs", 5, "Especial", "Muy Rapido", "Estructuras", 837, 74)
Bruja = Carta_Tropa("Bruja", "Witch", 5, "Epica", "Medio", "Terrestre y Aereo", 839, 135)
Globo = Carta_Tropa("Globo", "Balloon", 5, "Epica", "Medio", "Estructuras", 1679, 640)
Principe = Carta_Tropa("Principe", "Prince", 5, "Epica", "Medio", "Terrestre", 1920, 391)
Dragon_Electrico = Carta_Tropa("Dragon Electrico", "Electro Dragon", 5, "Epica", "Medio", "Terrestre y Aereo", 949, 192)
Lanzarocas = Carta_Tropa("Lanzarocas", "Bowler", 5, "Epica", "Lento", "Terrestre", 2081, 289)
Verdugo = Carta_Tropa("Verdugo", "Executioner", 5, "Epica", "Medio", "Terrestre y Aereo", 1280, 168)
Cañon_Con_Ruedas = Carta_Tropa("Cañon Con Ruedas", "Cannon Cart", 5, "Epica", "Medio", "Terrestre", 1809, 212)
Montacarneros = Carta_Tropa("Montacarneros", "Ram Rider", 5, "Legendaria", "Medio", "Estructuras", 1697, 250)
Cementerio = Carta_Hechizo("Cementerio", "Graveyard", 5, "Legendaria", "Terrestre", "???")
Maquina_Duende = Carta_Tropa("Maquina Duende", "Goblin Machine", 5, "Legendaria", "Media", "Terrestre", 2304, 212)
Reina_Arquera = Carta_Tropa("Reina Arquera", "Archer Queen", 5, "Campeon", "Medio", "Terrestre y Aereo", 1000, 225)
Monje = Carta_Tropa("Monje", "Monk", 5, "Campeon", "Medio", "Terrestre", 2214, 140)
Duendestein = Carta_Tropa("Duendestein", "Goblinstein", 5, "Campeon", "Medio", "Estructuras", 2393, 128)
#6 de Elixir
Gigante_Noble = Carta_Tropa("Gigante Noble", "Royal Giant", 6, "Comun", "Lento", "Estructuras", 3164, 307)
Barbaros_De_Elite = Carta_Tropa("Barbaros De Elite", "Elite Barbarians", 6, "Comun", "Rapido", "Terrestre", 1341, 384)
Cohete = Carta_Hechizo("Cohete", "Rocket", 6, "Especial", "Terrestre y Aereo", 1484)
Choza_De_Barbaros = Carta_Estructura("Choza De Barbaros", "Barbarian Hut", 6, "Especial", "Sin Objetivo", 1164, 192, "Barbaros")
Recolector_De_Elixir = Carta_Estructura("Recolector De Elixir", "Elixir Collector", 6, "Especial", "Sin Objetivo", 1070, 0, "Elixir")
Esqueleto_Gigante = Carta_Tropa("Esqueleto Gigante", "Giant Skeleton", 6, "Epica", "Medio", "Terrestre", 3617, 276)
Rayo = Carta_Hechizo("Rayo", "Lightning", 6, "Epica", "Terrestre y Aereo", 1057)
Duende_Gigante = Carta_Tropa("Duende Gigante", "Goblin Giant", 6, "Epica", "Medio", "Terrestre y Aereo", 3233, 176)
Ballesta = Carta_Estructura("Ballesta", "X-Bow", 6, "Epica", "Terrestre", 1600, 43, 0)
Chispitas = Carta_Tropa("Chispitas", "Sparky", 6, "Legendaria", "Lento", "Terrestre", 1451, 1331)
Emperatriz_Espiritual = Carta_Tropa("Emperatriz Espiritual", "Spirit Empress", 6, "Legendaria", "Medio", "Terrestre", 1318, 307)
Jefa_Bandida = Carta_Tropa("Jefa Bandida", "Boss Bandit", 6, "Campeon", "Rapido", "Terrestre", 2624, 268)
#7 de Elixir
Reclutas_Reales = Carta_Tropa("Reclutas Reales", "Royal Recruits", 7, "Comun", "Medio", "Terrestre", 547, 133)
Pekka = Carta_Tropa("P.E.K.K.A", "P.E.K.K.A", 7, "Epica", "Lento", "Terrestre", 3760, 816)
Gigante_Electrico = Carta_Tropa("Gigante Electrico", "Electro Giant", 7, "Epica", "Lento", "Estructuras", 3855, 163)
Mega_Caballero = Carta_Tropa("Mega Caballero", "Mega Knight", 7, "Legendaria", "Medio", "Terrestre", 3993, 268)
Sabueso_De_Lava = Carta_Tropa("Sabueso De Lava", "Lava Hound", 7, "Legendaria", "Lento", "Estructuras", 3581, 53)
#8 de Elixir
Golem = Carta_Tropa("Golem", "Golem", 8, "Epica", "Lento", "Estructuras", 5120, 312)
#9 de Elixir
Trio_De_Mosqueteras = Carta_Tropa("Trio De Mosqueteras", "Three Musketeers", 9, "Especial", "Medio", "Terrestre y Aereo", 721, 217)
Espejo = Carta_Hechizo("Espejo", "mirror", 1, "Epica", "Tropas Propias", "???")

def normalizar(texto):
    texto = texto.lower()
    texto = texto.replace("_", " ")
    texto = texto.replace(".", "")
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    return texto.strip()

root = CTk()
root.title("Cartas")
root.configure(fg_color="#33283e")
root.resizable(height=True, width=True)
set_appearance_mode("dark")

App_Ancho = 1200
App_Alto = 980
Ventana_Ancho = root.winfo_screenwidth()
Ventana_Alto = root.winfo_screenheight()
Cordenada_X = (Ventana_Ancho // 2) - (App_Ancho // 2)
Cordenada_Y = (Ventana_Alto // 2) - (App_Alto // 2)
root.geometry(f"{App_Ancho}x{App_Alto}+{Cordenada_X}+{Cordenada_Y}")

todas_las_cartas = [
    Esqueletos,
    Espíritu_Eléctrico,
    Espíritu_De_Fuego,
    Espíritu_De_Hielo,
    Espíritu_Sanador,
    Duendes,
    Duendes_Con_Lanza,
    Bombardero,
    Murcielagos,
    Descarga,
    Bola_De_Nieve,
    Berserker,
    Golem_De_Hielo,
    Arbusto_Sospechoso,
    Barril_De_Barbaro,
    Rompemuros,
    Maldicion_de_Duendes,
    Furia,
    Tronco,
    Arqueras,
    Flechas,
    Caballero,
    Esbirros,
    Cañón,
    Pandilla_De_Duendes,
    Barril_De_Esqueletos,
    Lanza_Fuegos,
    Paquete_Real,
    Lapida,
    Megaesbirro,
    Lanza_Dardos,
    Terremoto,
    Golem_De_Elixir,
    Barril_De_Duendes,
    Guardias,
    Ejército_De_Esqueletos,
    Clon,
    Tornado,
    Vacio,
    Minero,
    Princesa,
    Mago_De_Hielo,
    Fantasma_Real,
    Bandida,
    Pescador,
    Principito,
    Dragones_Esqueleto,
    Mortero,
    Tesla,
    Bola_De_Fuego,
    Mini_Pekka,
    Mosquetera,
    Jaula_Del_Forzudo,
    Choza_De_Duendes,
    Valquiria,
    Ariete,
    Torre_Bombardera,
    Maquina_Voladora,
    Monta_Puercos,
    Sanadora,
    Horno,
    Electrocutadores,
    Duende_Demoledor,
    Bebe_Dragon,
    Principe_Oscuro,
    Hielo,
    Veneno,
    Gigante_Runica,
    Cazador,
    Excavadora,
    Mago_Eléctrico,
    Dragón_Infernal,
    Fenix,
    Arquero_Mágico,
    Leñador,
    Bruja_Nocturna,
    Bruja_Madre,
    Caballero_Dorado,
    Rey_Esqueleto,
    Gran_Minero,
    Barbaros,
    Horda_De_Esbirros,
    Pillos,
    Gigante,
    Torre_Infernal,
    Mago,
    Cerdos_Reales,
    Bruja,
    Globo,
    Principe,
    Dragon_Electrico,
    Lanzarocas,
    Verdugo,
    Cañon_Con_Ruedas,
    Montacarneros,
    Cementerio,
    Maquina_Duende,
    Reina_Arquera,
    Monje,
    Duendestein,
    Gigante_Noble,
    Barbaros_De_Elite,
    Cohete,
    Choza_De_Barbaros,
    Recolector_De_Elixir,
    Esqueleto_Gigante,
    Rayo,
    Duende_Gigante,
    Ballesta,
    Chispitas,
    Emperatriz_Espiritual,
    Jefa_Bandida,
    Reclutas_Reales,
    Pekka,
    Gigante_Electrico,
    Mega_Caballero,
    Sabueso_De_Lava,
    Golem,
    Trio_De_Mosqueteras,
    Espejo
]

mapa_cartas = {}
for carta in todas_las_cartas:
    nombre_norm = normalizar(carta.Nombre_Español)
    mapa_cartas[nombre_norm] = carta

colores = {
    "Comun": "#1E90FF",
    "Especial": "#CD853F",
    "Epica": "#DA70D6",
    "Legendaria": "#90EE90",
    "Campeon": "#FFD700"
}
colores_oscuro = {
    "Comun": "#145EAA",
    "Especial": "#8B5A2B", 
    "Epica": "#7B3F7B", 
    "Legendaria": "#4C6B4C", 
    "Campeon": "#B8860B"
}
columnas = ["Comun", "Especial", "Epica", "Legendaria", "Campeon"]
filas_por_columna = [29, 30, 32, 21, 8]

tabla_frame = ctk.CTkFrame(root, fg_color="#33283e")
tabla_frame.pack(padx=20, pady=20)

celdas = {col: [] for col in columnas}

for col, titulo in enumerate(columnas):
    lbl = ctk.CTkLabel(
        tabla_frame,
        text=titulo,
        fg_color="black",
        text_color="white",
        width=150,
        height=20
    )
    lbl.grid(row=0, column=col, sticky="nsew", padx=1, pady=1)

for col, titulo in enumerate(columnas):
    for fila in range(1, filas_por_columna[col] + 1):
        celda = ctk.CTkLabel(
            tabla_frame,
            text="",
            fg_color=colores[titulo],
            width=150,
            height=25
        )
        celda.grid(row=fila, column=col, sticky="nsew", padx=1, pady=1)
        celdas[titulo].append(celda)

posiciones_por_calidad = {calidad: {} for calidad in columnas}
contador_por_calidad = {calidad: 0 for calidad in columnas}

for carta in todas_las_cartas:
    calidad = carta.Calidad
    if calidad in posiciones_por_calidad:
        clave_norm = normalizar(carta.Nombre_Español)
        posiciones_por_calidad[calidad][clave_norm] = contador_por_calidad[calidad]
        contador_por_calidad[calidad] += 1

for calidad in columnas:
    for celda in celdas[calidad]:
        celda.configure(text="", fg_color=colores[calidad])

entry_frame = ctk.CTkFrame(root, fg_color="#33283e")
entry_frame.pack(pady=10)

entry = ttk.Entry(entry_frame, width=40)
entry.grid(row=0, column=0, padx=5, pady=5)

def verificar_carta(event=None):
    texto = normalizar(entry.get())
    if texto in mapa_cartas:
        carta = mapa_cartas[texto]
        calidad = carta.Calidad
        if calidad in celdas:
            indice = posiciones_por_calidad[calidad].get(texto)
            if indice is not None:
                celda = celdas[calidad][indice]
                if celda.cget("text") == "":
                    texto_celda = f"{indice + 1}: {carta.Nombre_Español}"
                    celda.configure(
                    text=texto_celda,
                    fg_color=colores_oscuro[calidad],
                    text_color="white"
                    )
                    entry.delete(0, tk.END)
                else:
                    messagebox.showinfo("Aviso", f"La carta '{carta.Nombre_Español}' ya está colocada.")
                    entry.delete(0, tk.END)
            else:
                messagebox.showinfo("Aviso", "Carta no encontrada en posiciones.")
                entry.delete(0, tk.END)
    else:
        messagebox.showinfo("Aviso", f"No existe la carta '{entry.get()}'")
        entry.delete(0, tk.END)

entry.bind("<Return>", verificar_carta)

root.mainloop()