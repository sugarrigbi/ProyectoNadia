# app/queries.py
from app.db import get_db_connection

def get_user_by_name(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tbl_usuario WHERE Nombre = %s", (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def get_user_role(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT fk_rol FROM tbl_usuario WHERE Nombre = %s", (username,))
    role = cursor.fetchone()
    cursor.close()
    conn.close()
    return role[0] if role else None