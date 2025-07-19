from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # ✅ NEW
from .config import Config

db = SQLAlchemy()
migrate = Migrate()  # ✅ NEW

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)  # ✅ NEW

    from .models import Book, User, Review  # ✅ Make sure all models are imported

    from .services import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
