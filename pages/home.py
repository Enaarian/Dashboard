import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', name='Home', title='Home')

layout = dbc.Container([
    # title
    dbc.Row([
        dbc.Col([
            html.H3(['Willkommen!']),
            html.P([html.B(['App Overview'])], className='par')
        ], width=12, className='row-titles')
    ]),
    # Guidelines
    dbc.Row([
        dbc.Col([], width = 2),
        dbc.Col([
            html.P([html.B('1) lol Teilüberschrift hier'),html.Br(),
                    'text hier'],
                   className='guide'),
            html.P([html.B('2) Teilüberschrift hier'),html.Br(),
                    'texthier --->> zeilenumbruch',html.Br(),
                    'text hier'],
                   className='guide'),
            html.P([html.B('3) Teilüberschrift hier'),html.Br(),
                    'texthier --->> zeilenumbruch',html.Br(),
                    'texthier --->> zeilenumbruch',html.Br(),
                    'text hier'],
                   className='guide'),
            html.P([html.B('4) Teilüberschrift hier'),html.Br(),
                    'texthier --->> zeilenumbruch',html.Br(),
                    'texthier --->> zeilenumbruch',html.Br(),
                    'text hier'],
                   className='guide')
        ], width = 8),
        dbc.Col([], width = 2)
    ])
])