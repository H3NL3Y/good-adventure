from . import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    reviews = db.relationship('Review', backref='user', lazy=True)

    #def __repr__(self):
        #return f"<Book {self.title}>"

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100), unique=True,nullable=False)
    reviews = db.relationship('Review', backref='user', lazy=True)


# TODO: Create review table class. - https://www.notion.so/good-adventure-234614706360801c9af4ed7173b1d29c

#Use this to set foreign key within table.
#user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)