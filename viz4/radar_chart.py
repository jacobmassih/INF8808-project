import plotly.graph_objects as go
import numpy as np


def get_fig(data):
    
    # Define the categories
    categories = ['SoT%', 'Cmp%', 'TklW%', 'GCR', 'Save%', 'Poss']
    data = [90, 75, 82, 80, 85]
    # Define the angles for the custom angular axis
    angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)

    # Add the first category to the end of the list to close the polygon
    categories = categories + [categories[0]]
    data = data + [data[0]]
    
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=data,
        theta=categories,
        fill='toself',
        line=dict(color='#000000'),
        subplot='polar1'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            ),
            angularaxis=dict(
                direction='clockwise',
                tickmode='array',
                tickvals=angles,
                ticktext=[''] + categories[:-1] + [''],
                rotation=30,
                showline=False,
                showgrid=True
            ),
            sector=[0, 2*np.pi],
        ),
        showlegend=False
    )

    return fig