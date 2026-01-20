import unicodedata
from Clase import *
from customtkinter import *
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox

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