import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import pandas as pd
import plotly.express as px

import base64

df = pd.read_csv('data_covid_indo.csv')
df['Date'] = pd.to_datetime(df['Date'])
nan_df = df[df.isna().any(axis=1)]
df = df.dropna(how='all')
df = df.drop(df[df['Location'] == 'Indonesia'].index)

app = dash.Dash(
    external_stylesheets=[dbc.themes.CYBORG],
    name = 'covid 19'
)

app.title = 'COVID-19.Exploratory Dashbord Analytics'

path_img = 'image.png'
encode = base64.b64encode(open(path_img, 'rb').read()).decode('ascii')

# Jumbotron
jumbotron = html.Div(
    dbc.Container(
        [
            html.H1("COVID-19 Cases In Indonesia", className="display-3"),
            html.P(
                "Interactive Dashboard Analysis COVID-19 in Indonesia",
                className="lead",
            ),
            html.Hr(className="my-2"),
            html.P(
                "Use this dashboard and get the insight!"
            ),
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-light rounded-3",
)

pilihan = dbc.Tabs([
            dbc.Tab(
                dcc.Graph(
                    id='plotisland',
                ),
                label='Island'),

            dbc.Tab(
                dcc.Graph(
                    id='plotlocation',
                ),
                label='Location'),
        ])

title_line = dcc.Markdown(children='')
dropdown_line = dcc.Dropdown(id='choose', 
                        options = ['New Cases', 'New Deaths', 'New Recovered'],
                        value='New Cases')

### CARD CONTENT
new_cases = [
    dbc.CardHeader('Positive Cases'),
    dbc.CardBody([
        html.H1([df['New Cases'].sum()])
    ]),
]

new_deaths = [
    dbc.CardHeader('Deaths'),
    dbc.CardBody([
        html.H1(df['New Deaths'].sum())
    ]),
]
new_recovered = [
    dbc.CardHeader('Recovered'),
    dbc.CardBody([
        html.H1(df['New Recovered'].sum())
    ]),
]
sisa = df['New Cases'].sum() - (df['New Deaths'].sum() + df['New Recovered'].sum())
still = [
    dbc.CardHeader('Positive'),
    dbc.CardBody([
        html.H1(sisa)
    ]),
]


title_bar = dcc.Markdown(children='')
graph_bar = dcc.Graph(figure={})
dropdown_bar = dcc.Dropdown(options = ['New Cases', 'New Deaths', 'New Recovered'],
                        value='New Cases',  
                        clearable=False)

title_pie = dcc.Markdown(children='')
graph_pie = dcc.Graph(figure={})
dropdown_pie = dcc.Dropdown(options = ['New Cases', 'New Deaths', 'New Recovered'],
                        value='New Cases',  
                        clearable=False)


title_bar_loc = dcc.Markdown(children='')
graph_bar_loc = dcc.Graph(figure={})
dropdown_bar_loc = dcc.Dropdown(options = ['New Cases', 'New Deaths', 'New Recovered'],
                        value='New Cases', 
                        clearable=False)

title_pie_loc = dcc.Markdown(children='')
graph_pie_loc = dcc.Graph(figure={})
dropdown_pie_loc = dcc.Dropdown(options = ['New Cases', 'New Deaths', 'New Recovered'],
                        value='New Cases', 
                        clearable=False)




results_bar_cases_island = df.groupby('Island').sum().sort_values(by='New Cases', ascending=False)
fig_bar_cases_island = px.bar(results_bar_cases_island, x=results_bar_cases_island.index, y='New Cases', text_auto='.2s')

results_bar_deaths_island = df.groupby('Island').sum().sort_values(by='New Deaths', ascending=False)
fig_bar_deaths_island = px.bar(results_bar_deaths_island, x=results_bar_deaths_island.index, y='New Deaths', text_auto='.2s')

results_bar_recovered_island = df.groupby('Island').sum().sort_values(by='New Recovered', ascending=False)
fig_bar_recovered_island = px.bar(results_bar_recovered_island, x=results_bar_recovered_island.index, y='New Deaths', text_auto='.2s')

results_pie_cases_island = df.groupby('Island').sum().iloc[0:9].sort_values(by=['New Cases'], ascending=False)
fig_pie_cases_island = px.pie(results_pie_cases_island, values='New Cases', names=results_pie_cases_island.index)

results_pie_deaths_island = df.groupby('Island').sum().iloc[0:9].sort_values(by=['New Deaths'], ascending=False)
fig_pie_deaths_island = px.pie(results_pie_deaths_island, values='New Deaths', names=results_pie_deaths_island.index)

results_pie_recovered_island = df.groupby('Island').sum().iloc[0:9].sort_values(by=['New Recovered'], ascending=False)
fig_pie_recovered_island = px.pie(results_pie_recovered_island, values='New Recovered', names=results_pie_recovered_island.index)


results_bar_cases_loc = df.groupby('Location').sum().sort_values(by='New Cases', ascending=False).iloc[0:9]
fig_bar_cases_loc = px.bar(results_bar_cases_loc, x=results_bar_cases_loc.index, y='New Cases', text_auto='.2s')

results_bar_deaths_loc = df.groupby('Location').sum().sort_values(by='New Deaths', ascending=False).iloc[0:9]
fig_bar_deaths_loc = px.bar(results_bar_deaths_loc, x=results_bar_deaths_loc.index, y='New Deaths', text_auto='.2s')

results_bar_recovered_loc = df.groupby('Location').sum().sort_values(by='New Recovered', ascending=False).iloc[0:9]
fig_bar_recovered_loc = px.bar(results_bar_recovered_loc, x=results_bar_recovered_loc.index, y='New Deaths', text_auto='.2s')


results_pie_cases_loc = df.groupby('Location').sum().iloc[0:9].sort_values(by=['New Cases'], ascending=False)
fig_pie_cases_loc = px.pie(results_pie_cases_loc, values='New Cases', names=results_pie_cases_loc.index)

results_pie_deaths_loc = df.groupby('Location').sum().iloc[0:9].sort_values(by=['New Deaths'], ascending=False)
fig_pie_deaths_loc = px.pie(results_pie_deaths_loc, values='New Deaths', names=results_pie_deaths_loc.index)

results_pie_recovered_loc = df.groupby('Location').sum().iloc[0:9].sort_values(by=['New Recovered'], ascending=False)
fig_pie_recovered_loc = px.pie(results_pie_recovered_loc, values='New Recovered', names=results_pie_recovered_loc.index)


app.layout = html.Div([
    jumbotron,
    html.Br(),
    # navbar,
    dbc.Card(
        dbc.CardBody([
            html.H4('Background and Trend Of Covid-19', className="card-title", style={'textAlign': 'center'}),
        ]),

            ),
    html.Br(),

    #ROW 1
    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H5('Covid-19', className="card-title", style={'textAlign': 'center'}),
                    html.Div(html.Img(src='data:image/png;base64,{}'.format(encode))),
                    html.Br(),
                    html.P(
                        '''Coronavirus disease 2019 (COVID-19) is a contagious disease caused by a virus, the severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The first known case was identified in Wuhan, China, in December 2019.The disease quickly spread worldwide, resulting in the COVID-19 pandemic.
                            Symptoms of COVID‑19 are variable, but often include fever, cough, headache, fatigue, breathing difficulties, loss of smell, and loss of taste.Symptoms may begin one to fourteen days after exposure to the virus.''',
                        className="card-text",),
                    html.Br(),
                    dbc.CardLink("source from wikipedia", href="https://en.wikipedia.org/wiki/COVID-19", target="_blank"),
                ])
            )
        ]),
        dbc.Col([
            dbc.Card([
               dbc.Col([
                html.Br(),
                dbc.CardHeader([title_line], style={'textAlign': 'center'}),
                dbc.Container([pilihan,dropdown_line]),
                html.Br(),
            ]),
            ])
        ])
    ]),

    html.Br(),
    #ROW 2
    dbc.Row([
        dbc.Col([
            dbc.Card(new_cases)
        ]),
        dbc.Col([
            dbc.Card(new_deaths)
        ]),
        dbc.Col([
            dbc.Card(new_recovered)
        ]),
        dbc.Col([
            dbc.Card(still)
        ])
    ]),

    html.Br(),
    html.Hr(className="my-2"),
    html.Br(),
    # Row 3
    dbc.Row([
        dbc.Card(
                dbc.CardBody([
                    html.H5('Analysis Based On Island', className="card-title", style={'textAlign': 'center'}),
                ]),

            )
    ]),

    html.Br(),
    #ROW 4
    dbc.Row([
        dbc.Col([
            dbc.Card(
                html.Div([
                    html.Br(),
                    dbc.CardHeader([title_bar], style={'textAlign': 'center'}),
                    dbc.Container([dropdown_bar, graph_bar]),
                    html.Br(),
                ])
            )
        ]),
        dbc.Col([
            dbc.Card(html.Div([
                    html.Br(),
                    dbc.CardHeader([title_pie], style={'textAlign': 'center'}),
                    dbc.Container([dropdown_pie, graph_pie]),
                    html.Br(),
                ])
            )
        ])
    ]),


    html.Br(),
    html.Hr(className="my-2"),
    html.Br(),
    # Row 5
    dbc.Row([
        dbc.Card(
                dbc.CardBody([
                    html.H5('Analysis Based On Location', className="card-title", style={'textAlign': 'center'}),
                ]),

            )
    ]),

    html.Br(),
    #ROW 6
    dbc.Row([
        dbc.Col([
            dbc.Card(
                html.Div([
                    html.Br(),
                    dbc.CardHeader([title_bar_loc], style={'textAlign': 'center'}),
                    dbc.Container([dropdown_bar_loc, graph_bar_loc]),
                    html.Br(),
                ])
            )
        ]),
        dbc.Col([
            dbc.Card(html.Div([
                    html.Br(),
                    dbc.CardHeader([title_pie_loc], style={'textAlign': 'center'}),
                    dbc.Container([dropdown_pie_loc, graph_pie_loc]),
                    html.Br(),
                ])
            )
        ])
    ]),

    html.Br(),

    #ROW7
    dbc.Col([
        dbc.Card([
            html.H6('Create By : Ilham Fikriansyah')
        ]),
    ])

])

