from flask import session
from app.db import Conexion

class Usuario:
    def __init__(self, id_usuario=None, username=None, password=None, rol=None, estado=None):
        self.id_usuario = id_usuario
        self.username = username
        self.password = password
        self.rol = rol
        self.estado = estado

    # ========================
    #  Métodos de autenticación
    # ========================
    @classmethod
    def get_user_by_name(cls, username):
        sql = """
            SELECT Id_usuario, Nombre, Contraseña, fk_rol, fk_estado
            FROM tbl_usuario
            WHERE BINARY Nombre = %s
        """
        db = Conexion()
        row = db.execute_query(sql, (username,), fetchone=True)
        if row:
            return cls(id_usuario=row[0], username=row[1], password=row[2], rol=row[3], estado=row[4])
        return None


    @classmethod
    def get_user_by_role(cls, username):
        sql = "SELECT fk_rol FROM tbl_usuario WHERE Nombre = %s"
        db = Conexion()
        row = db.execute_query(sql, (username,), fetchone=True)
        return row[0] if row else None
    
    @classmethod
    def get_user_by_session(cls):
        """
        Retorna el id_usuario del usuario actual en sesión.
        Si no hay sesión activa o no existe en DB, retorna None.
        """
        username = session.get("username")
        if not username:
            return None

        conn = Conexion()
        row = conn.execute_query(
            "SELECT Id_usuario FROM tbl_usuario WHERE Nombre = %s",
            (username,), fetchone=True
        )
        return row[0] if row else None


    @classmethod
    def get_user_by_state(cls, username):
        sql = "SELECT fk_estado FROM tbl_usuario WHERE Nombre = %s"
        db = Conexion()
        row = db.execute_query(sql, (username,), fetchone=True)
        return row[0] if row else None


    # ========================
    #  Métodos de registro
    # ========================
    @classmethod
    def username_exists(cls, username):
        sql = "SELECT 1 FROM tbl_usuario WHERE BINARY Nombre = %s"
        db = Conexion()
        row = db.execute_query(sql, (username,), fetchone=True)
        return row is not None
    
    @classmethod
    def documento_exists(cls, id_persona):
        sql = "SELECT 1 FROM tbl_persona WHERE Id_Persona = %s"
        db = Conexion()
        row = db.execute_query(sql, (id_persona,), fetchone=True)
        return row is not None

    @classmethod
    def insert_user_with_details(cls,
                                 username, password,
                                 id_persona, pri_nom, seg_nom, pri_ape, seg_ape,
                                 tipo_doc, fecha_nac,
                                 edad, direccion, telefono, email,
                                 fk_rol="User", fk_estado="01"):
       
        db = Conexion()
        conn = db.get_connection()
        cursor = conn.cursor()
        try:
            # 1. Insertar en tbl_usuario
            cursor.execute(
                "INSERT INTO tbl_usuario (Nombre, Contraseña, fk_rol, fk_estado) VALUES (%s, %s, %s, %s)",
                (username, password, fk_rol, fk_estado)
            )
            conn.commit()
            
            cursor.execute("SELECT LAST_INSERT_ID()")
            id_usuario = cursor.fetchone()[0]

            # 2. Insertar en tbl_persona
            cursor.execute(
                """INSERT INTO tbl_persona
                   (Id_Persona, Pri_Nom, Seg_Nom, Pri_Ape, Seg_Ape, fk_Tipo_documento, Fecha_nacimiento, fk_usuario)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                (id_persona, pri_nom, seg_nom, pri_ape, seg_ape, tipo_doc, fecha_nac, id_usuario)
            )

            # 3. Insertar en tbl_adic_persona
            id_adic_persona = f"{id_persona}-1"
            cursor.execute(
                """INSERT INTO tbl_adic_persona
                   (Id_Adic_Persona, Edad, Direccion, Num_Contact, Email, fk_persona)
                   VALUES (%s, %s, %s, %s, %s, %s)""",
                (id_adic_persona, edad, direccion, telefono, email, id_persona)
            )

            conn.commit()
            return id_usuario

        except Exception as e:
            conn.rollback()
            print("❌ Error al insertar usuario:", e)
            raise e
        finally:
            cursor.close()
