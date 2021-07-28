import numpy as np
import pandas as pd

from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go

# Traz uma instância da aplicação para este arquivo
# É desta forma que é possível adicionar callbacks a nossa aplicação
from app.server import app

# --------------------------------------
# INIT COMPONENTS
# Nesta parte vamos inicializar opções
# --------------------------------------

@app.callback(
    [Output('coord_dropdown', 'options'),
     Output('coord_dropdown', 'value')],
    [Input('interval-component', 'n_intervals')]
)
def init_dropdown(n_intervals):
    from app import dados

    dados['latitude'] = dados['latitude'].astype(str)
    dados['longitude'] = dados['longitude'].astype(str)
    dados['lat_lon'] = dados['latitude'] + dados['longitude']

    coords = dados['lat_lon'].unique()
    options = [ {'label': coord, 'value': coord } for coord in coords]
    value = options[0]['value']

    return options, value


@app.callback(
    [Output('year_dropdown', 'options'),
     Output('year_dropdown', 'value')],
    [Input('interval-component', 'n_intervals')]
)
def init_dropdown(n_intervals):
    from app import dados

    years = dados['ano'].unique()
    options = [ {'label': year, 'value': year } for year in years]
    value = options[0]['value']

    return options, value


# --------------------------------------
# CALLBACKS 
# --------------------------------------
# @app.callback(
#     Output("main_graph_line", 'figure'),
#     [
#         Input('interval-component', 'n_intervals'),
#         Input('main_dropdown_state', 'value')
#     ])
# def update_chart(n_intervals, dropdown_state):
#     from app import data
    
#     df = data

#     df.vacina_dataaplicacao = pd.to_datetime(df.vacina_dataaplicacao)
#     df['vacina_dataaplicacao_dia'] = df.vacina_dataaplicacao.dt.date

#     df = df[df['paciente_endereco_nmmunicipio'] == dropdown_state]

#     df = df.groupby(["vacina_dataaplicacao_dia","vacina_descricao_dose"])["paciente_id"].count().reset_index()
#     df = df.rename(columns={'paciente_id':'contagem'})
#     df = df[df['vacina_descricao_dose'] != 'Dose']
    
#     fig = px.line(df, x='vacina_dataaplicacao_dia', y='contagem', color='vacina_descricao_dose', title='Número de vacinas por dose ao longo do tempo')

#     return fig

@app.callback(
    Output("geo_graph", 'figure'),
    [
        Input('interval-component', 'n_intervals')
    ])
def update_chart(n_intervals):
    from app import dados_mapa
    dados_mapa['text'] = 'Máxima: ' + dados_mapa['temperatura_max'].astype(str) + ' - Mínima: ' + dados_mapa['temperatura_min'].astype(str)

    fig = go.Figure(data=go.Scattergeo(
        locationmode = 'country names',
        lon = dados_mapa['longitude'],
        lat = dados_mapa['latitude'],
        text = dados_mapa['text'],
        mode = 'markers',
        marker = dict(
            size = 4,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'square',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorscale = 'Blues',
            cmin = 0
        )))

    return fig

# @app.callback(
#     Output("temperature_graph", 'figure'),
#     [
#         Input('interval-component', 'n_intervals'),
#         Input('coord_dropdown', 'value'),
#         Input('year_dropdown', 'value')
#     ])
# def update_chart(n_intervals, coord, year):
#     from app import dados
    
#     dados['latitude'] = dados['latitude'].astype(str)
#     dados['longitude'] = dados['longitude'].astype(str)
#     dados['lat_lon'] = dados['latitude'] + dados['longitude']

#     dados = dados[dados['ano'] == year]
#     dados = dados[dados['lat_lon'] == coord]

#     # meses = dados['mes'].unique().values
#     dados = (dados.groupby(['mes'], as_index=False)['temperatura_max'].mean())
    
#     fig = px.bar(dados, x='mes', y='temperatura_max')
#     return fig


@app.callback(
    Output("temperature_graph", 'figure'),
    [
        Input('interval-component', 'n_intervals'),
        Input('coord_dropdown', 'value'),
        Input('year_dropdown', 'value')
    ])
