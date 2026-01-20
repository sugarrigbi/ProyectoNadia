# app/routes/auth.py
from flask import Blueprint, render_template, request, redirect, url_for, session
from app.queries import get_user_by_name, get_user_role  # Importación absoluta
from app.insertions import insert_user  # Importación absoluta
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_user_by_name(username)
        print(f"Usuario: {user}, Contraseña ingresada: {password}")
        if user and user[2] == password:  # Comparación de contraseña en texto plano
            session['username'] = username  # Id_usuario
            role = get_user_role(username) # fk_rol
            print(f"Login exitoso para {username}, rol: {role}")
            if role == 'Admin':
                return redirect(url_for('admin.dashboard'))
            else:
                return redirect(url_for('user.dashboard'))
        print(f"Fallo de login para {username}")
        return "Invalid credentials"
    
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Asumiendo roles y estados predefinidos (ajusta según tu lógica)
        insert_user('002USU', username, password, 'Usu', 'usuario_01')  # Ejemplo, genera un ID único
        return redirect(url_for('auth.login'))
    return render_template('register.html')