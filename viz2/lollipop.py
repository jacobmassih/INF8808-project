import plotly.graph_objects as go

def create_lollipop(lollipop_data):  
    lollipop_data= lollipop_data.sort_values(by = ['Opponent'],
                    ascending = False).iloc[0:15].reset_index() 
    fig = go.Figure()
    fig.add_trace(go.Scatter(x = lollipop_data["Median_Performance"], 
                          y = lollipop_data["Opponent"],
                          mode = 'markers',
                          marker_color ='darkblue',
                          marker_size  = 10,
                          name = 'Median'))
    
    fig.add_trace(go.Scatter(x = lollipop_data["Mean_Performance"], 
                          y = lollipop_data["Opponent"],
                          mode = 'markers',
                          marker_color = 'darkorange', 
                          marker_size = 10,
                          name = 'Mean'))
    for i in range(0, len(lollipop_data)):
               fig.add_shape(type='line',
                              x0 = lollipop_data["Median_Performance"][i],
                              y0 = i,
                              x1 = lollipop_data["Mean_Performance"][i],
                              y1 = i,
                              line=dict(color='crimson', width = 3))
    fig.update_layout(title_text = 
                    "Argentina World Cup Performance",
                    title_font_size = 30)
    fig.update_xaxes(title = 'Performance' , range=[0, 79])
    fig.update_yaxes(autorange="reversed")
    return fig








