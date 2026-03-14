from App.Utilities.Tables import db
from App.Models.Case_Models import Caso as Tabla_Caso

class Case_Service():
    @staticmethod
    def Create(Data):
        Caso = Tabla_Caso(**Data)
        db.session.add(Caso)
        db.session.commit()
        return Caso
    @staticmethod
    def Read_All():
        Casos = Tabla_Caso.query.order_by(Tabla_Caso.ID.asc()).all()
        return Casos
    @staticmethod
    def Read_One(Case_ID):
        Caso = Tabla_Caso.query.get(Case_ID)

        if not Caso:
            return False

        return Caso
    @staticmethod
    def Read_By(Field, Value):
        if not hasattr(Tabla_Caso, Field):
            return False
        Column = getattr(Tabla_Caso, Field)
        Casos = Tabla_Caso.query.filter(Column.ilike(f"%{Value}%")).all()
        return Casos
    @staticmethod
    def Update(Case_ID, Data):
        Caso = Tabla_Caso.query.get(Case_ID)
        if not Caso:
            return False
        for Key, Value in Data.items():
            if Value not in (None, "") and hasattr(Caso, Key):
                setattr(Caso, Key, Value)
        db.session.commit()
        return Caso
    @staticmethod
    def Delete(Case_ID):
        Caso = Tabla_Caso.query.get(Case_ID)

        if not Caso:
            return False
        
        Caso.Estado_Caso_ID = 4
        db.session.commit()

        return Caso