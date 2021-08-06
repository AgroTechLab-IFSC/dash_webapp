# This Python file uses the following encoding: utf-8
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from sqlalchemy import create_engine
import psycopg2
import pandas as pd


# Import dos layouts
from app.frontend import main
from app.backend.callbacks import *
from app.server import app, server

import yaml

# Leitura dos dados que serão utilizados (é ideal que estes estejam em uma BD)
with open('./config.yaml') as file:
    env = yaml.load(file)

dbstring = 'postgresql+psycopg2://{}:{}@127.0.0.1/{}'.format(
    env['userdatabase'],
    env['passdatabase'],
    env['database'])

engine = create_engine(dbstring, pool_recycle=3600)
conn = engine.connect()

dados_mapa = pd.read_sql("""
SELECT 
	lat AS latitude, 
	lon AS longitude, 
	EXTRACT(MONTH FROM time) as mes, 
	AVG(tmax) temperatura_max,
	AVG(tmin) temperatura_min
FROM weather_data
WHERE EXTRACT(MONTH FROM time) = 1.0
GROUP BY lat, lon, EXTRACT(MONTH FROM time);
""", conn)

dados = pd.read_sql("""
SELECT 
	lat AS latitude, 
	lon AS longitude, 
	EXTRACT(MONTH FROM time) AS mes,
    EXTRACT(YEAR FROM time) AS ano,
    tmax AS temperatura_max,
    tmin AS temperatura_min,
    eto,
    rs,
    u2,
    prec,
    rh
FROM weather_data;
""", conn)

dados_mapa['longitude'] = dados_mapa['longitude'] * -1
dados_mapa['latitude'] = dados_mapa['latitude'] * -1

dados['longitude'] = dados['longitude'] * -1
dados['latitude'] = dados['latitude'] * -1

# Describe the layout UI of the app
app.layout = html.Div([
    # Este componente serve para inicializar outros componentes, se necessário
    dcc.Interval(id='interval-component', interval=1000,
                    n_intervals=0, max_intervals=0),

    dcc.Location(id="url", refresh=False),

    html.Div(id="page-content",
            # Classes de bootstrap usadas para responsividade
            className=""
    )
], className="")


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/":
        return main.layout
    '''
    if pathname == "/route_name":
        return route_name.layout
    '''
    return None

app.config.suppress_callback_exceptions = True
