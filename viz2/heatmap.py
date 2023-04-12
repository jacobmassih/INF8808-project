import plotly.graph_objs as go

def create_heatmap(heatmap_data):
    # Create the heatmap trace
    heatmap_trace = go.Heatmap(z=heatmap_data.values,
                               x=heatmap_data.columns,
                               y=heatmap_data.index,
                               colorscale="Greens")

    # Set the layout for the plot
    layout = go.Layout(title="Argentina Performance Metrics Heatmap",
                       xaxis=dict(title="Metrics"),
                       yaxis=dict(title="Opponent"))

    # Create the figure and add the trace and layout
    fig = go.Figure(data=[heatmap_trace], layout=layout)
    fig.update_xaxes(side='top')

    return fig


