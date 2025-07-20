from flask import Blueprint, request, jsonify
from database.db import books_table

books_bp = Blueprint('books', __name__)

@books_bp.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    if not data or 'title' not in data or 'author' not in data:
        return jsonify({'error': 'Title and author are required'}), 400
    books_table.insert({
        'title': data['title'],
        'author': data['author']
    })
    return jsonify({'message': 'Book created'}), 201

@books_bp.route('/books', methods=['GET'])
def list_books():
    return jsonify(books_table.all())
