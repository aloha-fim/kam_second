import dash_ag_grid as dag # type: ignore
import dash # type: ignore
from dash import dash_table
#import html
from dash import dcc
from dash import html
from dash import Dash, Input, Output, State, callback, Patch

from dash_bootstrap_templates import load_figure_template
import dash_bootstrap_components as dbc
import plotly.express as px
from flask import Flask, request, render_template, jsonify, Response, Blueprint, redirect, url_for, flash
import requests
import pandas as pd

graph = Blueprint('graph',__name__, template_folder="templates")


app = Flask(__name__)



# Define dashgraph route
@graph.route('/dashgraph/', methods=['GET','POST'])

def redirect_to_dashgraph():
    return redirect('/dashgraph/')


# Define dashgraph route
@graph.route('/dashboth/', methods=['GET','POST'])

def redirect_to_dashboth():
    return redirect('/dashboth/')


# Define dashintro route
@graph.route('/dashintro/', methods=['GET','POST'])

def redirect_to_dashintro():
    return redirect('/dashintro/')

# Define dashapp route
@graph.route('/dashapp/', methods=['GET','POST'])

def redirect_to_dashapp():
    return redirect('/dashapp/')



