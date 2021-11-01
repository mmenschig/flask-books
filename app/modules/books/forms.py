from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

class BookForm(FlaskForm):
    title = StringField(
        'Book Title', 
        validators=[
            DataRequired(), 
            Length(min=3, 
            message=('Your title is too short.'))]
    )
    author = StringField('Author')
    genre = StringField('Genre')
    release_year = IntegerField('Release Year')
    submit = SubmitField('Submit')
