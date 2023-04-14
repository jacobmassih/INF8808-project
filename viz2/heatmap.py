import plotly.express as px
import assets.shared_styles.colors as colors

def create_heatmap(heatmap_data):
    colorscale = [[0, colors.SECONDARY_COLORS['lighter_gold']], [0.5, colors.SECONDARY_COLORS['light_gold']], [1, colors.PRIMARY_COLORS['gold']]]
    fig = px.imshow(heatmap_data.values,
                    x=heatmap_data.columns,
                    y=heatmap_data.index,
                    color_continuous_scale=colorscale,
                    text_auto=True, aspect="auto",
                    labels= dict(y='Opponent')
                    )
    fig.update_layout(
        title="Argentina Performance Metrics Heatmap\n\n",
        xaxis=dict(side='top'),
        dragmode=False,
    )
    return fig
