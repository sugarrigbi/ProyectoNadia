from flask import request, redirect, url_for, render_template,session,jsonify, send_file
from flask_mail import Message
from app.models.utils import enviar_correo_registro, enviar_correo_caso, enviar_correo_actualización_datos
from urllib.parse import quote
from app.models.usuario import Usuario
from app.models.caso import Caso
from app.models.utils import validar_fecha
import re, os
import time
from datetime import datetime
import pandas as pd

class Login:
    def __init__(self):
        pass
    
    #Funcion para login de usuario 
    def login(self):
        # Manejo de datos del formulario
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            
            
            user = Usuario.get_user_by_name(username)
            print(f"Usuario: {user.username if user else None}, Contraseña ingresada: {password}")
            
            # Validar existencia de usuario en la base de datos
            if not user:
                msg = quote("Nombre de usuario no encontrado. Inténtelo de nuevo.❌")
                return redirect(url_for("auth.login", status="error", msg=msg))

            # Validar contraseña del usuario
            if user.password != password:
                print(f"Contraseña incorrecta para {username}")
                msg = quote("Credenciales incorrectas. Inténtelo de nuevo.❌")
                return redirect(url_for("auth.login", status="error", msg=msg))
            
            # Validar estado del usuario
            if user.estado == "00":  # 01 activo, 00 Inactivo
                print(f"Usuario {username} inactivo")
                msg = quote("Usuario inactivo. Contacte al administrador.⚠")
                return redirect(url_for("auth.login", status="warning", msg=msg))

            # GUardar datos en sesión
            session['username'] = user.username
            
            # Obtener el rol del usuario 
            if user.rol == 'Admin':
                msg = quote("Login exitoso para administrador ✅") # Redirigir a dashboard admin
                return redirect(url_for('admin.dashboard', status="success", msg=msg))

            else:
                msg = quote("Login exitoso para usuario ✅") # Redirigir a dashboard usuario
                return redirect(url_for('user.dashboard', status="success", msg=msg))
        
        # Mostrar la plantilla de login en caso de no pasar las validaciones
        return render_template('login.html')
    
    #Funcion para logout de usuario
    def logout(self):
        # Limpiar los datos guardados en la sesión
        session.pop('user_id', None)
        session.pop('username', None)
        session.pop('rol', None)
        msg = quote("Sesión cerrada exitosamente ✅") 
        return redirect(url_for('auth.login', status="success", msg=msg)) # Redirigir a la página de login

