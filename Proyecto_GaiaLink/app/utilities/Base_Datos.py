import mysql.connector
from mysql.connector import Error
Config_BaseDatos = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'Root',
    'database': 'prueba', 
    'port': '3306'
}

def Get_BaseDatos():
    conexion = mysql.connector.connect(**Config_BaseDatos)
    cursor = conexion.cursor(dictionary=True)
    return conexion, cursor

def Close_BaseDatos(conexion, cursor):
    if conexion and cursor:
        conexion.rollback()
        cursor.close()
        conexion.close()

def Get_Errores(conexion, error):
    print("DB error:", error)
    try:
        conexion.rollback()
    except:
        pass