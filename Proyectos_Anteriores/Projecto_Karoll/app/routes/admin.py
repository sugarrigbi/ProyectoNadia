"""
Vistas de administrador
"""

# app/routes/admin.py
from flask import Blueprint, render_template, request, redirect, url_for, session,jsonify
from app.controler.controler import Registro,Consulta,Actualizar


admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/dashboard')
def dashboard():
    return render_template('admin_dashboard.html', username = session["username"])


@admin_bp.route('/register_case', methods=["GET", "POST"])
def register_case():
    return Registro().registrar_caso_usuario()

@admin_bp.route('/query_cases')
def query_cases():
    casos = Consulta().buscar_casos_admin()
    return jsonify(casos)

@admin_bp.route('/generate_report', methods=["GET", "POST"])
def generate_report():
    return Consulta().generar_reporte()

@admin_bp.route('/manage-account')
def manage_account():
    return "Gestionar cuenta (placeholder)"

@admin_bp.route('/select_users')
def select():
    return Consulta().obtener_usuarios()

@admin_bp.route('/query_users')
def query_users():
    return Consulta().obtener_usuarios()

@admin_bp.route('/query-disasters')
def query_disasters():
    return "Consultar datos de desastres (placeholder)"