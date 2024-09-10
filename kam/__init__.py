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
from dotenv import load_dotenv
from os import environ
from flask import Flask, render_template, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import pandas as pd
import requests



# Load environment
load_dotenv('.env')

# Initialize app
app = Flask(__name__)
CORS(app)

app.secret_key = environ.get('SECRET_KEY')
app.config['DEBUG'] = environ.get('FLASK_DEBUG')

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
df = pd.read_csv("./data/postdefined_users_graph.csv")


def create_dashapp(app):
    app = dash.Dash(
        server=app,
        external_stylesheets=[dbc.themes.BOOTSTRAP],
        url_base_pathname='/dashapp/'
    )
    app.config['suppress_callback_exceptions'] = True

    heading = html.Div("Runner Demo Analytics (click on icons for visualization)", className="bg-success text-white p-2 mb-3")

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
                button,
                spacer,
                dash_table.DataTable(
                    id='table',
                    data=df.to_dict('records'),
                    page_size=5,
                    column_selectable='single',
                    style_data={
                        'whiteSpace': 'normal',
                        'height': 'auto',
                    },
                ), ]),
            dbc.Col([dcc.Graph(style={"height": "100%"}, id='year-bars')]),
        ]),

        html.Div(id='page', hidden=True)
    ], fluid=True)

    load_figure_template("bootstrap")

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
        if selection == None: fig = px.bar(df, template="bootstrap", x='count', y='age_group', orientation='h')

        else:
            fig = px.bar(df, template="bootstrap", x=selection[0], y='age_group', orientation='h')
            fig.update_xaxes(type='category')
        return fig


    @app.callback(Output('table', 'columns'),
                [Input('page', 'children')]
                )
    def paginate(page):
        if page == None: page = 0
        return [{"name": df.columns[0], "id": df.columns[0]}] + \
               [{"name": i, "id": i, "selectable": True} for i in df.columns[1 + page * 10:1 + (page + 1) * 10]]


    return app


# Initialize
create_dashapp(app)


def create_dashgraph(app):
    app = dash.Dash(
        server=app,
        external_stylesheets=[dbc.themes.MINTY],
        url_base_pathname='/dashgraph/'
    )
    app.config['suppress_callback_exceptions'] = True

    df = pd.read_csv("./data/postdefined_users.csv")

    #api_url = "http://localhost:5000/load_data"
    #response = requests.get(api_url)
    #df = response.json()

    columnDefs = [{"field": col} for col in ['category', 'full_name', 'age_year', 'location', 'run_year', 'age_group']]

    app.layout = html.Div(
        [

            html.Div('Runner Demo Input Filter', className="bg-success text-white p-2 mb-3"),
            html.H2("", className="bg-white text-white p-2 mb-3"),

            dcc.Input(id="quick-filter-input", placeholder="  filter here..."),
            html.H2("", className="bg-white text-white p-2 mb-3"),

            dag.AgGrid(
                id="quick-filter-simple",
                rowData=df.to_dict("records"),
                columnDefs=columnDefs,
                defaultColDef={"flex": 1},
                dashGridOptions={"animateRows": False}
            ),
        ]
    )


    @app.callback(
        Output("quick-filter-simple", "dashGridOptions"),
        Input("quick-filter-input", "value")
    )
    def update_filter(filter_value):
        newFilter = Patch()
        newFilter['quickFilterText'] = filter_value
        return newFilter

    return app



# Initialize
create_dashgraph(app)




def create_dashboth(app):
    app = dash.Dash(
        server=app,
        external_stylesheets=[dbc.themes.MINTY],
        url_base_pathname='/dashboth/'
    )
    app.config['suppress_callback_exceptions'] = True

    df = pd.read_csv("./data/postdefined_users_graph.csv")

    columnDefs = [{"field": i} for i in ["category", "age_year", "full_name", "run_year", "age_group", "count"]]

    app.layout = html.Div(
        [

            html.Div('Runner Demo Touch Filter (click on records for visualization)', className="bg-success text-white p-2 mb-3"),
            html.H2("", className="bg-white text-white p-2 mb-3"),

            dag.AgGrid(
                id="row-selection-options",
                columnDefs=columnDefs,
                rowData=df.to_dict("records"),
                columnSize="sizeToFit",
                defaultColDef={"filter": False},
                dashGridOptions={"animateRows": False, "rowSelection": 'single'}
            ),
            dcc.Graph(id='empty-graph', figure={})
        ],
    )


    @app.callback(
        Output("empty-graph", "figure"),
        Input("row-selection-options", "cellClicked"),
        prevent_initial_call=True
    )
    def disable__checkbox(cell_selected):
        print(cell_selected)
        cell_id = cell_selected['colId']
        cell_value = cell_selected['value']
        if cell_id== 'full_name':
            dff = df[df.full_name == cell_value]
            fig = px.histogram(dff, x='full_name', y='count', color='age_year')
        elif cell_id == 'age_year':
            dff = df[df.age_year == cell_value]
            fig = px.bar(dff, x='category', y='count', title=f"{cell_value} categories")
        elif cell_id == 'category':
            dff = df[df.category == cell_value]
            fig = px.bar(dff, x='age_group', y='count')
        elif cell_id == 'age_group':
            dff = df[df.age_group == cell_value]
            fig = px.bar(dff, x='run_year', y='count', title=f"{cell_value} age groups")
        elif cell_id == 'run_year':
            dff = df[df.run_year == cell_value]
            fig = px.bar(dff, x='category', y='count', title=f"{cell_value} at run year")
            fig.update_xaxes(type='category')
        else:
            fig = px.bar(df, x='category', y='count', title=f"{cell_value} categories")
        return fig

    return app



# Initialize
create_dashboth(app)



def create_dashintro(app):
    app = dash.Dash(
        server=app,
        external_stylesheets=[dbc.themes.MINTY],
        url_base_pathname='/dashintro/'
    )
    app.config['suppress_callback_exceptions'] = True


    df = pd.read_csv('./data/postdefined_users.csv')

    fig = px.histogram(df, x='run_year', color="age_group")
    fig.update_xaxes(type='category')


    app.layout = html.Div([
        html.Div('Runner Graph', className="bg-success text-white p-2 mb-3"),
        html.H2("", className="bg-white text-white p-2 mb-3"),
        dcc.Graph(figure=fig)
    ])

    return app



# Initialize
create_dashintro(app)




from kam.core.views import core
from kam.graph.views import graph
app.register_blueprint(core)
app.register_blueprint(graph)