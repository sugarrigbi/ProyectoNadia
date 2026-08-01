import secrets
from user_agents import parse as ua_parse
from flask import session, request
from app.utilities.Base_Datos import Get_BaseDatos, Close_BaseDatos
from datetime import datetime, date

def Crear_Dispositivo():
    token = secrets.token_hex(32)
    usuario = session["usuario_id"]
    session["token_session"] = token
    conexion, cursor = Get_BaseDatos()
    user_agent = ua_parse(request.headers.get("User-Agent"))
    navegador = user_agent.browser.family + " " + (user_agent.browser.version_string or "")
    sistema = user_agent.os.family + " " + (user_agent.os.version_string or "")
    ip = request.remote_addr
    if user_agent.is_mobile:
        dispositivo = "Móvil"
    elif user_agent.is_tablet:
        dispositivo = "Tablet"
    elif user_agent.is_pc:
        dispositivo = "Computador"
    else:
        dispositivo = "Desconocido"
    activo = 1

    cursor.execute("SELECT Id_dispositivo FROM tbl_dispositivos WHERE Fk_usuario = %s AND Navegador = %s AND Dispositivo = %s LIMIT 1", (usuario, navegador, dispositivo))
    resultado = cursor.fetchone()   
    if resultado:
        cursor.execute("UPDATE tbl_dispositivos SET Ultimo_uso = NOW(), IP = %s, Token = %s, Activo = 1 WHERE Id_dispositivo = %s",(ip, token, resultado["Id_dispositivo"]))
        conexion.commit()
        Close_BaseDatos(conexion, cursor)
        return None

    def generar_id(tabla, prefijo, longitud):
        cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
        resultado = cursor.fetchone()
        count = resultado.get('COUNT(*)', 0) if resultado else 0
        return str(count + 1).zfill(longitud) + prefijo      

    Id_dispositivo = generar_id("tbl_dispositivos", "DEV", longitud=3)
    cursor.execute("INSERT INTO tbl_dispositivos (Id_dispositivo, IP, Token, Navegador, Sistema, Dispositivo, Fecha_Inicio, Ultimo_uso, Activo, Fk_usuario) VALUES (%s, %s, %s, %s, %s, %s, NOW(), NOW(), %s, %s)", (Id_dispositivo, ip, token, navegador, sistema, dispositivo, activo, usuario))
    conexion.commit()
    Close_BaseDatos(conexion, cursor)
