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
data = [
        ("2020-01-01",79.2),
        ("2020-02-01", 59.6),
        ("2020-03-01", 64),
        ("2020-04-01", 51.6),
        ("2020-05-01", 56),
    ]
labels = [row[0]  for row in data ]
values = [row[1] for row in data]

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
    return render_template("base.html", form = login_form)

@app.route("/ps",methods = ['GET','POST'])
def ps():
    #print(current_user.username)
    if not current_user.is_authenticated:
        return "Please login if you want to access the content in this website"
    return render_template("ps.html", labels=labels , values=values)



@app.route("/logout",methods = ['GET'])
def logout():
    print(current_user.username)
    logout_user()
    return "you are logged out"


if __name__ == "__main__":
    app.run(debug=True)