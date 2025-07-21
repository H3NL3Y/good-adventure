from flask import Flask, render_template, request, redirect, session, url_for, flash
from tinydb import TinyDB, Query
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# TinyDB databases
users_db = TinyDB('users.json')
books_db = TinyDB('books.json')
User = Query()

@app.route('/')
def home():
    if 'username' in session:
        books = books_db.all()
        return render_template('home.html', username=session['username'], books=books)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        if users_db.search(User.username == username):
            flash("Username already exists.")
            return redirect(url_for('register'))
        users_db.insert({'username': username, 'password': password})
        flash("Registration successful!")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users_db.get(User.username == username)
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('home'))
        flash("Invalid credentials.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        review = request.form['review']
        books_db.insert({
            'title': title,
            'author': author,
            'review': review,
            'added_by': session['username']
        })
        return redirect(url_for('home'))

    return render_template('add_book.html')

if __name__ == '__main__':
    app.run(debug=True)