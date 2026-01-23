import random
import datetime

roles = ['admin', 'user']
states = ['active', 'inactive']
doc_types = ['cc', 'ti']
categories = ['Ficción', 'Ciencia', 'Historia']
publishers = ['Editorial Alfa', 'Editorial Beta']
languages = ['Español', 'Inglés', 'Francés']

print("INSERT INTO tbl_book_authors (Fk_Book, Fk_Author) VALUES")
for i in range(3, 101):
    book = i
    author = i
    print(f"({book}, {author}),")
