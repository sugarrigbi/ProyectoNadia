"""
Vistas de Usuario
"""
# app/routes/user.py
from flask import Blueprint, render_template, request, redirect, url_for, session
from app.queries import get_user_by_name,get_user_role

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/dashboard')
def dashboard():
    print(f"Accediendo a dashboard, session: {session}")  # Depuración
    if 'username' not in session or session.get('username') is None:
        print("Sesión no válida, redirigiendo a login")
        return redirect(url_for('auth.login'))
    
    # Obtener datos del usuario usando el Nombre de la sesión
    username = session.get('username')
    user = get_user_by_name(username)
    if not user:
        print("Usuario no encontrado, redirigiendo a login")
        return redirect(url_for('auth.login'))
    
    role = get_user_role(username)
    print(f"Dashboard para {username}, rol: {role}")  # Depuración
    
    return render_template('user_dashboard.html', username=username, role=role)