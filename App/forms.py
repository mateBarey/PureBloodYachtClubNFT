from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
  
    email = StringField('email',validators=[DataRequired()])
    pasword = StringField('password',validators=[DataRequired()])
    eth_address = StringField('eth_address',validators=[DataRequired()])