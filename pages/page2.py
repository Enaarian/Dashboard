from dash import html, dcc
import dash
import plotly.graph_objects as go
import pandas as pd

dash.register_page(__name__, name='Stress Analyse', title='Stress')

import assets.fig_layout as figy
# Daten einlesen und aggregieren

data = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
aggregated_data = data[["Occupation", "Stress Level", "Quality of Sleep"]].groupby("Occupation").mean().reset_index()

# Balkendiagramm erstellen
fig = go.Figure()

fig.add_trace(go.Bar(
    x=aggregated_data['Occupation'],
    y=aggregated_data['Stress Level'],
    name='Stress Level',
    marker_color='#EF553B',
    marker_line_width=0
))

fig.add_trace(go.Bar(
    x=aggregated_data['Occupation'],
    y=aggregated_data['Quality of Sleep'],
    name='Quality of Sleep',
    marker_color='#636EFA',
    marker_line_width=0
))

# Layout anpassen
fig.update_layout(figy.my_figlayout,
    title='Verhältnis Stresslevel und Schlafqualität nach Beruf',
    xaxis_title='Beruf',
    yaxis_title='Level (Stresslevel und Schlafqualität)',
    barmode='group',
    yaxis=dict(range=[0, 10], showgrid=False)
)


layout = html.Div([
    html.H1('Stress- und Schlafanalyse nach Beruf'),
    dcc.Graph(
        id='stress-sleep-analysis-graph',
        figure=fig
    ),
    html.Div(children='''
        Das Balkendiagramm zeigt das Verhältnis von Stresslevel und Schlafqualität für verschiedene Berufsgruppen. 
        Die x-Achse listet die Berufe auf, während die y-Achse die Werte für Stresslevel (Skala 1-10) und Schlafqualität 
        (Skala 1-10) darstellt. 
        Die roten Balken repräsentieren das Stresslevel und die blauen Balken die Schlafqualität.
        Diese Analyse bietet Einblicke in den Zusammenhang zwischen Stress und Schlaf in 
        verschiedenen Berufsgruppen um gezielte Gesundheitsmaßnahmen zu unterstützen.
    ''')
])
