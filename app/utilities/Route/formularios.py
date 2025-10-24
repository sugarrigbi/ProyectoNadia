from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.utilities.Formularios import Enviar_Form_Ayuda, Enviar_Form_Calificanos, Enviar_Form_Contactanos

def get_ayuda():
    if request.method == "POST":
        Nombre = request.form["Nombre"]
        Mensaje = request.form["Ayuda"]
        mensaje, tipo = Enviar_Form_Ayuda(Nombre, Mensaje)
        return render_template("ayuda.html", confirmacion=mensaje, tipo=tipo)
    return render_template("ayuda.html")
def get_calificanos():
    if request.method == "POST":
        Nombre = request.form["Nombre"]
        Pregunta1 = request.form["pregunta1"]
        Pregunta2 = request.form["pregunta2"]
        Pregunta3 = request.form["pregunta3"]
        Pregunta4 = request.form["pregunta4"]
        mensaje, tipo = Enviar_Form_Calificanos(Nombre, Pregunta1, Pregunta2, Pregunta3, Pregunta4)
        return render_template("calificanos.html", confirmacion=mensaje, tipo=tipo)
    return render_template("calificanos.html")
def get_contactanos():
    if request.method == "POST":
        Nombre = request.form["Nombre"]
        Telefono = request.form["Telefono"]
        Correo = request.form["Correo"]
        Descripcion = request.form["Descripcion"]

        mensaje, tipo = Enviar_Form_Contactanos(Nombre, Telefono, Correo, Descripcion)
        return render_template("index.html", confirmacion=mensaje, tipo=tipo, anchor="Index_Place7")
    return redirect("/#Index_Place7")