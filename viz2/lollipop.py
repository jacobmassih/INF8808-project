import plotly.graph_objects as go
import plotly.express as px

def create_lollipop(lollipop_data):
    # reset the multi-level index to make it a regular dataframe with one-level index
    lollipop_data = lollipop_data.reset_index()

    # create the plot
    fig = go.Figure()

    # add markers and lines
    fig.add_trace(go.Scatter(x=lollipop_data['Value'], y=lollipop_data['Full Name Metric'], mode='markers+lines', marker=dict(symbol='circle', size=5), line=dict(width=2)))

    # add lollipop sticks
    fig.add_trace(go.Scatter(x=[lollipop_data['Value'].min(), lollipop_data['Value'].max()], y=[lollipop_data['Full Name Metric'], lollipop_data['Full Name Metric']], mode='lines', line=dict(color='gray', dash='dash')))

    # add title and axis labels
    fig.update_layout(
        title='Argentina World Cup Performance', 
        xaxis_title='Metric Value', yaxis_title='Full Name Metric',
        dragmode=False
    )

    return fig








