from flask import Blueprint
from app.utilities.Route.formularios import get_ayuda, get_calificanos, get_contactanos
form_bp = Blueprint("form", __name__)

@form_bp.route("/ayuda", methods=["GET", "POST"])
def ayuda():
    return get_ayuda()

@form_bp.route("/calificanos", methods=["GET", "POST"])
def calificanos():
    return get_calificanos()

@form_bp.route("/contactanos", methods=["POST"])
def contactanos():
    return get_contactanos()
