#PERSONAS
INSERT INTO Rol (Nombre) 
VALUES
    ("Administrador"), 
    ("Usuario");

INSERT INTO Permiso (Permiso) 
VALUES
    ('CREAR_USUARIO'),
    ('EDITAR_USUARIO'),
    ('ELIMINAR_USUARIO'),
    ('VER_USUARIO'),
    ('CREAR_CASO'),
    ('EDITAR_CASO'),
    ('ELIMINAR_CASO'),
    ('VER_CASO'),
    ('ASIGNAR_ROL'),
    ('GESTIONAR_PERMISOS');

INSERT INTO Estado_Usuario (Nombre) 
VALUES 
    ("Activo"), 
    ("Inactivo"), 
    ("Suspendido"), 
    ("Bloqueado"), 
    ("Eliminado");

INSERT INTO Estado_Dispositivo (Nombre) 
VALUES 
    ("Activo"), 
    ("Inactivo"), 
    ("Eliminado");

INSERT INTO Tipo_Documento (Nombre, Abreviatura) 
VALUES 
    ("Cedula de Ciudadania","CC"),
    ("Cedula de Extranjeria","CE"), 
    ("Pasaporte","PA"), 
    ("Tarjeta de Identidad","TI"), 
    ("Registro Civil","RC");

INSERT INTO Pais (Nombre) 
VALUES 
    ("Colombia");

INSERT INTO Departamento (Nombre, Pais_ID) 
VALUES 
    ("Bogota D.C", 1);

INSERT INTO Ciudad (Nombre, Departamento_ID) 
VALUES 
    ("Bogota", 1);

INSERT INTO Localidad (Nombre, Ciudad_ID) 
VALUES 
    ("Rafael Uribe Uribe", 1);

INSERT INTO Usuario (Nombre, Correo, Contraseña, Estado_Usuario_ID, Rol_ID) 
VALUES 
    ("Administrador", "Administrador@gaialink.online", "Admin123*", 1, 1);

INSERT INTO Usuario_Auditoria (Accion, Modificado_Por, Usuario_ID)
VALUES
    ("Creacion de Usuario", 1, 1);

INSERT INTO Persona (Tipo_Documento_ID, Documento, Primer_Nombre, Segundo_Nombre, Primer_Apellido, Segundo_Apellido, Direccion, Telefono, Terminos_Condiciones, Fecha_Nacimiento, Usuario_ID, Barrio_ID)
VALUES
    (1, "1111111111", "Administrador", "Administrador", "Administrador", "Administrador", "Dg Admin #13-20", "3011111111", 1, '1999-09-09', 1, 1);

INSERT INTO Persona_Auditoria (Accion, Modificado_Por, Persona_ID)
VALUES 
    ("Creacion de Persona", 1, 1);

INSERT INTO Dispositivos (IP, Token, Navegador, Sistema, Dispositivo, Ultimo_Uso, Estado_Dispositivo_ID, Usuario_ID)
VALUES
    ("192.168.0.1", "AS73Uj4$j58kY789kIy89", "Brave", "Android 16", "Tablet", "1999-09-09", 1, 1);

INSERT INTO Dispositivos_Auditoria (Accion, Modificado_Por, Dispositivos_ID)
VALUES 
    ("Creacion de DDispositivo", 1, 1);
#Formularios
INSERT INTO Tipo_Formulario (Nombre)
VALUES
    ('Calificanos'),
    ('Ayuda'),
    ('Contactanos');

INSERT INTO Contactanos (Nombre, Telefono, Correo, Mensaje, Tipo_Formulario_ID)
VALUES 
    ('Juan Perez', '3011234567', 'juan@email.com', 'Deseo más información sobre el servicio.', 3);
#Casos
INSERT INTO Estado_Caso(Nombre)
VALUES
    ('Caso Pendiente'),
    ('Caso Activo'),
    ('Caso Resuelto'),
    ('Caso Eliminado'),
    ('En espera del usuario'),
    ('Escalado a supervisor'),
    ('Caso Reabierto');

INSERT INTO Prioridad (Prioridad)
VALUES
    ('Muy Baja'),
    ('Baja'),
    ('Media'),
    ('Alta'),
    ('Critica');

