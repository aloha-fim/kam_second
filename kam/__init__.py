import dash # type: ignore
from dash import dash_table
#import html
from dash import dcc
from dash import html
from dash import Input, Output, State

import dash_bootstrap_components as dbc
import plotly.express as px
from dotenv import load_dotenv
from os import environ
from flask import Flask, render_template, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy

import pandas as pd






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
df = pd.read_csv("./data/life_expectancy_years.csv")


def create_dashapp(app):
    app = dash.Dash(
        server=app,
        external_stylesheets=[dbc.themes.BOOTSTRAP],
        url_base_pathname='/dashapp/'
    )
    app.config['suppress_callback_exceptions'] = True

    heading = html.H2("Runner Demo", className="bg-success text-white p-2 mb-3")
    spacer = html.H2("", className="bg-white text-white p-2 mb-3")

    button = html.Div(
    [
        dbc.Button("Previous", outline=True, color="success", className="mr-1", id="b-prev"),
        dbc.Button("Next", outline=True, color="success", className="mr-1", id="b-next"),
    ],
    className="d-grid gap-2 d-md-flex justify-content-md-end",
)

    # Set the layout
    app.layout = dbc.Container([
        dbc.Row([
            dbc.Col([
                heading,
                #dbc.Button("Previous", color="secondary", className="mr-1", id="b-prev"),
                #dbc.Button("Next", color="secondary", className="mr-1", id="b-next"),
                button,
                spacer,
                dash_table.DataTable(
                    id='table',
                    # columns=[{"name": i, "id": i} for i in df.columns[0:10]],
                    data=df.to_dict('records'),
                    page_size=30,
                    column_selectable='single',
                ), ]),
            dbc.Col([dcc.Graph(style={"height": "100%"}, id='year-bars')]),
        ]),

        html.Div(id='page', hidden=True)
    ], fluid=True)


    @app.callback(Output('page', 'children'),
                  [Input('b-prev', 'n_clicks'),
                   Input('b-next', 'n_clicks')],
                  [State('page', 'children')])
    def update_page(bprev, bnext, page):
        if page == None: page = 0
        changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
        if 'b-prev' in changed_id:
            page -= 1
        if 'b-next' in changed_id:
            page += 1
        return page


    @app.callback(
        Output('year-bars', 'figure'),
        [Input('table', 'selected_columns')]
    )
    def select_year(selection):
        if selection == None: fig = px.bar(df, x='1800', y='country', orientation='h')
        else:
            fig = px.bar(df, x=selection[0], y='country', orientation='h')
        return fig


    @app.callback(Output('table', 'columns'),
                [Input('page', 'children')]
                )
    def paginate(page):
        if page == None: page = 0
        return [{"name": df.columns[0], "id": df.columns[0]}] + \
               [{"name": i, "id": i, "selectable": True} for i in df.columns[1 + page * 10:1 + (page + 1) * 10]]


        # Register callbacks here if you want...

    return app


# Initialize
create_dashapp(app)



from kam.core.views import core
app.register_blueprint(core)