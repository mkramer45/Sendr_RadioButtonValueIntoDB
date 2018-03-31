from flask import *
from functools import wraps
import sqlite3
from flask_bootstrap import Bootstrap
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_wtf import FlaskForm
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm, CsrfProtect



artists = ['Solomun', 'Dubfire']
# DJname = request.form['DJname']



DATABASE = 'Beatscrape.db'
DATABASE2 = 'NBA.db'

app = Flask(__name__)
app.secret_key = 'my precious'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\Users\Mike\Desktop\PythonSuccess\Beatscrape.db'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
app.config.from_object(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
csrf = CsrfProtect(app)





class LoginForm(FlaskForm):
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
	remember = BooleanField('remember me')


class RegisterForm(FlaskForm):
	email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])


class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(15), unique=True)
	email = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(80))

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


   
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def connect_db2():
	return sqlite3.connect(app.config['DATABASE2'])

@app.route('/')  
def home():
	return render_template('home.html')

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')



@app.route('/Celtics')
@csrf.exempt
def Celtics():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612738')
	info1 = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Celtics.html', selected='submit', info1=info1)


@app.route('/Wizards')
@csrf.exempt
def Wizards():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612764')
	info = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Wizards.html', selected='submit', info=info)

@app.route('/Raptors')
@csrf.exempt
def Raptors():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612761')
	info = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Raptors.html', selected='submit', info=info)

@app.route('/Sixers')
@csrf.exempt
def Sixers():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612755')
	info = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Sixers.html', selected='submit', info=info)

@app.route('/Magic')
@csrf.exempt
def Magic():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612753')
	info = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Magic.html', selected='submit', info=info)

@app.route('/Knicks')
@csrf.exempt
def Knicks():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612752')
	info = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Knicks.html', selected='submit', info=info)

@app.route('/Heat')
@csrf.exempt
def Heat():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612748')
	info = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Heat.html', selected='submit', info=info)


@app.route('/Bucks')
@csrf.exempt
def Bucks():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612749')
	info = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Bucks.html', selected='submit', info=info)

@app.route('/Pacers')
@csrf.exempt
def Pacers():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612754')
	info = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Pacers.html', selected='submit', info=info)


@app.route('/Pistons')
@csrf.exempt
def Pistons():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612765')
	info = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Pistons.html', selected='submit', info=info)


@app.route('/Cavaliers')
@csrf.exempt
def Cavaliers():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612739')
	info = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Cavaliers.html', selected='submit', info=info)

@app.route('/Bulls')
@csrf.exempt
def Bulls():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612741')
	info = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Bulls.html', selected='submit', info=info)

@app.route('/Hornets')
@csrf.exempt
def Hornets():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612751')
	info = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Hornets.html', selected='submit', info=info)

@app.route('/Nets')
@csrf.exempt
def Nets():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612751')
	info = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Nets.html', selected='submit', info=info)


@app.route('/Hawks')
@csrf.exempt
def Hawks():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612737')
	info = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Hawks.html', selected='submit', info=info)
	


@app.route('/Rockets')
@csrf.exempt
def Rockets():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612738')
	info1 = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Rockets.html', selected='submit', info1=info1)

@app.route('/Warriors')
@csrf.exempt
def Warriors():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612738')
	info1 = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Warriors.html', selected='submit', info1=info1)

@app.route('/Spurs')
@csrf.exempt
def Spurs():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612738')
	info1 = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Spurs.html', selected='submit', info1=info1)


@app.route('/Timberwolves')
@csrf.exempt
def Timberwolves():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612738')
	info1 = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Timberwolves.html', selected='submit', info1=info1)


@app.route('/Thunder')
@csrf.exempt
def Thunder():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612738')
	info1 = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Thunder.html', selected='submit', info1=info1)


@app.route('/Nuggets')
@csrf.exempt
def Nuggets():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612738')
	info1 = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Nuggets.html', selected='submit', info1=info1)

@app.route('/Pelicans')
@csrf.exempt
def Pelicans():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612738')
	info1 = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Pelicans.html', selected='submit', info1=info1)

@app.route('/Clippers')
@csrf.exempt
def Clippers():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612738')
	info1 = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Clippers.html', selected='submit', info1=info1)


@app.route('/Jazz')
@csrf.exempt
def Jazz():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612738')
	info1 = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Jazz.html', selected='submit', info1=info1)


@app.route('/Lakers')
@csrf.exempt
def Lakers():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612738')
	info1 = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Lakers.html', selected='submit', info1=info1)


@app.route('/Grizzlies')
@csrf.exempt
def Grizzlies():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612738')
	info1 = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Grizzlies.html', selected='submit', info1=info1)


@app.route('/Kings')
@csrf.exempt
def Kings():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612738')
	info1 = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Kings.html', selected='submit', info1=info1)

@app.route('/Mavericks')
@csrf.exempt
def Mavericks():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612738')
	info1 = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Mavericks.html', selected='submit', info1=info1)

