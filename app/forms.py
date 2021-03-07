from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, ValidationError
from app.models import Credentials

def invalid_credentials(form,field):
    username_entered = form.username.data
    password_entered = field.data
    user_object = Credentials.query.filter_by(username = username_entered).first()
    if user_object is None:
        raise ValidationError("Username or password is incorrect")
    elif password_entered!=user_object.password:
        raise ValidationError("Username or password is incorrect")


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(message = "Username required")])
    password = PasswordField('Password', validators=[InputRequired(message = "Password required"),invalid_credentials])
    submit_button = SubmitField('Login')
