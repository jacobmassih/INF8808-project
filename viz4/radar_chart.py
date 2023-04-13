import plotly.graph_objects as go
# import numpy as np
import plotly.express as px
import pandas as pd
import plotly.io as pio
import assets.shared_styles.colors as colors


def get_fig(data):
    fig = go.Figure(data=go.Scatterpolar(
        r=[data['SoT%'][0], data['Cmp%'][0], data['TklW/Tkl'][0], data['G/Sh'][0], data['Save%'][0], data['Poss'][0]],
        theta=['Shots on target %','Pass completion %','Successful tackle %','Goal conversion rate', 'Save %', 'Possession'],
        fill='toself'

        ))

    fig.update_layout(
        template=pio.templates['ggplot2+viz4_template']
    )

    return fig