def Buscar_Dispositivos(Codigo):
    conexion, cursor = Get_BaseDatos()
    fechas = []
    lista_fusionada = []

    cursor.execute("SELECT Id_dispositivo FROM tbl_dispositivos WHERE Fk_usuario = %s ORDER BY Id_dispositivo",(Codigo,))
    Id_dev = cursor.fetchall()
    if not Id_dev:
        Close_BaseDatos(conexion, cursor)
        return "No existen dispositivos", "error"
    
    cursor.execute("SELECT IP FROM tbl_dispositivos WHERE Fk_usuario = %s ORDER BY Id_dispositivo",(Codigo,))
    Ip = cursor.fetchall()
    if not Ip:
        Close_BaseDatos(conexion, cursor)
        return "No existen dispositivos", "error"
    
    cursor.execute("SELECT Token FROM tbl_dispositivos WHERE Fk_usuario = %s ORDER BY Id_dispositivo",(Codigo,))
    Token = cursor.fetchall()
    if not Token:
        Close_BaseDatos(conexion, cursor)
        return "No existen dispositivos", "error"
    
    cursor.execute("SELECT Navegador FROM tbl_dispositivos WHERE Fk_usuario = %s ORDER BY Id_dispositivo",(Codigo,))
    Navegador = cursor.fetchall()
    if not Navegador:
        Close_BaseDatos(conexion, cursor)
        return "No existen dispositivos", "error"
    
    cursor.execute("SELECT Sistema FROM tbl_dispositivos WHERE Fk_usuario = %s ORDER BY Id_dispositivo",(Codigo,))
    Sistema = cursor.fetchall()
    if not Sistema:
        Close_BaseDatos(conexion, cursor)
        return "No existen dispositivos", "error"
    
    cursor.execute("SELECT Dispositivo FROM tbl_dispositivos WHERE Fk_usuario = %s ORDER BY Id_dispositivo",(Codigo,))
    Dispositivo = cursor.fetchall()
    if not Dispositivo:
        Close_BaseDatos(conexion, cursor)
        return "No existen dispositivos", "error"
    
    cursor.execute("SELECT Fecha_Inicio FROM tbl_dispositivos WHERE Fk_usuario = %s ORDER BY Id_dispositivo",(Codigo,))
    Fecha_Inicio = cursor.fetchall()
    if not Fecha_Inicio:
        Close_BaseDatos(conexion, cursor)
        return "No existen dispositivos", "error"
    
    cursor.execute("SELECT Ultimo_uso FROM tbl_dispositivos WHERE Fk_usuario = %s ORDER BY Id_dispositivo",(Codigo,))
    Ultimo_uso = cursor.fetchall()
    if not Ultimo_uso:
        Close_BaseDatos(conexion, cursor)
        return "No existen dispositivos", "error"
    for i in Ultimo_uso:
        hoy = date.today()
        fecha = i["Ultimo_uso"].date()
        fecha_temporal = i["Ultimo_uso"].strftime("%d/%m/%Y")
        hora_temporal = i["Ultimo_uso"].strftime("%H:%M")
        diferencia = (hoy - fecha).days
        if diferencia == 0:
            dato_final = f"{hora_temporal}"
        elif diferencia == 1:
            dato_final = f"Ayer"
        elif 2 <= diferencia <= 7:
            dato_final = f"Hace {diferencia} dias"
        elif 8 <= diferencia <= 30:
            semanas = diferencia // 7
            if semanas == 1:
                dato_final = "Hace 1 semana"
            else:
                dato_final = f"Hace {semanas} semanas"
        elif 30 <= diferencia <= 365:
            meses = diferencia // 30
            if meses == 1:
                dato_final = "Hace 1 mes"
            else:
                dato_final = f"Hace {meses} meses"
        else:
            dato_final = fecha_temporal
        fechas.append(dato_final)
    
    cursor.execute("SELECT Activo FROM tbl_dispositivos WHERE Fk_usuario = %s ORDER BY Id_dispositivo",(Codigo,))
    Activo = cursor.fetchall()
    if not Activo:
        Close_BaseDatos(conexion, cursor)
        return "No existen dispositivos", "error"
    
    for i in range(len(Id_dev)):
        try: 
            dispositivo = {
                "Id_dispositivo": Id_dev[i]["Id_dispositivo"],
                "IP": Ip[i]["IP"],
                "Token": Token[i]["Token"],
                "Navegador": Navegador[i]["Navegador"],
                "Sistema": Sistema[0]["Sistema"],
                "Dispositivo": Dispositivo[i]["Dispositivo"],
                "Fecha_Inicio": Fecha_Inicio[i]["Fecha_Inicio"],
                "Ultimo_uso": fechas[i],
                "Activo": Activo[i]["Activo"],
            }
            if all(dispositivo.values()) and dispositivo["Activo"] == 1:
                lista_fusionada.append(dispositivo)                    
        except Exception as e:
            continue                    
    Close_BaseDatos(conexion, cursor)
    return lista_fusionada
def Eliminar_Dispositivos(Codigo):
    conexion, cursor = Get_BaseDatos()
    try:
        cursor.execute("UPDATE tbl_dispositivos SET Activo = 0, Token = NULL WHERE Id_dispositivo = %s", (Codigo,))
        conexion.commit()
        return True
    except:
        return False
    finally:
        Close_BaseDatos(conexion, cursor)
def obtener_token_actual(id):
    conexion, cursor = Get_BaseDatos()
    cursor.execute("SELECT Token FROM tbl_dispositivos WHERE Id_dispositivo = %s", (id,))
    token_bd = cursor.fetchone()
    Close_BaseDatos(conexion, cursor)   

    return token_bd
def obtener_total_dispositivos(Codigo):
    conexion, cursor = Get_BaseDatos()
    cursor.execute("SELECT COUNT(*) AS dispositivos_totales FROM tbl_dispositivos WHERE Fk_usuario = %s AND Activo = 1",(Codigo,))
    total = cursor.fetchone()
    total_dispositivos = total["dispositivos_totales"]
    Close_BaseDatos(conexion, cursor)

    return total_dispositivos