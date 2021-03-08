from app import app
from app.forms import *
from app.models import *
from flask import render_template, url_for, redirect
from flask_login import LoginManager, login_user, current_user, login_required, logout_user

app.config[
    'SQLALCHEMY_DATABASE_URI'] = "postgres://xmxtulwzfymycv:325459c809306339560bbad8dcae00e37b80ec1492f0360c5f495f25980817ec@ec2-18-207-95-219.compute-1.amazonaws.com:5432/dnh5em2ovkoou"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login = LoginManager(app)
login.init_app(app)
data = [
    ("2020-01-01", 79.2),
    ("2020-02-01", 59.6),
    ("2020-03-01", 64),
    ("2020-04-01", 51.6),
    ("2020-05-01", 56),
]
labels = [row[0] for row in data]
values = [row[1] for row in data]


@login.user_loader
def load_user(id):
    return Credentials.query.get(int(id))


@app.route('/', methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user_object = Credentials.query.filter_by(username=login_form.username.data).first()
        login_user(user_object)

        return redirect(url_for('home'))
    return render_template("base.html", form=login_form)


@app.route("/home", methods=['GET', 'POST'])
def home():
    # print(current_user.username)
    if not current_user.is_authenticated:
        return "Please login if you want to access the content in this website"
    return render_template("home.html", labels=labels, values=values)


@app.route('/challan', methods=['POST', 'GET'])
def challan():
    challan_form = challanForm()
    print(challan_form.date.data)
    if challan_form.validate_on_submit():
        newchallan = challans(overload_tripper_and_truck = challan_form.overload_truck.data, drunken_driving = challan_form.drunken_drive.data, over_speed = challan_form.over_speed.data, without_mask = challan_form.without_mask.data, without_helmet_seatbelt = challan_form.without_helmet_seatbelt.data, other= challan_form.other_challan.data, date = challan_form.date.data, ps_name = current_user.username)
        db.session.add(newchallan)
        db.session.commit()
        return "submitted successfully"
    return render_template('challan.html', form=challan_form)


@app.route('/recovery', methods=['POST', 'GET'])
def recovery():
    recovery_form = recoveryForm()
    print(recovery_form.errors)
    if recovery_form.validate_on_submit():
        print("hiii")
        return "{submited successfully}"
    return render_template('recovery.html', form=recovery_form)


@app.route("/logout", methods=['GET'])
def logout():
    print(current_user.username)
    logout_user()
    return "you are logged out"


if __name__ == "__main__":
    app.run(debug=True)
