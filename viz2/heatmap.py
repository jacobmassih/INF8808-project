import plotly.express as px

def create_heatmap(heatmap_data):
    fig = px.imshow(heatmap_data.values,
                    x=heatmap_data.columns,
                    y=heatmap_data.index,
                    color_continuous_scale='Greens',
                    text_auto=True, aspect="auto",
                    labels= dict(x='Metrics', y='Opponent')
                    )
    fig.update_layout(title="Argentina Performance Metrics Heatmap",
                      xaxis=dict(side='top'))
    return fig




