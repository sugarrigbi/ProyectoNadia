from app.utilities.Base_Datos import Get_BaseDatos, Close_BaseDatos, Get_Errores
from werkzeug.security import generate_password_hash, check_password_hash
from flask import flash, redirect, url_for, session, render_template, request
from email.utils import formatdate, make_msgid, formataddr
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
from email.mime.text import MIMEText
import smtplib
import uuid
import re
correo_emisor = "bot@gaialink.online"
contraseña = "1145224601Aa*"
MAX_INTENTOS = 3
BLOQUEO_MINUTOS = 15
bloqueado_hasta = datetime.now() + timedelta(minutes=BLOQUEO_MINUTOS)

def Verificar_Rol(id_usuario):
    try:
        conexion, cursor = Get_BaseDatos()
        cursor.execute("SELECT fk_rol FROM tbl_usuario WHERE Id_usuario = %s", (id_usuario,))
        resultado = cursor.fetchone()
        if not resultado:
            return False 

        rol = resultado['fk_rol']
        roles_admin = ['admin'] 

        return rol.lower() in roles_admin

    except Exception as e:
        print(f"Error al verificar rol admin: {e}")
        return False

    finally:
        Close_BaseDatos(conexion, cursor)
def verificar_estado_usuario(nombre_usuario):
    conexion, cursor = Get_BaseDatos()
    try:
        cursor.execute("SELECT Id_usuario, Intentos_fallidos, Bloqueado FROM tbl_usuario WHERE Nombre = %s",(nombre_usuario,))
        datos = cursor.fetchone()
        if not datos:
            return {"bloqueado": False, "intentos_restantes": MAX_INTENTOS, "mensaje": "Usuario no encontrado", "user_id": None}

        intentos = int(datos.get("Intentos_fallidos") or 0)
        bloqueado = datos.get("Bloqueado")

        if bloqueado and isinstance(bloqueado, str):
            try:
                bloqueado = datetime.fromisoformat(bloqueado)
            except:
                bloqueado = None

        if bloqueado and bloqueado > datetime.now():
            tiempo_restante = (bloqueado - datetime.now()).seconds // 60
            return {
                "bloqueado": True,
                "bloqueado_hasta": bloqueado,
                "intentos_restantes": 0,
                "mensaje": f"Usuario bloqueado hasta {bloqueado.strftime('%H:%M:%S')} ({tiempo_restante} min restantes)",
                "user_id": datos["Id_usuario"]
            }

        return {
            "bloqueado": False,
            "bloqueado_hasta": bloqueado,
            "intentos_restantes": MAX_INTENTOS - intentos,
            "mensaje": f"Intentos restantes: {MAX_INTENTOS - intentos}",
            "user_id": datos["Id_usuario"]
        }
    finally:
        Close_BaseDatos(conexion, cursor)
def hash_contraseña(contraseña):
    return generate_password_hash(contraseña)
def hash_verificar(hash, contraseña):
    return check_password_hash(hash, contraseña)
