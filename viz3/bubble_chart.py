import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import assets.shared_styles.colors as colors

def get_default_fig():
    return go.Figure()

def get_fig(data):
    fig = px.scatter(
            data_frame=data,
            x="Gls",
            y="GCA",
            custom_data=[data['KP']],
            range_x=[-2, 10],
            range_y=[-2, 10],
            color=data['Player'],
            size=data['KP'],
            size_max=60,
            hover_name=data['Player'],
            hover_data=['Player', 'KP']
        )

    fig.update_traces(
        {'marker': {'sizemin': 0}}
    )
    
    fig.update_layout(
        xaxis_title='Goals',
        yaxis_title='Goal-creating actions',
        template=pio.templates['simple_white'],
        dragmode=False
    )

    return fig
