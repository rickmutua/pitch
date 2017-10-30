from . import db
from datetime import datetime


class Pitch(db.Model):

    __tablename__ = 'pitch'

    id = db.Column(db.Integer, primary_key = True)

    username = db.Column(db.String(255), index = True)

    idea = db.Column(db.String(255))

    posted = db.Column(db.DateTime, default=datetime.utcnow)

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

