INSERT INTO tbl_user_roles (ID, Role_Name) VALUES 
('admin', 'Administrador'), 
('user', 'Usuario');

INSERT INTO tbl_user_states (ID, State_Name) VALUES 
('active', 'Activo'), 
('inactive', 'Inactivo');

INSERT INTO tbl_document_type (ID, Document_Type) VALUES 
('cc', 'Cédula de Ciudadanía'), 
('ti', 'Tarjeta de Identidad');

INSERT INTO tbl_categories (Category_Name) VALUES 
('Ficción'), 
('Ciencia'), 
('Historia');

INSERT INTO tbl_publishers (Publisher_Name) VALUES 
('Editorial Alfa'), 
('Editorial Beta');

INSERT INTO tbl_loan_status (ID, Status_Name) VALUES 
('active', 'Activo'), 
('returned', 'Devuelto');

INSERT INTO tbl_book_status (ID, Status_Name) VALUES 
('available', 'Disponible'), 
('loaned', 'Prestado');

INSERT INTO tbl_penalties_status (ID, Status_Name) VALUES 
('pending', 'Pendiente'), 
('paid', 'Pagado');

INSERT INTO tbl_reservation_status (ID, Status_Name) VALUES 
('reserved', 'Reservado'), 
('cancelled', 'Cancelado');

INSERT INTO tbl_notification_status (ID, Status_Name) VALUES 
('sent', 'Enviado'), 
('read', 'Leído');

-- =========================================
-- 2. Usuarios
-- =========================================
INSERT INTO tbl_user (Username, Password_Hash, Fk_Role, Fk_State) VALUES
('kevin', 'hash123', 'admin', 'active'),
('tatiana', 'hash456', 'user', 'active');

-- =========================================
-- 3. Direcciones
-- =========================================
INSERT INTO tbl_address (Address, Country, City) VALUES
('Calle 123 #45-67', 'Colombia', 'Bogotá'),
('Carrera 89 #12-34', 'Colombia', 'Medellín');

-- =========================================
-- 4. Personas
-- =========================================
INSERT INTO tbl_person (First_Name, First_LastName, Fk_DocumentType, Fk_User, Fk_Address) VALUES
('Kevin', 'Anzola', 'cc', 1, 1),
('Tatiana', 'Gómez', 'cc', 2, 2);

-- =========================================
-- 5. Contactos
-- =========================================
INSERT INTO tbl_contacts (Email, Phone) VALUES
('kevin@example.com', '3101234567'),
('tatiana@example.com', '3107654321');

-- =========================================
-- 6. tbl_add_person
-- =========================================
INSERT INTO tbl_add_person (Privacy_Terms, Fk_Person, Fk_Contacts) VALUES
(1, 1, 1),
(1, 2, 2);

-- =========================================
-- 7. Libros
-- =========================================
INSERT INTO tbl_books (Title, Isbn, Publication_Year, Pages, Language, Fk_Category, Fk_Publisher) VALUES
('Cien Años de Soledad', '111-AAA', 1967, 417, 'Español', 1, 1),
('La Casa de los Espíritus', '222-BBB', 1982, 350, 'Español', 1, 2),
('Breve Historia del Tiempo', '333-CCC', 1988, 212, 'Español', 2, 2);

-- =========================================
-- 8. Autores
-- =========================================
INSERT INTO tbl_authors (First_Name, Last_Name) VALUES
('Gabriel', 'García Márquez'),
('Isabel', 'Allende'),
('Stephen', 'Hawking');

-- =========================================
-- 9. Relación libros-autores
-- =========================================
INSERT INTO tbl_book_authors (Fk_Book, Fk_Author) VALUES
(1, 1),
(2, 2),
(3, 3);

-- =========================================
-- 10. Copias de libros
-- =========================================
INSERT INTO tbl_book_copies (Barcode, Fk_Status, Fk_Book) VALUES
('BC-001', 'available', 1),
('BC-002', 'loaned', 2),
('BC-003', 'available', 3);

-- =========================================
-- 11. Préstamos
-- =========================================
INSERT INTO tbl_loans (Due_Date, Fk_Book_Copy, Fk_User, Fk_Status, Fk_Created_By) VALUES
('2026-01-30', 2, 2, 'active', 1);

-- =========================================
-- 12. Multas
-- =========================================
INSERT INTO tbl_penalties (Amount, Fk_Status, Fk_Loan, Fk_User) VALUES
(10.50, 'pending', 1, 2);

-- =========================================
-- 13. Pagos de multas
-- =========================================
INSERT INTO tbl_penalties_payments (Amount, Fk_Penalty) VALUES
(5.50, 1);

-- =========================================
-- 14. Movimientos de inventario
-- =========================================
INSERT INTO tbl_inventory_history (Fk_Book_Copy, Fk_Previous_Status, Fk_New_Status, Fk_Performed_By_User, Notes) VALUES
(2, 'available', 'loaned', 1, 'Prestado a Tatiana');

-- =========================================
-- 15. Historial de préstamos
-- =========================================
INSERT INTO tbl_loan_history (Fk_Loan, Fk_Previous_Status, Fk_New_Status, Fk_Performed_By, Notes) VALUES
(1, 'active', 'returned', 1, 'Préstamo devuelto a tiempo');

-- =========================================
-- 16. Reservas
-- =========================================
INSERT INTO tbl_reservations (Expiration_Date, Fk_Book, Fk_User, Fk_Status) VALUES
('2026-01-25', 3, 2, 'reserved');

-- =========================================
-- 17. Historial de reservas
-- =========================================
INSERT INTO tbl_reservations_history (Fk_Reservation, Action, Fk_Performed_By) VALUES
(1, 'Reserva creada', 1);

-- =========================================
-- 18. Notificaciones
-- =========================================
INSERT INTO tbl_notifications (ID, Title, Message, Fk_Status, Fk_User) VALUES
(1, 'Bienvenida', 'Bienvenida a la biblioteca virtual', 'sent', 2);

-- =========================================
-- 19. Historial de notificaciones
-- =========================================
INSERT INTO tbl_notification_history (Fk_Notification, Notes) VALUES
(1, 'Notificación enviada a Tatiana');

-- =========================================
-- 20. Refresh tokens
-- =========================================
INSERT INTO tbl_refresh_tokens (Token, Expires_At, Fk_User) VALUES
('token123', '2026-02-01 00:00:00', 2);