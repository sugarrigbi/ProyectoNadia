from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__,template_folder="Templates",static_folder="Statics")

API_URL = "http://127.0.0.1:5000/"

@app.route("/")
def Inicio():
    return render_template("homepage/inicio.html")
@app.route("/mision-y-vision")
def Mision():
    return render_template("homepage/mision.html")
@app.route("/soporte-tickets")
def Soporte():
    return render_template("homepage/soporte.html")
@app.route("/terminos-condiciones")
def Terminos():
    return render_template("homepage/terminos.html")
@app.route("/registro")
def Registro():
    return render_template("homepage/registro.html")
@app.route("/registro/codigo")
def Registro_Codigo():
    return render_template("homepage/registro2.html")
@app.route("/formularios")
def Formulario():
    return render_template("homepage/formularios.html")
@app.route("/login")
def Login():
    return render_template("homepage/login.html")
@app.route("/login/autenticador")
def Autenticador():
    return render_template("homepage/autenticador.html")
@app.route("/login/recuperar/usuario")
def Recuperar_Usuario():
    return render_template("homepage/recuperar1.html")
@app.route("/login/recuperar/codigo")
def Recuperar_Codigo():
    return render_template("homepage/recuperar2.html")
@app.route("/dashboard/admin")
def Dashboard_Admin():
    return render_template("dashboard/admin/dashboard.html")
@app.route("/dashboard/admin/inicio")
def Dashboard_Admin_Inicio():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return render_template("dashboard/admin/inicio.html")
    return render_template("dashboard/admin/dashboard.html")
@app.route("/dashboard/admin/casos")
def Dashboard_Admin_Casos():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return render_template("dashboard/admin/casos.html")
    return render_template("dashboard/admin/dashboard.html")
@app.route("/dashboard/admin/entidades")
def Dashboard_Admin_Entidades():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return render_template("dashboard/admin/entidades.html")
    return render_template("dashboard/admin/dashboard.html")
@app.route("/dashboard/admin/usuarios")
def Dashboard_Admin_Usuarios():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return render_template("dashboard/admin/usuarios.html")
    return render_template("dashboard/admin/dashboard.html")




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5009, debug=True)