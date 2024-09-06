from dotenv import load_dotenv
from os import environ
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.models import KamUser, Db

# Load environment
load_dotenv('.env')

# Initialize app
app = Flask(__name__)
app.secret_key = environ.get('SECRET_KEY')

# Initialize DB
Db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/kam_users_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Db.init_app(app)

@app.route('/')
def index():

	return render_template("index.html")

@app.route('/show_data')
def show_data():

	return render_template("show.html")

@app.route('/load_data', methods=['GET'])
def load_data():
	users_json = {'users': []}
	users = KamUser.query.all() # this is the db query
	for user in users:
		user_info = user.__dict__
		del user_info['_sa_instance_state']
		users_json['users'].append(user_info)
	return jsonify(users_json)


############################################################
# START localhost virtual environment ######################
# virtualenv venv for python 2.7 and Windows
# python3 -m venv venv for python 3+
# source venv/bin/activate
# .\venv\Scripts\activate for Windows
# pip install -r requirements.txt for setup
# pip freeze > requirements.txt for update after pip install
# python3 app.py
############################################################

############################################################
# Flask DB commands after pip3 install migrate workflow ####
# 1) flask db init / flask db stamp head
# 2) flask db migrate -m "first migration"
# 3) flask db upgrade
# to push migrations
# 4) python3 app.py
############################################################
