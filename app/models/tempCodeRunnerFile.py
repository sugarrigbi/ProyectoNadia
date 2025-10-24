    def Buscar_Persona(self):
        conexion, cursor = Get_BaseDatos()
        try:
            conexion, cursor = Get_BaseDatos()
            if conexion is None:
                return {"error": "No se pudo conectar a la base de datos"}

            cursor.execute("SELECT Id_Persona FROM tbl_persona JOIN tbl_usuario ON tbl_persona.fk_Usuario = tbl_usuario.Id_usuario WHERE tbl_persona.fk_Usuario = %s", (self.Codigo,))
            Resultado2 = cursor.fetchone()
            if not Resultado2:
                return
            self.Documento = Resultado2["Id_Persona"]

            Buscar_Codigo = self.Documento        
            cursor.execute("SELECT fk_usuario FROM tbl_persona WHERE Id_Persona = %s", (Buscar_Codigo,))
            Resultado_Usuario = cursor.fetchone()
        
            if not Resultado_Usuario:
                return
            Id_Usuario = Resultado_Usuario["fk_usuario"]

            cursor.execute("SELECT fk_estado FROM tbl_usuario WHERE Id_usuario = %s", (Id_Usuario,))
            Resultado_Estado = cursor.fetchone()
            if not Resultado_Estado:
                return None
        
            Estado_Actual = Resultado_Estado["fk_estado"]
            if Estado_Actual == "Usuario_00":
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
            Get_Errores(conexion, err)
            return {"error": str(err)}

        finally:
            Close_BaseDatos(conexion, cursor) 