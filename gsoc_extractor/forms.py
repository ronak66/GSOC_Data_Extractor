from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class Search(FlaskForm):
    search = StringField('Search', validators=[DataRequired()])
    search_type = StringField()
    submit = SubmitField("Submit")