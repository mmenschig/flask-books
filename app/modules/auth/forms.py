from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length
)


class SignUpForm(FlaskForm):
    """User Sign-up Form."""
    email = StringField(
        'Email',
        validators=[
            Length(min=6),
            Email(message='Please enter a valid email.'),
            DataRequired()
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=8, message='Select a password with at least 8 characters.')
        ]
    )
    confirm = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    """User Log-In Form."""
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message='Enter a valid email.')
        ]
    )
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')