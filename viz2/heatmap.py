import pandas as pd
import plotly.graph_objs as go

def create_heatmap(pivot_table):
 
    # Create a list of lists for the data
    table_data = []
    for row in pivot_table.itertuples():
        table_data.append(list(row[1:]))

    # Create a list of column names
    column_names = list(pivot_table.columns)

    # Create color scale for the heatmap
    color_scale = [[0, '#FFFFFF'], [0.2, '#FFCCCC'], [0.5, '#FF6666'], [0.8, '#FF0000'], [1, '#660000']]

    # Create the table-like heatmap
    heatmap = go.Table(header=dict(values=column_names),
                       cells=dict(values=table_data, fill=dict(colorscale=color_scale, reversescale=True),
                                  font=dict(color='#000000'), format=[None] + ['{:.1f}%'] * 3 + ['{:.1f}']),
                       columnwidth=[1] * 5)

    # Set layout and return the heatmap
    layout = go.Layout(title="Comparison of Argentina's performance against its opponents")
    fig = go.Figure(data=[heatmap], layout=layout)
    return fig
