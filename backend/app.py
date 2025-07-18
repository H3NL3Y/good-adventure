# backend/app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from backend.config import Config
from backend.models import Book
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

# Import models AFTER db is defined to avoid circular import


@app.route("/")
def home():
    return "Hello from Flask with SQLAlchemy!"

if __name__ == "__main__":
    app.run(debug=True)
