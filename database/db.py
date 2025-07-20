from tinydb import TinyDB

db = TinyDB('database.json')

users_table = db.table('users')
books_table = db.table('books')
reviews_table = db.table('reviews')
