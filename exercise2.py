# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

# static data
na_lcs_team = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
liquid = [13]
cloud9 = [11]
tsm = [9]
flyquest = [7]
goldenguardians = [6]
optic = [6]
clg = [5]
clutch = [5]
echofox = [4]
hundredthieves = [4]

# initialize Dash environment
app = dash.Dash(__name__)

# set up an layout
app.layout = html.Div(children=[
    # H1 title on the page
    html.H1(children='North America League of Legends Championship Series'),

    # a div to put a short description
    html.Div(children='''
        Week 8 Standings
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': [
                # set x to be the league, and y to be the team name. We use bars to represent our data.
                {'x': na_lcs_team, 'y': liquid, 'type': 'bar', 'name': 'Team Liquid'},
                {'x': na_lcs_team, 'y': cloud9, 'type': 'bar', 'name': 'Cloud 9'},
                {'x': na_lcs_team, 'y': tsm, 'type': 'bar', 'name': 'TSM'},
                {'x': na_lcs_team, 'y': flyquest, 'type': 'bar', 'name': 'FlyQuest'},
                {'x': na_lcs_team, 'y': goldenguardians, 'type': 'bar', 'name': 'Golden Guardians'},
                {'x': na_lcs_team, 'y': optic, 'type': 'bar', 'name': 'Optic'},
                {'x': na_lcs_team, 'y': clg, 'type': 'bar', 'name': 'CLG'},
                {'x': na_lcs_team, 'y': clutch, 'type': 'bar', 'name': 'Clutch Gaming'},
                {'x': na_lcs_team, 'y': echofox, 'type': 'bar', 'name': 'Echo Fox'},
                {'x': na_lcs_team, 'y': hundredthieves, 'type': 'bar', 'name': '100 Thieves'},


            ],
            # configure the layout of the visualization --
            # set the title to be "Usage of the BGT North of NE 70th per week day"
            'layout': {
                'title': 'NA LCS Week 8 Standings - Number of Wins'
            }
        }
    )
])

if __name__ == '__main__':
    # start the Dash app
    app.run_server(debug=True)