def procesar_login(usuario, contraseña):
    conexion, cursor = Get_BaseDatos()

    cursor.execute("SELECT Id_usuario, Contraseña, Intentos_fallidos, Bloqueado, fk_estado FROM tbl_usuario WHERE Nombre = %s",(usuario,))
    datos = cursor.fetchone()

    if not datos:
        flash("Usuario no encontrado")
        Close_BaseDatos(conexion, cursor)
        return render_template("login.html", usuario_invalido=True)

    bloqueado_hasta = datos.get("Bloqueado")
    if bloqueado_hasta and datetime.now() < bloqueado_hasta:
        desbloqueo_timestamp = int(bloqueado_hasta.timestamp())
        Close_BaseDatos(conexion, cursor)
        return render_template("login.html", estado_bloqueado=True, desbloqueo_timestamp=desbloqueo_timestamp)
    elif bloqueado_hasta and datetime.now() >= bloqueado_hasta:
        cursor.execute("UPDATE tbl_usuario SET Bloqueado = NULL, Intentos_fallidos = 0 WHERE Id_usuario = %s",(datos["Id_usuario"],))
        conexion.commit()

    if datos["fk_estado"] != "usuario_01":
        Close_BaseDatos(conexion, cursor)
        return render_template("login.html", usuario_invalido=True)

    if not check_password_hash(datos["Contraseña"], contraseña):
        intentos = int(datos.get("Intentos_fallidos") or 0) + 1

        if intentos >= MAX_INTENTOS:
            bloqueado_hasta = datetime.now() + timedelta(minutes=BLOQUEO_MINUTOS)
            cursor.execute(
                "UPDATE tbl_usuario SET Intentos_fallidos = %s, Bloqueado = %s WHERE Id_usuario = %s",
                (intentos, bloqueado_hasta, datos["Id_usuario"])
            )
            conexion.commit()
            Close_BaseDatos(conexion, cursor)

            desbloqueo_timestamp = int(bloqueado_hasta.timestamp())
            return render_template("login.html", estado_bloqueado=True, desbloqueo_timestamp=desbloqueo_timestamp)
        else:
            cursor.execute(
                "UPDATE tbl_usuario SET Intentos_fallidos = %s WHERE Id_usuario = %s",
                (intentos, datos["Id_usuario"])
            )
            conexion.commit()
            Close_BaseDatos(conexion, cursor)
            intentos_restantes = MAX_INTENTOS - intentos
            return render_template("login.html", intentos_restantes=intentos_restantes, contraseña_invalida=True)

    cursor.execute(
        "UPDATE tbl_usuario SET Intentos_fallidos = 0, Bloqueado = NULL WHERE Id_usuario = %s",
        (datos["Id_usuario"],)
    )
    conexion.commit()
    Close_BaseDatos(conexion, cursor)

    session["usuario_id"] = datos["Id_usuario"]
    session["username"] = usuario
    session["rol"] = "admin" if Verificar_Rol(datos["Id_usuario"]) else "usuario"

    if session["rol"] == "admin":
        return redirect(url_for("auth.dashboard"))
    return redirect(url_for("auth.dashboard"))
def mostrar_dashboard():
    usuario_id = session.get("usuario_id")
    rol = (session.get("rol") or "").lower()
    username = session.get("username")

    if not usuario_id:
        return redirect(url_for("auth.login"))

    frame_activo = request.args.get("frame", "Frame1")

    if rol == "admin":
        return render_template("dashboard_admin.html", username=username)
    elif rol == "usuario":
        if request.path != "/dashboard/user":
            return redirect(url_for("dashboard.user", frame=frame_activo))
        return render_template("dashboard_usuario.html", username=username, frame_activo=frame_activo)
    else:
        flash("Rol no permitido")
        return redirect(url_for("auth.login"))
def Validar_Contraseña(Contraseña):
    if len(Contraseña) < 8:
        return "La contraseña debe tener mas de 8 caracteres"
    if not any(c.isupper() for c in Contraseña):
        return "La contraseña debe tener una mayuscula"
    if not any(c.isdigit() for c in Contraseña):
        return "la contraseña debe tener un numero"
    if not re.search(r'[/!@#$%^&*(),.?":{}|<>]', Contraseña):
        return "La contraseña debe tener un caracter especial"
    return None
def Comparar_Contraseña(Contraseña, Contraseña2):
    if Contraseña == Contraseña2:
        return None
    else:
        return "Las contraseñas no coinciden"
def Comparar_Contraseña_2(Contraseña, Contraseña2):
    if Contraseña == Contraseña2:
        return Contraseña
    else:
        return "Las contraseñas no coinciden"
def Validar_Telefono(Telefono):
    if len(Telefono) != 10:
        return "El Telefono debe tener entre 6 y 10 digitos"
    else:
        return None
def Validar_Documento(Documento):
    if len(Documento) < 6 or len(Documento) > 10:
        return "El documento debe tener entre 6 y 10 digitos"
    else:
        return None
def Verificar_Documento(Documento):
    try:
        conexion, cursor = Get_BaseDatos()
        cursor.execute("SELECT * FROM tbl_persona WHERE Id_Persona = %s", (Documento,))
        if cursor.fetchone():
            return "El documento ya está en uso."
    except Exception as e:
        print(f"Error al verificar el documento: {e}")
        return False