@app.route('/Suns')
@csrf.exempt
def Suns():
	g.db = connect_db2()
	cur2 = g.db.execute('select FirstName, LastName, College_Country, Height, Weight, Position, BirthDate from Players where teamid = 1610612738')
	info1 = [dict(FirstName=row[0], LastName=row[1], College_Country=row[2], Height=row[3], Weight=row[4], Position=row[5], BirthDate=row[6]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('Suns.html', selected='submit', info1=info1)


	

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		conn = sqlite3.connect('Beatscrape.db')
		cursor = conn.cursor()
		hashed_password = generate_password_hash(form.password.data, method='sha256')
		new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		posts = [dict(username=row[0], email=row[1], password=row[2]) for row in cursor.fetchall()]
#        usr = User(username=form.username.data, email=form.email.data, password=hashed_password)
		usrname = form.username.data
		emailname = form.email.data
		pw = password=hashed_password
		cursor.execute("INSERT INTO users VALUES (NULL,?,?,?)", (usrname,emailname,pw,))
		conn.commit()
		cursor.close()
		conn.close()
		flash('User Created')
		#return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

	return render_template('register.html', form=form)


@app.route('/youtube', methods=['GET', 'POST'])
@csrf.exempt
def youtube():
	if request.method == 'POST':
		URL = request.form['URL']
		TimeMM = request.form['TimeMM']
		TimeSS = request.form['TimeSS']
		scl = '&t='
		m = 'm'
		s = 's'
		appendx = "".join((URL, scl, TimeMM, m, TimeSS, s))

		return render_template('youtube.html', URL=URL, TimeMM=TimeMM, TimeSS=TimeSS, scl=scl, appendx=appendx)
	return render_template('youtube.html')


@app.route('/soundcloud', methods=['GET', 'POST'])
@csrf.exempt
def soundcloud():
	if request.method == 'POST':
		URL_sc = request.form['URL']
		Time_sc = request.form['Time']
		scl_sc = '#t='
		appendx_sc = "".join((URL_sc, scl_sc, Time_sc))

		return render_template('soundcloud.html', URL_sc=URL_sc, Time_sc=Time_sc, scl_sc=scl_sc, appendx_sc=appendx_sc)
	return render_template('soundcloud.html')


@app.route('/sendr', methods=['GET', 'POST'])
@csrf.exempt
def sendr():
	if request.method == 'POST':
		global feed
		conn = sqlite3.connect('Beatscrape.db')
		cursor = conn.cursor()
		posts = [dict(URL_sc=row[0], Time_sc=row[1] ) for row in cursor.fetchall()]
		# FirstName
		FN = request.form['FirstName']
		# Email
		EM = request.form['Email']
		# Radio Button Value
		Radio_sc = request.form['options']
		cursor.execute("INSERT INTO Sendr_Usr VALUES (?,?,?)", (EM,FN,Radio_sc,))
		conn.commit()
		cursor.close()
		conn.close()


		scl_sc = '#t='
		appendx_sc = "".join((FN, scl_sc, EM))

		return render_template('soundcloudx.html', FN=FN, EM=EM, scl_sc=scl_sc, appendx_sc=appendx_sc)
	return render_template('soundcloudx.html')




@app.route('/log', methods=['GET', 'POST'])
@csrf.exempt
def log():
	form = LoginForm()
   
	if form.validate_on_submit():
		username_form  = request.form['username']
		g.db = connect_db()
		user = g.db.execute("SELECT COUNT(1) FROM users WHERE username = (?)", (username_form,))
		# if not user.fetchone()[0]:
		# 	return '<h1>Invalid username or password</h1>'
		if user.fetchone()[0]:
			# if check_password_hash(user.password, form.password.data):
			# 	login_user(user, remember=form.remember.data)
			return redirect(url_for('scrapelist2'))
		else:

			return '<h1>Invalid username or password</h1>'
		#return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

	return render_template('log.html', form=form)
	
	

# 11/14 ... updated scrapelist2 in attempts to get the user input to be saved in ArtistMonitor table
@app.route('/scrapelist2', methods=['GET', 'POST'])
@csrf.exempt
def scrapelist2():
	if request.method == 'POST':
		global feed
		conn = sqlite3.connect('Beatscrape.db')
		cursor = conn.cursor()
		posts = [dict(DJname=row[0]) for row in cursor.fetchall()]
		DJname = request.form['Producername']
		cursor.execute("INSERT INTO ArtistMonitor VALUES (NULL,?)", (DJname,))
		conn.commit()
		cursor.close()
		conn.close()
		artists.append(request.form['Producername'])
	g.db = connect_db()
	cur = g.db.execute('select DJName from ArtistMonitor')
	cur2 = g.db.execute('select * from Tracks where artist in (select DJname from ArtistMonitor)')
	pull = [dict(DJname=row[0]) for row in cur.fetchall()]
	watch = [dict(Artist=row[0], Song=row[1], Websource=row[2], Genre=row[3]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('scrapelist2.html', selected='submit', pull=pull, watch=watch)



	
@app.route('/delete_artist/<DJName>', methods=['POST'])
def delete_artist(DJName):
	conn = sqlite3.connect('Beatscrape.db')
	cursor = conn.cursor()
	del1 = [dict(id=row[0], DJName=row[1]) for row in cursor.fetchall()]
#	DJName1 = request.args.get('DJName')
	cursor.execute("DELETE FROM ArtistMonitor WHERE DJName = ?", (DJName,))
	conn.commit()
	cursor.close()
	conn.close()
	flash('Artist Deleted')
	return redirect(url_for('scrapelist2', del1=del1))
	
	
def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('log'))
	return wrap


@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect (url_for('log'))

@app.route('/hello')
@login_required
def hello():
	g.db = connect_db()
	cur = g.db.execute('select Artist, Song, Label, Price from BeatPortTechHouse')
	info = [dict(Artist=row[0], Song=row[1], Label=row[2], Price=row[3]) for row in cur.fetchall()]
	g.db.close()
	return render_template('hello.html', info=info)




if __name__ == '__main__':
	app.run(debug=True)