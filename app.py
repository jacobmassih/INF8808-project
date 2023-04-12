from dash import Dash, html, dcc, callback, Output, Input, State
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

import preprocess as preprocess
import viz1.bar_chart as bar_chart
import viz2.heatmap as heatmap
import viz2.lollipop as lollipop
import viz3.bubble_chart as bubble_chart
import viz4.radar_chart as radar_chart
import viz5.horizontal_bar_chart as horizontal_bar_chart
import html_component as html_component

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Projet 8808"

SCORES_AND_FIXTURES = pd.read_csv('./data/scores_and_fixtures.csv')
SHOOTING = pd.read_csv('./data/shooting.csv')
PASSING = pd.read_csv('./data/passing.csv')
GOAL_AND_SHOT_CREATION = pd.read_csv('./data/goal_and_shot_creation.csv')
DEFENSIVE = pd.read_csv('./data/defensive.csv')
GOALKEEPING = pd.read_csv('./data/goalkeeping.csv')
POSESSION = pd.read_csv('./data/possession.csv')
MatchReport = pd.read_excel('./data/MatchReport.xlsx')

@app.callback(
    [Output('bar-chart', 'figure'), Output('mode', 'children')],
    [Input('radio-items', 'value')],
    [State('bar-chart', 'figure')]
)
def radio_updated(mode, figure):
    new_fig = bar_chart.update_y_axis(figure, mode)
    new_fig = bar_chart.draw(new_fig, viz1_data, mode)

    return new_fig, mode

@app.callback(
    Output('bubble-chart', 'figure'),
    [Input('scroller', 'value')]
)
def update_figure(value):
    if value < 0.5:
        return bubble_chart.get_fig(viz3_data)
    else:
        return bubble_chart.get_default_fig()


# DATA
viz1_data = preprocess.viz1_get_results(SCORES_AND_FIXTURES)
viz2_data_heatmap = preprocess.viz2_get_MatchReport_for_heatmap(MatchReport)
viz2_data_lolipop = preprocess.viz2_get_MatchReport_for_lollipop(MatchReport)
viz3_data = preprocess.viz3_get_offensive_stats(SHOOTING, PASSING, GOAL_AND_SHOT_CREATION)
viz4_data = preprocess.viz4_get_stats(SHOOTING, PASSING, DEFENSIVE, GOALKEEPING, POSESSION)
viz5_data = preprocess.viz5_get_stats(SHOOTING)

# CHARTS
viz1 = bar_chart.init_figure()
viz2_heatmap = heatmap.create_heatmap(viz2_data_heatmap)
viz2_lollipop = lollipop.create_lollipop(viz2_data_lolipop)
viz3 = bubble_chart.get_fig(viz3_data)
viz4 = radar_chart.get_fig(viz4_data)
viz5 = horizontal_bar_chart.get_horizontal_bar_chart(viz5_data)


# Define the app layout
app.layout = html.Div(children=[
    html_component.welcome_page(),
    html_component.viz1_html(viz1),
    html_component.viz2_html_heatmap(viz2_heatmap),
    html_component.viz2_html_lollipop(viz2_lollipop),
    html_component.viz3_html(viz3),
    html_component.viz4_html(viz4),
    html_component.viz5_html(viz5)
])
