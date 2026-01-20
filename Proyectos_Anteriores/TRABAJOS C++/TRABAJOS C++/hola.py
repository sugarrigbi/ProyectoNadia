import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from time import strftime
from colorama import Fore, Style, init

if __name__ == "__main__":
#CREAR PANTALLA
    ventana = tk.Tk()
    ventana.title("Menu GaiaLink")
    ventana.geometry("1600x900")
    ventana.resizable(height = True, width = True)
    ventana.configure(background='#8cfdff')
#CREAR BOTON
    BotonArchivo = tk.Button(text='Elegir Archivo de datos', font=("Comic Sans MS", 28), bg="#CB9DFF", fg="black", bd=10)
    BotonArchivo.place(relx=0.5, rely=0.6, anchor="center")
    BotonArchivo.config(width=26, height=1)