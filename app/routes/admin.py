from flask import Blueprint, session
from app.utilities.Route.Admin import get_miscasos_admin, get_crear_caso_admin
admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/dashboard/admin/casos", methods=["GET"])
def miscasos_admin(): 
    return get_miscasos_admin()
@admin_bp.route("/dashboard/admin/crear-caso", methods=["GET", "POST"])
def Crear_caso():
    return get_crear_caso_admin()
@admin_bp.route("/dashboard/admin/entidades", methods=["GET"])
def entidades(): 
    return get_entidades_admin()
@admin_bp.route('/dashboard/admin/entidad/buscar', methods=["POST"])
def buscar_entidad(): 
    return get_entidad_admin()
@admin_bp.route('/dashboard/admin/persona/datos',methods=["GET"])
def buscar_datos():
    return get_misdatos_admin()
@admin_bp.route('/dashboard/admin/persona/eliminar',methods=["POST"])
def eliminar_datos():
    return get_eliminardatos_admin()
@admin_bp.route('/dashboard/admin/persona/modificar',methods=["GET"])
def modificar_datos1():
    return get_modificardatos1_admin()
@admin_bp.route('/dashboard/admin/persona/modificar/enviar',methods=["POST"])
def modificar_datos2():
    return get_modificardatos2_admin()
@admin_bp.route('/dashboard/admin/persona/modificar/contraseña',methods=["POST"])
def modificar_contraseña():
    return get_modificarcontraseña_admin()