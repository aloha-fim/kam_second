import dash # type: ignore
from dash import dash_table
#import html
from dash import dcc
from dash import html
from dash import Input, Output, State

from dash_bootstrap_templates import load_figure_template
import dash_bootstrap_components as dbc
import plotly.express as px

import pandas as pd

from dash import Dash


app = Dash(__name__)

# Route to dashapp
data = pd.read_csv("./data/postdefined_users.csv")


def create_dashgraph(app):
    app = dash.Dash(
        server=app,
        external_stylesheets=[dbc.themes.MINTY],
        url_base_pathname='/dashgraph/'
    )
    app.config['suppress_callback_exceptions'] = True

    app.layout = html.Div([
    html.H4('Runner by Age Group'),
    dcc.Dropdown(
        id="dropdown",
        options=['<20', '21-30', '31-40', '41-50', '>50'],
        value="<20",
        clearable=False,
    ),
    dcc.Graph(id="graph"),
    ])

    load_figure_template("minty")

    @app.callback(
        Output("graph", "figure"),
        Input("dropdown", "value"))

    def update_bar_chart(group):
        df = data
        mask = df["age_group"] == group

        count_df = pd.DataFrame(data["age_group"])

        fig = px.bar(df[mask], x=data["age_group"].to_string(), y=count_df.count(), color="minty", barmode="group")
        return fig


    return app


# Initialize
create_dashgraph(app)

