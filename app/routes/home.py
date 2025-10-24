from flask import Blueprint, render_template
from app.models.Casos import Caso
home_bp  = Blueprint('home', __name__)

@home_bp.route("/")
def home():
    return render_template("index.html")

#PRUEBA
@home_bp.route("/Contraseña-Recuperar")
def home4():
    return render_template("Contraseña-Recuperar.html")
@home_bp.route("/mision")
def home6():
    return render_template("mision.html")
@home_bp.route("/soporte")
def home8():
    return render_template("soporte.html")
@home_bp.route("/terminos")
def home9():
    return render_template("terminos.html")