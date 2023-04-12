from dash import html, dcc
import dash_bootstrap_components as dbc
from viz1.modes import MODES

def welcome_page():
    return html.Div(className='welcome-page-container', children=[
        html.Div(className='upper-part', children=[
            html.Div(className='welcome-title', children=[
                'Examining Argentina\'s Performance in the 2023 World Cup: A Statistical Analysis'
            ])
        ]),
        html.Div(className='lower-part', children=[
            html.Div(className='welcome-text', children=[
                'INF8808'
            ]),
            html.Div(className='welcome-text', children=[
                'DATA VISUALIZATION'
            ])
        ]),
    ])

def viz1_html(fig):
    markdown_text = """
    ## What are Argentina's National Team's results from the 2022 World Cup?

    """
    return html.Div(className='page-container', children=[
        dcc.Markdown(children=markdown_text),
        html.Div(className='app-container', children=[
            html.Div(className='graph-container', children=[
                dcc.Graph(
                    className='graph',
                    figure=fig,
                    config=dict(
                        scrollZoom=False,
                        showTips=False,
                        showAxisDragHandles=False,
                        doubleClick=False,
                        displayModeBar=False
                    ),
                    id='bar-chart'
                )
            ]),
            html.Div(className='radio-group', children=[
                html.Div(className='radio-group-text', id='info', children=[
                    html.Span(MODES['goals'], id='mode', className='metric-text')
                ]),
                html.Div(className='radio-container', children=[
                    html.Div(className='radio-items', children=[                            
                        html.Span(
                            'Metric :',
                            style={
                                'margin-right': 10
                                }),
                        dcc.RadioItems(
                            id='radio-items',
                            options=[
                                dict(
                                    label=[
                                        MODES[mode],
                                        html.Span(style={
                                            'margin-right': 10
                                            })
                                        ],
                                    value=MODES[mode]) for mode in MODES
                            ],
                            value=MODES['goals'],
                            inline=True
                        )
                    ])
                ])
            ])
        ])
    ])
    
def viz3_html(fig):
    markdown_text = """
    ## Who are the players that have contributed the most to the team's success?

    """
    return html.Div(className='page-container', children=[
        html.Div(className='app-container', children=[
            html.Div(className='graph-container', children=[
                dcc.Markdown(children=markdown_text),
                dcc.Graph(
                    id='bubble-chart',
                    figure=fig,
                    config=dict(
                        scrollZoom=False,
                        showTips=False,
                        showAxisDragHandles=False,
                        doubleClick=False,
                        displayModeBar=False
                    ),
                )
            ])
        ])
    ])

def viz5_html(fig):
    markdown_text = """
    ## Who are the most efficient scorers?

    """
    return html.Div(className='page-container', children=[
        html.Div(className='app-container', children=[
            html.Div(className='graph-container', children=[
                dcc.Markdown(children=markdown_text),
                dcc.Graph(
                    id='horizontal-bar-chart',
                    figure=fig,
                    config=dict(
                        scrollZoom=False,
                        showTips=False,
                        showAxisDragHandles=False,
                        doubleClick=False,
                        displayModeBar=False
                    ),
                ),
            ])
        ])
    ])