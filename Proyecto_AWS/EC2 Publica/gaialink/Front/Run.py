from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request, redirect, url_for
from requests.exceptions import ConnectionError
from datetime import datetime
import requests
import os

app = Flask(__name__,template_folder="Templates",static_folder="Statics")

API_URL = os.getenv("API_URL")

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
        
        Pagina = request.args.get("page", 1, type=int)       
        Response = requests.get(f"{API_URL}/case/read/all/{Pagina}", headers=headers)
        if Response.status_code == 401:
            return Response.json(), 401
        elif Response.status_code == 403:
            return render_template("dashboard/no_auth.html")

        Datos = Response.json()

        Casos = Datos.get("Casos", [])
        Data = Datos.get("Datos", {})
        Linea = Datos.get("Linea", [])
        Paginas_Validas = int(Datos.get("Paginas_Validas", 1))
        Pagina_Actual = int(Datos.get("Pagina", 1))

        return render_template("dashboard/casos_admin.html", Casos=Casos, Data=Data, Linea_Tiempo=Linea, Paginas_Validas=Paginas_Validas, Pagina_Actual=Pagina_Actual)
    return render_template("dashboard/dashboard.html")
@app.route("/dashboard/staff/casos/search")
def Dashboard_Admin_Casos_By():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return render_template("dashboard/no_auth.html")
        headers = {"Authorization": auth_header}

        Filtros = request.args.to_dict(flat=False)
        Pagina = request.args.get("page", 1, type=int)         
        Response = requests.get(f"{API_URL}/case/read/search/{Pagina}", params=Filtros, headers=headers)
        if Response.status_code == 401:
            return Response.json(), 401
        elif Response.status_code == 403:
            return render_template("dashboard/no_auth.html")
        
        Datos = Response.json()

        Casos = Datos.get("Casos", [])
        Data = Datos.get("Datos", {})
        Linea = Datos.get("Linea", [])
        Paginas_Validas = int(Datos.get("Paginas_Validas", 1))
        Pagina_Actual = int(Datos.get("Pagina", 1))        

        return render_template("dashboard/casos_admin.html", Casos=Casos, Data=Data, Linea_Tiempo=Linea, Paginas_Validas=Paginas_Validas, Pagina_Actual=Pagina_Actual)
    return render_template("dashboard/dashboard.html")
@app.route("/dashboard/user/casos")
def Dashboard_User_Casos():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return render_template("dashboard/no_auth.html")
        headers = {"Authorization": auth_header}
        
        Pagina = request.args.get("page", 1, type=int)              
        Response = requests.get(f"{API_URL}/case/read/all/{Pagina}", headers=headers)
        if Response.status_code == 401:
            return Response.json(), 401
        elif Response.status_code == 403:
            return render_template("dashboard/no_auth.html") 
        
        Datos = Response.json()

        Casos = Datos.get("Casos", [])
        Data = Datos.get("Datos", {})
        Linea = Datos.get("Linea", [])
        Paginas_Validas = int(Datos.get("Paginas_Validas", 1))
        Pagina_Actual = int(Datos.get("Pagina", 1))          

        return render_template("dashboard/casos_user.html", Casos=Casos, Data=Data, Linea_Tiempo=Linea, Paginas_Validas=Paginas_Validas, Pagina_Actual=Pagina_Actual)
    return render_template("dashboard/dashboard.html")
@app.route("/dashboard/usuarios")
def Dashboard_Admin_Usuarios():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return render_template("dashboard/usuarios.html")
    return render_template("dashboard/dashboard.html")
@app.route("/dashboard/staff/entidades")
def Dashboard_Admin_Entidades():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return render_template("dashboard/no_auth.html")
        headers = {"Authorization": auth_header}
        
        Response = requests.get(f"{API_URL}/entity/read/all", headers=headers)
        if Response.status_code == 401:
            return Response.json(), 401
        elif Response.status_code == 403:
            return render_template("dashboard/no_auth.html")

        Datos = Response.json()
        Entidades = Datos.get("Entidades", [])
        Data = Datos.get("Datos", {})

        return render_template("dashboard/entidades_admin.html", Entidades=Entidades, Data=Data)
    return render_template("dashboard/dashboard.html")
