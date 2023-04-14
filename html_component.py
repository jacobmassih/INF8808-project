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
    
def viz2_html_heatmap(fig):
    markdown_title="""
    ## How did Argentina perform in each game?
    """
    markdown_text = """
     
    The Albiceleste started off on the wrong foot in the World Cup 2022, losing their first match as one of the tournament favorites against Saudi Arabia. However, they 
    soon picked up the pace and took the crown from reigning champions France. Argentina had an overall strong performance throughout the tournament.

    It should be noted that the save percentage against Poland is unavailable as Robert Lewandowski's side failed to take any shots on target, meaning no saves were necessary. 
    

    """
    return html.Div(className='page-container', children=[
        html.Div(className='app-container', children=[
            html.Div(className='graph-container', children=[
                dcc.Markdown(children=markdown_title),
                dcc.Markdown(children=markdown_text),
                dcc.Graph(
                    id='Heatmap',
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
    
def viz3_html(fig):
    markdown_title="""
    ## Which offensive player contributed the most to Argentina's success?
    """

    markdown_text = """
     
    Argentina is known for their offensive prowess with world-class players such as Lionel Messi and Angel Di Maria dominating any pitch they compete on. 
    In such manners, we have chosen 3 key metrics that best represent a well rounded attacking player.
    
    
    GCA (Goal-creating actions): The last two offensive actions directly leading to a goal. These can be passes, take-ons and drawing fouls.

    KP (Key passes): Passes that lead directly to a shot
    
    Gls (Goals): Number of goals scored by the player (penalty and non-penalties included)
    """
    # pour les fonts, checker dans asssets. on a 4 fonts dans le projet. si vous voulez dautres, faut download.
    style = {'font-family': 'Arial, sans-serif', 'font-size': '16px', 'text-align' : 'left'}
    return html.Div(className='page-container', children=[
        html.Div(className='app-container', children=[
            html.Div(className='graph-container', children=[
                dcc.Markdown(children=markdown_title),
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
    
# vy - i'll be right back if yall dont sleep
def viz4_html(fig):
    markdown_text = """
    ## What were Argentina's strengths and weaknesses?
    """
    return html.Div(className='page-container', children=[
        html.Div(className='app-container', children=[
            html.Div(className='graph-container', children=[
                dcc.Markdown(children=markdown_text),
                dcc.Graph(
                    id='radar-chart',
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