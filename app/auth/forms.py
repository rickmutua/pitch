from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import Required, Email, EqualTo

from ..models import User


class RegistrationForm(FlaskForm):

    email = StringField('Your Email Address', validators=[Required(), Email()])

    username = StringField('User Name', validators=[Required()])

    password = PasswordField('Password', validators=[Required(),
                                                     EqualTo('password_confirm', message='Passwords do not match!')])

    password_confirm = PasswordField('Confirm Passwords', validators=[Required()])

    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('Email already exists')

    def valdate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('Username already taken')


class LoginForm(FlaskForm):

    email = StringField('Email Address', validators=[Required()])

    password = PasswordField('Password', validators=[Required()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Sign In')