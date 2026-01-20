# app/insertions.py
from app.db import get_db_connection

def insert_user(id_usuario, nombre, contraseña, fk_rol, fk_estado):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tbl_usuario (Id_usuario, Nombre, Contraseña, fk_rol, fk_estado) VALUES (%s, %s, %s, %s, %s)",
        (id_usuario, nombre, contraseña, fk_rol, fk_estado)
    )
    conn.commit()
    cursor.close()
    conn.close()

def insert_case(id_caso, fecha, descripcion, personas_afectadas, fk_usuario, fk_desastre, fk_dep, fk_tipo_caso, fk_estado):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tbl_caso (Id_Caso_Desastre, Fecha, Descripción, Personas_Afectadas, Fk_Usuario, Fk_Desastre, Fk_Dep, Fk_Tipo_Caso, Fk_Estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (id_caso, fecha, descripcion, personas_afectadas, fk_usuario, fk_desastre, fk_dep, fk_tipo_caso, fk_estado)
    )
    conn.commit()
    cursor.close()
    conn.close()