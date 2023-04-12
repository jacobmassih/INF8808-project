import pandas as pd
import numpy as np
from scipy import stats


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

def viz2_get_MatchReport_for_heatmap(MatchReport_df):
    
    #Drop column not need for the heatmap
    heatmap_data = MatchReport_df.drop(['Possession Against Argentina','Passing Accuracy Against Argentina','Shots On Target Against Argentina','Saves Against Argentina','Goal For Argentina ','Goal per Shot Against Argentina'], axis=1)
    
    #Transfor column Goal per Shot for Argentina to have the percentage as all data here are in percentage
    heatmap_data['Goal per Shot For Argentina'] = heatmap_data['Goal per Shot For Argentina'].apply(lambda x: x * 100)
    
    # rename the columns to be used in the heatmap 
    heatmap_data = heatmap_data.rename(columns=lambda x: x.replace(' For Argentina', ''))
  
    """  
    # Select all columns except the first (which is Opponent)
    cols_to_zscore = heatmap_data.columns[1:]
    
    # Compute z-scores for the selected columns
    z_scores = stats.zscore(heatmap_data[cols_to_zscore])
    
    # Replace any negative values in the z-scores with 0
    positions = pd.DataFrame(np.maximum(z_scores, 0))
    
    # Create a list of weights with the same length as the number of selected columns
    weights = [1] * len(cols_to_zscore)
    
    # Multiply each position by its weight
    weight_positions = positions.multiply(weights, axis=1)
    
    # Compute the distance for each row by summing the weighted positions
    distance = weight_positions.sum(axis=1)
    
    # Add the distance column to the heatmap_data dataframe
    heatmap_data['Distance'] = distance
    """
    # Set the Opponent column as the index for the heatmap data
    heatmap_data = heatmap_data.set_index('Opponent')
    
    # Sort the heatmap data by distance in descending order
    # heatmap_data_sorted = heatmap_data.sort_values(by='Distance', ascending=False)
    heatmap_data_sorted = heatmap_data.sort_values(by='Goal Against Argentina', ascending=False)
    
    # drop the 'Distance' column before passing it to the heatmap
    # heatmap_data_sorted = heatmap_data_sorted.drop('Distance', axis=1)
    heatmap_data_sorted = heatmap_data_sorted.drop('Goal Against Argentina', axis=1)
    
    # Return the sorted heatmap data
    return heatmap_data_sorted

def viz2_get_MatchReport_for_lollipop(MatchReport_df):
    # Create a new column that groups the data by opponent and calculates the average
   # MatchReport_df["Average Performance"] = MatchReport_df.iloc[:, 1:].mean(axis=1)
    lollipop_data = MatchReport_df
    print(lollipop_data )
    return lollipop_data 


def viz3_get_offensive_stats(shooting_df, passing_df, gca_df):
    df = pd.concat([shooting_df, passing_df, gca_df], axis=1)
    df = df.loc[:, ~df.columns.duplicated()]
    df = df[['Player', 'Pos', 'Gls', 'KP', 'GCA']]
    df = df.iloc[:-2]
    df = df[df['Pos'].isin(['FW', 'MFFW', 'MF'])]
    df = df[df['KP'] != 0]
    return df


def viz4_get_stats(shooting_df, passing_df, def_act_df, goalkeeping_df, possession_df):
    sot = shooting_df.loc[shooting_df['Player'] == 'Squad Total', ['SoT%']]
    
    cmp = passing_df.loc[passing_df['Player'] == 'Squad Total', ['Cmp%']]
    
    tkl_tklw = def_act_df.loc[def_act_df['Player'] == 'Squad Total', ['Tkl', 'TklW']]
    tkl_tklw['TklW/Tkl'] = tkl_tklw['TklW'] / tkl_tklw['Tkl'] * 100
    tkl_tklw = tkl_tklw.drop(['Tkl', 'TklW'], axis=1)
    
    save = goalkeeping_df.loc[goalkeeping_df['Player'] == 'Squad Total', ['Save%']]
    save = save.reset_index(drop=True)
    
    poss = possession_df['Poss']
    poss = possession_df['Poss'].iloc[11]
    
    conversion = shooting_df.loc[shooting_df['Player'] == 'Squad Total', ['Gls', 'Sh']]
    conversion['Conversion'] = conversion['Gls'] / conversion['Sh'] * 100
    conversion = conversion.drop(['Gls', 'Sh'], axis=1)
    
    df = pd.concat([sot, cmp, tkl_tklw, conversion], axis=1).reset_index(drop=True)
    df = pd.concat([df,save], axis=1)
    df['Poss'] = poss
    
    return df


def viz5_get_stats(shooting_df):
    df = pd.DataFrame(shooting_df[['Player','Sh', 'Gls']])
    df['nGls'] = shooting_df['Sh'] - shooting_df['Gls']

    df = df.drop(df[df['Gls'] == 0].index)
    df = df.drop(df.tail(2).index)
    
    df = df.sort_values(['nGls', 'Gls'])

    return df