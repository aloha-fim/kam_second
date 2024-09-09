from flask import Flask, request, render_template, jsonify, Response, Blueprint, redirect, url_for, flash
import requests

graph = Blueprint('graph',__name__, template_folder="templates")

# Define dashgraph route
@graph.route('/dashgraph/', methods=['GET','POST'])

def redirect_to_dashgraph():
    return redirect('/dashgraph/')


# Define dashgraph route
@graph.route('/dashboth/', methods=['GET','POST'])

def redirect_to_dashboth():
    return redirect('/dashboth/')


