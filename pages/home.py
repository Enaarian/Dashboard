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
        dbc.Col([], width=2),
        dbc.Col([
            html.P([html.B('1. Willkommen auf unserem interaktiven Dashboard'),
                    html.Br(),
                    'Dieses Dashboard bietet eine umfassende Übersicht über die wichtigsten Kennzahlen und '
                    'Analysen unseres Projekts. Hier könnt ihr die Daten einsehen und verschiedene '
                    'Visualisierungen nutzen, um tiefere Einblicke zu gewinnen.', html.Br(), html.Br()],
                   className='guide'),
            html.P([html.B('2. Thema: Schlaf, Gesundheit und Lebensstil'),
                    html.Br(),
                    'Datensatz: ',
                    dbc.Button("Kaggle Dataset",
                               href='https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset',
                               color="primary",
                               target="_blank",
                               className='dbc-button'
                               ), html.Br(), html.Br(),
                    html.U('Beschreibung des Datensatzes:'), html.Br(),
                    'Der Sleep Health and Lifestyle Datensatz umfasst 374 '
                    'Einträge und 13 Variablen zu Schlaf und Alltagsgewohnheiten. '
                    'Enthalten sind Informationen wie Geschlecht, Alter, Beruf, Schlafdauer, '
                    'Schlafqualität, körperliche Aktivität, Stresslevel, BMI-Kategorie, '
                    'Blutdruck, Herzfrequenz, tägliche Schritte und das '
                    'Vorhandensein von Schlafstörungen.', html.Br(), html.Br(),
                    html.U('Hinweis:'), html.Br(),
                    'Der Datensatz besteht aus rein fiktiven Daten.', html.Br(), html.Br()],
                   className='guide'),
            html.P([html.B('3. Mitwirkende:'), html.Br(),
                    html.U('Micail Micon Kruse'), ': Head of Planning and '
                                                  'Implementation, Dashboard, Code Description and '
                                                  'Visualization', html.Br(),
                    html.U('Max Pieper'), ': Head of Presentation and Animation',
                    html.Br(),
                    html.U('Demian in den Birken'), ': Head of Code '
                                                    'Description and '
                                                    'Visualization', html.Br(),
                    html.U('Hugo Flückiger'), ': Head of Code Description and '
                                              'Visualization', html.Br(), html.Br(), ],
                   className='guide'),
        ], width=8),
        dbc.Col([], width=2)
    ])
])
