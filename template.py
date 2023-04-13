'''
    Creates the theme to be used in our bar chart.
'''
import plotly.graph_objects as go
import plotly.io as pio
import assets.shared_styles.colors as colors

def create_template():
    '''
        Adds a new layout template to pio's templates.

        The template sets the font color and
        font to the values defined above in
        the THEME dictionary.

        The plot background and paper background
        are the background color defined
        above in the THEME dictionary.

        Also, sets the hover label to have a
        background color and font size
        as defined for the label in the THEME dictionary.
        The hover label's font color is the same
        as the theme's overall font color. The hover mode
        is set to 'closest'.

        Also sets the colors for the bars in
        the bar chart to those defined in
        the THEME dictionary.

    '''
    # Define a theme as defined above
    pio.templates['viz1_template'] = go.layout.Template()
    
    pio.templates['viz1_template'].data.bar = [
        go.Bar(marker_color = colors.PRIMARY_COLORS[color]) for color in colors.PRIMARY_COLORS
    ]

    #VIZ 4
    template = go.layout.Template({
    'data': {
        'scatterpolar': [{
            'line': {'color': colors.PRIMARY_COLORS['blue'] },
            'marker': {'color': colors.PRIMARY_COLORS['navy_blue']},
        }],
    },
    'layout': {
        'polar': {
            'radialaxis': {
                'range': [0, 100],
                'tickvals': [20, 40, 60, 80, 100],
            },
            'angularaxis': {
                'tickfont': {'size': 12},
                'direction':"clockwise", # Set the direction of rotation
                'rotation': 30 # Set the rotation angle in degrees
            },
        },
        'font': {'size': 14},
        'showlegend': False,
        'dragmode': False,
        'width':600, 
        'height':600
    },
    })
    
    pio.templates['viz4_template'] = template
    
    # TODO: viz2_template, etc