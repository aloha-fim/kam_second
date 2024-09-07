from flask import Flask, request, render_template, jsonify, Response, Blueprint, redirect, url_for, flash
#from werkzeug.utils import secure_filename
import requests
import json

#from flask_login import current_user, login_required
from kam import Db
from kam.models import KamUser
#from kam.core.forms import KamPostForm

from dotenv import load_dotenv

from os import environ


load_dotenv(".env")

core = Blueprint('core',__name__, template_folder="templates")


@core.route('/', methods=['GET','POST'])
def index():

	return render_template("index.html")

@core.route('/show_data', methods=['GET','POST'])
def show_data():

	return render_template("show.html")

@core.route('/load_data', methods=['GET'])
def load_data():
	users_json = {'users': []}
	users = KamUser.query.all() # this is the db query
	for user in users:
		user_info = user.__dict__
		del user_info['_sa_instance_state']
		users_json['users'].append(user_info)
	return jsonify(users_json)


# Define dashapp route
@core.route('/dashapp/', methods=['GET','POST'])

def redirect_to_dashapp():
    return redirect('/dashapp/')
