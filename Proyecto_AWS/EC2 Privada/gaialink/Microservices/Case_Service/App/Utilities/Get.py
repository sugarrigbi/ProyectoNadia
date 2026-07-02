from App.Services.Case_Logic import Case_Service
from flask import request, jsonify, send_file
from App.Utilities.Util import Validar_JWT
from datetime import date

class Get_Case:
    @staticmethod
    def Case_Create():
        Data = request.get_json()
        if not Data:
            return jsonify({"Error": "No data provided"}), 400
        
        Auth_Data, Error = Validar_JWT()
        if Error:
            if Error in ["Token expirado", "Token inválido"]:
                return jsonify({"Error": Error}), 401
            return jsonify({"Error": Error}), 400
        User_ID = Auth_Data["user_id"]   
        
        Data_C = {
            "Nombre": Data.get("CasoNuevo_Nombre"),
            "Descripcion": Data.get("CasoNuevo_Descripcion"),
            "Usuario_Creador_ID": User_ID,
            "Usuario_Asociado_ID": Data.get("CasoNuevo_Usuario_Cargo"),
            "Estado_Caso_ID": Data.get("CasoNuevo_Estado"),
            "Prioridad_ID": Data.get("CasoNuevo_Prioridad"),
            "Incidente_ID": Data.get("CasoNuevo_Incidente"),
            "Afectados": Data.get("CasoNuevo_Afectados"),
            "Direccion": Data.get("CasoNuevo_Direccion")
        }
        Data_C_C = {
            "Mensaje": Data.get("CasoNuevo_Comentario"),
            "Usuario_ID": Data.get("Usuario_Id")
        }
        Data_L = {
            "Barrio": Data.get("Caso_Barrio_Nombre"),
            "Barrio_ID": Data.get("Caso_Barrio_ID"),
            "Localidad": Data.get("Caso_Localidad_Nombre"),
            "Localidad_ID": Data.get("Caso_Localidad_ID"),
            "Ciudad": Data.get("Caso_Ciudad_Nombre"),
            "Ciudad_ID": Data.get("Caso_Ciudad_ID"),
            "Departamento": Data.get("Caso_Departamento_Nombre"),
            "Departamento_ID": Data.get("Caso_Departamento_ID")
        }

        if Data.get('CasoNuevo_Relacion_Radicado') and Data.get("CasoNuevo_Relacion_Tipo"):
            Data_R = {
                "Relacion_Radicado": Data['CasoNuevo_Relacion_Radicado'],
                "Relacion_Tipo": Data['CasoNuevo_Relacion_Tipo']
            }
        else:
            Data_R = {}     
        
        Caso = Case_Service.Create(Data_C, Data_L, User_ID, Data_C_C, Data_R)
        if Caso == "Auth":
            return jsonify({"Error": "No Auth"}), 403
        if not Caso:
            return jsonify({"Error": "Case creation failed"}), 400
        
        return jsonify({"Message": "Case created successfully"}), 201
    @staticmethod
    def Case_Read_All(Pagina):
        Auth_Data, Error = Validar_JWT()
        if Error:
            if Error in ["Token expirado", "Token inválido"]:
                return jsonify({"Error": Error}), 401
            return jsonify({"Error": Error}), 400
        User_ID = Auth_Data["user_id"]

        Casos = Case_Service.Read_All(User_ID, Pagina)
        Datos_Obtener = Case_Service.Obtener_Datos(User_ID)
        Linea_Tiempo = Case_Service.Linea_Tiempo(User_ID, Casos)
        if Casos == "Auth":
            return jsonify({"Error": "No Auth"}), 403    
        if not Datos_Obtener:
            return jsonify({"Error": "No cases found"}), 404
        if not Linea_Tiempo or Linea_Tiempo == "Auth":
            Tiempo_Dict = []
        else:        
            Tiempo_Dict = [T.to_dict2() for T in Linea_Tiempo]            

        return jsonify({"Casos": [C.to_dict2() for C in Casos.items], "Datos": Datos_Obtener, "Linea": Tiempo_Dict, "Paginas_Validas": Casos.pages, "Pagina": Casos.page}), 200
    @staticmethod
    def Case_Read_By(Filtros, Pagina):
        Auth_Data, Error = Validar_JWT()
        if Error:
            if Error in ["Token expirado", "Token inválido"]:
                return jsonify({"Error": Error}), 401
            return jsonify({"Error": Error}), 400
        User_ID = Auth_Data["user_id"]

        Casos = Case_Service.Read_By(Filtros, User_ID, Pagina)
        Datos_Obtener = Case_Service.Obtener_Datos(User_ID)
        Linea_Tiempo = Case_Service.Linea_Tiempo(User_ID, Casos)        
        if Casos == "Auth":
            return jsonify({"Error": "No Auth"}), 403             
        if not Casos or not Datos_Obtener or not Linea_Tiempo:
            return jsonify({"Error": "No cases found"}), 404
        if not Linea_Tiempo or Linea_Tiempo == "Auth":
            Tiempo_Dict = []
        else:        
            Tiempo_Dict = [T.to_dict2() for T in Linea_Tiempo]    

        return jsonify({"Casos": [C.to_dict2() for C in Casos.items], "Datos": Datos_Obtener, "Linea": Tiempo_Dict, "Paginas_Validas": Casos.pages, "Pagina": Casos.page}), 200
    @staticmethod
    def Case_Update(Case_ID):
        Data = request.get_json()
        if not Data:
            return jsonify({"Error": "No data provided"}), 400
        
        Auth_Data, Error = Validar_JWT()
        if Error:
            if Error in ["Token expirado", "Token inválido"]:
                return jsonify({"Error": Error}), 401
            return jsonify({"Error": Error}), 400
        User_ID = Auth_Data["user_id"]
        
        Data_C = {
            "ID": Data["Caso_Id"],
            "Creacion": Data['Caso_Fecha_Creacion'], 
            "Nombre": Data["Caso_Nombre"], 
            "Descripcion": Data["Caso_Descripcion"], 
            "Afectados": Data["Caso_Afectados"], 
            "Direccion": Data["Caso_Direccion"], 
            "Usuario_Creador_ID": Data["Caso_Usuario_Creador"], 
            "Usuario_Asociado_ID": Data["Caso_Usuario_Cargo"],
            "Incidente_ID": Data["Caso_Incidente"], 
            "Estado_Caso_ID": Data["Caso_Estado"], 
            "Prioridad_ID": Data["Caso_Prioridad"], 
            "Barrio_ID": Data["Caso_Barrio_ID"]
        }            
        Data_C_C = {
            "Caso_ID": Data['Caso_Id'], 
            "Usuario_ID": User_ID, 
            "Mensaje": Data['Caso_Comentario']       
        }
        Data_L = {
            "Barrio": Data['Caso_Barrio_Nombre'],
            "Barrio_ID": Data['Caso_Barrio_ID'],
            "Localidad": Data['Caso_Localidad_Nombre'],
            "Localidad_ID": Data['Caso_Localidad_ID'],
            "Ciudad": Data['Caso_Ciudad_Nombre'],
            "Ciudad_ID": Data['Caso_Ciudad_ID'],
            "Departamento": Data['Caso_Departamento_Nombre'],
            "Departamento_ID": Data['Caso_Departamento_ID']
        }
        if Data.get('Caso_Relacion_Radicado') and Data.get("Caso_Relacion_Tipo"):
            Data_R = {
                "Relacion_Radicado": Data['Caso_Relacion_Radicado'],
                "Relacion_Tipo": Data['Caso_Relacion_Tipo']
            }
        else:
            Data_R = {}

        Caso = Case_Service.Update(Case_ID, Data_C, Data_C_C, Data_L, Data_R, User_ID)
        if Caso == "Auth":
            return jsonify({"Error": "No Auth"}), 403   
        if not Caso:
            return jsonify({"Error": "No case found"}), 404
        
        return jsonify({"Message": "Case updated successfully"}), 200
    @staticmethod
    def Case_Delete(Case_ID, User_ID):
        Auth_Data, Error = Validar_JWT()
        if Error:
            if Error in ["Token expirado", "Token inválido"]:
                return jsonify({"Error": Error}), 401
            return jsonify({"Error": Error}), 400
        User_ID2 = Auth_Data["user_id"]        
        
        Caso = Case_Service.Delete(Case_ID, User_ID, User_ID2)
        if Caso == "Auth":
            return jsonify({"Error": "No Auth"}), 403
        if not Caso:
            return jsonify({"Error": "No case found"}), 404

        return jsonify({"Message": "Case deleted successfully"}), 200      
    @staticmethod
    def Delete_Relacion(CasePadre_Rad, CasoHijo_Rad, Tipo_Relacion, User_ID):
        Caso = Case_Service.Delete_Relacion(CasePadre_Rad, CasoHijo_Rad, Tipo_Relacion, User_ID)
        if not Caso:
            return jsonify({"Error": "No relation found"}), 404
        return jsonify({"Message": "Relation deleted successfully"}), 200      
    @staticmethod
    def Estadisticas():
        Auth_Data, Error = Validar_JWT()
        if Error:
            if Error in ["Token expirado", "Token inválido"]:
                return jsonify({"Error": Error}), 401
            return jsonify({"Error": Error}), 400
        User_ID = Auth_Data["user_id"]

        Data = Case_Service.Obtener_Estadisticas(User_ID)

        if Data == "Auth":   
            return jsonify({"Error": "No Auth"}), 403    
        elif not Data:
            return jsonify({"Error": "No data found"}), 404
        return jsonify(Data), 200  
    @staticmethod
    def Exportar_Excel():
        Auth_Data, Error = Validar_JWT()
        if Error:
            if Error in ["Token expirado", "Token inválido"]:
                return jsonify({"Error": Error}), 401
            return jsonify({"Error": Error}), 400
        User_ID = Auth_Data["user_id"]

        Excel  = Case_Service.Exportar_Exel(User_ID)

        if Excel == "Auth":
            return jsonify({"Error": "No Auth"}), 403
        elif not Excel:
            return jsonify({"Error": "No data found"}), 404
        
        Hoy = date.today().strftime("%d-%m-%Y")

        return send_file(Excel, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", as_attachment=True, download_name=f"Reporte_Casos_{Hoy}.xlsx")