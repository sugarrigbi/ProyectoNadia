from flask import Blueprint
from app.utilities.Route.login import get_registrar, get_login, get_logout, get_recuperar, get_recuperar_token, get_dashboard

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/registro", methods=["GET", "POST"])
def registrar():
    return get_registrar()
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    return get_login()
@auth_bp.route("/logout")
def logout():
    return get_logout()
@auth_bp.route("/recuperar", methods=["GET", "POST"])
def recuperar():
    return get_recuperar()
@auth_bp.route("/recuperar-token", methods=["GET", "POST"])
def recuperar_token():
    return get_recuperar_token()
@auth_bp.route("/dashboard/admin")
def admin():
    return get_dashboard()
@auth_bp.route("/dashboard/user")
def user():
    return get_dashboard()
