from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    cellphone = StringField('phone', validators=[DataRequired()])
    
