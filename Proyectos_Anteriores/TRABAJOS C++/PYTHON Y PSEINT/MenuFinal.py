import tkinter as tk
import webbrowser
from PIL import Image, ImageTk

def accion1():
    texto.configure(text="Bienvenido al apartado de Logica de Programacion", font=("Comic Sans MS", 40), bg="#F2B9FF")
    texto.place(relx=0.5, rely=0.4, anchor='center')
    abutton.place(relx=0.5, rely=0.6, anchor="center")
    bbutton.place_forget()
    cbutton.place_forget()
    dbutton.place_forget()
def accion2():
    texto.configure(text="Bienvenido al apartado de Sistemas Operativos", font=("Comic Sans MS", 40), bg="#F2B9FF")
    texto.place(relx=0.5, rely=0.4, anchor='center')
    bbutton.place(relx=0.5, rely=0.6, anchor="center")
    abutton.place_forget()
    cbutton.place_forget()
    dbutton.place_forget()
def accion3():
    texto.configure(text="Bienvenido al apartado de Introduccion al Hardware", font=("Comic Sans MS", 40), bg="#F2B9FF")
    texto.place(relx=0.5, rely=0.4, anchor='center')
    cbutton.place(relx=0.5, rely=0.6, anchor="center")
    bbutton.place_forget()
    abutton.place_forget()
    dbutton.place_forget()
def accion4():
    texto.configure(text="Bienvenido al apartado de Ingles", font=("Comic Sans MS", 40), bg="#F2B9FF")
    texto.place(relx=0.5, rely=0.4, anchor='center')
    dbutton.place(relx=0.5, rely=0.6, anchor="center")
    bbutton.place_forget()
    cbutton.place_forget()
    abutton.place_forget()
def open_webside():
    webbrowser.open('https://andressagux14.wixsite.com/master-engineering/copia-de-sistemas-operativos')
def open_webside2():
    webbrowser.open('https://andressagux14.wixsite.com/master-engineering/sistemas-operativos')
def open_webside3():
    webbrowser.open('https://andressagux14.wixsite.com/master-engineering/introducci%C3%B3n-al-hardware')
def open_webside4():
    webbrowser.open('https://andressagux14.wixsite.com/master-engineering/english')
    
ventana = tk.Tk()

ventana.title("Menu interactivo")
ventana.geometry("1250x1024")
ventana.resizable(height = True, width = True)

barra_menus = tk.Menu(ventana)
ventana.config(menu=barra_menus)

menu = tk.Menu(barra_menus, tearoff=False)

submenu = tk.Menu(menu, tearoff=False)

menu.add_command(label="Logica de Programacion", command=accion1)

menu.add_command(label="Sistemas Operativos", command=accion2)

menu.add_command(label="Introduccion al Hardware", command=accion3)

menu.add_command(label="Ingles", command=accion4)

abutton = tk.Button(text='Página Lógica de Programacion', command=open_webside, font=("Comic Sans MS", 28), bg="#CB9DFF", fg="black", bd=10)
abutton.place(relx=0.5, rely=0.6, anchor="center")
abutton.config(width=26, height=1)

bbutton = tk.Button(text='Página Sistemas Operativos', command=open_webside2, font=("Comic Sans MS", 28), bg="#CB9DFF", fg="black", bd=10)
bbutton.place(relx=0.5, rely=0.6, anchor="center")
bbutton.config(width=26, height=1)

cbutton = tk.Button(text='Página Introduccion al Hardware', command=open_webside3, font=("Comic Sans MS", 28), bg="#CB9DFF", fg="black", bd=10)
cbutton.place(relx=0.5, rely=0.6, anchor="center")
cbutton.config(width=28, height=1)

dbutton = tk.Button(text='Página Inglés', command=open_webside4, font=("Comic Sans MS", 28), bg="#CB9DFF", fg="black", bd=10)
dbutton.place(relx=0.5, rely=0.6, anchor="center")
dbutton.config(width=18, height=1)

abutton.place_forget()
bbutton.place_forget()
cbutton.place_forget()
dbutton.place_forget()

barra_menus.add_cascade(label="Asignaturas", menu=menu)

texto = tk.Label(ventana, text="Hola, bienvenido a nuestro Proyecto Integrador", font=("Comic Sans MS", 40), bg="#F2B9FF")
texto.place(relx=0.5, rely=0.5, anchor='center')

if __name__ == "__main__":
    
 ventana.mainloop()