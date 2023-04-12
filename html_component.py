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
    
def viz2_html(fig):
    markdown_title="""
    ## Against which team did Argentina have the least difficulty during the 2022 World Cup?
    """
    markdown_text = """
     
    This data visualization compares Argentina's performance against its opponents during the 2022 World Cup, 
    focusing on four key metrics: possession, passing accuracy, shots on target, saves, Cards and Goals. Overall, Argentina had a strong performance in the tournament, winning X out of Y matches and scoring Z goals.
    
    
    The distance calculation can be effective in identifying the opponent which the Argentina team has the most difficulty to win against.
    By using z-scores to standardize the selected features and then computing the distance from the reference point 
    (in this case, the mean values of the selected features), we was able to identify the opponents that are furthest from the mean and therefore more challenging for Argentina to beat.
    The larger the distance, the more difficult it may be for Argentina to win against that opponent based on the selected features.
    The heatmap is sorted base on this Distance value that is calculate  with the stats library from scipy.
    
    In terms of possession, Argentina generally dominated its opponents, with an average possession of 57,43%. 
    The team's passing accuracy was also quite high, with an average of 84%. 
    When it came to shots on target, Argentina also performed well, with an average of 44,29%.

    Overall, this data suggests that Argentina had a solid performance in the 2022 World Cup, but faced varying levels of difficulty depending on the opponent. 
    Going forward, the team may want to focus on maintaining its strong possession and passing accuracy stats, while also developing strategies to improve its performance in matches where opponents are able to challenge its dominance."
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
    ## VIZ4 
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