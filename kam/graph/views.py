from flask import Flask, request, render_template, jsonify, Response, Blueprint, redirect, url_for, flash
#from werkzeug.utils import secure_filename
import requests
import json

#from flask_login import current_user, login_required
from kam import Db
from kam.models import KamUser
#from kam.graph.forms import GraphPostForm

from dotenv import load_dotenv

from os import environ


load_dotenv(".env")

graph = Blueprint('graph',__name__, template_folder="templates")

# Define dashapp route
@graph.route('/dashgraph/', methods=['GET','POST'])

def redirect_to_dashgraph():
    return redirect('/dashgraph/')


