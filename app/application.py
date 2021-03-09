from app import app
from app.forms import *
from app.models import *
from flask import render_template, url_for, redirect,request
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from sqlalchemy import create_engine

engine = create_engine('postgres://xmxtulwzfymycv:325459c809306339560bbad8dcae00e37b80ec1492f0360c5f495f25980817ec@ec2-18-207-95-219.compute-1.amazonaws.com:5432/dnh5em2ovkoou')
connection = engine.raw_connection()
mycursor = connection.cursor()
app.config[
    'SQLALCHEMY_DATABASE_URI'] = "postgres://xmxtulwzfymycv:325459c809306339560bbad8dcae00e37b80ec1492f0360c5f495f25980817ec@ec2-18-207-95-219.compute-1.amazonaws.com:5432/dnh5em2ovkoou"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# session = db.session()
# cursor = session.execute(sql).cursor

login = LoginManager(app)
login.init_app(app)



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

        return redirect(url_for('home', userdata = login_form.username.data))
    return render_template("base.html", form=login_form)


@app.route("/home", methods=['GET', 'POST'])
def home():
    userdata = request.args.get('userdata',None)
    mycursor.execute("SELECT * FROM challans WHERE ps_name = '{0}' " .format( str(current_user.username)))

    data = mycursor.fetchall()
    labels = []
    values = []
    for i in range(-6,0):
        labels.append((data[i][7]).strftime('%Y-%m-%d'))
        sum = data[i][1] + data[i][2] + data[i][3] + data[i][4] + data[i][5] + data[i][6]
        values.append(sum)
    colors = [
        "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
        "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
        "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]
    # print(values)
    # print(labels)
    mycursor.execute("SELECT * FROM challans WHERE ps_name='{0}' ".format(str(current_user.username)))
    challan_data_ps = mycursor.fetchall()

    labels1 = ['overload_tripper_and_truck', 'drunken_driving', 'over_speed', 'without_mask', 'without_helmet_seatbelt',
               'other']
    values1 = []
    for j in range(1,7):
        sum = 0
        for i in range(-6,0):
            sum = challan_data_ps[i][j] + sum
        values1.append(sum)

    mycursor.execute("SELECT marks,date FROM marks WHERE ps_Name='{0}' ORDER BY date ".format(str(current_user.username)))
    marks_data = mycursor.fetchall()
    labels2 = []
    values2 = []
    for i in range(-6,0):
        labels2.append(marks_data[i][1])
        values2.append(marks_data[i][0])
    if not current_user.is_authenticated:
        return "Please login if you want to access the content in this website"
    return render_template("home.html", labels=labels, values=values, colors=colors, labels1 = labels1, values1 = values1, labels2=labels2, values2=values2, userdata = userdata)


@app.route('/challan', methods=['POST', 'GET'])
def challan():

    challan_form = challanForm()
    if challan_form.validate_on_submit():
        newchallan = challans(overload_tripper_and_truck = challan_form.overload_truck.data, drunken_driving = challan_form.drunken_drive.data, over_speed = challan_form.over_speed.data, without_mask = challan_form.without_mask.data, without_helmet_seatbelt = challan_form.without_helmet_seatbelt.data, other= challan_form.other_challan.data, date = challan_form.date.data, ps_name = current_user.username)
        db.session.add(newchallan)
        db.session.commit()
        return "submitted successfully"
    return render_template('challan.html', form=challan_form)


@app.route('/recovery', methods=['POST', 'GET'])
def recovery():
    recovery_form = recoveryForm()

    if recovery_form.validate_on_submit():
        new_recovery = recoveries(illicit = recovery_form.illicit.data, licit=recovery_form.licit.data, lahan=recovery_form.lahan.data,opium=recovery_form.opium.data, poppy=recovery_form.poppy.data, heroine=recovery_form.heroine.data,charas=recovery_form.charas.data, ganja=recovery_form.ganja.data, injections=recovery_form.injections.data, tablets=recovery_form.tablets.data, other_recovery =recovery_form.other_recovery.data, date=recovery_form.date.data,ps_name=current_user.username)
        db.session.add(new_recovery)
        db.session.commit()
        return "submited successfully"
    return render_template('recovery.html', form=recovery_form)

@app.route('/admin',methods=['GET',"POST"])
def admin():
    aform = adminForm()
    if aform.validate_on_submit():
        ps1=aform.ps_name1.data
        ps2=aform.ps_name2.data
        attributef = aform.attribute_field.data
        return redirect(url_for('output',ps1=ps1,ps2=ps2,attributef=attributef))
    return render_template('tempadmin.html', form=aform)

@app.route('/output',methods=['GET','POST'])
def output():
    x=request.args.get('ps1')
    y=request.args.get('ps2')
    z=request.args.get('attributef')
    if z == 'challan':
        mycursor.execute("SELECT * FROM challans WHERE ps_Name='{0}' ORDER BY date ".format(str(x)))
        ssp_data = mycursor.fetchall()
        values3=[0,0,0,0,0,0]
        for j in range(len(ssp_data)):
            values3[0]+=ssp_data[j][0]
            values3[1] += ssp_data[j][0]
            values3[1] += ssp_data[j][1]
            values3[2] += ssp_data[j][2]
            values3[3] += ssp_data[j][3]
            values3[4] += ssp_data[j][4]
        mycursor.execute("SELECT * FROM challans WHERE ps_Name='{0}' ORDER BY date ".format(str(y)))
        ssp_data = mycursor.fetchall()
        values4 = [0, 0, 0, 0, 0, 0]
        for j in range(len(ssp_data)):
            values4[0] += ssp_data[j][0]
            values4[1] += ssp_data[j][0]
            values4[1] += ssp_data[j][1]
            values4[2] += ssp_data[j][2]
            values4[3] += ssp_data[j][3]
            values4[4] += ssp_data[j][4]
        labels2 = ['overloadedTruck','drunkenDrive','overSpeed','withoutMask','without_helmet_seatbelt','others']
    return render_template('output.html',ps1=request.args.get('ps1'),ps2=request.args.get('ps2'),attributef=request.args.get('attributef'),
                           values=values3, values1=values4,labels=labels2,x=x,y=y)

@app.route("/pre",methods = ['GET'])
def pre():
    return render_template('admin.html')


@app.route("/logout", methods=['GET'])
def logout():

    logout_user()
    return "you are logged out"


if __name__ == "__main__":
    app.run(debug=True)
