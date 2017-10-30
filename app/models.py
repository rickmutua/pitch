from . import db
from datetime import datetime


class PitchCategory(db.Model):

    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key = True)

    category_name = db.Column(db.String(255))

    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))


class Pitch(db.Model):

    __tablename__ = 'pitch'

    id = db.Column(db.Integer, primary_key = True)

    username = db.Column(db.String(255), index = True)

    idea = db.Column(db.String(255))

    posted = db.Column(db.DateTime, default=datetime.utcnow)

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()


class Review(db.Model):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key = True)

    pitch_id = db.Column(db.Integer)
    pitch_author = db.Column(db.String)
    pitch_idea = db.Column(db.String)

    posted = db.Column(db.DateTime, default=datetime.utcnow)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls, id):
        reviews = Review.query.filter_by(movie_id=id).all()
        return reviews



