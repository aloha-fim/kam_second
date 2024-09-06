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

@app.route('/load_data', methods=['GET'])
def load_data():
	users_json = {'users': []}
	users = KamUser.query.all() # this is the db query
	for user in users:
		user_info = user.__dict__
		del user_info['_sa_instance_state']
		users_json['users'].append(user_info)
	return jsonify(users_json)