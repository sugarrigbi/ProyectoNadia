from flask import render_template, request, redirect, url_for, flash, session, jsonify
from app.utilities.Autenticador import procesar_login, mostrar_dashboard, Validar_Datos, Enviar_Token, validar_token, Comparar_Contraseña_2, Validar_Contraseña2
from app.models.Persona import Persona
from app.utilities.Base_Datos import Get_BaseDatos, Close_BaseDatos
import pyotp, qrcode
from io import BytesIO
import base64
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
    if "usuario_id" in session:
        rol = (session.get("rol") or "").lower()
        if rol == "admin":
            return redirect(url_for("auth.admin"))
        else:
            return redirect(url_for("auth.user"))
    if request.method == "POST":
        usuario = request.form["usuario"]
        contraseña = request.form["contraseña"]
        datos2 = {
            "usuario": usuario,
            "contraseña": contraseña
        }
        respuesta = procesar_login(usuario, contraseña, datos2)
        if "usuario_id" in session:
            session.permanent = True
        return respuesta
    return render_template("login.html", datos2={})
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
def get_autenticador():
    if session.get("2fa_ok"):
        rol = (session.get("rol") or "").lower()
        if rol == "admin":
            return redirect(url_for("auth.admin"))
        return redirect(url_for("auth.user"))    
    if request.method == "GET":
        return render_template("autenticador.html")    
    if request.method == "POST":
        codigo = request.form["2fa"]
        usuario = session.get("usuario_id")

        conexion, cursor = Get_BaseDatos()
        cursor.execute("SELECT Secret_Key FROM tbl_usuario WHERE Id_usuario = %s", (usuario,))
        secreto = cursor.fetchone()
        Close_BaseDatos(conexion, cursor)

        totp = pyotp.TOTP(secreto["Secret_Key"])
        if totp.verify(codigo):
            session["2fa_ok"] = True
            rol = (session.get("rol") or "").lower()
            if rol == "admin":
                return redirect(url_for("auth.admin"))
            return redirect(url_for("auth.user"))
        else:
            return render_template("autenticador.html", mensaje="Codigo de autenticacion invalido", tipo="error")            
def get_dashboard():
    return mostrar_dashboard()
def get_QR():
    try:
        usuario_id = session["usuario_id"]
        conexion, cursor = Get_BaseDatos()
        cursor.execute("SELECT `2FA`, Secret_Key, Nombre FROM tbl_usuario WHERE Id_usuario = %s", (usuario_id,))
        usuario = cursor.fetchone()
        Close_BaseDatos(conexion, cursor)

        if not usuario:
            return jsonify({"error": "Usuario no encontrado"}), 404

        if not usuario["Secret_Key"]:
            return jsonify({"error": "El usuario no tiene 2FA activado"}), 400

        secret = usuario["Secret_Key"]
        totp = pyotp.TOTP(secret)
        uri = totp.provisioning_uri(name=usuario["Nombre"], issuer_name="GaiaLink")

        # Generar la imagen QR en base64
        img = qrcode.make(uri)
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        qr_b64 = base64.b64encode(buffer.getvalue()).decode("ascii")

        return jsonify({
            "qr": f"data:image/png;base64,{qr_b64}",
            "secret": secret
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500