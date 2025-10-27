from flask import render_template, request, redirect, url_for, flash, session
from app.utilities.Autenticador import procesar_login, mostrar_dashboard, Validar_Datos, Enviar_Token, validar_token, Comparar_Contraseña_2, Validar_Contraseña2
from app.models.Persona import Persona

def get_registrar():
    if request.method == "POST":
        datos = {
            "Primer_Nombre": request.form["Primer_Nombre"],
            "Segundo_Nombre": request.form.get("Segundo_Nombre", ""),
            "Primer_Apellido": request.form["Primer_Apellido"],
            "Segundo_Apellido": request.form.get("Segundo_Apellido", ""),
            "Tipo_Documento": request.form["Tipo_Documento"],
            "Documento": request.form["Documento"],
            "Fecha_Nacimiento": request.form["Fecha_Nacimiento"],
            "Departamento": request.form['Departamento'],
            "Ciudad": request.form['Ciudad'],
            "Localidad": request.form.get('Localidad', ""),
            "Barrio": request.form.get('Barrio', ""),
            "Direccion": request.form['Direccion'],
            "Correo": request.form['Correo'],
            "Telefono": request.form['Telefono'],
            "Usuario": request.form['Usuario'],
            "Contraseña": request.form['Contraseña'],
            "Contraseña2": request.form['Contraseña2'],
            "Terminos": request.form["Terminos"]
        }
        
        Mensaje_Error = Validar_Datos(datos)
        if Mensaje_Error:
            return render_template("registrarse.html", errores=Mensaje_Error, datos=datos)
        p = Persona(Codigo=None, Tipo_Documento=datos["Tipo_Documento"], Documento=datos["Documento"],
                    Primer_Nombre=datos["Primer_Nombre"], Segundo_Nombre=datos["Segundo_Nombre"], Primer_Apellido=datos["Primer_Apellido"],
                    Segundo_Apellido=datos["Segundo_Apellido"], Fecha_Nacimiento=datos["Fecha_Nacimiento"], Codigo_Adic=None,
                    Edad=None, Direccion=datos["Direccion"], Departamento=datos["Departamento"], Ciudad=datos["Ciudad"],
                    Localidad=datos["Localidad"], Barrio=datos["Barrio"], Numero_Contacto=datos["Telefono"], Email=datos["Correo"],
                    Usuario=datos["Usuario"], Contraseña=datos["Contraseña"], Rol=None, Estado=None, Terminos=datos["Terminos"])
        resultado, tipo = p.Crear_Persona()
        flash(resultado) 
        return render_template("registrarse.html", confirmacion=resultado, tipo=tipo)    
    return render_template("registrarse.html")
def get_login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        contraseña = request.form["contraseña"]
        return procesar_login(usuario, contraseña)
    return render_template("login.html")
def get_logout():
    session.clear()
    return redirect(url_for("auth.login"))
def get_recuperar():
    if request.method == "POST":
        Nombre = request.form["usuario"]
        datos = Enviar_Token(Nombre) 

        if datos["Variable"] == "error":
            return render_template("Contraseña-Recuperar.html", confirmacion=datos["Mensaje"], tipo=datos["Variable"])

        session["Mensaje"] = datos["Mensaje"]
        session["Variable"] = datos["Variable"]
        session["Usuario"] = datos["Usuario"]
        session["Token_bot"] = datos["Token"]
        session["Correo"] = datos["Correo"]
        session["Hora"] = datos["Hora"]
        return render_template("recuperar-token.html", errores=datos["Mensaje"])
    return render_template("Contraseña-Recuperar.html")
def get_recuperar_token():
    if request.method == "POST":
        Token_Usu = request.form["token"]
        Contraseña = request.form["Contraseña"]
        Contraseña2 = request.form["Contraseña2"]
        Contraseña3 = Comparar_Contraseña_2(Contraseña, Contraseña2)
        Token_bot = session.get("Token_bot")
        Correo = session.get("Correo")
        Hora = session.get("Hora")
        Nombre = session.get("Usuario")
        datos = {
            "Token_Usu": request.form["token"],
            "Contraseña": request.form["Contraseña"],
            "Contraseña2": request.form["Contraseña2"]
        }

        if Contraseña3 == False:
            return render_template("recuperar-token.html", errores2={"Contraseña": "Las contraseñas no coinciden"}, tipo="error" , datos=datos)

        Mensaje_Error = Validar_Contraseña2(Contraseña)
        if Mensaje_Error:
            return render_template("recuperar-token.html", errores2=Mensaje_Error, datos=datos)

        resultado, tipo = validar_token(Token_bot, Correo, Hora, Token_Usu, Nombre, Contraseña3)
        return render_template("recuperar-token.html", confirmacion=resultado, tipo=tipo)
    return render_template("recuperar-token.html")
def get_dashboard():
    return mostrar_dashboard()