@app.callback(
    Output(component_id='plotisland', component_property='figure'),
    Input(component_id='choose', component_property='value')
)

def update_plot(cases_name):
    if cases_name == "New Cases":
        fig_line_island = px.line(df, x='Date', y='New Cases', color="Island")
    elif  cases_name == "New Deaths" :
        fig_line_island = px.line(df, x='Date', y='New Deaths', color="Island")
    elif  cases_name == "New Recovered" :
        fig_line_island = px.line(df, x='Date', y='New Recovered', color="Island")
    return fig_line_island

@app.callback(
    Output(component_id='plotlocation', component_property='figure'),
    Input(component_id='choose', component_property='value')
)

def update_plot(cases_name):
    if cases_name == "New Cases":
        fig_line_loc = px.line(df, x='Date', y='New Cases', color="Location")
    elif  cases_name == "New Deaths" :
        fig_line_loc = px.line(df, x='Date', y='New Deaths', color="Location")
    elif  cases_name == "New Recovered" :
        fig_line_loc = px.line(df, x='Date', y='New Recovered', color="Location")
    return fig_line_loc

@app.callback(
    Output(title_line, component_property ='children'),
    Input(dropdown_line, component_property =  'value'))

def update_title(column_name):
    if column_name == 'New Cases':
        name = 'Positve Cases'
    elif column_name == 'New Deaths':
        name = 'Deaths'
    elif column_name == 'New Recovered':
        name = 'Recovered'
    return f'''Trend of Covid-19 Based on Time (by : {name})'''

