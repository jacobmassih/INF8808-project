'''
    Creates the theme to be used in our bar chart.
'''
import plotly.graph_objects as go
import plotly.io as pio

from assets.shared_styles.colors import PRIMARY_COLORS, BACKGROUND_COLOR

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
        go.Bar(marker_color = PRIMARY_COLORS[color]) for color in PRIMARY_COLORS
    ]
    
    # TODO: viz2_template, etc