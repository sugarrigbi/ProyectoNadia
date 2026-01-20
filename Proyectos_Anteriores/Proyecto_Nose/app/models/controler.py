from flask import request, redirect, url_for, render_template,session
from urllib.parse import quote
from app.models.usuario import Usuario
from app.models.caso import Caso
import re
class Login:
    def __init__(self):
        pass

    def login(self):
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            
            
            user = Usuario.get_user_by_name(username)
            print(f"Usuario: {user.username if user else None}, Contraseña ingresada: {password}")
            
            # Validar existencia de usuario
            if not user:
                msg = quote("Nombre de usuario no encontrado. Inténtelo de nuevo.")
                return redirect(url_for("auth.login", status="error", msg=msg))

            # Validar contraseña
            if user.password != password:
                print(f"Contraseña incorrecta para {username}")
                msg = quote("Credenciales incorrectas. Inténtelo de nuevo.")
                return redirect(url_for("auth.login", status="error", msg=msg))
            
            # Validar estado del usuario
            if user.estado == "00":  # 01 activo, 00 Inactivo
                print(f"Usuario {username} inactivo")
                msg = quote("Usuario inactivo. Contacte al administrador.")
                return redirect(url_for("auth.login", status="warning", msg=msg))

            # Si pasa todas las validaciones
            session['username'] = user.username
            print(f"Login exitoso para {username}, rol: {user.rol}")

            if user.rol == 'Admin':
                msg = quote("Login exitoso para administrador")
                return redirect(url_for('admin.dashboard', status="success", msg=msg))

            else:
                msg = quote("Login exitoso para usuario")
                return redirect(url_for('user.dashboard', status="success", msg=msg))

        return render_template('login.html')


class Registro:
    def __init__(self):
        pass
    
    #Funcion para registro de usuario
    def registro(self):
        if request.method == 'POST':
            print("📌 Datos recibidos del formulario:", request.form.to_dict())

            username = request.form["username"]
            password = request.form["password"]
            id_persona = request.form["documento"]
            primer_nombre = request.form["primer_nombre"]
            segundo_nombre = request.form.get("segundo_nombre", "")
            primer_apellido = request.form["primer_apellido"]
            segundo_apellido = request.form.get("segundo_apellido", "")
            tipo_doc = request.form["tipo_documento"]
            fecha_nac = request.form["fecha_nacimiento"]
            edad = request.form["edad"]
            direccion = request.form["direccion"]
            num_contacto = request.form["telefono"]
            email = request.form["email"]

            # Validaciones para usuario existente
            if Usuario.username_exists(username):
                mensaje = quote("El nombre de usuario ya existe. Por favor, elige otro.⚠️")
                return redirect(url_for("auth.register", status="error", msg=mensaje))

            if Usuario.documento_exists(id_persona):
                mensaje = quote("El documento ya está registrado. Por favor, verifica los datos.⚠️")
                return redirect(url_for("auth.register", status="error", msg=mensaje))
            
            # Validacion de contraseña con condiciones
            patron_password = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&.,;:\-_])[A-Za-z\d@$!%*?&.,;:\-_]{8,}$'
            if not re.fullmatch(patron_password, password):
                mensaje = quote("La contraseña debe tener mínimo 8 caracteres, una mayúscula, un número y un caracter especial.⚠️")
                return redirect(url_for("auth.register", status="error", msg=mensaje))
            
            # Validaciones de tipo de dato y longitud en numero de telefono y documento
            if not id_persona.isdigit() or len(id_persona) != 10:
                mensaje = quote("El número de documento debe tener 10 dígitos.⚠️")
                return redirect(url_for("auth.register", status="error", msg=mensaje))
            
            if not num_contacto.isdigit() or len(num_contacto) != 10:
                mensaje = quote("El número de teléfono debe tener exactamente 10 dígitos.⚠️")
                return redirect(url_for("auth.register", status="error", msg=mensaje))
            
            
            # Validacion de tipo de documento seleccionado
            documento = ["CC", "TI", "CE", "PA"]
            if tipo_doc not in documento:
                mensaje = quote("Seleccione una opción correcta para el tipo de documento.⚠️")
                return redirect(url_for("auth.register", status="error", msg=mensaje))
            
            # Registro de usuario
            try:
                Usuario.insert_user_with_details(
                    username, password,
                    id_persona, primer_nombre, segundo_nombre,
                    primer_apellido, segundo_apellido, tipo_doc, fecha_nac,
                    edad, direccion, num_contacto, email
                )
                mensaje = quote("Usuario registrado correctamente ✅")
                return redirect(url_for("user.dashboard", status="success", msg=mensaje))

            except Exception as e:
                mensaje = quote(f"Error al registrar usuario, inténtelo nuevamente ❌")
                return redirect(url_for("auth.register", status="error", msg=mensaje))
            
        return render_template('register.html')


    # Funcion para registro de casos usuario
    def registrar_caso_usuario(self):
        if request.method == "POST":
            fecha = request.form ["fecha"]
            descripcion = request.form["descripcion"]
            direccion = request.form["direccion"]
            personas_afectadas = request.form["personas_afectadas"]
            fk_desastre= request.form["tipo_desastre"]
            fk_ciudad = request.form["ciudad"]
            radicado = None  


            try:
                id_caso = Caso.insert_case(fecha, descripcion, direccion, personas_afectadas, fk_desastre,fk_ciudad,radicado)
                mensaje = quote(f"Caso registrado correctamente ✅")
                return redirect(url_for("user.dashboard", status="success", msg=mensaje))


            except Exception as e:
                mensaje = quote(f"Error al registrar caso, inténtelo nuevamente ❌")
                return redirect(url_for("user.dashboard", status="error", msg=mensaje))
        
        return render_template('register_case.html')


class Consulta:
    def __init__(self):
        pass
    
    def buscar_caso_usuario(self):
        try:
            casos = Caso.get_cases_user()
            return casos
        except Exception as e:
            print(f"❌ Error consultando casos: {e}")
            return []
        

    
    
    

