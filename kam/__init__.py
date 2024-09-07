import dash # type: ignore
#import html
from dash import dcc
from dash import html
from dotenv import load_dotenv
from os import environ
from flask import Flask, render_template, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy


# Load environment
load_dotenv('.env')

# Initialize app
app = Flask(__name__)


app.secret_key = environ.get('SECRET_KEY')

# Initialize DB
Db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



app.app_context().push()

# app.app_context():
#    Db.create_all()

def create_app():
    Db.init_app(app)

    return app



# Route to dashapp

def create_dashapp(app):
    app = dash.Dash(
        server=app,
        url_base_pathname='/dashapp/'
    )
    app.config['suppress_callback_exceptions'] = True
    app.title='Dash App'

    # Set the layout
    app.layout = layout = html.Div('Hello Dash app')

    # Register callbacks here if you want...

    return app


# Initialize
create_dashapp(app)



from kam.core.views import core
app.register_blueprint(core)