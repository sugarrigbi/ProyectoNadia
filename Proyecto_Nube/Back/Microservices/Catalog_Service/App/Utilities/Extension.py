from flask_sqlalchemy import SQLAlchemy
from flask import Response, json
from sqlalchemy.inspection import inspect
db = SQLAlchemy()

class Base_Model(db.Model):
    __abstract__ = True
    
    def to_dict(self):
        data = {}

        mapper = inspect(self.__class__)

        for column in mapper.columns:
            value = getattr(self, column.key)
            data[column.key] = value if value is not None else ""

        for relationship in mapper.relationships:
            rel_value = getattr(self, relationship.key)

            if rel_value is None:
                data[relationship.key] = None

            elif relationship.uselist is False:
                if hasattr(rel_value, "Name"):
                    data[relationship.key] = rel_value.Name
                elif hasattr(rel_value, "Title"):
                    data[relationship.key] = rel_value.Title
                elif hasattr(rel_value, "Category_Name"):
                    data[relationship.key] = rel_value.Category_Name                    
                elif hasattr(rel_value, "Publisher_Name"):
                    data[relationship.key] = rel_value.Publisher_Name        
                else:
                    data[relationship.key] = rel_value.id if hasattr(rel_value, "id") else None

            else:
                items = []
                for item in rel_value:
                    if hasattr(item, "First_Name") and hasattr(item, "Last_Name"):
                        first = getattr(item, "First_Name") or ""
                        last = getattr(item, "Last_Name") or ""
                        items.append((first + " " + last).strip())
                    elif hasattr(item, "Name"):
                        items.append(item.Name)
                    elif hasattr(item, "Title"):
                        items.append(item.Title)
                    else:
                        items.append(str(item))
                data[relationship.key] = ", ".join(items)

        return data