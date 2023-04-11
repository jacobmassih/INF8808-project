from dash import Dash, html, dcc, callback, Output, Input, State
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
# from dash_extensions import scroll

import preprocess as preprocess
import viz1.bar_chart as bar_chart
import viz2.heatmap as heatmap
import viz3.bubble_chart as bubble_chart
import html_component as html_component

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Projet 8808"


def preprocess_viz1():
    scores_and_fixtures_df = pd.read_csv('./data/scores_and_fixtures.csv')
    return preprocess.viz1_get_results(scores_and_fixtures_df)

# def preprocess_viz2():
#     MatchReport_df = pd.read_excel('./data/MatchReport.xlsx')
#     return preprocess.viz2_get_results(MatchReport_df)

def preprocess_viz3():
    shooting_df = pd.read_csv('./data/shooting.csv')
    passing_df = pd.read_csv('./data/passing.csv')
    gca_df = pd.read_csv('./data/goal_and_shot_creation.csv')
    off_res = preprocess.viz3_get_offensive_stats(
        shooting_df, passing_df, gca_df)
    return off_res

def app_layout(fig):
    return html.Div(className='app-page', children=[
        html_component.viz1_html(fig), html_component.viz3_html(
            bubble_chart.get_fig(viz3_data))
    ])


# TODO : viz2_layout, viz3_layout, etc...
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
    # determine which section of the scrollytelling the user is in
    # and update the figure based on that
    if value < 0.5:
        return bubble_chart.get_fig(viz3_data)
    else:
        return bubble_chart.get_default_fig()

# DATA
viz1_data = preprocess_viz1()
# viz2_data = preprocess_viz2()
viz3_data = preprocess_viz3()

# CHARTS
viz1 = bar_chart.init_figure()
# viz2 = heatmap.create_heatmap(viz2_data)
viz3 = bubble_chart.get_fig(viz3_data)

# Define the app layout
app.layout = html.Div(children=[
    html_component.welcome_page(),
    html_component.viz1_html(viz1),
    # html_component.viz2_html(viz2),
    html_component.viz3_html(viz3),

    # scroll(
    #     id='scroll',
    #     children=[
    #         html.Div([
    #             html.H2('Chart 1'),
    #             html.P('This is the first chart'),
    #             html.P('It shows some data'),
    #         ], id='chart-1-text'),
            
    #         html.Div([
    #             html.H2('Chart 2'),
    #             html.P('This is the second chart'),
    #             html.P('It shows some other data'),
    #         ], id='chart-2-text')
    #     ]
    # # )
])
