from . import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True) #Sets primary key.
    title = db.Column(db.String(100), nullable=False) #nullable will prevent empty input.
    author = db.Column(db.String(100), nullable=False)
    reviews = db.relationship('Review', backref='user', lazy=True)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100), unique=True,nullable=False)
    reviews = db.relationship('Review', backref='user', lazy=True)

class Review(db.model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Ingteger, nullable=True)
    comment = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) #Creates foreign key from other methods.
    book_id = db.Column(db.Integer, db.ForeignKey('bood.id'), nullable=False)






#Use this to set foreign key within table.
#user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)