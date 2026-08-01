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
@admin_bp.route('/dashboard/admin/usuarios/buscar',methods=["GET"])
def Buscar_Usuario_Admin():
    return Admin.get_buscar_usuarios_admin()
@admin_bp.route('/dashboard/admin/usuarios/crear',methods=["GET", "POST"])
def Crear_Usuario_Admin():
    return Admin.get_crear_usuarios_admin()
@admin_bp.route('/dashboard/admin/usuarios/modificar', methods=["POST"])
def Modificar_Usuario_Admin():
    return Admin.get_modificar_buscar_usuarios_admin()
@admin_bp.route('/dashboard/admin/usuarios/modificar/enviar',methods=["GET", "POST"])
def Modificar_Usuario_Enviar_Admin():
    return Admin.get_modificar_enviar_usuarios_admin()
@admin_bp.route('/dashboard/admin/usuarios/eliminar',methods=["GET", "POST"])
def Eliminar_Usuario_Admin():
    return Admin.get_eliminar_usuarios_admin()
@admin_bp.route("/actualizar_2FA", methods=['POST'])
def Actualizar_2FA():
    return Admin.get_actualizar_2fa()
@admin_bp.route("/dashboard/admin/cuenta/dispositivos")
def Buscar_Dispositivos_Admin():
    return Admin.get_buscar_dispositivos()
@admin_bp.route('/dispositivos/eliminar/<id>', methods=["POST"])
def Eliminar_Dispositivo_Admin(id):
    return Admin.get_eliminar_dispositivos(id)
@admin_bp.route('/dashboard/admin/cuenta/datos', methods=["GET"])
def Cuenta_Datos_Admin():
    return Admin.get_cuenta_datos()