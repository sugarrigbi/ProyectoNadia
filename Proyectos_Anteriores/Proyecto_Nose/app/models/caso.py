from app.db import Conexion
from app.models.usuario import Usuario

  # 🔹 Mapeo de desastres
DESASTRES = {
        "incendio": "In",
        "inundacion": "Inund",
        "sismo_temblor": "SI-T",
        "terremoto": "Ter"
    }

class Caso:
    def __init__(self, id_caso=None, fecha=None, descripcion=None, personas_afectadas=None, direccion=None,
                 fk_usuario=None, fk_desastre=None, fk_ciudad=None,fk_tipo_caso="Case", fk_estado="01"):
        self.id_caso = id_caso
        self.fecha = fecha
        self.descripcion = descripcion
        self.direccion = direccion
        self.personas_afectadas = personas_afectadas
        self.fk_usuario = fk_usuario
        self.fk_desastre = fk_desastre
        self.fk_ciudad= fk_ciudad
        self.fk_tipo_caso = fk_tipo_caso
        self.fk_estado = fk_estado

  
    @classmethod
    def insert_case(cls, fecha, descripcion, direccion, personas_afectadas, fk_desastre, fk_ciudad,radicado):
        
        fk_usuario = Usuario.get_user_by_session()
        if not fk_usuario:
            raise ValueError("No hay usuario en sesión o no existe en DB")

        conn = Conexion().get_connection()
        cursor = conn.cursor()
        try:
            sql = """
            INSERT INTO tbl_caso
            (Fecha, Descripción,Direccion, Personas_Afectadas, Fk_Usuario, Fk_Desastre, Fk_Ciu, Fk_Tipo_Caso, Fk_Estado)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)
        """
            cursor.execute(sql, (fecha, descripcion, direccion, personas_afectadas, fk_usuario, fk_desastre,fk_ciudad, "Case", "01"))

        # 2. Obtener ID autogenerado del caso
            id_caso = cursor.lastrowid

        # 3. Insertar en tbl_num_caso (radicado opcional)
            if radicado:
                sql_num = "INSERT INTO tbl_num_caso (Radicado, Fk_Caso) VALUES (%s, %s)"
                cursor.execute(sql_num, (radicado, id_caso))
            else:
                sql_num = "INSERT INTO tbl_num_caso (Fk_Caso) VALUES (%s)"
                cursor.execute(sql_num, (id_caso,))
                
            conn.commit()

            print(f"✅ Caso {id_caso} registrado con radicado {radicado or 'NULL'}")
            return id_caso

        except:
                conn.rollback()
                print(f"❌ Error al insertar el caso, intente de nuevo")
                raise   
        finally:
            cursor.close()
            conn.close()
    
    
    @classmethod
    def get_cases_user(cls):

        # 1. Obtener el usuario
        fk_usuario = Usuario.get_user_by_session()
        if not fk_usuario:
            raise ValueError("No hay usuario en sesión o no existe en DB")
        

        # 2. Consultar casos de ese usuario
        sql = """
        SELECT c.Id_Caso_Desastre, c.Fecha, c.Descripción, c.Direccion, c.Personas_Afectadas,
               d.Nombre AS desastre,
               ci.Nombre AS ciudad,
               t.Nombre AS tipo_caso,
               e.Nombre AS estado
        FROM tbl_caso c
        INNER JOIN tbl_desastre d ON c.Fk_Desastre = d.Id_Desastre
        INNER JOIN tbl_ciudad ci ON c.Fk_Ciu = ci.Id_Ciu
        INNER JOIN tbl_tipo_caso t ON c.Fk_Tipo_Caso = t.Id_Tipo_Caso
        INNER JOIN tbl_estado e ON c.Fk_Estado = e.Id_Estado
        WHERE c.Fk_Usuario = %s
        ORDER BY c.Fecha DESC
        """
        
        db = Conexion()
        rows = db.execute_query(sql, (fk_usuario,), fetchall=True)

        # 3. Transformar resultados en objetos Caso o lista de dicts
        casos = []
        for row in rows:
            casos.append({
                "id": row[0],
                "fecha": row[1],
                "descripcion": row[2],
                "direccion": row[3],
                "personas_afectadas": row[4],
                "desastre": row[5],
                "ciudad": row[6],
                "tipo_caso": row[7],
                "estado": row[8]
            })
        return casos
            
    
       