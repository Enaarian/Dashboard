from dash import html
import dash_bootstrap_components as dbc

_footer = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([html.Hr([], className = 'hr-footer')], width = 12)
        ]),
        dbc.Row([
	        dbc.Col([], width = 1),
            dbc.Col(['Created with Plotly Dash'], width = 3),
            dbc.Col([], width =6),
	        dbc.Col([
                html.Ul([
                    html.Li([
                        html.A([ html.I(className="fa-brands fa-github me-3 fa-1x")],
                               href='https://github.com/Enaarian/Dashboard'),
                        html.A([ html.I(className="fa-brands fa-linkedin me-3 fa-1x")],
                               href='https://www.linkedin.com/in/micail-micon-k-75666a204/'),
                        html.A([ html.I(className="fa-brands fa-linkedin me-3 fa-1x")],
                               href='https://www.linkedin.com/in/max-pieper-96ba85299/'),
                        html.A([ html.I(className="fa-brands fa-linkedin me-3 fa-1x")],
                               href='https://www.linkedin.com/in/hugo-flückiger-a099b224b/')
                    ])
                ], className='list-unstyled d-flex justify-content-center justify-content-md-start')
            ], width = 2)
        ])
    ], fluid=True)
], className = 'footer')