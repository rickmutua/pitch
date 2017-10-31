from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))


class Category(db.Model):

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.String(255))

    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))


class Pitch(db.Model):

    __tablename__ = 'pitch'

    id = db.Column(db.Integer, primary_key = True)

    username = db.Column(db.String(255), index = True)

    pitch = db.Column(db.String(300))

    posted = db.Column(db.DateTime, default=datetime.utcnow)

    category = db.relationship('Category', backref='user', lazy='dynamic')

    review = db.relationship('Review', backref='user', lazy='dynamic')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()


class Review(db.Model):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key = True)

    pitch_id = db.Column(db.Integer)
    pitch_author = db.Column(db.String)
    pitch_idea = db.Column(db.String)

    review = db.Column(db.String)

    posted = db.Column(db.DateTime, default=datetime.utcnow)

    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls, id):
        reviews = Review.query.filter_by(pitch_id=id).all()
        return reviews


class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(255), index = True)

    email = db.Column(db.String(255), unique=True, index=True)

    password_hash = db.Column(db.String(255))

    pitch = db.relationship('Pitch', backref='user', lazy='dynamic')

    reviews = db.relationship('Review', backref='user', lazy='dynamic')


    @property
    def password(self):
        raise AttributeError('Access to the password attribute Denied!')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.username}'




