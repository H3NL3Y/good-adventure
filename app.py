from flask import Flask, request, jsonify
from tinydb import TinyDB, Query
from datetime import datetime

app = Flask(__name__)
db = TinyDB('db.json')
users_table = db.table('users')
books_table = db.table('books')
reviews_table = db.table('reviews')

@app.route('/')
def index(): #This creates a route which allows a page test. http://127.0.0.1:5000
    return "Hello, Flask with TinyDB!"



# Example route to add a user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    User = Query()
    if users_table.search(User.username == username):
        return jsonify({"error": "Username already exists"}), 400
    users_table.insert({'username': username})
    return jsonify({"message": "User added"}), 201

# More routes here...

if __name__ == '__main__':
    app.run(debug=True)


