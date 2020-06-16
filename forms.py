from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Lenght, Email, EqualTo




class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(), Lenght(min=2, max=20)])
    
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                      validators=[DataRequired(), EqualTo('password')])
    
    
    
    
    
    
    