@app.callback(
    Output(graph_bar, component_property ='figure'),
    Input(dropdown_bar, component_property = 'value'))

def update_graph(user_input):
    if user_input == 'New Cases':
        fig = fig_bar_cases_island
    elif user_input == 'New Deaths':
        fig = fig_bar_deaths_island
    elif user_input == 'New Recovered':
        fig = fig_bar_recovered_island
    return fig

@app.callback(
    Output(title_bar, component_property ='children'),
    Input(dropdown_bar, component_property =  'value'))

def update_title(column_name):
    if column_name == 'New Cases':
        name = 'Cases'
    elif column_name == 'New Deaths':
        name = 'Deaths'
    elif column_name == 'New Recovered':
        name = 'Recovered'
    return f'''Value Based on Islands (by : {name}) '''

@app.callback(
    Output(graph_pie, component_property ='figure'),
    Input(dropdown_pie, component_property =  'value'))

def update_graph(user_input):
    if user_input == 'New Cases':
        fig = fig_pie_cases_island
    elif user_input == 'New Deaths':
        fig = fig_pie_deaths_island
    elif user_input == 'New Recovered':
        fig = fig_pie_recovered_island
    return fig

@app.callback(
    Output(title_pie, component_property ='children'),
    Input(dropdown_pie, component_property =  'value'))

def update_title(column_name):
    if column_name == 'New Cases':
        name = 'Positive Cases'
    elif column_name == 'New Deaths':
        name = 'Deaths'
    elif column_name == 'New Recovered':
        name = 'Recovered'
    return f'''Percentage Based on Islands (by : {name}).'''

@app.callback(
    Output(graph_bar_loc, component_property ='figure'),
    Input(dropdown_bar_loc, component_property = 'value'))

def update_graph(user_input):
    if user_input == 'New Cases':
        fig = fig_bar_cases_loc
    elif user_input == 'New Deaths':
        fig = fig_bar_deaths_loc
    elif user_input == 'New Recovered':
        fig = fig_bar_recovered_loc
    return fig

@app.callback(
    Output(title_bar_loc, component_property ='children'),
    Input(dropdown_bar_loc, component_property =  'value'))

def update_title(column_name):
    if column_name == 'New Cases':
        name = 'Positive Cases'
    elif column_name == 'New Deaths':
        name = 'Deaths'
    elif column_name == 'New Recovered':
        name = 'Recovered'
    return f'''Value Based on 10 Locations highest (by : {name})'''

@app.callback(
    Output(graph_pie_loc, component_property ='figure'),
    Input(dropdown_pie_loc, component_property =  'value'))

def update_graph(user_input):
    if user_input == 'New Cases':
        fig = fig_pie_cases_loc
    elif user_input == 'New Deaths':
        fig = fig_pie_deaths_loc
    elif user_input == 'New Recovered':
        fig = fig_pie_recovered_loc
    return fig

@app.callback(
    Output(title_pie_loc, component_property ='children'),
    Input(dropdown_pie_loc, component_property =  'value'))

def update_title(column_name):
    if column_name == 'New Cases':
        name = 'Positive Cases'
    elif column_name == 'New Deaths':
        name = 'Deaths'
    elif column_name == 'New Recovered':
        name = 'Recovered'
    return f'''Percentage Based on 10 Locations highest (by : {name})'''



if __name__ == "__main__":
    app.run_server()
