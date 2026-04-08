INSERT INTO prioridad (Prioridad)
VALUES
    ('Muy Baja'),
    ('Baja'),
    ('Media'),
    ('Alta'),
    ('Critica');
INSERT INTO estado_caso (Nombre)
VALUES
    ('Pendiente'),
    ('Activo'),
    ('Resuelto'),
    ('Eliminado'),
    ('En espera del usuario'),
    ('Escalado a supervisor'),
    ('Reabierto'),
    ('En espera del asesor'),
    ('Tomando desicion ');
INSERT INTO estado_dispositivo (Nombre)
VALUES
    ('Activo'),
    ('Inactivo'),
    ('Eliminado');
INSERT INTO estado_entidad (Nombre)
VALUES
    ('Activa'),
    ('Inactiva'),
    ('Suspendida'),
    ('Eliminada');
INSERT INTO estado_usuario (Nombre)
VALUES
    ('Activo'),
    ('Inactivo'),
    ('Suspendido'),
    ('Bloqueado'),
    ('Eliminado');
INSERT INTO incidente (Incidente, Prioridad_ID)
VALUES
    ('Desplazamiento',4),
    ('Predios Despojados',5),
    ('Expropiacion',2),
    ('Hurto',3);
INSERT INTO permiso (Permiso)
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
    ('caso_crear_propio');
INSERT INTO rol (Nombre)
VALUES
    ('Administrador'),
    ('Lider'),
    ('Analista'),
    ('Auxiliar'),
    ('Revisor'),
    ('Usuario');
INSERT INTO rol_a_permiso (Rol_ID, Permiso_ID)
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
    (6,1),
    (6,5),
    (6,12),
    (6,13);
INSERT INTO tipo_documento (Nombre, Abreviatura)
VALUES       
    ('Cedula de Ciudadania','CC'),
    ('Cedula de Extranjeria','CE'),
    ('Pasaporte','PA'),
    ('Tarjeta de Identidad','TI'),
    ('Registro Civil','RC');
INSERT INTO tipo_formulario (Nombre)
VALUES
    ('Calificanos'),
    ('Ayuda'),
    ('Contactanos');
INSERT INTO tipo_relacion (Nombre)
VALUES    
    ('Relacionado'),
    ('Eliminado'),
    ('Duplicado'),
    ('Dependiente');
INSERT INTO Pais (Nombre)
VALUES
    ('Colombia');