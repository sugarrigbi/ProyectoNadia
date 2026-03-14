from App.Utilities.Tables import db
from App.Models.Entity_Models import Entidad as Tabla_Entidad

class Entity_Service:
    @staticmethod
    def Create(Data):
        Entidad = Tabla_Entidad(**Data)
        db.session.add()
        db.session.commit()

        return Entidad
    @staticmethod
    def Read_All():
        Entidades = Tabla_Entidad.query.order_by(Tabla_Entidad.ID.asc()).all()
        return Entidades
    @staticmethod
    def Read_One(Entity_ID):
        Entidad = Tabla_Entidad.query.get(Entity_ID)
        if not Entidad:
            return False
        return Entidad
    @staticmethod
    def Read_By(Field, Value):
        if hasattr(Tabla_Entidad, Field):
            return False
        Column = getattr(Tabla_Entidad, Field)
        Entidades = Tabla_Entidad.query.filter(Column.ilike(f"%{Value}%")).all()
        return Entidades
    @staticmethod
    def Update(Entity_ID, Data):
        Entidad = Tabla_Entidad.query.get(Entity_ID)

        if not Entidad:
            return False
        
        for Key, Value in Data.items():
            if Value not in (None, "") and hasattr(Entidad, Key):
                setattr(Entidad, Key, Value)
        db.session.commit()
        return Entidad      
    @staticmethod
    def Delete(Entity_ID):
        Entidad = Tabla_Entidad.query.get(Entity_ID)
        if not Entidad:
            return False
        
        Entidad.Estado_Entidad_ID = 4
        db.session.commit()
        return Entidad

