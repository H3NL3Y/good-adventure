from flask import Blueprint, request, jsonify
from tinydb import TinyDB

reviews_bp = Blueprint('reviews', __name__)
db = TinyDB('database.json')
reviews_table = db.table('reviews')


@reviews_bp.route('/reviews', methods=['POST'])
def create_review():
    data = request.get_json()

    required_fields = ['user_id', 'book_id', 'rating', 'comment']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required review fields"}), 400

    new_review = {
        "user_id": data['user_id'],
        "book_id": data['book_id'],
        "rating": data['rating'],
        "comment": data['comment']
    }
    reviews_table.insert(new_review)
    return jsonify({"message": "Review added!", "review": new_review}), 201
