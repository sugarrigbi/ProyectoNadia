from App.Models.Forms_Models import Ayuda, Contactanos
from App.Utilities.Tables import db
import requests
import os

class Forms_Service:
    @staticmethod
    def Form_Create(Tabla_Form, Data):
        Formulario = Tabla_Form(**Data)
        
        db.session.add(Formulario)
        db.session.commit()

        if Tabla_Form == Ayuda:
            Formulario_Text = "Ayuda"
        if Tabla_Form == Contactanos:
            Formulario_Text = "Contactanos"

        if Tabla_Form == Ayuda or Tabla_Form == Contactanos:
            requests.post(os.getenv("EMAIL_SERVICE"),
                json={
                    "Template": "Crear_Formulario",
                    "Datos": {"Nombre": Data["Nombre"], "Formulario": Formulario_Text},
                    "Correo": Data["Correo"],
                    "Asunto": "Envio de Formulario"
                }
            )

        return Formulario 
    @staticmethod
    def Form_Delete(Tabla_Form, ID):
        Formulario = Tabla_Form.query.get(ID)
        db.session.delete(Formulario)
        db.session.commit()
        return Formulario
    @staticmethod
    def Form_Read_All(Tabla_Form):
        Formularios = Tabla_Form.query.order_by(Tabla_Form.ID.asc()).all()
        return Formularios     
    @staticmethod
    def Form_Read_One(Tabla_Form,Forms_ID):
        Formulario = Tabla_Form.query.get(Forms_ID)
        if not Formulario:
            return False
        return Formulario
    @staticmethod
    def Form_Read_By(Tabla_Form, Field, Value):
        if not hasattr(Tabla_Form, Field):
            return False
        Column = getattr(Tabla_Form, Field)
        Formularios = Tabla_Form.query.filter(Column.ilike(f"%{Value}%")).all()
        return Formularios    
