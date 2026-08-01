INSERT INTO Tipo_Formulario (Nombre)
VALUES
    ('Calificanos'),
    ('Ayuda'),
    ('Contactanos');

INSERT INTO Calificanos (Pregunta1, Pregunta2, Pregunta3, Pregunta4, Tipo_Formulario_ID)
VALUES 
    (1, 5, 1, 'La plataforma me ayudo con mi caso', 1);

INSERT INTO Ayuda (Nombre, Correo, Soporte, Tipo_Formulario_ID)
VALUES 
    ('Administrador', 'administrador@gaialink.online', 'Problemas con la aplicación móvil', 2);    

INSERT INTO Contactanos (Nombre, Telefono, Correo, Mensaje, Tipo_Formulario_ID)
VALUES 
    ('Juan Perez', '3011234567', 'juan@email.com', 'Deseo más información sobre el servicio.', 3);

INSERT INTO Pais (Nombre) 
VALUES 
    ("Colombia");

INSERT INTO Departamento (Nombre, Pais_ID) 
VALUES 
    ("Cundinamarca", 1);

INSERT INTO Ciudad (Nombre, Departamento_ID) 
VALUES 
    ("Bogota D.C", 1);

INSERT INTO Localidad (Nombre, Ciudad_ID) 
VALUES 
    ("Rafael Uribe Uribe", 1);

INSERT INTO Barrio (Nombre, Localidad_ID) 
VALUES 
    ("Santa Lucia", 1);    

INSERT INTO Estado_Usuario(Nombre)
VALUES
    ('Activo'),
    ('Inactivo'),
    ('Suspendido'),
    ('Bloqueado'),
    ('Eliminado');

INSERT INTO Rol (Nombre) 
VALUES
    ("Administrador"),
    ("Lider"),
    ("Analista"),
    ("Auxiliar"),
    ("Revisor"),
    ("Usuario");

INSERT INTO Permiso(Nombre)
VALUES
    ('caso_crear'),
    ('caso_ver'),
    ('caso_editar'),
    ('caso_eliminar'),
    ('caso_ver_propio'),
    ('caso_relacionar'),
    ('caso_desrelacionar'),
    ('caso_modificar_estado'),
    ('caso_modificar_direccion'),
    ('caso_asignar_usuario'),
    ('caso_ver_linea_tiempo'),
    ('caso_comentar'),
    ('caso_crear_propio'),
    ('entidad_crear'),
    ('entidad_ver'),
    ('entidad_editar'),
    ('entidad_eliminar'),
    ('health_check'),
    ('dispositivo_ver'),
    ('dispositivo_eliminar'),
    ('estadisticas_ver'),
    ('cuenta_ver');    

INSERT INTO Rol_A_Permiso (Rol_ID, Permiso_ID)
VALUES
    (1,1),
    (1,2),
    (1,3),
    (1,4),
    (1,6),
    (1,7),
    (1,8),
    (1,9),
    (1,10),
    (1,11),
    (1,12),
    (2,1),
    (2,2),
    (2,3),
    (2,4),
    (2,6),
    (2,7),
    (2,8),
    (2,10),
    (2,11),
    (2,12),
    (3,1),
    (3,2),
    (3,3),
    (3,6),
    (3,7),
    (3,8),
    (3,10),
    (3,11),
    (3,12),
    (4,1),
    (4,2),
    (4,3),
    (4,6),
    (4,7),
    (4,11),
    (4,12),
    (5,2),
    (5,11),
    (6,13),
    (6,5),
    (1,14),
    (1,15),
    (1,16),
    (1,17),
    (2,14),
    (2,15),
    (2,16),
    (2,17),
    (3,14),
    (3,15),
    (3,16),
    (4,15),
    (5,15),
    (1,18),
    (2,18),
    (3,18),
    (1,19),
    (2,19),
    (3,19),
    (4,19),
    (5,19),
    (6,19),
    (1,20),
    (2,20),
    (3,20),
    (4,20),
    (5,20),
    (6,20),
    (1,21),
    (2,21),
    (3,21),
    (5,21),
    (1,22),
    (2,22),
    (3,22),
    (4,22),
    (5,22),
    (6,22);

