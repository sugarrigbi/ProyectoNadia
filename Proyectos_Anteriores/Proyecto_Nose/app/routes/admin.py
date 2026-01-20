"""
Vistas de administrador
"""

# app/routes/admin.py
from flask import Blueprint, render_template, request, redirect, url_for, session
admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/dashboard')
def dashboard():
    
    return render_template('admin_dashboard.html')


@admin_bp.route('/register-case')
def register_case():
    return "Formulario para registrar caso (placeholder)"

@admin_bp.route('/query-cases')
def query_cases():
    return "Listado de casos (placeholder)"

@admin_bp.route('/generate-report')
def generate_report():
    return "Generar reporte (placeholder)"

@admin_bp.route('/manage-cases')
def manage_cases():
    return redirect(url_for('admin.query_cases'))

@admin_bp.route('/manage-account')
def manage_account():
    return "Gestionar cuenta (placeholder)"

@admin_bp.route('/account-help')
def account_help():
    return "Ayuda de cuenta (placeholder)"

@admin_bp.route('/query-user')
def query_user():
    return "Consultar usuario (placeholder)"

@admin_bp.route('/query-disasters')
def query_disasters():
    return "Consultar datos de desastres (placeholder)"