from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DateField
from wtforms.validators import InputRequired, ValidationError
from app.models import Credentials
import datetime

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

class challanForm(FlaskForm):
    date = DateField(format = '%Y-%m-%d')
    ps_name = StringField()
    overload_truck = IntegerField("overload truck",default=0)
    drunken_drive = IntegerField("drunken drive",default=0)
    over_speed = IntegerField("over speed",default=0)
    without_mask = IntegerField("without mask",default=0)
    without_helmet_seatbelt = IntegerField("without helmet/seatbelt",default=0)
    other_challan = IntegerField("other challan",default=0)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.date.data:
            self.date.data = datetime.date.today()

class recoveryForm(FlaskForm):
    illicit = StringField("illicit")
    licit = StringField("licit")
    lahan = StringField("lahan")
    opium = StringField("opium")
    poppy = StringField("poppy")
    heroin = StringField("heroin")
    charas = StringField("charas")
    ganja = StringField("ganja")
    tablets = StringField("tablets")
    injections = StringField("injections")
    others = StringField("others")
