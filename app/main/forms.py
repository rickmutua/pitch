from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

from .. import db


class PitchForm(FlaskForm):

    title = StringField('Pitch Title', validators=[Required()])

    pitch = TextAreaField('Pitch Idea', db.String(300), validators=[Required()])

    submit = SubmitField('Submit')


class ReviewForm(FlaskForm):

    title = StringField('Review Title', validators=[Required()])

    review = TextAreaField('Pitch Review', validators=[Required()])

    submit = SubmitField('Submit')