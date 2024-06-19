from dash import html
import dash

dash.register_page(__name__, name='Page2', title='Page2 Demian')

layout = html.Div([
    html.H1('Seite 2'),
    html.P('Dies ist eine andere Seite des Dashboards.')
])
