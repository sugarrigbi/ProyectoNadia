from flask import Blueprint, render_template
from app.utilities.Route.routes import get_grafico
routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/grafico/<doc_id>', methods=['GET'])
def grafico(doc_id):
    return get_grafico(doc_id) 
