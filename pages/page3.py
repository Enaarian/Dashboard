# pages/page3.py
from dash import html, dcc, Input, Output, callback
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash

dash.register_page(__name__, name='Step Analyse', title='Step Analyse')

file_path = 'Sleep_health_and_lifestyle_dataset.csv'
df = pd.read_csv(file_path)

import assets.fig_layout as figy

avg_daily_steps = df.groupby('Occupation')['Daily Steps'].mean().reset_index()
avg_daily_steps = avg_daily_steps.sort_values(by='Daily Steps', ascending=True)

fig = px.bar(avg_daily_steps,
             x='Daily Steps',
             y='Occupation',
             orientation='h',
             #title='Durchschnittliche tägliche Schritte nach Beruf',
             labels={'Occupation': 'Beruf',
                     'Daily Steps': 'Durchschnittliche tägliche Schritte'},
             color='Daily Steps',
             # Farbpalette basierend auf den täglichen Schritten
             color_continuous_scale=px.colors.sequential.Bluered)  # Benutzerdefinierte Farbpalette
fig.update_layout(figy.my_figlayout,
    # title={
    #     'text': 'Durchschnittliche tägliche Schritte nach Beruf',
    #     'y': 0.95,
    #     'x': 0.5,
    #     'xanchor': 'center',
    #     'yanchor': 'top'},
    xaxis_title='Durchschnittliche tägliche Schritte',
    yaxis_title='Beruf',
    font=dict(
        family="Arial",
        size=12,
        color="white"
    ),
    height=600   # Größe des Plots anpassen
)

avg_daily_steps_value = avg_daily_steps['Daily Steps'].mean()

# Layout Dash

layout = html.Div([
    html.H1('Durchschnittliche tägliche Schritte nach Beruf'),
    dcc.Dropdown(
        id='avg-dropdown',
        options=[
            {'label': 'Durchschnittliche tägliche Schritte',
             'value': 'avg_daily_steps'}
        ],
        multi=True,
        placeholder='Durchschnittswerte auswählen',
        style={
            'backgroundColor': '#444',
            'color': '#f6f6f6',
            'border': '1px solid #555',
        },
        className='dcc-dropdown'
    ),
    dcc.Graph(
        id='daily-steps-graph',
        figure=fig
    ),
    html.Div(children='''
        In dieser Übersicht wird deutlich, dass Personen, die einer sitzenden Tätigkeit 
        nachgehen, im Vergleich zu Berufen, die körperliche Aktivität erfordern, wie 
        beispielsweise die Arbeit als Krankenschwester, signifikant weniger Schritte 
        am Tag machen. Dies zeigt, dass die Art der beruflichen Tätigkeit einen 
        erheblichen Einfluss auf das tägliche Bewegungsverhalten hat. Berufe, 
        die überwiegend im Sitzen ausgeübt werden, führen tendenziell zu einem 
        niedrigeren Aktivitätsniveau, während körperlich anstrengende Berufe mit 
        einer höheren Schrittzahl einhergehen.
    ''')
])


# Callback-Funktion zum Aktualisieren des Diagramms basierend auf Dropdown-Auswahl
@callback(
    Output('daily-steps-graph', 'figure'),
    [Input('avg-dropdown', 'value')]
)
def update_graph(selected_avg):
    fig = px.bar(avg_daily_steps,
                 x='Daily Steps',
                 y='Occupation',
                 orientation='h',
                 #title='Durchschnittliche tägliche Schritte nach Beruf',
                 labels={'Occupation': 'Beruf',
                         'Daily Steps': 'Durchschnittliche tägliche Schritte'},
                 color='Daily Steps',
                 # Farbpalette basierend auf den täglichen Schritten
                 color_continuous_scale=px.colors.sequential.Bluered)  # Benutzerdefinierte Farbpalette
    fig.update_layout(figy.my_figlayout,
        # title={
        #     'text': 'Durchschnittliche tägliche Schritte nach Beruf',
        #     'y': 0.95,
        #     'x': 0.5,
        #     'xanchor': 'center',
        #     'yanchor': 'top'},
        xaxis_title='Durchschnittliche tägliche Schritte',
        yaxis_title='Beruf',
        font=dict(
            family="Arial",
            size=12,
            color="white"
        ),
        height=600  # Größe des Plots anpassen
    )

    if selected_avg and 'avg_daily_steps' in selected_avg:
        fig.add_trace(
            go.Scatter(
                x=[avg_daily_steps_value] * len(avg_daily_steps),
                y=avg_daily_steps['Occupation'],
                mode='lines',
                name='Durchschnittliche tägliche Schritte',
                line=dict(dash="dash", color="#636EFA")
            )
        )

    return fig