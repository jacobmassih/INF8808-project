import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import assets.shared_styles.colors as colors

def get_horizontal_bar_chart(df):

    fig = go.Figure()

    fig.add_trace(go.Bar(
        y= df['Player'], 
        x= df['nGls'],
        name='Non Scored Shots',
        orientation='h',
        marker=dict(
            color=colors.SECONDARY_COLORS['light_gold'],
        )
    ))
    
    fig.add_trace(go.Bar(
        y= df['Player'], 
        x= df['Gls'],
        name='Scored Shots',
        orientation='h',
        marker=dict(
            color=colors.SECONDARY_COLORS['light_navy_blue'],
        )
    ))

    fig.update_layout(barmode='stack')

    return fig

    
    