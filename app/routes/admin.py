from flask import Blueprint, session
from app.utilities.Route import Admin
admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/dashboard/admin/casos/buscar", methods=["GET"])
def Buscar_Caso_Admin(): 
    return Admin.get_buscar_casos_admin()
@admin_bp.route("/dashboard/admin/casos/crear", methods=["GET", "POST"])
def Crear_Caso_Admin():
    return Admin.get_crear_casos_admin()
@admin_bp.route('/dashboard/admin/casos/modificar', methods=["POST"])
def Modificar_Caso_Admin():
    return Admin.get_modificar_buscar_casos_admin()
@admin_bp.route('/dashboard/admin/casos/modificar/enviar',methods=["GET", "POST"])
def Modificar_Caso_Enviar_Admin():
    return Admin.get_modificar_enviar_casos_admin()
@admin_bp.route('/dashboard/admin/casos/eliminar',methods=["POST"])
def Eliminar_Caso_Admin():
    return Admin.get_eliminar_casos_admin()
@admin_bp.route('/dashboard/admin/entidades/buscar',methods=["GET"])
def Buscar_Entidad_Admin():
    return Admin.get_buscar_entidades_admin()
@admin_bp.route('/dashboard/admin/entidades/crear', methods=["GET", "POST"])
def Crear_Entidad_Admin():
    return Admin.get_crear_entidades_admin()
@admin_bp.route('/dashboard/admin/entidades/modificar', methods=["POST"])
def Modificar_Entidad_Admin():
    return Admin.get_modificar_buscar_entidades_admin()
@admin_bp.route('/dashboard/admin/entidades/modificar/enviar',methods=["GET", "POST"])
def Modificar_Entidad_Enviar_Admin():
    return Admin.get_modificar_enviar_entidades_admin()
@admin_bp.route('/dashboard/admin/entidades/eliminar',methods=["GET", "POST"])
def Eliminar_Entidad_Admin():
    return Admin.get_eliminar_entidades_admin()