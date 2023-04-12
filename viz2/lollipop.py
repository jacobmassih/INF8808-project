import plotly.express as px
import pandas as pd

def create_lollipop(lolipop_data):
    # Read the data from the Excel file
    data = lolipop_data

    # Get the opponent names and their respective statistics
    opponents = data["Opponent"].tolist()
    possession_for = data["Possession For Argentina"].tolist()
    possession_against = data["Possession Against Argentina"].tolist()
    passing_for = data["Passing Accuracy For Argentina"].tolist()
    passing_against = data["Passing Accuracy Against Argentina"].tolist()
    shots_for = data["Shots On Target For Argentina"].tolist()
    shots_against = data["Shots On Target Against Argentina"].tolist()
    saves_for = data["Saves For Argentina"].tolist()
    saves_against = data["Saves Against Argentina"].tolist()
    Goal_Per_Shot_for = data["Goal per Shot For Argentina"].tolist()
    Goal_Per_Shot_against = data["Goal per Shot Against Argentina"].tolist()

    # Check the length of each array
    array_lengths = [len(x) for x in [opponents, possession_for, possession_against, passing_for, passing_against, shots_for, shots_against, saves_for, saves_against, Goal_Per_Shot_for, Goal_Per_Shot_against]]
    if len(set(array_lengths)) != 1:
        raise ValueError("All arrays must be of the same length")

    # Create the data frame
    df = pd.DataFrame({'Opponent': opponents*10,
                    'Statistic': ['Possession For Argentina']*len(opponents) + ['Possession Against Argentina']*len(opponents) + ['Passing Accuracy For Argentina']*len(opponents) + ['Passing Accuracy Against Argentina']*len(opponents) + ['Shots On Target For Argentina']*len(opponents) + ['Shots On Target Against Argentina']*len(opponents) + ['Saves For Argentina']*len(opponents) + ['Saves Against Argentina']*len(opponents) + ['Goal per Shot For Argentina']*len(opponents) + ['Goal per Shot Against Argentina']*len(opponents),
                    'Value': possession_for + possession_against + passing_for + passing_against + shots_for + shots_against + saves_for + saves_against + Goal_Per_Shot_for + Goal_Per_Shot_against })

    # Add a new column for the marker color based on whether the value is positive or negative
    df['Color'] = ['green' if x >= 0 else 'red' for x in df['Value']]

    # Create the scatter plot
    fig = px.scatter(df, x='Opponent', y='Value', color='Color', size='Value', size_max=20,
                 labels={'Opponent':'Opponent', 'Value':'Value'},
                 title='Performance comparison of Argentina and its opponents at the 2022 World Cup')

    fig.update_traces(mode='markers+text', textposition='middle right', textfont_size=10,
                    marker=dict(line=dict(width=1, color='DarkSlateGrey')))
    fig.update_xaxes(showgrid=False, tickangle=45)
    fig.update_yaxes(showgrid=True, gridcolor='LightGrey')
    fig.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01))
    return fig