@app.route("/dashboard/staff/entidades/search")
def Dashboard_Admin_Entidades_By():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return render_template("dashboard/no_auth.html")
        headers = {"Authorization": auth_header}

        Filtros = request.args.to_dict(flat=False)
        Response = requests.get(f"{API_URL}/entity/read/search", params=Filtros, headers=headers)
        if Response.status_code == 401:
            return Response.json(), 401
        elif Response.status_code == 403:
            return render_template("dashboard/no_auth.html")

        Datos = Response.json()
        Entidades = Datos.get("Entidades", [])
        Data = Datos.get("Datos", {})

        return render_template("dashboard/entidades_admin.html", Entidades=Entidades, Data=Data)
    return render_template("dashboard/dashboard.html")
@app.route("/dashboard/staff/health")
def Dashboard_Admin_Health():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        try:
            Response = requests.get(f"{API_URL}/health")
            Data = Response.json()
        except ConnectionError:
            Data = {
                "API": "OFF",
                "Account": "OFF",
                "Authenticator": "OFF",
                "Case": "OFF",
                "Entity": "OFF",
                "Forms": "OFF",
                "Notification": "OFF",
                "User": "OFF",
                "ZTime": datetime.now().strftime("%d/%m/%Y %H:%M:%S")            
            }
        return render_template("dashboard/health.html", Data=Data)
    return render_template("dashboard/dashboard.html")
@app.route("/dashboard/estadisticas")
def Dashboard_Estadisticas():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return render_template("dashboard/estadisticas.html")
    return render_template("dashboard/dashboard.html")
@app.route("/dashboard/cuenta")
def Dashboard_Cuenta():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return render_template("dashboard/no_auth.html")
        headers = {"Authorization": auth_header}

        Response = requests.get(f"{API_URL}/account/data", headers=headers)
        if Response.status_code == 401:
            return Response.json(), 401
        elif Response.status_code == 403:
            return render_template("dashboard/no_auth.html")        
        Datos = Response.json()
        return render_template("dashboard/cuenta.html", Usuario=Datos["usuario"], Dispositivos=Datos["dispositivos"], Datos=Datos["datos"])
    return render_template("dashboard/dashboard.html")

@app.route("/dashboard/forms")
def Dashboard_Forms():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return render_template("dashboard/forms.html")
    return render_template("dashboard/dashboard.html")
@app.route("/dashboard/forms/ayuda")
def Dashboard_Forms_Ayuda():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        Response = requests.get(f"{API_URL}/forms/ayuda/read/all")
        Data = Response.json()        
        return render_template("dashboard/forms_ayuda.html", Data=Data)
    return render_template("dashboard/dashboard.html")
@app.route("/dashboard/forms/calificanos")
def Dashboard_Forms_Calificanos():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        Response = requests.get(f"{API_URL}/forms/calificanos/read/all")
        Data = Response.json()        
        return render_template("dashboard/forms_calificanos.html", Data=Data)
    return render_template("dashboard/dashboard.html")
@app.route("/dashboard/forms/contactanos")
def Dashboard_Forms_Contactanos():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        Response = requests.get(f"{API_URL}/forms/contactanos/read/all")
        Data = Response.json()
        return render_template("dashboard/forms_contactanos.html", Data=Data)
    return render_template("dashboard/dashboard.html")


@app.route("/dashboard/help")
def Help():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return render_template("dashboard/ayuda.html")
    return render_template("dashboard/dashboard.html")
@app.route("/dashboard/unauthorized")
def Unauthorized():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return render_template("dashboard/no_auth.html")
    return render_template("dashboard/dashboard.html")
@app.route("/rate-limit")
def Rate_Limit():
    return render_template("homepage/rate_limit.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5009)