def update_chart(n_intervals, coord, year):
    from app import dados
    
    dados['latitude'] = dados['latitude'].astype(str)
    dados['longitude'] = dados['longitude'].astype(str)
    dados['lat_lon'] = dados['latitude'] + dados['longitude']

    dados = dados[dados['ano'] == year]
    dados = dados[dados['lat_lon'] == coord]

    fig = go.Figure()
    
    dados_min = (dados.groupby(['mes'], as_index=False)['temperatura_min'].mean())
    dados_max = (dados.groupby(['mes'], as_index=False)['temperatura_max'].mean())

    fig.add_trace(go.Scatter(x=dados_min['mes'], y=dados_min['temperatura_min'],
                    mode='lines',
                    name='temperatura_min'))
    
    fig.add_trace(go.Scatter(x=dados_max['mes'], y=dados_max['temperatura_max'],
                    mode='lines',
                    name='temperatura_max'))

    # meses = dados['mes'].unique().values
    # dados = (dados.groupby(['mes'], as_index=False)['temperatura_min'].mean())
    
    # fig = px.bar(dados, x='mes', y='temperatura_min')
    return fig

@app.callback(
    Output("eto_graph", 'figure'),
    [
        Input('interval-component', 'n_intervals'),
        Input('coord_dropdown', 'value'),
        Input('year_dropdown', 'value')
    ])
def update_chart(n_intervals, coord, year):
    from app import dados
    
    dados['latitude'] = dados['latitude'].astype(str)
    dados['longitude'] = dados['longitude'].astype(str)
    dados['lat_lon'] = dados['latitude'] + dados['longitude']

    dados = dados[dados['ano'] == year]
    dados = dados[dados['lat_lon'] == coord]

    # meses = dados['mes'].unique().values
    dados = (dados.groupby(['mes'], as_index=False)['eto'].mean())
    
    fig = px.bar(dados, x='mes', y='eto')
    return fig


@app.callback(
    Output("u2_graph", 'figure'),
    [
        Input('interval-component', 'n_intervals'),
        Input('coord_dropdown', 'value'),
        Input('year_dropdown', 'value')
    ])
def update_chart(n_intervals, coord, year):
    from app import dados
    
    dados['latitude'] = dados['latitude'].astype(str)
    dados['longitude'] = dados['longitude'].astype(str)
    dados['lat_lon'] = dados['latitude'] + dados['longitude']

    dados = dados[dados['ano'] == year]
    dados = dados[dados['lat_lon'] == coord]

    # meses = dados['mes'].unique().values
    dados = (dados.groupby(['mes'], as_index=False)['u2'].mean())
    
    fig = px.bar(dados, x='mes', y='u2')
    return fig


@app.callback(
    Output("rs_graph", 'figure'),
    [
        Input('interval-component', 'n_intervals'),
        Input('coord_dropdown', 'value'),
        Input('year_dropdown', 'value')
    ])
def update_chart(n_intervals, coord, year):
    from app import dados
    
    dados['latitude'] = dados['latitude'].astype(str)
    dados['longitude'] = dados['longitude'].astype(str)
    dados['lat_lon'] = dados['latitude'] + dados['longitude']

    dados = dados[dados['ano'] == year]
    dados = dados[dados['lat_lon'] == coord]

    # meses = dados['mes'].unique().values
    dados = (dados.groupby(['mes'], as_index=False)['rs'].mean())
    
    fig = px.bar(dados, x='mes', y='rs')
    return fig


@app.callback(
    Output("prec_graph", 'figure'),
    [
        Input('interval-component', 'n_intervals'),
        Input('coord_dropdown', 'value'),
        Input('year_dropdown', 'value')
    ])
def update_chart(n_intervals, coord, year):
    from app import dados
    
    dados['latitude'] = dados['latitude'].astype(str)
    dados['longitude'] = dados['longitude'].astype(str)
    dados['lat_lon'] = dados['latitude'] + dados['longitude']

    dados = dados[dados['ano'] == year]
    dados = dados[dados['lat_lon'] == coord]

    # meses = dados['mes'].unique().values
    dados = (dados.groupby(['mes'], as_index=False)['prec'].mean())
    
    fig = px.bar(dados, x='mes', y='prec')
    return fig


@app.callback(
    Output('temp_hist_graph', 'figure'),
    [
        Input('interval-component', 'n_intervals')
    ])
def update_chart(n_intervals):
    from app import dados

    dados_min = (dados.groupby(['ano'], as_index=False)['temperatura_min'].mean())
    dados_max = (dados.groupby(['ano'], as_index=False)['temperatura_max'].mean())

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=dados_min['ano'], y=dados_min['temperatura_min'],
                    mode='lines',
                    name='temperatura_min'))
    
    fig.add_trace(go.Scatter(x=dados_max['ano'], y=dados_max['temperatura_max'],
                    mode='lines',
                    name='temperatura_max'))

    return fig