class Registro:
    def __init__(self):
        pass
    
    #Funcion para registro de usuario
    def registro(self):
        if request.method == 'POST':
            print("Datos recibidos del formulario:", request.form.to_dict())
            
            # Obtener datos del formulario
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
            
            #VALIDACIONES ANTES DE REGISTRAR
            
            # Validacion de todos los campos obligatorios
            campos_obligatorios = [username, password, id_persona, primer_nombre, primer_apellido, tipo_doc, fecha_nac, edad, direccion, num_contacto, email]
            if not all(campos_obligatorios):
                mensaje = quote("Por favor, complete todos los campos obligatorios. ⚠")
                return redirect(url_for("auth.register", status="warning", msg=mensaje))
            
            
            # Validacion para usuario existente
            if Usuario.username_exists(username):
                mensaje = quote("El nombre de usuario ya existe. Por favor, elige otro.⚠")
                return redirect(url_for("auth.register", status="warning", msg=mensaje))
            
            if len(username) < 4 or len(username) > 10:
                mensaje = quote("El nombre de usuario debe tener entre 4 y 10 caracteres.⚠")
                return redirect(url_for("auth.register", status="warning", msg=mensaje))
            
            # Validacion de nombres con letras y espacios
            patron_nombres = r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$'
            if not re.fullmatch(patron_nombres, primer_nombre):
                mensaje = quote("Los nombres solo deben contener letras y espacios.⚠")
                return redirect(url_for("auth.register", status="warning", msg=mensaje))
            
            if segundo_nombre and not re.fullmatch(patron_nombres, segundo_nombre):
                mensaje = quote("Los nombres solo deben contener letras y espacios.⚠")
                return redirect(url_for("auth.register", status="warning", msg=mensaje))
            
            # Validacion de apellidos con letras y espacios
            if not re.fullmatch(patron_nombres, primer_apellido):
                mensaje = quote("Los apellidos solo deben contener letras y espacios.⚠")
                return redirect(url_for("auth.register", status="error", msg=mensaje))
            if segundo_apellido and not re.fullmatch(patron_nombres, segundo_apellido):
                mensaje = quote("Los apellidos solo deben contener letras y espacios.⚠")
                return redirect(url_for("auth.register", status="warning", msg=mensaje))
            
            # Validacion de usuario existente por documento
            if Usuario.documento_exists(id_persona):
                mensaje = quote("El documento ya está registrado. Por favor, verifica los datos.⚠")
                return redirect(url_for("auth.register", status="warning", msg=mensaje))
            
            # Validacion de usuario existente por email
            if Usuario.email_exist(id_persona):
                mensaje = quote("El correo ya está registrado. Por favor, elige otro.⚠")
                return redirect(url_for("auth.register", status="warning", msg=mensaje))
            
            # Validacion de contraseña con condiciones
            patron_password = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&.,;:\-_])[A-Za-z\d@$!%*?&.,;:\-_]{8,}$'
            if not re.fullmatch(patron_password, password):
                mensaje = quote("La contraseña debe tener mínimo 8 caracteres, una mayúscula, un número y un caracter especial.⚠")
                return redirect(url_for("auth.register", status="warning", msg=mensaje))
            
            # Validacion en numero de telefono y documento
            if not id_persona.isdigit() or len(id_persona) < 6:
                mensaje = quote("El número de documento debe tener mínimo 6 dígitos.⚠")
                return redirect(url_for("auth.register", status="warning", msg=mensaje))
            
            if not num_contacto.isdigit() or len(num_contacto) != 10:
                mensaje = quote("El número de teléfono debe tener exactamente 10 dígitos.⚠")
                return redirect(url_for("auth.register", status="warning", msg=mensaje))
            
            # Validacion de edad
            try:
                edad = int(edad)
            except ValueError:
                mensaje = quote("La edad ingresada no es válida.⚠")
                return redirect(url_for("auth.register", status="warning", msg=mensaje))
            if edad < 18 or edad > 90:
                mensaje = quote("La edad debe estar entre 18 y 90 años.⚠")
                return redirect(url_for("auth.register", status="warning", msg=mensaje))
            
            # Validacion de tipo de documento seleccionado
            documento = ["CC", "TI", "CE", "PA"]
            if tipo_doc not in documento:
                mensaje = quote("Seleccione una opción correcta para el tipo de documento.⚠")
                return redirect(url_for("auth.register", status="warning", msg=mensaje))
            
            
            # REGISTRO DE USUARIO DESPUES DE VALIDACIONES
            try:
                Usuario.insert_user_with_details(
                    username, password,
                    id_persona, primer_nombre, segundo_nombre,
                    primer_apellido, segundo_apellido, tipo_doc, fecha_nac,
                    edad, direccion, num_contacto, email
                )
                
                enviar_correo_registro(primer_nombre, primer_apellido,email,username)
                
                session['username'] = username
                
                mensaje = quote("Usuario registrado correctamente ✅") # Redirigir a dashboard usuario
                return redirect(url_for("user.dashboard", status="success", msg=mensaje))

            except Exception as e:
                print("Error al ingresar el usuario", e)
                mensaje = quote(f"Error al registrar usuario, inténtelo nuevamente ❌") # Redirigir a registro
                return redirect(url_for("auth.register", status="error", msg=mensaje))
            
        return render_template('register.html')

    # Funcion para registro de casos usuario
    def registrar_caso_usuario(self):
        # Manejo de datos del formulario
        if request.method == "POST":
            fecha = request.form ["fecha"]
            descripcion = request.form["descripcion"]
            direccion = request.form["direccion"]
            personas_afectadas = request.form["personas_afectadas"]
            fk_desastre= request.form["tipo_desastre"]
            fk_ciudad = request.form["ciudad"]
            radicado = None  
            
            #  Detectar si es admin o usuario
            if "fk_usuario" in request.form:  # caso del admin
                fk_usuario = request.form["fk_usuario"]
            else:  # caso del usuario autenticado
                fk_usuario = Usuario.get_user_by_session()
            
            # VALIDACIONES ANTES DE REGISTRAR
            # Validacion de todos los campos obligatorios
            campos_obligatorios = [fecha, descripcion, direccion, personas_afectadas, fk_desastre, fk_ciudad]
            if not all(campos_obligatorios):
                return jsonify({"status":"warning", "msg": "Por favor, complete todos los campos obligatorios.⚠"}), 400
            # Validacion de personas afectadas
            if not personas_afectadas.isdigit() or int(personas_afectadas) < 1 or int(personas_afectadas) > 25:
                return jsonify({"status":"warning", "msg": "El número de personas afectadas deben ser del núcleo familiar,no superior a 25 personas.⚠"}), 400
            
            resultado_validacion_fecha = validar_fecha(fecha)
            if resultado_validacion_fecha is not None:
                return jsonify({"status":"warning", "msg": "La fecha no puede ser posterior a la actual. ⚠"}),400
    
            # REGISTRO DE CASO DESPUES DE VALIDACIONES
            try:
                id_caso = Caso.insert_case(fecha, descripcion, direccion, personas_afectadas,fk_usuario, fk_desastre,fk_ciudad,radicado)
                
                usuario = Usuario.get_user_account(fk_usuario)
                caso= Caso.get_case_by_id(id_caso)
                
                if not usuario:
                    raise Exception("No se encontró información del usuario")
                
                if not caso or len(caso) == 0:
                    raise Exception("No se encontró el caso recién registrado.")
                
                email = usuario["email"]
                nombre = usuario["nombres"]
                apellido = usuario["apellidos"]
                desastre = caso["desastre"]
                
                enviar_correo_caso(fecha,descripcion,personas_afectadas,email,nombre,apellido,desastre)
                
                return jsonify({"status":"success", "msg": "Caso registrado correctamente ✅"}), 200
            
            except Exception as e:
                print("Error al ingresar el caso", e)
                return jsonify({"status":"error", "msg": "Error al registrar caso, inténtelo nuevamente ❌"}), 500

