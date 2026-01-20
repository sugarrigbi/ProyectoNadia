from flask import Flask, render_template
from conexion import ConexionDB


app = Flask(__name__)

db= ConexionDB(app)
conexion = db.mysql


#Creamos una ruta
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/registro')
def registro():
    return render_template('registro.html')
    

@app.route('/menu')
def menu():
    return render_template('menu.html')

if __name__=='__main__':
    app.run(debug=True, port=5000)