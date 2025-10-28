from flask import Blueprint, session
from app.utilities.Route.User import get_crear_caso, get_miscasos, get_entidad, get_misdatos, get_eliminardatos, get_modificardatos1, get_modificardatos2, get_entidades
user_bp = Blueprint("user", __name__)

@user_bp.route("/crear-caso", methods=["GET", "POST"])
def Crear_caso():
    return get_crear_caso()
@user_bp.route("/dashboard/user/casos", methods=["GET"])
def miscasos(): 
    return get_miscasos()
@user_bp.route("/dashboard/user/entidades", methods=["GET"])
def entidades(): 
    return get_entidades()
@user_bp.route('/dashboard/user/entidad/buscar', methods=["POST"])
def buscar_entidad(): 
    return get_entidad()
@user_bp.route('/dashboard/user/persona/datos',methods=["GET"])
def buscar_datos():
    return get_misdatos()
@user_bp.route('/dashboard/user/persona/eliminar',methods=["POST"])
def eliminar_datos():
    return get_eliminardatos()
@user_bp.route('/dashboard/user/persona/modificar',methods=["GET"])
def modificar_datos1():
    return get_modificardatos1()
@user_bp.route('/dashboard/user/persona/modificar/enviar',methods=["POST"])
def modificar_datos2():
    return get_modificardatos2()
