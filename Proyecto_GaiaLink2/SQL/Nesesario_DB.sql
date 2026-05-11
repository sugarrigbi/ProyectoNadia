INSERT INTO Estado_Entidad (Nombre)
VALUES
    ('Activa'),
    ('Inactiva'),
    ('Suspendida'),
    ('Eliminada');

INSERT INTO Prioridad (Prioridad)
VALUES
    ('Muy Baja'),
    ('Baja'),
    ('Media'),
    ('Alta'),
    ('Critica');

INSERT INTO Incidente (Incidente, Prioridad_ID)
VALUES
    ('Desplazamiento', 3),
    ('Predios Despojados', 5),
    ('Expropiacion', 4),
    ('Hurto', 2);    

INSERT INTO Entidad (Nombre, Direccion, Telefono, Website, Descripcion, Incidente_ID, Estado_Entidad_ID)
VALUES
    ("Empresa de Acueducto", "Av. Central #45-10", "6011234567", "www.acueducto.com", "Entidad encargada del suministro de agua", 2, 1),
    ("Unidad de Restitución de Tierras", "Calle 26 #13-19", "6017456789", "www.restituciondetierras.gov.co", "Entidad encargada de la restitución de predios despojados", 2, 1),
    ("Instituto Colombiano de Bienestar", "Av. 68 #64-01", "6013456789", "www.icbf.gov.co", "Entidad de apoyo a familias desplazadas", 1, 2),
    ("Agencia Nacional de Tierras",	"Cra. 10 #16-82", "6014567890",	"www.ant.gov.co", "Gestión de procesos de expropiación rural", 3, 1),
    ("Policía Nacional", "Av. El Dorado #75-25", "6015678901", "www.policia.gov.co", "Entidad encargada de atender casos de hurto",	4, 3),
    ("Defensoría del Pueblo", "Calle 55 #10-32", "6016789012", "www.defensoria.gov.co",	"Entidad de defensa de derechos en casos de desplazamiento", 1, 4),
    ("Superintendencia de Notariado", "Cra. 9 #14-31", "6017890123", "www.supernotariado.gov.co", "Entidad de control en procesos de predios despojados", 2, 3);

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

INSERT INTO Estado_Dispositivo(Nombre)
VALUES
    ('Activo'),
    ('Inactivo'),
    ('Eliminado');

INSERT INTO Estado_Usuario(Nombre)
VALUES
    ('Activo'),
    ('Inactivo'),
    ('Suspendido'),
    ('Bloqueado'),
    ('Eliminado');

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

INSERT INTO Rol (Nombre) 
VALUES
    ("Administrador"),
    ("Lider"),
    ("Analista"),
    ("Auxiliar"),
    ("Revisor"),
    ("Usuario");

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

INSERT INTO Tipo_Documento (Nombre, Abreviatura) 
VALUES 
    ("Cedula de Ciudadania","CC"),
    ("Cedula de Extranjeria","CE"), 
    ("Pasaporte","PA"), 
    ("Tarjeta de Identidad","TI"), 
    ("Registro Civil","RC"); 

INSERT INTO Tipo_Formulario (Nombre)
VALUES
    ('Calificanos'),
    ('Ayuda'),
    ('Contactanos');

INSERT INTO Tipo_Relacion (Nombre) 
VALUES
    ('Relacionado'),
    ('Duplicado'),
    ('Dependiente'),
    ('Eliminado');