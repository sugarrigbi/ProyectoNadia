import re
from flask import Flask, request, jsonify, send_file, render_template, redirect, url_for, session
import pandas as pd
import os
import mysql.connector
from datetime import date
from Utilities import Verificar_Rol


Tipo_Documento_Valores2 = {
    "Cedula Ciudadania": "CC",
    "Cedula Extranjeria": "CE",
    "Pasaporte": "PA",
    "Registro Civil": "RC",
    "Tarjeta de identidad": "TI"
}
Tipo_Documento_Valores = {
    "CC": "Cedula Ciudadania",
    "CE": "Cedula Extranjeria",
    "PA": "Pasaporte",
    "RC": "Registro Civil",
    "TI": "Tarjeta de identidad"
}
def Conexion_Base():
    global cursor, conexion
    try:
        conexion = mysql.connector.connect(
            host=app.config['MYSQL_HOST'],
            port=app.config['MYSQL_PORT'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            database=app.config['MYSQL_DB'],
            auth_plugin='mysql_native_password'
            )
        cursor = conexion.cursor(dictionary=True)
    except mysql.connector.Error as e:
        return jsonify({'error': f"Error en MySQL: {str(e)}"}), 500
    except Exception as e:
        return jsonify({'error': f"Error interno: {str(e)}"}), 500
def Cerrar_Conexion_Base():
    conexion.rollback()
    cursor.close()
    conexion.close()
class Persona:
    def __init__(self, Codigo, Tipo_Documento, Documento, Primer_Nombre,
                Segundo_Nombre, Primer_Apellido, Segundo_Apellido,
                Fecha_Nacimiento, Codigo_Adic, Edad, Direccion, Departamento,
                Ciudad, Localidad, Barrio, Numero_Contacto, Email, Usuario, Contraseña, Rol, Estado):
        self.Codigo = Codigo
        self.Tipo_Documento = Tipo_Documento
        self.Documento = Documento
        self.Primer_Nombre = Primer_Nombre
        self.Segundo_Nombre = Segundo_Nombre
        self.Primer_Apellido = Primer_Apellido
        self.Segundo_Apellido = Segundo_Apellido
        self.Fecha_Nacimiento = Fecha_Nacimiento
        self.Codigo_Adic = Codigo_Adic
        self.Edad = Edad
        self.Direccion = Direccion
        self.Departamento = Departamento
        self.Ciudad = Ciudad
        self.Localidad = Localidad
        self.Barrio = Barrio
        self.Numero_Contacto = Numero_Contacto
        self.Email = Email
        self.Usuario = Usuario
        self.Contraseña = Contraseña
        self.Rol = Rol
        self.Estado = Estado

    def Buscar_Persona(self):
        Conexion_Base()
        Buscar_Codigo = self.Documento
        if not Buscar_Codigo:
            print("Error, no existe self.Documento_Buscar")
            try:
                if conexion and conexion.is_connected():
                    Cerrar_Conexion_Base()
            except:
                pass
            return            
        try:
            cursor.execute("SELECT fk_usuario FROM tbl_persona WHERE Id_Persona = %s", (Buscar_Codigo,))
            Resultado_Usuario = cursor.fetchone()
        
            if not Resultado_Usuario:
                print("Error, No se encontró el usuario.")
                return
            Id_Usuario = Resultado_Usuario["fk_usuario"]

            cursor.execute("SELECT fk_estado FROM tbl_usuario WHERE Id_usuario = %s", (Id_Usuario,))
            Resultado_Estado = cursor.fetchone()

            if not Resultado_Estado:
                print("Error, No se encontró el Usuario.")
                Cerrar_Conexion_Base()
                return
            Estado_Actual = Resultado_Estado["fk_estado"]

            if Estado_Actual == "Usuario_00":
                print("Usuario no encontrado, El usuario no existe.")
                return

            cursor.execute("""
                SELECT 
                    tbl_persona.Id_Persona, 
                    tbl_persona.fk_Tipo_documento, 
                    tbl_persona.Pri_Nom, 
                    tbl_persona.Seg_Nom, 
                    tbl_persona.Pri_Ape, 
                    tbl_persona.Seg_Ape, 
                    tbl_persona.Fecha_nacimiento, 
                    tbl_adic_persona.Id_Adic_Persona, 
                    tbl_adic_persona.Edad, 
                    tbl_adic_persona.Dirección, 
                    tbl_ciudad.Nom_ciudad, 
                    tbl_localidad.Localidad, 
                    tbl_barrio.Barrio, 
                    tbl_adic_persona.Num_Contact, 
                    tbl_adic_persona.Email, 
                    tbl_departamento.Nom_departamento,
                    tbl_usuario.Nombre,
                    tbl_usuario.Contraseña,
                    tbl_usuario.fk_rol,
                    tbl_usuario.fk_estado
                FROM tbl_adic_persona JOIN tbl_persona ON tbl_adic_persona.fk_persona = tbl_persona.Id_persona 
                JOIN tbl_tipo_documento ON tbl_persona.fk_Tipo_documento = tbl_tipo_documento.Id_Documento 
                JOIN tbl_usuario ON tbl_persona.fk_usuario = tbl_usuario.Id_usuario JOIN tbl_barrio ON tbl_adic_persona.fk_dir = tbl_barrio.Id_barrio 
                JOIN tbl_localidad ON tbl_barrio.fk_local = tbl_localidad.Id_local JOIN tbl_ciudad ON tbl_localidad.fk_ciudad = tbl_ciudad.Id_ciudad 
                JOIN tbl_departamento ON tbl_ciudad.Fk_Dep = tbl_departamento.Id_dep WHERE tbl_usuario.Id_usuario = %s
                """, (Id_Usuario,))
            Resultado = cursor.fetchone()
            if not Resultado:
                return None  

            persona_data = {
                "Codigo": Id_Usuario,
                "Tipo_Documento": Tipo_Documento_Valores.get(Resultado["fk_Tipo_documento"]),
                "Documento": Resultado["Id_Persona"],
                "Primer_Nombre": Resultado["Pri_Nom"],
                "Segundo_Nombre": Resultado["Seg_Nom"],
                "Primer_Apellido": Resultado["Pri_Ape"],
                "Segundo_Apellido": Resultado["Seg_Ape"],
                "Fecha_Nacimiento": Resultado["Fecha_nacimiento"].strftime("%d/%m/%Y") if Resultado["Fecha_nacimiento"] else "",
                "Codigo_Adic": Resultado["Id_Adic_Persona"],
                "Edad": Resultado["Edad"],
                "Direccion": Resultado["Dirección"],
                "Departamento": Resultado["Nom_departamento"],
                "Ciudad": Resultado["Nom_ciudad"],
                "Localidad": Resultado["Localidad"],
                "Barrio": Resultado["Barrio"],
                "Numero_Contacto": Resultado["Num_Contact"],
                "Email": Resultado["Email"],
                "Nombre": Resultado["Nombre"],
                "Contraseña": Resultado["Contraseña"],
                "Rol": Resultado ["fk_rol"],
                "Estado": Resultado ["fk_estado"],
            }

            conexion.commit()
            return persona_data

        except mysql.connector.Error as err:
            try:
                if conexion and conexion.is_connected() and conexion.in_transaction:
                    conexion.rollback()
            except:
                print("No se pudo hacer rollback: conexión cerrada.")
            print(f"Error, Ocurrió un error al consultar los datos: {err}")

        finally:
            try:
                if conexion and conexion.is_connected():
                    Cerrar_Conexion_Base()
            except:
                print("No se pudo cerrar la conexión: ya se había cerrado.")            
'''
    def Crear_Persona(self):
        Conexion_Base()
        Verificar_Rol()



        data = request.get_json()
        self.Codigo = id_usuario
        Pasar = data.get("Tipo_Documento")
        self.Tipo_Documento = Tipo_Documento_Valores2.get(Pasar)
        self.Documento = data.get("Documento")
        self.Primer_Nombre = data.get("Primer Nombre")
        self.Segundo_Nombre = data.get("Segundo Nombre")
        self.Primer_Apellido = data.get("Primer Apellido")
        self.Segundo_Apellido = data.get("Segundo Apellido")
        self.Fecha_Nacimiento = data.get("Fecha_Nacimiento")
        self.Codigo_Adic = id_adic_persona
        self.Direccion = data.get("Direccion")
        self.Departamento = data.get("Departamento")
        self.Ciudad = data.get("Ciudad")
        self.Localidad = data.get("Localidad")
        self.Barrio = data.get("Barrio")
        self.Numero_Contacto = data.get("Numero Contacto")
        self.Email = data.get("Email")
        hoy = date.today()
        self.Edad = hoy.year - self.Fecha_Nacimiento.year - ((hoy.month, hoy.day) < (self.Fecha_Nacimiento.month, self.Fecha_Nacimiento.day))
        Conexion_Base()    
        if not all([self.Tipo_Documento, self.Documento, self.Primer_Nombre, self.Segundo_Nombre, 
                    self.Primer_Apellido, self.Segundo_Apellido, self.Fecha_Nacimiento, self.Direccion, 
                    self.Departamento, self.Ciudad, self.Barrio, self.Numero_Contacto, self.Email, self.Edad]):
            print("Error, Todos los campos son obligatorios")
            Cerrar_Conexion_Base()
            return
        if not self.Documento.isdigit() or not (8 <= len(self.Documento) <= 10):
            print("Error, El documento debe tener entre 8 a 10 digitos")
            Cerrar_Conexion_Base()
            return
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.Email):
            print("Error, Correo invalido")
            Cerrar_Conexion_Base()
            return     
        if not self.Numero_Contacto.isdigit() or len(self.Numero_Contacto) != 10:
            print("Error, El telefono debe tener 10 digitos")
            Cerrar_Conexion_Base()
            return
        
        cursor.execute("SELECT * FROM tbl_persona WHERE Id_Persona = %s", (self.Documento,))
        if cursor.fetchone():
            print("Error, El documento ya está registrado.")
            Cerrar_Conexion_Base()
            return
     try:
        if not conexion.in_transaction:
            conexion.start_transaction()

        cursor.execute("SELECT Id_dep FROM tbl_departamento WHERE Nom_departamento = %s", (persona.Departamento,))
        dep = cursor.fetchone()
        id_departamento = dep[0] if dep else generar_id("tbl_departamento", "DEP")
        if not dep:
            cursor.execute("INSERT INTO tbl_departamento (Id_dep, Nom_departamento) VALUES (%s, %s)",
                           (id_departamento, persona.Departamento))

        cursor.execute("SELECT Id_ciudad FROM tbl_ciudad WHERE Nom_ciudad = %s", (persona.Ciudad,))
        c = cursor.fetchone()
        id_ciudad = c[0] if c else generar_id("tbl_ciudad", "CIU")
        if not c:
            cursor.execute("INSERT INTO tbl_ciudad (Id_ciudad, Nom_ciudad, Fk_Dep) VALUES (%s, %s, %s)",
                           (id_ciudad, persona.Ciudad, id_departamento))

        cursor.execute("SELECT Id_local FROM tbl_localidad WHERE Localidad = %s", (persona.Localidad,))
        l = cursor.fetchone()
        id_localidad = l[0] if l else generar_id("tbl_localidad", "LOC")
        if not l:
            cursor.execute("INSERT INTO tbl_localidad (Id_local, Localidad, fk_ciudad) VALUES (%s, %s, %s)",
                           (id_localidad, persona.Localidad, id_ciudad))

        cursor.execute("SELECT Id_barrio FROM tbl_barrio WHERE Barrio = %s AND fk_local = %s", (persona.Barrio, id_localidad))
        b = cursor.fetchone()
        id_barrio = b[0] if b else generar_id("tbl_barrio", "BAR")
        if not b:
            cursor.execute("INSERT INTO tbl_barrio (Id_barrio, Barrio, fk_local) VALUES (%s, %s, %s)",
                           (id_barrio, persona.Barrio, id_localidad))
            
        cursor.execute("SELECT Id_Documento FROM tbl_tipo_documento WHERE Id_Documento = %s", (persona.Valor_Tipo_Documento,))
        tipo_doc = cursor.fetchone()
        id_tipo_documento = persona.Valor_Tipo_Documento 
        if not tipo_doc:
            cursor.execute("INSERT INTO tbl_tipo_documento (Id_Documento, Tipo_documento) VALUES (%s, %s)",
                   (id_tipo_documento, persona.Tipo_Documento))

        id_usuario = generar_id("tbl_usuario", "USU")
        cursor.execute("INSERT INTO tbl_usuario (Id_usuario, Nombre, Contraseña, fk_rol, fk_estado) VALUES (%s, %s, %s, %s, %s)", 
                       (id_usuario, persona.Usuario, persona.Contraseña, id_rol, id_activo))

        cursor.execute("INSERT INTO tbl_persona (Id_Persona, Pri_Nom, Seg_Nom, Pri_Ape, Seg_Ape, fk_Tipo_documento, Fecha_nacimiento, fk_Usuario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                       (persona.Documento, persona.Primer_Nombre, persona.Segundo_Nombre, persona.Primer_Apellido, persona.Segundo_Apellido, persona.Valor_Tipo_Documento, persona.Fecha_Nacimiento, id_usuario))

        cursor.execute("INSERT INTO tbl_adic_persona (Id_Adic_Persona, Edad, Dirección, Num_Contact, Email, fk_persona, fk_dir) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                       (id_adic_persona, persona.Edad, persona.Direccion, persona.Numero, persona.Email, persona.Documento, id_barrio)) 

        conexion.commit()
        messagebox.showinfo("Éxito", "Usuario y datos asociados creados correctamente.")
'''




app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Root'
app.config['MYSQL_DB'] = 'proyecto'
app.config['MEDIA_ROOT'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media')

@app.route('/personas/<doc_id>', methods=['GET'])
def get_persona(doc_id):
    Conexion_Base()
    persona = Persona(None, None, doc_id, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
    resultado = persona.Buscar_Persona()
    if not resultado:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(resultado)



#PRUEBAS DE KEVIN
@app.route('/grafico/<doc_id>', methods=['GET'])
def grafico(doc_id):
    Conexion_Base()
    persona = Persona(None, None, doc_id, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
    resultado = persona.Buscar_Persona()
    print(Persona)    
    if not resultado:
        return render_template("error.html", mensaje="Usuario no encontrado")
    return render_template("grafico.html", persona=resultado)

if __name__ == "__main__":
    app.run(debug=True)
