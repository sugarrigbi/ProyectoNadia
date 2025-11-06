from flask import Blueprint, session
from app.utilities.Route.Admin import get_buscar_casos_admin, get_crear_casos_admin, get_modificar_buscar_casos_admin, get_modificar_enviar_casos_admin, get_eliminar_casos_admin, get_buscar_entidades_admin, get_crear_entidades_admin
admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/dashboard/admin/casos/buscar", methods=["GET"])
def Buscar_Caso_Admin(): 
    return get_buscar_casos_admin()
@admin_bp.route("/dashboard/admin/casos/crear", methods=["GET", "POST"])
def Crear_Caso_Admin():
    return get_crear_casos_admin()
@admin_bp.route('/dashboard/admin/casos/modificar', methods=["POST"])
def Modificar_Caso_Admin():
    return get_modificar_buscar_casos_admin()
@admin_bp.route('/dashboard/admin/casos/modificar/enviar',methods=["GET", "POST"])
def Modificar_Caso_Enviar_Admin():
    return get_modificar_enviar_casos_admin()
@admin_bp.route('/dashboard/admin/casos/eliminar',methods=["POST"])
def Eliminar_Caso_Admin():
    return get_eliminar_casos_admin()
@admin_bp.route('/dashboard/admin/entidades/buscar',methods=["GET"])
def Buscar_Entidad_Admin():
    return get_buscar_entidades_admin()
@admin_bp.route('/dashboard/admin/entidades/crear', methods=["GET", "POST"])
def Crear_Entidad_Admin():
    return get_crear_entidades_admin()
@admin_bp.route('/dashboard/admin/entidades/modificar', methods=["POST"])
def Modificar_Entidad_Admin():
    return get_modificar_buscar_entidades_admin()





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