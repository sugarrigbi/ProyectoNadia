from flask import Flask, render_template, request
import requests

app = Flask(__name__,template_folder="Templates",static_folder="Statics")

API_URL = "http://127.0.0.1:5000/api"

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


@app.route("/dashboard")
def Dashboard_Admin():
    return render_template("dashboard/dashboard.html")
@app.route("/dashboard/inicio")
def Dashboard_Admin_Inicio():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return render_template("dashboard/inicio.html")
    return render_template("dashboard/dashboard.html")
@app.route("/dashboard/staff/casos")
def Dashboard_Admin_Casos():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return render_template("dashboard/no_auth.html")
        headers = {"Authorization": auth_header}
        
        Response = requests.get(f"{API_URL}/case/read/all", headers=headers)
        Response2 = requests.get(f"{API_URL}/case/read/data", headers=headers)
        Response3 = requests.get(f"{API_URL}/case/read/tiempo", headers=headers)
        if Response.status_code == 401 and Response2.status_code == 401 and Response3.status_code == 401:
            return render_template("dashboard/no_auth.html")
        
        Casos = Response.json()
        Data = Response2.json()
        Linea = Response3.json()

        return render_template("dashboard/casos.html", Casos=Casos, Data=Data, Linea_Tiempo=Linea)
    return render_template("dashboard/dashboard.html")
@app.route("/dashboard/staff/casos/<int:Case_ID>")
def Dashboard_Admin_Casos_One(Case_ID):
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return render_template("dashboard/no_auth.html")
        headers = {"Authorization": auth_header}

        Response = requests.get(f"{API_URL}/case/read/{Case_ID}", headers=headers)
        Response2 = requests.get(f"{API_URL}/case/read/data", headers=headers)
        Response3 = requests.get(f"{API_URL}/case/read/tiempo", headers=headers)
        if Response.status_code == 401 and Response2.status_code == 401 and Response3.status_code == 401:
            return render_template("dashboard/no_auth.html")        

        Casos = Response.json()
        Data = Response2.json()
        Linea = Response3.json()
        return render_template("dashboard/casos.html", Casos=Casos, Data=Data, Linea_Tiempo=Linea)
    return render_template("dashboard/dashboard.html")
@app.route("/dashboard/staff/casos/search")
def Dashboard_Admin_Casos_By():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return render_template("dashboard/no_auth.html")
        headers = {"Authorization": auth_header}

        Filtros = request.args.to_dict(flat=False)
        Response = requests.get(f"{API_URL}/case/read/search", params=Filtros, headers=headers)
        Response2 = requests.get(f"{API_URL}/case/read/data", headers=headers)
        Response3 = requests.get(f"{API_URL}/case/read/tiempo", headers=headers)
        if Response.status_code == 401 and Response2.status_code == 401 and Response3.status_code == 401:
            return render_template("dashboard/no_auth.html")        

        Casos = Response.json()
        Data = Response2.json()
        Linea = Response3.json()

        return render_template("dashboard/casos.html", Casos=Casos, Data=Data, Linea_Tiempo=Linea)
    return render_template("dashboard/dashboard.html")
@app.route("/dashboard/entidades")
def Dashboard_Admin_Entidades():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return render_template("dashboard/entidades.html")
    return render_template("dashboard/dashboard.html")
@app.route("/dashboard/usuarios")
def Dashboard_Admin_Usuarios():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return render_template("dashboard/usuarios.html")
    return render_template("dashboard/dashboard.html")
@app.route("/dashboard/preferencias")
def Dashboard_Admin_Preferencias():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return render_template("dashboard/preferencias.html")
    return render_template("dashboard/dashboard.html")
@app.route("/dashboard/pruebas")
def Dashboard_Admin_Pruebas():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return render_template("dashboard/asd.html")
    return render_template("dashboard/dashboard.html")

@app.route("/dashboard/unauthorized")
def Unauthorized():
    return render_template("dashboard/no_auth.html")
@app.route("/rate-limit")
def Rate_Limit():
    return render_template("homepage/rate_limit.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5009, debug=True)