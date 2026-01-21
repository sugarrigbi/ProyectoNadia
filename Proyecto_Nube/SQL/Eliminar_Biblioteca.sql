SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE TABLE tbl_notification_history;
TRUNCATE TABLE tbl_notifications;
TRUNCATE TABLE tbl_reservations_history;
TRUNCATE TABLE tbl_reservations;
TRUNCATE TABLE tbl_loan_history;
TRUNCATE TABLE tbl_inventory_history;
TRUNCATE TABLE tbl_penalties_payments;
TRUNCATE TABLE tbl_penalties;
TRUNCATE TABLE tbl_loans;
TRUNCATE TABLE tbl_book_copies;
TRUNCATE TABLE tbl_book_authors;
TRUNCATE TABLE tbl_books;
TRUNCATE TABLE tbl_authors;
TRUNCATE TABLE tbl_add_person;
TRUNCATE TABLE tbl_contacts;
TRUNCATE TABLE tbl_person;
TRUNCATE TABLE tbl_address;
TRUNCATE TABLE tbl_user;
TRUNCATE TABLE tbl_refresh_tokens;

TRUNCATE TABLE tbl_user_roles;
TRUNCATE TABLE tbl_user_states;
TRUNCATE TABLE tbl_document_type;
TRUNCATE TABLE tbl_categories;
TRUNCATE TABLE tbl_publishers;
TRUNCATE TABLE tbl_loan_status;
TRUNCATE TABLE tbl_book_status;
TRUNCATE TABLE tbl_penalties_status;
TRUNCATE TABLE tbl_reservation_status;
TRUNCATE TABLE tbl_notification_status;

SET FOREIGN_KEY_CHECKS = 1;