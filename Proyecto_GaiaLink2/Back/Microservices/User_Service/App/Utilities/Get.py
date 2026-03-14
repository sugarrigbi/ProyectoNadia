from flask import Response, request, jsonify, json
from App.Services.User_Logic import User_Service

class Get_User:
    @staticmethod
    def Registro():
        Data = request.get_json()

        Data_U = {
            "Correo": Data["Correo"],
            "Nombre": Data["Nombre"],
            "Contraseña": Data["Contraseña"]
        }
        Data_P = {
            "Primer_Nombre": Data["Primer_Nombre"],
            "Segundo_Nombre": Data["Segundo_Nombre"],
            "Primer_Apellido": Data["Primer_Apellido"],
            "Segundo_Apellido": Data["Segundo_Apellido"],
            "Tipo_Documento_ID": Data["Tipo_Documento_ID"],
            "Documento": Data["Documento"],
            "Fecha_Nacimiento": Data["Fecha_Nacimiento"],
            "Departamento_ID": Data["Departamento_ID"],
            "Ciudad_ID": Data["Ciudad_ID"],
            "Localidad_ID": Data["Localidad_ID"],
            "Barrio_ID": Data["Barrio_ID"],
            "Direccion": Data["Direccion"],
            "Telefono": Data["Telefono"]
        }

        Respuesta = User_Service.Registro(Data_U, Data_P)
        if "Error" in Respuesta:
            return jsonify(Respuesta), 400
        return jsonify(Respuesta), 200
    @staticmethod
    def Create():
        Data = request.get_json()

        Correo = Data["Correo"]
        Codigo = Data["Codigo"]

        Respuesta = User_Service.Create(Correo, Codigo)

        if isinstance(Respuesta, dict) and "Error" in Respuesta:
            return jsonify(Respuesta), 400
        return jsonify({"Message": "Usuario creado"}), 200