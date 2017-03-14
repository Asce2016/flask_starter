from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length

class RegisterForm(FlaskForm):
    firstname = StringField('FirstName', validators=[InputRequired()])
    lastname = StringField('LastName', validators=[InputRequired()])
    username = StringField('UserName', validators=[InputRequired()])
    age = IntegerField('Age', validators=[InputRequired()])
    gender = SelectField( 'Gender',choices=[('M', 'male'), ('F', 'female')])
    bio = TextAreaField('Biography', validators=[InputRequired(), Length(min = 20, max = 30)])
    
