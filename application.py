from app import app
from app.forms import *
from app.models import *
from flask import render_template, url_for, redirect
from flask_login import LoginManager, login_user, current_user,login_required,logout_user

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://xmxtulwzfymycv:325459c809306339560bbad8dcae00e37b80ec1492f0360c5f495f25980817ec@ec2-18-207-95-219.compute-1.amazonaws.com:5432/dnh5em2ovkoou"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login = LoginManager(app)
login.init_app(app)


@login.user_loader
def load_user(id):
    return Credentials.query.get(int(id))

@app.route('/', methods = ['GET','POST'])

@app.route("/login", methods = ['GET','POST'])

def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user_object = Credentials.query.filter_by(username = login_form.username.data).first()
        login_user(user_object)
        return redirect(url_for('ps'))
        return "not logged in"
    return render_template("login.html", form = login_form)

@app.route("/ps",methods = ['GET','POST'])
def ps():
    if not current_user.is_authenticated:
        return "Please login if you want to access the content in this website"
    return "hello"

@app.route("/logout",methods = ['GET'])
def logout():
    logout_user()
    return "you are logged out"


if __name__ == "__main__":
    app.run(debug=True)