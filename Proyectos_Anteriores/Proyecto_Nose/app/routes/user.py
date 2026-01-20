"""
Vistas de Usuario
"""
# app/routes/user.py
from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models.controler import Registro, Consulta


user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/dashboard')
def dashboard():
    return render_template('user_dashboard.html', username=session["username"])

@user_bp.route("/register_case", methods=["GET", "POST"])
def register_case():
    return Registro().registrar_caso_usuario()


@user_bp.route('/manage-account')
def manage_account():
    return "Gestionar cuenta (placeholder)"

@user_bp.route("/query_cases", methods=["GET"])
def query_cases():
    return Consulta().buscar_caso_usuario()