from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField, DateField, FileField
from wtforms.validators import DataRequired

class RickyForm(FlaskForm):
    id = IntegerField('id', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    status = StringField('status')
    species = StringField('species')
    typee = StringField('typee')
    gender = StringField('gender')
    origin_name = StringField('origin_name')
    location_name = StringField('location_name')
    image = TextAreaField('image')
    created = StringField('created')
    dimension = StringField('dimension')
    episode_id = StringField('episode_id')
    episode_name = StringField('episode_name')
    episode_air_date = StringField('episode_air_date')
    episode = StringField('episode')
    submit = SubmitField('Create ricky')