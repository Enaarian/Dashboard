import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)


app.layout = html.Div(children=[
    html.H1(children='Überschrift des Dashboards'),

    html.Div(children='''
        Bespiel Text
    ''')
])


if __name__ == '__main__':
    app.run_server(debug=True)
