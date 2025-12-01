from app.models.Persona import Persona

def obtener_persona_por_doc(doc_id):
    persona = Persona(None, None, doc_id, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
    resultado = persona.Buscar_Persona()
    return resultado  