from app.server import app

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

layout = html.Div([

    html.Nav([
        html.Div([
            html.A([
                html.B('Agrotech4all')
            ], className='navbar-brand d-flex align-items-center', href='#')
        ], className='container'),
    ], className="navbar navbar-expand-lg navbar-light bg-light"),
    
    html.Div([
        html.Div([
            html.Div([
                html.H3(['Painel'], className='text-lead')
            ], className='col-md-12  mt-3')
        ], className='row'),
        
        html.Div([
            html.Div([
                html.H5(['Mapa das estações'], className=''),
                dcc.Loading([     
                    dcc.Graph(id='geo_graph', className="")
                ]),
            ], className='mt-3 col-md-6'),

            html.Div([
                dcc.Loading([
                    dcc.Graph(id='temp_hist_graph', className='')
                ]),
            ], className='mt-3 col-md-6')
        ], className='row'),

        html.Div([
            html.Div([
                html.P(['Coordenadas: ']),
                dcc.Dropdown(id='coord_dropdown'),
            ], className='mt-3 col-md-6'),
            html.Div([
                html.P(['Ano: ']),
                dcc.Dropdown(id='year_dropdown'),
            ], className='mt-3 col-md-6')
        ], className='row'),

        html.Div([
            html.Div([
                dcc.Loading([
                    html.H5(['Temperatura média por coordenada e ano'], className=''),
                    dcc.Graph(id='temperature_graph', className="col-12")
                ]),
            ], className='mt-3 col-md-12')
        ], className='row'),

        html.Div([
            html.Div([
                dcc.Loading([
                    html.H5(['ETO média por coordenada e ano'], className=''),
                    dcc.Graph(id='eto_graph', className="col-12")
                ]),
            ], className='mt-3 col-md-12')
        ], className='row'),

        html.Div([
            html.Div([
                dcc.Loading([
                    html.H5(['Precipicação média por coordenada e ano'], className=''),
                    dcc.Graph(id='prec_graph', className="col-12")
                ]),
            ], className='mt-3 col-md-12')
        ], className='row'),

        html.Div([
            html.Div([
                dcc.Loading([
                    html.H5(['U2 média por coordenada e ano'], className=''),
                    dcc.Graph(id='u2_graph', className="col-12")
                ]),
            ], className='mt-3 col-md-12')
        ], className='row'),

        html.Div([
            html.Div([
                dcc.Loading([
                    html.H5(['RS média por coordenada e ano'], className=''),
                    dcc.Graph(id='rs_graph', className="col-12")
                ]),
            ], className='mt-3 col-md-12')
        ], className='row')
    ], className='container')

], className="container-fluid overflow-hidden")
