from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

from .. import db


class PitchForm(FlaskForm):

    title = StringField('Pitch Title', validators=[Required()])

    pitch = TextAreaField('Pitch Idea', validators=[Required()])

    submit = SubmitField('Submit')


class ReviewForm(FlaskForm):

    review = TextAreaField('Pitch Review')

    submit = SubmitField('Submit')


class CategoryForm(FlaskForm):

    name = StringField('Category Name', validators=[Required()])

    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):

    bio = TextAreaField('Tell us about you.',validators = [Required()])

    submit = SubmitField('Submit')