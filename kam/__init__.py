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
                    page_size=10,
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

    columnDefs = [{"field": col} for col in ['category', 'full_name', 'age_year', 'location', 'run_year', 'age_group']]

    spacer = html.H2("", className="bg-white text-white p-2 mb-3")

    app.layout = html.Div(
        [
            html.Div('Filter:'),

            dcc.Input(id="quick-filter-input", placeholder="filter..."),

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

    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv")

    columnDefs = [{"field": i} for i in ["country", "year", "athlete", "age", "sport", "total"]]

    app.layout = html.Div(
        [
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
        if cell_id== 'athlete':
            dff = df[df.athlete == cell_value]
            fig = px.histogram(dff, x='athlete', y='total', color='year')
        elif cell_id == 'year':
            dff = df[df.year == cell_value]
            fig = px.bar(dff, x='country', y='total', title=f"{cell_value} Olympics")
        elif cell_id == 'country':
            dff = df[df.country == cell_value]
            fig = px.bar(dff, x='sport', y='total')
        elif cell_id == 'sport':
            dff = df[df.sport == cell_value]
            fig = px.bar(dff, x='country', y='total', title=f"{cell_value} in the Olympics")
        elif cell_id == 'age':
            dff = df[df.age == cell_value]
            fig = px.bar(dff, x='athlete', y='total', title=f"{cell_value} year-olds with medals in the Olympics")
        else:
            fig = px.bar(df, x='country', y='total', title=f"{cell_value} Olympics")
        return fig

    return app



# Initialize
create_dashboth(app)





from kam.core.views import core
from kam.graph.views import graph
app.register_blueprint(core)
app.register_blueprint(graph)