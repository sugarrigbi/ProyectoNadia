import mysql.connector

# Configuración de la conexión a MySQL
DB_CONFIG = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'database': 'proyecto', 
    'port': '3306'
}

def get_db_connection():
    conn = mysql.connector.connect(**DB_CONFIG)
    return conn