INSERT INTO Usuario (Nombre, Correo, Contraseña, Estado_Usuario_ID, Rol_ID)
VALUES
    ("Administrador", "Administrador@gaialink.online", "$2b$12$oQdxiCVMY9AioqBK4BPQZ.lsoVN86442m4weat7OvnXE/B42YVzPS", 1, 1)

INSERT INTO Usuario_Auditoria (Accion, Modificado_Por, Usuario_ID)
VALUES
    ("Creacion de Usuario", 1, 1)

INSERT INTO Tipo_Documento (Nombre, Abreviatura) 
VALUES 
    ("Cedula de Ciudadania","CC"),
    ("Cedula de Extranjeria","CE"), 
    ("Pasaporte","PA"), 
    ("Tarjeta de Identidad","TI"), 
    ("Registro Civil","RC"); 

INSERT INTO Persona (Tipo_Documento_ID, Documento, Primer_Nombre, Segundo_Nombre, Primer_Apellido, Segundo_Apellido, Direccion, Telefono, Terminos_Condiciones, Fecha_Nacimiento, Usuario_ID, Barrio_ID)
VALUES
    (1, "000000000", "Admin", "Admin", "Admin", "Admin", "Dg Admin #13-20", "3011111111", 1, "2000-01-01", 1, 1)

INSERT INTO Persona_Auditoria (Accion, Modificado_Por, Persona_ID)
VALUES
    ("Creacion de Persona", 1, 1)

INSERT INTO Prioridad (Prioridad)
VALUES
    ('Muy Baja'),
    ('Baja'),
    ('Media'),
    ('Alta'),
    ('Critica');

INSERT INTO Estado_Caso(Nombre)
VALUES
    ('Pendiente'),
    ('Activo'),
    ('Resuelto'),
    ('Eliminado'),
    ('En espera del usuario'),
    ('Escalado a supervisor'),
    ('Reabierto'),
    ('En espera del asesor'),
    ('Tomando desicion');   

INSERT INTO Incidente (Incidente, Prioridad_ID)
VALUES
    ('Desplazamiento', 3),
    ('Predios Despojados', 5),
    ('Expropiacion', 4),
    ('Hurto', 2);      

INSERT INTO Caso (Nombre, Descripcion, Afectados, Direccion, Usuario_Creador_ID, Usuario_Asociado_ID, Incidente_ID, Estado_Caso_ID, Prioridad_ID, Barrio_ID)
VALUES
    ("Hurto con violencia", "Robo con intimidacion", 5, "Carrera 24 #15-30", 1, 1, 4, 1, 2, 1)
    ("Predios despojados sur", "Zona sur con multiples despojos", 12, "Calle 70 sur #80-90", 1, 1, 2, 2, 4, 1)