def Verificar_Correo(Correo):
    try:
        conexion, cursor = Get_BaseDatos()
        cursor.execute("SELECT Email FROM tbl_adic_persona WHERE Email = %s", (Correo,))
        if cursor.fetchone():
            return "El correo ya está en uso."
    except Exception as e:
        print(f"Error al verificar el correo: {e}")
        return False
def Verificar_Usuario(Usuario):
    try:
        conexion, cursor = Get_BaseDatos()
        cursor.execute("SELECT Nombre FROM tbl_usuario WHERE Nombre = %s", (Usuario,))
        if cursor.fetchone():
            return "El usuario ya está en uso."
    except Exception as e:
        print(f"Error al verificar el usuario: {e}")
        return False

    except Exception as e:
        print(f"Error al verificar el bloqueo: {e}")
        return "Error al verificar el estado del usuario."
def Validar_Datos(Datos):
    errores = {}

    resultado = Datos["Fecha_Nacimiento"]
    fecha_nac_obj = datetime.strptime(resultado, "%Y-%m-%d").date()
    hoy = datetime.today().date()
    edad = hoy.year - fecha_nac_obj.year
    if (hoy.month, hoy.day) < (fecha_nac_obj.month, fecha_nac_obj.day):
        edad -= 1

    if edad < 13:
        errores["Fecha_Nacimiento"] = "Debes tener al menos 13 años para registrarte."

    resultado = Validar_Contraseña(Datos["Contraseña"])
    if resultado:
        errores["Contraseña"] = resultado    

    resultado = Comparar_Contraseña(Datos["Contraseña"], Datos["Contraseña2"])
    if resultado:
        errores["Contraseña2"] = resultado   

    resultado = Validar_Telefono(Datos["Telefono"])
    if resultado:
        errores["Telefono"] = resultado    
    
    resultado = Validar_Documento(Datos["Documento"])
    if resultado:
        errores["Documento"] = resultado    

    resultado = Verificar_Documento(Datos["Documento"])
    if resultado:
        errores["Documento"] = resultado   

    resultado = Verificar_Correo(Datos["Correo"])
    if resultado:
        errores["Correo"] = resultado   

    resultado = Verificar_Usuario(Datos["Usuario"])
    if resultado:
        errores["Usuario"] = resultado    

    for campo in ["Primer_Nombre", "Segundo_Nombre", "Primer_Apellido", "Segundo_Apellido", "Departamento", "Ciudad", "Localidad", "Barrio"]:
        valor = Datos[campo].replace(" ", "")
        if valor and not valor.isalpha():
            errores[campo] = f"El campo '{campo.replace('_', ' ').capitalize()}' solo puede contener letras"

    for campo in ["Documento", "Telefono"]:
        valor = Datos[campo].replace(" ", "")
        if valor and not valor.isdigit():
            errores[campo] = f"El campo '{campo}' solo puede contener numeros"

    valor = Datos["Correo"]
    if not re.match(r"[^@]+@[^@]+\.[^@]+", valor):
        errores["Correo"] ="ingrese un correo valido"

    return errores 
