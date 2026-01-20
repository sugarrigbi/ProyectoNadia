import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import re

def parse_line(line):
    """
    Extrae función y condición (opcional) de una línea tipo:
    'f(x) = 2*x + 4, (x > 0)' o solo '2*x + 4'
    Devuelve (func_str, interval_str) o (func_str, None)
    """
    parts = line.split(',')
    func_part = parts[0].strip()
    cond_part = parts[1].strip() if len(parts) > 1 else None

    # Si la función empieza con 'f(x)=' o 'f(x) =', quita esa parte
    match = re.match(r'f\(x\)\s*=\s*(.*)', func_part)
    if match:
        func_str = match.group(1)
    else:
        func_str = func_part  # Asume que toda la parte es función

    if cond_part:
        cond_str = cond_part.strip('()')
    else:
        cond_str = None

    return func_str, cond_str

def graficar():
    texto = text_input.get("1.0", tk.END).strip()
    if not texto:
        messagebox.showerror("Error", "Escribe al menos una función")
        return

    lineas = texto.split('\n')
    funcs = []
    intervals = []

    for linea in lineas:
        func_str, interval_str = parse_line(linea)
        if func_str is None:
            return

        try:
            # Usamos eval para la función; permite usar np (numpy) para funciones más complejas
            f = lambda x, expr=func_str: eval(expr, {"x": x, "np": np})
            if interval_str:
                interval = lambda x, cond=interval_str: eval(cond, {"x": x, "np": np})
            else:
                # Si no hay condición, válido para todo x
                interval = lambda x: True

            funcs.append(f)
            intervals.append(interval)
        except Exception as e:
            messagebox.showerror("Error", f"Error al crear funciones:\n{e}")
            return

    x_vals = np.linspace(-50, 50, 2000)
    y_vals = []

    for x in x_vals:
        y = np.nan
        for f, interval in zip(funcs, intervals):
            try:
                if interval(x):
                    y = f(x)
                    break
            except:
                continue
        y_vals.append(y)

    ax.clear()
    ax.plot(x_vals, y_vals, label='f(x)')
    ax.set_title("Funciones por tramos")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True)
    ax.legend()
    canvas.draw()

root = tk.Tk()
root.title("Graficador tipo GeoGebra")

instrucciones = tk.Label(root, text="Escribe funciones con condición (opcional), una por línea, ejemplo:\n2*x + 4, (x > 0)\n-x + 6\n")
instrucciones.pack()

text_input = tk.Text(root, height=8, width=60)
text_input.pack()

boton = tk.Button(root, text="Graficar", command=graficar)
boton.pack(pady=10)

fig, ax = plt.subplots(figsize=(7,4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()