class Consulta:
    def __init__(self):
        pass
    # Funcion para consultar casos de usuario
    def buscar_caso_usuario(self):
        try:
            # Obtener el id del usuario desde la sesión para buscar sus casos
            fk_usuario = Usuario.get_user_by_session()
            if not fk_usuario:
                raise ValueError("No hay usuario en sesión o no existe en la base de datos.")
            
            # Obtener los casos asociados al usuario
            casos = Caso.get_cases_user(fk_usuario)
            if not casos:
                raise ValueError("No se encontraron casos para este usuario.")
            return casos
        
        #manejo de errores
        except:
            print("Error al consultar casos")
            
    def buscar_casos_admin(self):
        try:
            # Obtener los casos asociados al usuario
            casos = Caso.get_cases_admin()
            if not casos:
                raise ValueError("No se encontraron casos registrados.")
            return casos
        
        #manejo de errores
        except:
            print("Error al consultar casos")
    # Funcion para ver datos de usuario           
    def ver_datos_usuario(self):
        try:
            #  Obtener el nombre de usuario desde la sesión
            username = session.get("username")
            if not username:
                raise ValueError("No hay usuario en sesión.")

            # Obtener el id del usuario desde la sesión
            fk_usuario = Usuario.get_user_by_session()
            if not fk_usuario:
                raise ValueError("El usuario no existe en la base de datos.")

            # Obtener los datos del usuario desde la base de datos
            usuario = Usuario.get_user_account(fk_usuario)
            
            # Enmascarar la contraseña para mostrarla parcialmente al usuario
            raw_password = usuario["contrasena"] or ""
            visible_part = raw_password[-2:] 
            masked ="••" * (len(raw_password) - 2) + visible_part 
            usuario["contrasena_masked"] = masked
            
            # Validar que se hayan obtenido datos del usuario
            if not usuario:
                raise ValueError("No se encontraron datos para este usuario.") 
            print("Datos del usuario obtenidos:", usuario)
            return jsonify(usuario) # Devolver los datos del usuario en formato JSON
        
        except Exception as e:
            print("Error al obtener datos del usuario: {e}")
            return jsonify({"error": f"Error al obtener datos del usuario: {str(e)}"}), 500
    
    def obtener_usuarios(self):
        usuarios = Usuario.get_all_users()
        usuarios_json = [{"id": u[0], "nombre": u[1]} for u in usuarios]
        print("Resultado de usuarios:", usuarios)
        return jsonify(usuarios_json)

    def generar_reporte(self):
        initial_date = request.form ["FechaInicial"]
        final_date = request.form["FechaFinal"]
        
        print("Fechas recibidas:", initial_date, final_date) 
        
        if not initial_date or not final_date:
            return jsonify({"status":"warning", "msg": "Faltan datos en el formulario. ⚠"}), 400
        if initial_date > final_date:
            return jsonify({"status":"warning", "msg": "La fecha inicial no puede ser mayor a la fecha final. ⚠"}), 400
        
        try:
            reporte = Caso.generate_report(initial_date, final_date)
            
            
            output_directory = os.path.join('reportes')
            os.makedirs(output_directory, exist_ok=True)
            fecha_actual = datetime.now().strftime("%Y%m%d_%H%M%S")
            generated_excel = os.path.join(output_directory, f"Reporte_Casos_{fecha_actual}.xlsx")
            
            if not reporte:
                df = pd.DataFrame([{"Mensaje": "No se encontraron datos para las fechas seleccionadas."}])
            else:
                df = pd.json_normalize(reporte)
                
            df.to_excel(generated_excel, index=False)

            time.sleep(1)
            return send_file(
            generated_excel,
            as_attachment=True,
            download_name=f"Reporte_Casos_{fecha_actual}.xlsx",
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        except Exception as e:
            print(f"Error al generar el reporte:{e}")
            return jsonify({"status": "error", "msg": "Error al generar el reporte ❌"}), 500
    
class Actualizar:
    def __init__(self):
        pass
    
    # Funcion para actualizar datos de usuario
    def actualizar_datos_usuario(self):    
        try:
            # Obtener el id del usuario desde la sesión
            fk_usuario = Usuario.get_user_by_session()
            if not fk_usuario:
                raise ValueError("Usuario no encontrado en sesión.")

            # Obtener los datos del formulario
            pri_nom = (request.form.get("pri_nom") or "").strip()
            seg_nom = (request.form.get("seg_nom") or "").strip()
            pri_ape = (request.form.get("pri_ape") or "").strip()
            seg_ape = (request.form.get("seg_ape") or "").strip()
            direccion = (request.form.get("direccion_user") or "").strip()
            email = (request.form.get("email") or "").strip()
            telefono = (request.form.get("telefono") or "").strip()
            edad = (request.form.get("edad") or "").strip()
            username = (request.form.get("username") or "").strip()
            
            # VALIDACIONES DE DATOS ANTES DE ACTUALIZAR
            # Validar que haya al menos un campo para actualizar
            if not any([pri_nom, seg_nom,pri_ape,seg_ape, direccion, email,telefono, edad, username]):
                return jsonify({"status":"warning", "msg": "Debe proporcionar al menos un campo para actualizar. ⚠"}), 400
            
            #validar si el nombre de usuario ya existe
            if username:
                if Usuario.username_exists(username):
                    return jsonify({"status":"error", "msg": "El nombre de usuario ya existe. Por favor, elige otro. ❌ "}), 400
                # Validar la longitud del nombre de usuario
                if len(username) < 4 or len(username) > 10:
                    return jsonify({"status":"warning", "msg": "El nombre de usuario debe tener entre 4 y 10 caracteres. ⚠"}), 400
            
            # Validacion de edad si fue proporcionada
            if edad:
                try:
                    edad = int(edad)
                    if edad < 18 or edad > 90:
                       return jsonify({"status":"warning", "msg": "La edad debe estar entre 18 y 90 años.  ⚠"}), 400
                except ValueError:
                    return jsonify({"status":"warning", "msg": "La edad debe ser un número válido.  ⚠"}), 400
            
            # Validacion de telefono si fue proporcionado
            if telefono:
                if not telefono.isdigit() or len(telefono) < 7 or len(telefono) > 13:
                    return jsonify({"status":"warning", "msg": "El número de teléfono debe ser válido y tener todos los dígitos. ⚠"}), 400
                telefono = telefono           
            
            # Actualizar los datos del usuario en la base de datos
            actualizar= Usuario.update_user_account(fk_usuario, pri_nom, seg_nom, pri_ape, seg_ape, direccion, email, telefono, edad, username)
                        
            # Manejo de errores en la actualización
            if not actualizar:
                raise ValueError("No se pudo actualizar los datos del usuario.")
            print("Datos del usuario actualizados:", actualizar)
            
            #Actualizar nombre de usuario en sesión si fue modificado
            if username:
                session['username'] = username
                print("Nombre de usuario en sesión actualizado a:", username)
                
            usuario = Usuario.get_user_account(fk_usuario)
            
            if not usuario:
                raise Exception("No se encontró información del usuario")
            
            nombre = usuario["nombres"]
            apellido = usuario["apellidos"]
            email = usuario["email"]
            direccion = usuario["direccion"]
            telefono = usuario["telefono"]
            edad = usuario["edad"] 
            username = usuario["nombre_usuario"]
            
            enviar_correo_actualización_datos(nombre, apellido, direccion, email,telefono, edad, username)
            
            # Mensaje de éxito
            return jsonify({"status":"success", "msg": "Datos actualizados correctamente ✅"}), 200
        
        except Exception as e:
            print("Error al actualizar los datos del usuario: {e}") # Manejo de errores 
            return jsonify({"status":"error", "msg": "Error al actualizar los datos. Inténtelo nuevamente ❌"}), 500
    
    # Funcion para cambiar contraseña de usuario
    def cambiar_contrasena_usuario(self):
        try:
            # Obtener el id del usuario desde la sesión
            fk_usuario = Usuario.get_user_by_session()
            if not fk_usuario:
                raise ValueError("Usuario no encontrado en sesión.")
            print("Usuario ID en sesión:", fk_usuario)
            
            # Obtener la contraseña del usuario almacenada en la base de datos
            stored_password = Usuario.get_user_password(fk_usuario)
            print("Contraseña almacenada :", stored_password)
            
             # Obtener los datos del formulario
            new_password = request.form.get("new_password","").strip()
            confirm_password = request.form.get("confirm_password","").strip()
            actual_password = request.form.get("actual_password","").strip()

            # Imprimir los datos recibidos para depuración
            print("Cambio de contraseña solicitado para usuario ID:", fk_usuario
                  , "Contraseña actual ingresada:", actual_password
                  , "Nueva contraseña ingresada:", new_password
                  , "Confirmación de nueva contraseña ingresada:", confirm_password
                )
                    
            # VALIDACIONES ANTES DE ACTUALIZAR 
            
            #Validar que se haya obtenido la contraseña almacenada
            if stored_password is None:
                return jsonify({"status":"error", "msg": "No se pudo obtener la contraseña almacenada ❌"}), 400
            
             #Validar que la contraseña actual ingresada coincida con la almacenada
            if actual_password != stored_password:
                return jsonify({"status":"error", "msg": "La contraseña actual es incorrecta ❌"}), 400
            
            # Validar que los campos no esten vacios
            if not new_password or not confirm_password:
                return jsonify({"status":"warning","msg" : "Los campos no pueden estar vacíos  ⚠"}), 400
            
            # Validar que la nueva contraseña no sea igual a la actual
            if new_password == actual_password:
                return jsonify({"status":"warning", "msg" : "La nueva contraseña no puede ser igual a la actual ⚠"}), 400
            
            # Validar condiciones de la nueva contraseña
            if new_password != confirm_password:
                return jsonify({"status":"warning", "msg": "La nueva contraseña y su confirmación no coinciden ⚠"}), 400
            
            if len(new_password) < 8:
                return jsonify({"status":"warning", "msg": "La contraseña debe tener mínimo 8 caracteres ⚠"}), 400
            
            if len(new_password) > 20:
                return jsonify({"status":"warning", "msg": "La contraseña debe tener máximo 20 caracteres ⚠"}), 400
            
            # Validar complejidad de la nueva contraseña
            patron_password = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&.,;:\-_])[A-Za-z\d@$!%*?&.,;:\-_]{8,}$'
            if not re.fullmatch(patron_password, new_password):
                return jsonify({"status":"warning", "msg": "La contraseña debe tener mínimo 8 caracteres, una mayúscula, un número y un caracter especial ⚠"}), 400
            
            
            # Actualizar la contraseña en la base de datos cuando pase todas las validaciones
            actualizado = Usuario.change_user_password(fk_usuario, new_password)
            
            # Manejo de errores en la actualización
            if not actualizado: 
                return jsonify({"status":"error", "msg": "No se pudo actualizar la contraseña ❌"}), 400
            return jsonify({"status":"success", "msg": "Contraseña actualizada correctamente ✅"}), 200 # Mensaje de éxito

        except Exception as e:
            print(f" Error al cambiar contraseña: {e}") 
            return jsonify({"status":"error", "msg": "Error al cambiar la contraseña. Inténtelo nuevamente ❌"}), 500 # Mensaje de error