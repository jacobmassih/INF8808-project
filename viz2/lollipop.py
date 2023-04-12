import plotly.express as px
import pandas as pd

def create_lollipop(lolipop_data):
    # Read the data from the Excel file
    data = lolipop_data

    # Get the opponent names and their respective statistics
    opponents = data["Opponent"].tolist()
    possession_for = data["Possession For Argentina"].tolist()
    possession_against = [-1*x for x in data["Possession Against Argentina"].tolist()]
    passing_for = data["Passing Accuracy For Argentina"].tolist()
    passing_against = [-1*x for x in data["Passing Accuracy Against Argentina"].tolist()]
    shots_for = data["Shots On Target For Argentina"].tolist()
    shots_against = [-1*x for x in data["Shots On Target Against Argentina"].tolist()]
    saves_for = data["Saves For Argentina"].tolist()
    saves_against = [-1*x for x in data["Saves Against Argentina"].tolist()]
    cards_for = data["Cards For Argentina"].tolist()
    cards_against = [-1*x for x in data["Cards For Opponent"].tolist()]
    goals_for = data["Goal For Argentina"].tolist()
    goals_against = [-1*x for x in data["Goal Against Argentina"].tolist()]

    # Create the data frame
    df = pd.DataFrame({'Opponent': opponents*7,
                       'Statistic': ['Possession For Argentina']*len(opponents) + ['Possession Against Argentina']*len(opponents) + ['Passing Accuracy For Argentina']*len(opponents) + ['Passing Accuracy Against Argentina']*len(opponents) + ['Shots On Target For Argentina']*len(opponents) + ['Shots On Target Against Argentina']*len(opponents) + ['Saves For Argentina']*len(opponents) + ['Saves Against Argentina']*len(opponents) + ['Cards For Argentina']*len(opponents) + ['Cards Against Argentina']*len(opponents) + ['Goals For Argentina']*len(opponents) + ['Goals Against Argentina']*len(opponents),
                       'Value': possession_for + possession_against + passing_for + passing_against + shots_for + shots_against + saves_for + saves_against + cards_for + cards_against + goals_for + goals_against})

    # Create the lollipop chart
    fig = px.scatter(df, x="Opponent", y="Value", color="Statistic", symbol="Statistic", size="Value", size_max=20, hover_data=["Statistic", "Value"], labels={"Opponent": "Opponent", "Value": "Value"}, title="Performance comparison of Argentina and its opponents at the 2022 World Cup")

    return fig




