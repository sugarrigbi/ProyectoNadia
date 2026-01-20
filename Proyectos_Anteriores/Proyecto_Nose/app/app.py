from flask import Flask, render_template, request, redirect, url_for, flash, session
from conexion import ConexionDB
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)

app.secret_key = 'Tu clave secreta'

db= ConexionDB(app)
conexion = db.mysql


#Creamos una ruta
@app.route('/')
def home():
    return render_template('home.html')


# GET y POST:
# GET se usa solo para mostrar páginas (no envía datos).
# POST se usa para enviar información (como contraseñas) sin mostrarla en la URL.
@app.route('/login', methods = ['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        usuario = request.form['usuario'] # request.form → toma los datos del formulario (lo que el usuario escribió).
        contraseña = request.form['contraseña'] # Guardamos lo que el usuario escribió en el formulario
        
        # Abrimos conexión con la base de datos usando un "cursor"
        # (el cursor sirve para ejecutar comandos SQL dentro de la base de datos)
        cursor = conexion.connection.cursor() #cursor: sirve para hablar con la base de datos (buscar, guardar, etc.).
        sql = """
            SELECT id_usuario, id_persona, id_contacto, id_rol,
                   usuario, password_hash, activo
            FROM usuarios
            WHERE usuario = %s
            LIMIT 1
        """# Creamos la consulta que buscará si el usuario y la contraseña existen
        cursor.execute(sql,(usuario,))  # Ejecutamos la consulta con los datos que el usuario escribió
        user = cursor.fetchone() # Buscamos si hay un registro que coincida
        cursor.close()  # Cerramos el cursor (ya no lo necesitamos)
        
        # Verificamos que se encontró el usuario
        if user is None:
            flash("Usuario o contraseña incorrectos.", "error")
            return render_template('login.html')
        
        if user[4] != usuario:
            flash("Usuario o contraseña incorrectos.", "error")
            return render_template('login.html')

        # Verificamos que la cuenta esté activa
        # Adaptamos por si el campo viene como 0/1 o como None
        activo = user[6]
        if activo is not None and int(activo) == 0:
            flash("Cuenta desactivada. Contacta al administrador.", "error")
            return render_template('login.html')

        # Verificamos la contraseña usando el hash almacenado
        password_hash = user[5]

        if user is not None and user[4] == usuario and check_password_hash(password_hash, contraseña):
            return render_template('menu_principal.html')  # acceso permitido
        else:
            flash("Usuario y contraseña incorrectos.", "error")
            return render_template('login.html')

    return render_template('login.html')


@app.route('/registro')
def registro():
    return render_template('registro.html')
    

@app.route('/menu')
def menu():
    
    return render_template('menu.html')


if __name__=='__main__':
    app.run(debug=True, port=5000)