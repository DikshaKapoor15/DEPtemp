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
    date = DateField(format='%Y-%m-%d')
    ps_name = StringField()
    illicit = IntegerField(label='illicit',default=0)
    licit   = IntegerField(label='licit',default=0)
    lahan  = IntegerField(label='lahan' , default=0)
    opium  = IntegerField(label='opium',default=0)
    poppy =  IntegerField(label='poppy',default=0)
    heroine = IntegerField(label='heroine',default=0)
    charas = IntegerField(label='charas',default=0)
    ganja   = IntegerField(label='ganja',default=0)
    tablets = IntegerField(label='tablets',default=0)
    injections = IntegerField(label='injections',default=0)
    other_recovery = StringField(label='other_recovery',default='nil')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.date.data:
            self.date.data = datetime.date.today()

class adminForm(FlaskForm):
    ps_name1 = StringField(label = 'ps_name1')
    ps_name2 = StringField(label = 'ps_name2')
    attribute_field = StringField(label='attribute_field')
