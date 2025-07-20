from flask import Blueprint, request, jsonify
from database.db import reviews_table

reviews_bp = Blueprint('reviews', __name__)

@reviews_bp.route('/reviews', methods=['POST'])
def create_review():
    data = request.get_json()
    required_fields = ['user_id', 'book_id', 'rating', 'comment']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    # Optional: validate rating between 1 and 5
    if not (1 <= int(data['rating']) <= 5):
        return jsonify({'error': 'Rating must be between 1 and 5'}), 400

    reviews_table.insert({
        'user_id': data['user_id'],
        'book_id': data['book_id'],
        'rating': data['rating'],
        'comment': data['comment']
    })
    return jsonify({'message': 'Review created'}), 201

@reviews_bp.route('/reviews', methods=['GET'])
def list_reviews():
    return jsonify(reviews_table.all())
