from flask import Flask, request, render_template, jsonify, Response, Blueprint, redirect, url_for, flash
#from werkzeug.utils import secure_filename
import requests
import json

#from flask_login import current_user, login_required
from kam import Db
from kam.models import KamUser
#from kam.core.forms import KamPostForm
from kam.pdf_processor import process_json_magic

from dotenv import load_dotenv

from os import environ


load_dotenv(".env")

core = Blueprint('core',__name__, template_folder="templates")


@core.route('/', methods=['GET','POST'])
def index():

	return render_template("index.html")

# API endpoint of JSON data
@core.route('/load_data', methods=['GET'])
def load_data():
	users_json = {'users': []}
	users = KamUser.query.all() # this is the db query
	for user in users:
		user_info = user.__dict__
		del user_info['_sa_instance_state']
		users_json['users'].append(user_info)
	return jsonify(users_json)


# GPT RAG prompt input, using LangChain to link with json route /load_data.
@core.route('/gpt_more', methods=['GET','POST'])
def gpt_more():

	if request.method == 'POST':
		question = request.form['question']

		answer = process_json_magic(question)

		response = answer.get('output_text')

		return render_template('upload_gpt_more.html', response=response)

	return render_template('upload_gpt_more.html')



# Define dashapp route
@core.route('/dashapp/', methods=['GET','POST'])

def redirect_to_dashapp():
    return redirect('/dashapp/')
