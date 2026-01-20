import tkinter as tk

def accion1():
    texto.configure(text="Logica de programacion")
def acciona():
    texto.configure(text="Bienvenido al aplicativo de Logica de programacion")

ventana = tk.Tk()
ventana.title("ventana principal")
ventana.geometry("800x600")

barra_menus = tk.Menu(ventana)
ventana.config(menu=barra_menus)

menu = tk.Menu(barra_menus, tearoff=False)

menu.add_command(label="Materia Eje", command=accion1)

submenu = tk.Menu(menu, tearoff=False)
submenu.add_command(label="aplicativo", command=acciona)

menu.add_cascade(label="submenu", menu=submenu)

barra_menus.add_cascade(label="menu", menu=menu)

texto = tk.Label(ventana, text="Hola, bienvenido al Proyecto integrador, integrantes.")

texto.place(x=200, y=200)

if __name__ == "__main__":
 ventana.mainloop()