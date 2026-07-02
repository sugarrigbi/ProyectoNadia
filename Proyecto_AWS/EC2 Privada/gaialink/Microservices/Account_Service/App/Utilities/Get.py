from App.Services.Account_Logic import Account_Service
from flask import Response, jsonify, request
from App.Utilities.Util import Validar_JWT
import json

class Get_Account:
    @staticmethod
    def Device_Delete(Device_ID):
        Auth_Data, Error = Validar_JWT()
        if Error:
            if Error in ["Token expirado", "Token invalido"]:
                return jsonify({"Error": Error}), 401
            return jsonify({"Error": Error}), 400
        User_ID = Auth_Data["user_id"]

        Dispositivo = Account_Service.Delete_Device(User_ID, Device_ID)
        if Dispositivo == "Auth":
            return jsonify({"Error": "No auth"}), 403
        if not Dispositivo:
            return jsonify({"Error": "No device found"}), 404
        
        return jsonify({"Message": "Device deleted successfully"}), 200
    @staticmethod
    def Cambiar_Mfa():
        Auth_Data, Error = Validar_JWT()
        if Error:
            if Error in ["Token expirado", "Token invalido"]:
                return jsonify({"Error": Error}), 401
            return jsonify({"Error": Error}), 400
        User_ID = Auth_Data["user_id"]

        Mfa = Account_Service.Cambiar_Mfa(User_ID) 
        if Mfa == "Auth":
            return jsonify({"Error": "No auth"}), 403  
        return jsonify({"Status": Mfa}), 200                
    @staticmethod
    def Read_Data():
        Auth_Data, Error = Validar_JWT()
        if Error:
            if Error in ["Token expirado", "Token invalido"]:
                return jsonify({"Error": Error}), 401
            return jsonify({"Error": Error}), 400
        User_ID = Auth_Data["user_id"] 

        Persona, Dispositivos, Data = Account_Service.Read_Data(User_ID)

        return Response(json.dumps({"usuario": Persona.to_dict2(),"dispositivos": [D.to_dict() for D in Dispositivos], "datos": Data},ensure_ascii=False, indent=2), status=200, mimetype='application/json')
    @staticmethod
    def Cambiar_Personal():
        Data = request.get_json()

        Auth_Data, Error = Validar_JWT()
        if Error:
            if Error in ["Token expirado", "Token invalido"]:
                return jsonify({"Error": Error}), 401
            return jsonify({"Error": Error}), 400
        User_ID = Auth_Data["user_id"]     

        Persona = Account_Service.Cambiar_Personal(User_ID, Data)
        if Persona == "Auth":
            return jsonify({"Error": "No Auth"}), 403
        if Persona == "Documento":
            return jsonify({"Error": "El documento ya existe"}), 400
        if Persona == "Edad":
            return jsonify({"Error": "No cumple con la edad requerida"}), 400
        if not Persona:
            return jsonify({"Error": "No person found"}), 404

        return jsonify({"Message": "Person updated successfully"}), 200
    @staticmethod
    def Cambiar_Ubicacion():
        Data = request.get_json()

        Auth_Data, Error = Validar_JWT()
        if Error:
            if Error in ["Token expirado", "Token invalido"]:
                return jsonify({"Error": Error}), 401
            return jsonify({"Error": Error}), 400
        User_ID = Auth_Data["user_id"]    

        Persona = Account_Service.Cambiar_Ubicacion(User_ID, Data)
        if Persona == "Auth":
            return jsonify({"Error": "No Auth"}), 403
        if not Persona:
            return jsonify({"Error": "No person found"}), 404
        
        return jsonify({"Message": "Person updated successfully"}), 200
    @staticmethod
    def Cambiar_Contraseña():
        Data = request.get_json()

        Auth_Data, Error = Validar_JWT()
        if Error:
            if Error in ["Token expirado", "Token invalido"]:
                return jsonify({"Error": Error}), 401
            return jsonify({"Error": Error}), 400
        User_ID = Auth_Data["user_id"]
        Device_ID = Auth_Data["session_id"]

        Persona = Account_Service.Cambiar_Contraseña(User_ID, Device_ID, Data)
        if not Persona:
            return jsonify({"Error": "No person found"}), 404
        elif Persona == "Auth":
            return jsonify({"Error": "No Auth"}), 403  
        elif Persona == "Correcto":
            return jsonify({"Message": "Password updated successfully"}), 200        
        else:
            return jsonify({"Error": Persona}), 400     
    @staticmethod
    def Cambiar_Imagen():
        Imagen = request.files.get("imagen_usuario")

        Auth_Data, Error = Validar_JWT()
        if Error:
            if Error in ["Token expirado", "Token invalido"]:
                return jsonify({"Error": Error}), 401
            return jsonify({"Error": Error}), 400
        User_ID = Auth_Data["user_id"]

        Respuesta = Account_Service.Cambiar_Imagen(User_ID, Imagen)
        if not Respuesta:        
            return jsonify({"Error": "No user found"}), 404
        elif Respuesta == "Auth":
            return jsonify({"Error": "No Auth"}), 403  
        else:
            return jsonify({"Nombre_Nuevo": Respuesta}), 200
    @staticmethod
    def Eliminar_Imagen():
        Auth_Data, Error = Validar_JWT()
        if Error:
            if Error in ["Token expirado", "Token invalido"]:
                return jsonify({"Error": Error}), 401
            return jsonify({"Error": Error}), 400
        User_ID = Auth_Data["user_id"]        

        Respuesta = Account_Service.Eliminar_Imagen(User_ID)
        if not Respuesta:        
            return jsonify({"Error": "No user found"}), 404
        elif Respuesta == "Auth":
            return jsonify({"Error": "No Auth"}), 403  
        elif Respuesta == "Correcto":
            return jsonify({"Message": "User image deleted successfully"}), 200
        else:
            return jsonify({"Error": Respuesta}), 400      
    @staticmethod
    def Delete_All_Devices():
        Auth_Data, Error = Validar_JWT()
        if Error:
            if Error in ["Token expirado", "Token invalido"]:
                return jsonify({"Error": Error}), 401
            return jsonify({"Error": Error}), 400
        User_ID = Auth_Data["user_id"] 

        Respuesta = Account_Service.Delete_All_Device(User_ID) 
        if not Respuesta:        
            return jsonify({"Error": "No user found"}), 404
        elif Respuesta == "Auth":
            return jsonify({"Error": "No Auth"}), 403  
        else:
            return jsonify({"Message": "All devices deleted successfully"}), 200        
    @staticmethod
    def Delete_Account():
        Auth_Data, Error = Validar_JWT()
        if Error:
            if Error in ["Token expirado", "Token invalido"]:
                return jsonify({"Error": Error}), 401
            return jsonify({"Error": Error}), 400
        User_ID = Auth_Data["user_id"] 

        Respuesta = Account_Service.Delete_Account(User_ID)   
        if not Respuesta:        
            return jsonify({"Error": "No user found"}), 404
        elif Respuesta == "Auth":
            return jsonify({"Error": "No Auth"}), 403  
        else:
            return jsonify({"Message": "Account deleted successfully"}), 200                            