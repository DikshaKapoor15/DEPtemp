from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Credentials(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(25), unique = True, nullable = False)
    password = db.Column(db.String(), nullable= False)

class challans(db.Model):
    _tablename_ = "challan"
    id             = db.Column(db.Integer, primary_key=True)
    overload_tripper_and_truck = db.Column(db.Integer,nullable=False)
    drunken_driving  = db.Column(db.Integer,nullable=False)
    over_speed     = db.Column(db.Integer,nullable=False)
    without_mask = db.Column(db.Integer, nullable=False)
    without_helmet_seatbelt = db.Column(db.Integer,nullable=False)
    other = db.Column(db.Integer,nullable=False)
    date = db.Column(db.DateTime(timezone=False), nullable = False)
    ps_name = db.Column(db.String(15),nullable = False)

    def _init_(self, ovt, dd, os, wohsb, wom, oc,d,ps):
        self.overload_truck = ovt
        self.drunken_drive = dd
        self.over_speed = os
        self.without_helmet_seatbelt = wohsb
        self.without_mask = wom
        self.other_challan = oc
        self.date =d
        self.ps_name = ps

class recoveries(db.Model):
    tablename = "recoveries"

    id = db.Column(db.Integer, primary_key=True)
    illicit = db.Column(db.Integer,nullable=False)
    licit   = db.Column(db.Integer,nullable=False)
    lahan  = db.Column(db.Integer,nullable=False)
    opium = db.Column(db.Integer,nullable=False)
    poppy = db.Column(db.Integer,nullable=False)
    heroine = db.Column(db.Integer,nullable=False)
    charas = db.Column(db.Integer,nullable=False)
    ganja = db.Column(db.Integer,nullable=False)
    tablets = db.Column(db.Integer,nullable=False)
    injections= db.Column(db.Integer,nullable=False)
    other_recovery = db.Column(db.String(),nullable=False)
    date       =db.Column(db.DateTime(timezone=False),nullable=False)
    ps_name    = db.Column(db.String(15),nullable=False)


    def _init_(self,illicit,licit,lahan,opium,poppy,heroine,charas,ganja,tablets,injections,other,d,ps):
        self.illicit = illicit
        self.licit   = licit
        self.lahan   = lahan
        self.opium  = opium
        self.poppy  = poppy
        self.heroine = heroine
        self.charas = charas
        self.ganja =ganja
        self.tablets = tablets
        self.injections = injections
        self.other_recovery =other
        self.date=d
        self.ps_name =ps

