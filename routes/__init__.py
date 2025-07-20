from .users import users_bp
from .books import books_bp
from .reviews import reviews_bp

def register_routes(app):
    app.register_blueprint(users_bp)
    app.register_blueprint(books_bp)
    app.register_blueprint(reviews_bp)
