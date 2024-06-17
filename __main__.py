import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
sleep_occ = df[["Occupation", "Sleep Duration", "Quality of Sleep"]].groupby("Occupation").mean().reset_index()


fig = px.bar(
    sleep_occ,
    x="Occupation",
    y=["Sleep Duration", "Quality of Sleep"],
    labels={"Occupation": "Beruf", "value": "Wert", "variable": "Metrik"},
    title="Schlafanalyse nach Beruf",
    barmode="group",
    color_discrete_sequence=["#636EFA", "#EF553B"]
)


fig.update_layout(
    legend_title_text='Metrik',
    title={
        'text': "Schlafanalyse nach Beruf",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title="Beruf",
    yaxis_title="Durchschnittswerte",
    template="plotly_white"
)


avg_sleep_duration = sleep_occ["Sleep Duration"].mean()
avg_quality_sleep = sleep_occ["Quality of Sleep"].mean()

app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='Überschrift des Dashboards'),

    html.Div(children='''
        Dies ist ein Beispiel für ein Dashboard mit Dash.
        Sie können hier zusätzlichen Text hinzufügen, um Informationen zu präsentieren.
    '''),

    dcc.Dropdown(
        id='avg-dropdown',
        options=[
            {'label': 'Durchschnittliche Schlafdauer', 'value': 'avg_sleep_duration'},
            {'label': 'Durchschnittliche Schlafqualität', 'value': 'avg_quality_sleep'}
        ],
        multi=True,
        placeholder='Durchschnittswerte auswählen'
    ),

    dcc.Graph(
        id='sleep-analysis-graph',
        figure=fig
    )
])

@app.callback(
    Output('sleep-analysis-graph', 'figure'),
    Input('avg-dropdown', 'value')
)
def update_graph(selected_avg):
    fig = px.bar(
        sleep_occ,
        x="Occupation",
        y=["Sleep Duration", "Quality of Sleep"],
        labels={"Occupation": "Beruf", "value": "Wert", "variable": "Metrik"},
        title="Schlafanalyse nach Beruf",
        barmode="group",
        color_discrete_sequence=["#636EFA", "#EF553B"]
    )

    fig.update_layout(
        legend_title_text='Metrik',
        title={
            'text': "Schlafanalyse nach Beruf",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Beruf",
        yaxis_title="Durchschnittswerte",
        template="plotly_white"
    )

    if selected_avg:
        if 'avg_sleep_duration' in selected_avg:
            fig.add_trace(
                go.Scatter(
                    x=sleep_occ["Occupation"],
                    y=[avg_sleep_duration] * len(sleep_occ),
                    mode="lines",
                    name="Durchschnittliche Schlafdauer",
                    line=dict(dash="dash", color="#636EFA")
                )
            )
        if 'avg_quality_sleep' in selected_avg:
            fig.add_trace(
                go.Scatter(
                    x=sleep_occ["Occupation"],
                    y=[avg_quality_sleep] * len(sleep_occ),
                    mode="lines",
                    name="Durchschnittliche Schlafqualität",
                    line=dict(dash="dash", color="#EF553B")
                )
            )

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

