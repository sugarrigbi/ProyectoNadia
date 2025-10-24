from flask import render_template
from app.utilities.Persona import obtener_persona_por_doc
 
def get_grafico(doc_id):
    resultado = obtener_persona_por_doc(doc_id)
    if not resultado:
        return render_template("error.html", mensaje="Usuario no encontrado")
    
    return render_template("grafico.html", persona=resultado)