INSERT INTO Caso_Auditoria (Accion, Anterior, Modificado_Por, Caso_ID)
VALUES 
    ("Caso creado", '{"ID":1,"Creacion":"2026-04-25T00:00:00","Nombre":"Hurto con violencia","Descripcion":"Robo con intimidacion","Afectados":5,"Direccion":"Carrera 24 #15-30","Caso_Asociado":"NO","Actualizado_En":"2026-04-25T00:00:00","Usuario_Creador_ID":1,"Usuario_Asociado_ID":1,"Incidente_ID":4,"Estado_Caso_ID":1,"Prioridad_ID":2,"Barrio_ID":1,"usuario_creador":{"ID":1,"Nombre":"Administrador","Correo":"administrador@gaialink.online","Estado_Usuario_ID":1,"Rol_ID":1,"Persona":{"ID":1,"Documento":"1111111111","Primer_Nombre":"Admin","Segundo_Nombre":"","Primer_Apellido":"Admin","Segundo_Apellido":"Admin"}},"usuario_asociado":{"ID":1,"Nombre":"Administrador","Correo":"administrador@gaialink.online","Estado_Usuario_ID":1,"Rol_ID":1,"Persona":{"ID":1,"Documento":"1111111111","Primer_Nombre":"Admin","Segundo_Nombre":"","Primer_Apellido":"Admin","Segundo_Apellido":"Admin"}},"incidente":{"ID":4,"Incidente":"Hurto","Prioridad_ID":2},"estado":{"ID":1,"Nombre":"Pendiente"},"prioridad":{"ID":2,"Prioridad":"Baja"},"barrio":{"ID":1,"Nombre":"Santa Lucia","Localidad":{"ID":1,"Nombre":"Rafael Uribe Uribe","Ciudad":{"ID":1,"Nombre":"Bogota D.C","Departamento":{"ID":1,"Nombre":"Cundinamarca"}}}},"auditorias":[],"radicados":[{"ID":1,"Radicado":"000001R","Caso_ID":1}],"discusiones":[],"casos_asociados":[],"casos_principales":[]}', 1, 1)
    ("Caso creado", '{"ID":2,"Creacion":"2026-04-25T00:00:00","Nombre":"Predios despojados sur","Descripcion":"Zona sur con multiples despojos","Afectados":12,"Direccion":"Calle 70 sur #80-90","Caso_Asociado":"NO","Actualizado_En":"2026-04-25T00:00:00","Usuario_Creador_ID":1,"Usuario_Asociado_ID":1,"Incidente_ID":2,"Estado_Caso_ID":2,"Prioridad_ID":4,"Barrio_ID":1,"usuario_creador":{"ID":1,"Nombre":"Administrador","Correo":"administrador@gaialink.online","Estado_Usuario_ID":1,"Rol_ID":1,"Persona":{"ID":1,"Documento":"1111111111","Primer_Nombre":"Admin","Segundo_Nombre":"","Primer_Apellido":"Admin","Segundo_Apellido":"Admin"}},"usuario_asociado":{"ID":1,"Nombre":"Administrador","Correo":"administrador@gaialink.online","Estado_Usuario_ID":1,"Rol_ID":1,"Persona":{"ID":1,"Documento":"1111111111","Primer_Nombre":"Admin","Segundo_Nombre":"","Primer_Apellido":"Admin","Segundo_Apellido":"Admin"}},"incidente":{"ID":2,"Incidente":"Predios Despojados","Prioridad_ID":5},"estado":{"ID":2,"Nombre":"Activo"},"prioridad":{"ID":4,"Prioridad":"Alta"},"barrio":{"ID":1,"Nombre":"Santa Lucia","Localidad":{"ID":1,"Nombre":"Rafael Uribe Uribe","Ciudad":{"ID":1,"Nombre":"Bogota D.C","Departamento":{"ID":1,"Nombre":"Cundinamarca"}}}},"auditorias":[],"radicados":[{"ID":2,"Radicado":"000002R","Caso_ID":2}],"discusiones":[],"casos_asociados":[],"casos_principales":[]}', 1, 2)

INSERT INTO Radicado_Caso (Radicado, Caso_ID)
VALUES
    ("000001R", 1)

INSERT INTO Caso_Discusion (Caso_ID, Usuario_ID, MENSAJE)
VALUES
    (1, 1, "Este caso requiere seguimiento inmediato")
    (2, 1, "Este caso se encuentra escalado")

INSERT INTO Tipo_Relacion (Nombre) 
VALUES
    ('Relacionado'),
    ('Duplicado'),
    ('Dependiente'),
    ('Eliminado');

INSERT INTO Casos_A_Casos (Caso_Principal_ID, Caso_Asociado_ID, Tipo_Relacion_ID)
VALUES
    (1, 2, 1)

INSERT INTO Estado_Dispositivo(Nombre)
VALUES
    ('Activo'),
    ('Inactivo'),
    ('Eliminado');

INSERT INTO Dispositivos (IP, Token, Navegador, Sistema, Dispositivo, Ultimo_Uso, Estado_Dispositivo_ID, Usuario_ID)
VALUES
    ("201.244.139.61", "8a30da11fafe39ca7cc82928da5ef03b54ec16f8b8412af40568ae4b0dd80b8b", "Opera 128.0.0", "Windows", "Computador", "2026-03-26 16:28:35", 1, 1)

INSERT INTO dispositivos_auditoria (Accion, Modificado_Por, Dispositivos_ID)
VALUES
    ("Creacion de Dispositivo", 1, 1)

