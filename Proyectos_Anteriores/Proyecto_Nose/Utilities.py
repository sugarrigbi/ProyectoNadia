import mysql.connector
from flask import current_app
def Verificar_Rol(id_usuario):

    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Root",
            database="proyecto",
            port="3306"
        )
        cursor = conexion.cursor()

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
        if cursor:
            cursor.close()
        if conexion and conexion.is_connected():
            conexion.close()