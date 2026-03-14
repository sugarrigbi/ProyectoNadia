from App.Models.User_Model import Persona as Tabla_Persona, Usuario as Tabla_Usuario, Departamento as T_Departamento, Ciudad as T_Ciudad, Localidad as T_Localidad, Barrio as T_Barrio
from App.Utilities.Tables import db
from App.Utilities.Util import Normalizar_Datos, Validar_Datos, Generar_Codigo, Enviar_Correo, Guardar_Codigo, Guardar_Datos, Obtener_Codigo, Obtener_Datos, Eliminar_Datos, Hashear_Contraseña

class User_Service:
    @staticmethod
    def Registro(Data_U, Data_P):
        Error = Validar_Datos(Data_U, Data_P)
        if Error:
            return Error
        
        Codigo = Generar_Codigo()
        Enviar_Correo(Data_U["Correo"], Codigo)

        Guardar_Codigo(Data_U["Correo"], Codigo)
        Guardar_Datos(Data_U["Correo"], Data_U, Data_P)

        return "Codigo Enviado"
    @staticmethod
    def Create(Correo, Codigo):
        Codigo_Real = Obtener_Codigo(Correo)
        
        if Codigo != Codigo_Real:
            return {"Error": "Codigo Incorrecto"}
        
        Data_UN, Data_PN = Obtener_Datos(Correo)
        
        Data_U, Data_P, Data_C = Normalizar_Datos(Data_UN, Data_PN)

        Dep_Existe = T_Departamento.query.filter_by(Nombre=Data_C["Departamento_ID"]).first()
        if not Dep_Existe:
            Dep_Existe = T_Departamento(Nombre=Data_C["Departamento_ID"], Pais_ID=1)
            db.session.add(Dep_Existe)
            db.session.commit()
        Ciu_Existe = T_Ciudad.query.filter_by(Nombre=Data_C["Ciudad_ID"]).first()
        if not Ciu_Existe:
            Ciu_Existe = T_Ciudad(Nombre=Data_C["Ciudad_ID"], Departamento_ID=Dep_Existe.ID)
            db.session.add(Ciu_Existe)
            db.session.commit()
        Loc_Existe = T_Localidad.query.filter_by(Nombre=Data_C["Localidad_ID"]).first()
        if not Loc_Existe:
            Loc_Existe = T_Localidad(Nombre=Data_C["Localidad_ID"], Ciudad_ID=Ciu_Existe.ID)
            db.session.add(Loc_Existe)
            db.session.commit()
        Bar_Existe = T_Barrio.query.filter_by(Nombre=Data_C["Barrio_ID"]).first()
        if not Bar_Existe:
            Bar_Existe = T_Barrio(Nombre=Data_C["Barrio_ID"], Localidad_ID=Loc_Existe.ID)
            db.session.add(Bar_Existe)
            db.session.commit()                                   
        Data_P["Barrio_ID"] = Bar_Existe.ID

        Data_U["Contraseña"] = Hashear_Contraseña(Data_U["Contraseña"])

        Usuario = Tabla_Usuario(**Data_U)
        db.session.add(Usuario)
        db.session.flush()

        Data_P["Usuario_ID"] = Usuario.ID

        Persona = Tabla_Persona(**Data_P)
        db.session.add(Persona)
        db.session.commit()
        
        Eliminar_Datos(Correo)

        return Usuario