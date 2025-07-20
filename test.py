import requests
from tinydb import TinyDB


from routes import users_bp, books_bp

def addNewBook():
    # Load your database file
    db = TinyDB('database.json')  # Replace with the correct path if needed

    base = 'http://127.0.0.1:5000'

    # Example: Print all tables and their data
    print("== Add New Book  ==")
    username = input("Enter your name/username: ")
    title = input("Enter title of the book: ")
    author = input("Enter author of the book: ")
    review = input("Enter a short review: ")
    rating = int(input("Enter rating [1-5]: "))

    requests.post(f'{base}/users', json={'username':username})
    requests.post(f'{base}/books', json={'title':title, 'author':author})




    review_data = {
        "rating": rating,
        "comment": review,   # from your input
        "user_id": users_id,  # get this from your users DB or API response
        "book_id": books_bp   # get this from your books DB or API response
    }
    requests.post(f'{base}/reviews', json={'reviews':review_data})

addNewBook()