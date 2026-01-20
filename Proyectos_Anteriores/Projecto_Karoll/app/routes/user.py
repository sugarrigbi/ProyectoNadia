"""
Vistas de Usuario
"""
# app/routes/user.py
from flask import Blueprint, render_template, session,jsonify
from app.controler.controler import Registro, Consulta, Actualizar


user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/dashboard')
def dashboard():
    return render_template('user_dashboard.html', username=session["username"])

@user_bp.route("/register_case", methods=["GET", "POST"])
def register_case():
    return Registro().registrar_caso_usuario()


@user_bp.route('/manage-account', methods=["GET"])
def manage_account():
    return Consulta().ver_datos_usuario()

@user_bp.route("/query_cases", methods=["GET"])
def query_cases():
    casos =Consulta().buscar_caso_usuario()
    return jsonify (casos)

@user_bp.route('/update_account', methods=['POST'])
def update_account():
    return Actualizar().actualizar_datos_usuario()

@user_bp.route('/change_password', methods=['POST'])
def change_password():
    return Actualizar().cambiar_contrasena_usuario()
    
    