INSERT INTO Estado_Entidad (Nombre)
VALUES
    ('Activa'),
    ('Inactiva'),
    ('Suspendida'),
    ('Eliminada');

INSERT INTO Entidad (Nombre, Direccion, Telefono, Website, Descripcion, Incidente_ID, Estado_Entidad_ID)
VALUES
    ("Empresa de Acueducto", "Av. Central #45-10", "6011234567", "www.acueducto.com", "Entidad encargada del suministro de agua", 2, 1),
    ("Unidad de Restitución de Tierras", "Calle 26 #13-19", "6017456789", "www.restituciondetierras.gov.co", "Entidad encargada de la restitución de predios despojados", 2, 1),
    ("Instituto Colombiano de Bienestar", "Av. 68 #64-01", "6013456789", "www.icbf.gov.co", "Entidad de apoyo a familias desplazadas", 1, 2),
    ("Agencia Nacional de Tierras",	"Cra. 10 #16-82", "6014567890",	"www.ant.gov.co", "Gestión de procesos de expropiación rural", 3, 1),
    ("Policía Nacional", "Av. El Dorado #75-25", "6015678901", "www.policia.gov.co", "Entidad encargada de atender casos de hurto",	4, 3),
    ("Defensoría del Pueblo", "Calle 55 #10-32", "6016789012", "www.defensoria.gov.co",	"Entidad de defensa de derechos en casos de desplazamiento", 1, 4),
    ("Superintendencia de Notariado", "Cra. 9 #14-31", "6017890123", "www.supernotariado.gov.co", "Entidad de control en procesos de predios despojados", 2, 3);

INSERT INTO Entidad_Auditoria (Accion, Anterior, Modificado_Por, entidad_auditoria)
VALUES
    ("Entidad creada", '{"ID":1,"Nombre":"Empresa de Acueducto","Direccion":"Av. Central #45-10","Telefono":"6011234567","Website":"www.acueducto.com","Descripcion":"Entidad encargada del suministro de agua","Incidente_ID":"2","Estado_Entidad_ID":"1"}', 1, 1)
    ("Entidad creada", '{"ID":2,"Nombre":"Unidad de Restitución de Tierras","Direccion":"Calle 26 #13-19","Telefono":"6017456789","Website":"www.restituciondetierras.gov.co","Descripcion":"Entidad encargada de la restitución de predios despojados","Incidente_ID":"2","Estado_Entidad_ID":"1"}', 1, 2)
    ("Entidad creada", '{"ID":3,"Nombre":"Instituto Colombiano de Bienestar","Direccion":"Av. 68 #64-01","Telefono":"6013456789","Website":"www.icbf.gov.co","Descripcion":"Entidad de apoyo a familias desplazadas","Incidente_ID":"1","Estado_Entidad_ID":"2"}', 1, 3)
    ("Entidad creada", '{"ID":4,"Nombre":"Agencia Nacional de Tierras","Direccion":"Cra. 10 #16-82","Telefono":"6014567890","Website":"www.ant.gov.co","Descripcion":"Gestión de procesos de expropiación rural","Incidente_ID":"3","Estado_Entidad_ID":"1"}', 1, 4)
    ("Entidad creada", '{"ID":5,"Nombre":"Policía Nacional","Direccion":"Av. El Dorado #75-25","Telefono":"6015678901","Website":"www.policia.gov.co","Descripcion":"Entidad encargada de atender casos de hurto","Incidente_ID":"4","Estado_Entidad_ID":"3"}', 1, 5)
    ("Entidad creada", '{"ID":6,"Nombre":"Defensoría del Pueblo","Direccion":"Calle 55 #10-32","Telefono":"6016789012","Website":"www.defensoria.gov.co","Descripcion":"Entidad de defensa de derechos en casos de desplazamiento","Incidente_ID":"1","Estado_Entidad_ID":"4"}', 1, 6)
    ("Entidad creada", '{"ID":7,"Nombre":"Superintendencia de Notariado","Direccion":"Cra. 9 #14-31","Telefono":"6017890123","Website":"www.supernotariado.gov.co","Descripcion":"Entidad de control en procesos de predios despojados","Incidente_ID":"2","Estado_Entidad_ID":"3"}', 1, 7)
