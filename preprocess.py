import pandas as pd
import numpy as np


def viz1_get_results(scores_and_fixtures_df):
    scores_and_fixtures_df['Opponent'] = scores_and_fixtures_df['Opponent'].str.split(
        ' ', n=1).str[1]

    df = pd.DataFrame(
        scores_and_fixtures_df[['Opponent', 'Gls', 'xG', 'npxG']])
    df['npG'] = scores_and_fixtures_df['Gls'] - scores_and_fixtures_df['PK']

    df = df.rename(columns={
        "Gls": "Goals",
        'xG': "expected Goals",
        'npG': "Non Penalty Goals",
        'npxG': "expected Non Penalty Goals"
    })

    return df

# def viz2_get_results(MatchReport_df):
#     # Create a pivot table with mean values for each statistic
#     pivot_table = pd.pivot_table(MatchReport_df, values=["Possession", "Passing Accuracy", "Shots on Target", "Saves"],
#                     index="Opponent", aggfunc="mean")
#     return pivot_table


def viz3_get_offensive_stats(shooting_df, passing_df, gca_df):

    df = pd.concat([shooting_df, passing_df, gca_df], axis=1)
    df = df.loc[:, ~df.columns.duplicated()]
    df = df[['Player', 'Pos', 'Gls', 'KP', 'GCA']]
    df = df.iloc[:-2]
    df = df[df['Pos'].isin(['FW', 'MFFW', 'MF'])]
    df = df[df['KP'] != 0]
    return df

def viz5_get_stats(shooting_df):
    df = pd.DataFrame(shooting_df[['Player','Sh', 'Gls']])
    df['nGls'] = shooting_df['Sh'] - shooting_df['Gls']

    df = df.drop(df[df['Gls'] == 0].index)
    df = df.drop(df.tail(2).index)
    
    df = df.sort_values(['nGls', 'Gls'])

    return df