def Enviar_Token(Nombre):              
    conexion, cursor = Get_BaseDatos()

    Usuario = Nombre
    cursor.execute("SELECT COUNT(*) AS total FROM tbl_usuario WHERE Nombre = %s", (Usuario,))
    resultado = cursor.fetchone()
    if resultado["total"] == 0:
        return {
            "Mensaje": "El nombre ingresado no está registrado como usuario.",
            "Variable": "error",
            "Usuario": None,
            "Token": None,
            "Correo": None,
            "Hora": None
        }

    cursor.execute("SELECT tbl_adic_persona.Email FROM tbl_usuario  JOIN tbl_persona ON tbl_persona.fk_usuario = tbl_usuario.Id_usuario JOIN tbl_adic_persona ON tbl_adic_persona.fk_persona = tbl_persona.Id_Persona WHERE tbl_usuario.Nombre = %s", (Usuario,))
    resultado_correo = cursor.fetchone()
    if not resultado_correo:
        return {
            "Mensaje": "El correo ingresado no está registrado como usuario.",
            "Variable": "error",
            "Usuario": Usuario,
            "Token": None,
            "Correo": None,
            "Hora": None
        }  
    correo = resultado_correo["Email"]

    Close_BaseDatos(conexion, cursor) 

    token_recuperacion = str(uuid.uuid4())[:8] 
    correo_token = correo
    hora = datetime.now()
    hora_token = hora.strftime("%Y-%m-%d %H:%M:%S")

    mensaje = MIMEMultipart()
    mensaje["From"] =   formataddr(("Soporte GaiaLink", correo_emisor))
    mensaje["To"] = correo_token
    mensaje["Subject"] = f"Estimado/a {Usuario}"
    mensaje['Date'] = formatdate(localtime=True)
    mensaje['Message-ID'] = make_msgid(domain="gaialink.online")
    cuerpo = f"Tu código para recuperar la contraseña es: {token_recuperacion}\nEste código es válido por 10 minutos\nRecuerda no compartirlo con nadie\nAtentamente,El equipo de Gaialink"
    mensaje.attach(MIMEText(cuerpo, "plain"))    
    try:
        servidor = smtplib.SMTP_SSL("gaialink.online", 465)
        servidor.login(correo_emisor, contraseña)
        servidor.send_message(mensaje)
        servidor.quit()
        print('Correo del usuario:', correo_emisor)
        print("Correo enviado exitosamente")
        return {
            "Mensaje": "Se envió un codigo al correo.",
            "Variable": "exito",
            "Usuario": Usuario,
            "Token": token_recuperacion, 
            "Correo": correo_token, 
            "Hora": hora_token
        }
    except Exception as e:
        return {
            "Mensaje": f"Error al enviar el correo: {e}",
            "Variable": "error",
            "Usuario": Usuario,
            "Token": token_recuperacion, 
            "Correo": correo_token, 
            "Hora": hora_token
        }
def validar_token(token_recuperacion, correo_token, hora_token, token_usuario, Nombre, Contraseña3):
    conexion, cursor = Get_BaseDatos()

    try:
        print("hora_token:", hora_token)
        hora_token = datetime.strptime(hora_token, "%Y-%m-%d %H:%M:%S")
    except Exception:
        return "Formato de hora inválido.", "error"

    if not token_recuperacion or not correo_token or not hora_token:
        return "Primero solicita el código de recuperación.", "error"
    if token_recuperacion != token_usuario:
        return "Codigo de recuperacion incorrecto", "error"
    if datetime.now() > hora_token + timedelta(minutes=10):
        return "El codigo de recuperacion ya expiro", "error"
    
    cursor.execute("SELECT id_usuario FROM tbl_usuario WHERE Nombre = %s", (Nombre,))
    resultado_usuario = cursor.fetchone()
    if not resultado_usuario:
        return "No se encontró el usuario.", "error"
    id_usuario = resultado_usuario["id_usuario"]
    cursor.execute("UPDATE tbl_usuario SET Contraseña = %s WHERE Id_usuario = %s", (Contraseña3, id_usuario))
    conexion.commit()
    Close_BaseDatos(conexion, cursor)
    return "Contraseña recuperada con exito", "exito"
def Obtener_Contraseña(usuario):
    conexion, cursor = Get_BaseDatos()
    try:
        cursor.execute("SELECT Contraseña FROM tbl_usuario WHERE Id_usuario = %s", (usuario,))
        resultado = cursor.fetchone()
        if not resultado:
            return None
        return resultado["Contraseña"]
    except Exception as e:
        print(f"Error al obtener la contraseña del usuario {usuario}: {e}")
        return None
    finally:
        Close_BaseDatos(conexion, cursor)
def Obtener_DocumentoCodigo(codigo):
    conexion, cursor = Get_BaseDatos()

    try:
        cursor.execute("SELECT Id_Persona FROM prueba.tbl_persona WHERE fk_Usuario = %s", (codigo,))
        documento = cursor.fetchone()
        if not documento:
            return "Error en el documento"
        return documento["Id_Persona"]
    except Exception as e:
        print(f"Error al obtener el documento: {e}")
        return None
    finally:
        Close_BaseDatos(conexion, cursor)