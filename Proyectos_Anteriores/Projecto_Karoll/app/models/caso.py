from app.db import Conexion
from app.models.usuario import Usuario
from app.models.utils import formatear_fecha


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

    # ======================== Métodos de Inserción general ========================
    # Insertar un nuevo caso
    @classmethod
    def insert_case(cls, fecha, descripcion, direccion, personas_afectadas, fk_usuario,fk_desastre, fk_ciudad,radicado):
        conn = Conexion().get_connection()
        cursor = conn.cursor()
        
        try: # Insertar datos en tbl_caso
            sql = """
            INSERT INTO tbl_caso
            (Fecha, Descripción,Direccion, Personas_Afectadas, Fk_Usuario, Fk_Desastre, Fk_Ciu, Fk_Tipo_Caso, Fk_Estado)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)
        """
            cursor.execute(sql, (fecha, descripcion, direccion, personas_afectadas, fk_usuario, fk_desastre,fk_ciudad, "Case", "01"))

        # Obtener ID autogenerado del caso
            id_caso = cursor.lastrowid

        # Insertar datos en tbl_num_caso (radicado opcional)
            if radicado:
                sql_num = "INSERT INTO tbl_num_caso (Radicado, Fk_Caso) VALUES (%s, %s)"
                cursor.execute(sql_num, (radicado, id_caso))
            else:
                sql_num = "INSERT INTO tbl_num_caso (Fk_Caso) VALUES (%s)"
                cursor.execute(sql_num, (id_caso,))
                
            conn.commit()

            print(f"Caso {id_caso} registrado con radicado {radicado or 'NULL'}")
            return id_caso # Retornar el ID del caso generado

        except:
                conn.rollback()
                print(f"Error al insertar el caso, intente de nuevo") # Mensaje de error en consola
                raise   
        finally:
            cursor.close()
            conn.close()
    
    @classmethod
    def get_case_by_id(cls,id_caso):
        try:
            sql = """
            SELECT 
                c.Fecha,
                c.Descripción,
                c.Direccion,
                c.Personas_Afectadas,
                d.Desastre AS Desastre,
                ci.Nom_Municipio AS Municipio,
                t.Tipo_Caso AS Tipo_Caso,
                e.Estado AS Estado
            FROM tbl_caso c
            INNER JOIN tbl_desastre d ON c.Fk_Desastre = d.Id_Desastre
            INNER JOIN tbl_ciudad ci ON c.Fk_Ciu = ci.Id_Ciudad
            INNER JOIN tbl_tipo_caso t ON c.Fk_Tipo_Caso = t.Id_Caso
            INNER JOIN tbl_estado e ON c.Fk_Estado = e.Id_Estado
            WHERE c.Id_Caso_Desastre = %s;
            """
            db = Conexion()
            row = db.execute_query(sql, (id_caso,), fetchone=True)

            if not row:
                return None
            
            fecha = row[0]
            fecha_formateada = formatear_fecha(fecha) 
                
            caso = {
                    "fecha": fecha_formateada,
                    "descripcion": row[1],
                    "direccion": row[2],
                    "personas_afectadas": row[3],
                    "desastre": row[4],
                    "municipio": row[5],
                    "tipo_caso": row[6],
                    "estado": row[7]
                }

            return caso
        except Exception as e:
            print(f"Error al obtener datos del caso: {e}")
            return None
    
    # ======================== Métodos de Consulta general ========================
    # Obtener casos por usuario
    @classmethod
    def get_cases_user(cls, fk_usuario):
        # Consulta para obtener los casos del usuario
        sql = """
        SELECT 
            c.Id_Caso_Desastre,
            c.Fecha,
            c.Descripción,
            c.Direccion,
            c.Personas_Afectadas,
            d.Desastre AS Desastre,
            ci.Nom_Municipio AS Municipio,
            t.Tipo_Caso AS Tipo_Caso,
            e.Estado AS Estado
        FROM tbl_caso c
        INNER JOIN tbl_desastre d ON c.Fk_Desastre = d.Id_Desastre
        INNER JOIN tbl_ciudad ci ON c.Fk_Ciu = ci.Id_Ciudad
        INNER JOIN tbl_tipo_caso t ON c.Fk_Tipo_Caso = t.Id_Caso
        INNER JOIN tbl_estado e ON c.Fk_Estado = e.Id_Estado
        WHERE c.Fk_Usuario = %s
        ORDER BY c.Fecha DESC;
        """

        db = Conexion()
        rows = db.execute_query(sql, (fk_usuario,), fetchall=True)

        # Formatear los resultados para JSON (accesible desde el frontend)
        casos = []
        for row in rows:
            fecha = row[1]
            fecha_formateada = formatear_fecha(fecha) 

            casos.append({
                "id": row[0],
                "fecha": fecha_formateada,
                "descripcion": row[2],
                "direccion": row[3],
                "personas_afectadas": row[4],
                "desastre": row[5],
                "municipio": row[6],
                "tipo_caso": row[7],
                "estado": row[8]
            })
        return casos # Retornar lista de casos

    @classmethod
    def get_cases_admin(cls):
        # Consulta para obtener los casos del usuario
        sql = """
        SELECT 
            c.Id_Caso_Desastre,
            c.Fecha,
            c.Descripción,
            c.Direccion,
            c.Personas_Afectadas,
            d.Desastre AS Desastre,
            ci.Nom_Municipio AS Municipio,
            t.Tipo_Caso AS Tipo_Caso,
            e.Estado AS Estado,
            u.Id_usuario,
            u.Nombre AS Nombre_Usuario,
            CONCAT_WS(' ', p.Pri_Nom, p.Pri_Ape) AS Nombre_Completo
        FROM tbl_caso c
        INNER JOIN tbl_desastre d ON c.Fk_Desastre = d.Id_Desastre
        INNER JOIN tbl_ciudad ci ON c.Fk_Ciu = ci.Id_Ciudad
        INNER JOIN tbl_tipo_caso t ON c.Fk_Tipo_Caso = t.Id_Caso
        INNER JOIN tbl_estado e ON c.Fk_Estado = e.Id_Estado
        INNER JOIN tbl_usuario u ON c.Fk_Usuario = u.Id_usuario
        INNER JOIN tbl_persona p ON u.Id_usuario = p.fk_usuario
        ORDER BY c.Fecha DESC;
        """

        db = Conexion()
        rows = db.execute_query(sql, fetchall=True)

        # Formatear los resultados para JSON (accesible desde el frontend)
        casos = []
        for row in rows:
            fecha = row[1]
            fecha_formateada = formatear_fecha(fecha) 

            casos.append({
                "id": row[0],
                "fecha": fecha_formateada,
                "descripcion": row[2],
                "direccion": row[3],
                "personas_afectadas": row[4],
                "desastre":row[5],
                "municipio": row[6],
                "tipo_caso": row[7],
                "estado": row[8],
                "id_usuario": row[9],
                "nombre_usuario": row[10],
                "nombre_completo": row[11]
            })
        return casos # Retornar lista de casos
    
    @classmethod
    def generate_report(cls, initial_date, final_date):
        sql = f"""
            SELECT 
                c.Id_Caso_Desastre,
                c.Fecha,
                c.Descripción,
                c.Direccion,
                c.Personas_Afectadas,
                d.Desastre AS Desastre,
                ci.Nom_Municipio AS Municipio,
                t.Tipo_Caso AS Tipo_Caso,
                e.Estado AS Estado,
                en.Nombre_Entidad AS Entidad_Encargada,
                u.Id_Usuario,
                u.Nombre AS Nombre_Usuario,
                CONCAT_WS(' ', p.Pri_Nom, p.Pri_Ape) AS Nombre_Completo
            FROM tbl_caso c
            INNER JOIN tbl_desastre d ON c.Fk_Desastre = d.Id_Desastre
            INNER JOIN tbl_ciudad ci ON c.Fk_Ciu = ci.Id_Ciudad
            INNER JOIN tbl_tipo_caso t ON c.Fk_Tipo_Caso = t.Id_Caso
            INNER JOIN tbl_estado e ON c.Fk_Estado = e.Id_Estado
            INNER JOIN tbl_usuario u ON c.Fk_Usuario = u.Id_Usuario
            INNER JOIN tbl_persona p ON u.Id_Usuario = p.Fk_Usuario
            INNER JOIN tbl_entidad en ON d.fk_entidad = en.Id_entidad
            WHERE c.Fecha BETWEEN %s AND %s
            ORDER BY c.Fecha DESC;
        """
        db = Conexion()
        try: 
            print(f"Ejecutando reporte entre {initial_date} y {final_date}")
            rows = db.execute_query(sql, (initial_date, final_date), fetchall=True)
            print(f"Filas encontradas: {len(rows)}")
            casos = []
            for row in rows:
                fecha_formateada = formatear_fecha(row[1])
                casos.append({
                    "id": row[0],
                    "fecha": fecha_formateada,
                    "descripcion": row[2],
                    "direccion": row[3],
                    "personas_afectadas": row[4],   
                    "desastre":row[5],
                    "municipio": row[6],
                    "tipo_caso": row[7],
                    "estado": row[8],
                    "entidad_encargada": row[9],
                    "id_usuario": row[10],
                    "nombre_usuario": row[11],
                    "nombre_completo": row[12]  
                })
            return casos # Retornar lista de casos
        except Exception as e:
            print(f"Error al generar el reporte, intente de nuevo: {e}") # Mensaje de error en consola
            raise
            
    
        
        
       