INSERT INTO Incidente (Incidente, Prioridad_ID)
VALUES
    ('Desplazamiento', 5),
    ('Predios Despojados', 5),
    ('Expropiacion', 4),
    ('Hurto', 3);

INSERT INTO Caso_Auditoria (Accion, Modificado_Por, Caso_ID) 
VALUES 
    ('Creacion del caso', 1, 1);

INSERT INTO Radicado_Caso (Radicado, Caso_ID) 
VALUES 
    ('RAD-2026-0001', 1);
#Entidad
INSERT INTO Estado_Entidad (Nombre)
VALUES
    ('Activa'),
    ('Inactiva'),
    ('Suspendida'),
    ('Eliminada');

INSERT INTO Entidad (Nombre, Direccion, Telefono, Website, Descripcion, Incidente_ID, Estado_Entidad_ID)
VALUES 
    ('Empresa de Acueducto', 'Av. Central #45-10', '6011234567', 'www.acueducto.com', 'Entidad encargada del suministro de agua.', 1, 1);

INSERT INTO Entidad_Auditoria (Accion, Modificado_Por, Entidad_ID)
VALUES 
    ('Creacion de entidad', 1, 1);

INSERT INTO Tipo_Relacion (Nombre) 
VALUES
    ('Relacionado'),
    ('Duplicado'),
    ('Dependiente');

INSERT INTO Casos_a_Casos (Caso_Principal_ID, Caso_Asociado_ID, Tipo_Relacion_ID)
VALUES
    (1, 2, 1),
    (1, 3, 2);

INSERT INTO Caso_Discusion (Caso_ID, Usuario_ID, MENSAJE)
VALUES
    (1, 1, 'Este caso requiere seguimiento inmediato.'),
    (1, 1, 'Se notificó al usuario sobre el cambio de estado.'),
    (2, 1, 'El afectado reportó más detalles sobre la dirección.'),
    (3, 1, 'Este caso parece duplicado del principal.'),
    (4, 1, 'El usuario solicitó actualización del estado.'),
    (4, 1, 'Se notificó al usuario vía correo.'),
    (7, 1, 'Este caso no tiene relación con otros, pero requiere validación.');


/*NO NESESARIOS*/

INSERT INTO Ayuda (Nombre, Correo, Soporte, Tipo_Formulario_ID)
VALUES 
    ('Administrador', 'administrador@gaialink.online', 'Problemas con la aplicación móvil', 2);

INSERT INTO Barrio (Nombre, Localidad_ID) 
VALUES 
    ("Santa Lucia", 1);

INSERT INTO Calificanos (Pregunta1, Pregunta2, Pregunta3, Pregunta4, Tipo_Formulario_ID)
VALUES 
    ('Admin1_1', 'Admin1_2', 'Admin1_3', 'Admin1_4', 1);

INSERT INTO Caso (Nombre, Descripcion, Afectados, Direccion, Caso_Asociado, Usuario_Creador_ID, Usuario_Asociado_ID, Incidente_ID, Estado_Caso_ID, Prioridad_ID, Barrio_ID) 
VALUES 
    ('Caso1','Caso principal con dos asociados', 10, 'Carrera 5 #10-20', 'SI', 1, 1, 1, 1, 1, 1),
    ('Caso2','Caso asociado 1', 5, 'Calle 8 #12-30', 'NO', 1, 1, 1, 1, 1, 1),
    ('Caso3','Caso asociado 2', 7, 'Avenida 20 #25-40', 'NO', 1, 1, 1, 1, 1, 1),
    ('Caso4','Caso del mismo usuario 1', 12, 'Calle 50 #60-70', 'NO', 1, 1, 2, 2, 2, 1),
    ('Caso5','Caso del mismo usuario 2', 15, 'Carrera 15 #20-25', 'NO', 1, 1, 2, 2, 2, 1),
    ('Caso6','Caso del mismo usuario 3', 20, 'Diagonal 30 #40-50', 'NO', 1, 1, 2, 2, 2, 1),
    ('Caso7','Caso independiente sin asociados', 8, 'Transversal 12 #34-56', 'NO', 1, 1, 3, 3, 3, 1);


























