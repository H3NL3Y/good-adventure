from flask import Flask
from routes import register_routes


app = Flask(__name__)
register_routes(app)

@app.route('/')
def home():
    return "Welcome to the TinyDB Book Review App!"

if __name__ == '__main__':
    app.run(debug=True)



