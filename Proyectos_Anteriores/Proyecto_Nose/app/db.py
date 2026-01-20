import mysql.connector
from mysql.connector import Error

class Conexion:
    def __init__(self,
                 host="localhost",
                 user="root",
                 password="root",
                 database="proyecto"):
        self.config = {
            "host": host,
            "user": user,
            "password": password,
            "database": database,
            "autocommit": False  # control manual de transacciones
        }

    def get_connection(self):
        try:
            conn = mysql.connector.connect(**self.config)
            if conn.is_connected():
                print("✅ Conexión establecida a la base de datos")
                return conn
        except Error as e:
            print(f"❌ Error de conexión: {e}")
            raise

    def execute_query(self, query, params=None, fetchone=False, fetchall=False, commit=False, rollback= None):
        """
        Ejecuta una consulta en la base de datos de forma segura.
        """
        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()

            cursor.execute(query, params or ())

            if commit:
                conn.commit()

            if fetchone:
                return cursor.fetchone()
            if fetchall:
                return cursor.fetchall()
            
            if rollback:
                return conn.rollback()

        except Error as e:
            if conn:
                conn.rollback()
            print(f"❌ Error ejecutando query: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()



        