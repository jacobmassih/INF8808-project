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
    heatmap_data = MatchReport_df.drop(['Possession Against Argentina','Passing Accuracy Against Argentina','Shots On Target Against Argentina','Saves Against Argentina','Goal per Shot Against Argentina'], axis=1)
    heatmap_data['Goal per Shot For Argentina'] = heatmap_data['Goal per Shot For Argentina'].apply(lambda x: x * 100)
    heatmap_data['Goal Difference'] = heatmap_data['Goal Against Argentina'] - heatmap_data['Goal For Argentina']
    heatmap_data= heatmap_data.drop(['Goal For Argentina', 'Goal Against Argentina'], axis=1)
    heatmap_data = heatmap_data.rename(columns=lambda x: x.replace(' For Argentina', ''))
    heatmap_data = heatmap_data.set_index('Opponent')
    heatmap_data_sorted = heatmap_data.sort_values(by=('Goal Difference'), ascending=False)
    heatmap_data_sorted = heatmap_data_sorted.drop('Goal Difference', axis=1)
    return heatmap_data_sorted

def viz2_get_MatchReport_for_lollipop(MatchReport_df):
    MatchReport_df['Goal per Shot Against Argentina'] = MatchReport_df['Goal per Shot Against Argentina'].apply(lambda x: x * 100)     
    print(MatchReport_df)   
    MatchReport_df['Goal per Shot For Argentina'] = MatchReport_df['Goal per Shot For Argentina'].apply(lambda x: x * 100)
    new_df = pd.DataFrame()
    for _, row in MatchReport_df.iterrows():
            # Create a copy of the row
            new_row = row.copy()
                    
            # Rename the Opponent column of the new row
            new_row['Opponent'] = 'Performance of Argentina Against ' + new_row['Opponent']
                    
            # Modify the other columns of the new row as needed
            new_row['Possession Against Argentina'] = new_row['Possession For Argentina']
            new_row['Passing Accuracy Against Argentina'] = new_row['Passing Accuracy For Argentina']
            new_row['Shots On Target Against Argentina'] = new_row['Shots On Target For Argentina']
            new_row['Saves Against Argentina'] = new_row['Saves For Argentina']
            new_row['Goal Against Argentina'] = new_row['Goal For Argentina']
            new_row['Goal per Shot Against Argentina'] = new_row['Goal per Shot For Argentina']
            
            # Append the modified row to the new DataFrame
            new_df = new_df.append(new_row, ignore_index=True)

    # Concatenate the original DataFrame with the new DataFrame
    MatchReport_df = pd.concat([MatchReport_df, new_df], ignore_index=True)

    
    for idx, row in MatchReport_df.iterrows():
    # Check if the opponent name starts with 'Performance'
        if 'Performance' not in row['Opponent']:
        # Rename the opponent name
            MatchReport_df.at[idx, 'Opponent'] = 'Performance of ' + row['Opponent'] + ' Against Argentina'

    MatchReport_df = MatchReport_df.sort_values('Opponent')
    MatchReport_df= MatchReport_df.drop(['Possession For Argentina','Passing Accuracy For Argentina','Shots On Target For Argentina','Saves For Argentina','Passing Accuracy For Argentina','Goal per Shot For Argentina','Goal Against Argentina','Goal For Argentina'], axis=1)
    MatchReport_df = MatchReport_df.rename(columns=lambda x: x.replace(' Against Argentina', ''))
    MatchReport_df['Median_Performance'] = MatchReport_df.median(axis=1)
    MatchReport_df['Mean_Performance'] = MatchReport_df.mean(axis=1)
    lollipop_data = MatchReport_df
    print("loliipop data")
    print (lollipop_data)
    return lollipop_data

def viz2_get_MatchReport_for_heatmap2(MatchReport_df):
    data = MatchReport_df
    data['Goal per Shot Against Argentina'] = data['Goal per Shot Against Argentina'].apply(lambda x: x * 100)     
    data['Goal per Shot For Argentina'] = data['Goal per Shot For Argentina'].apply(lambda x: x * 100)
    print("in heatmap2")
    print(data)
    new_df = pd.DataFrame()
    for _, row in data.iterrows():
            # Create a copy of the row
            new_row = row.copy()
            # Rename the Opponent column of the new row
            new_row['Opponent'] = 'Performance of Argentina Against ' + new_row['Opponent']
            # Modify the other columns of the new row as needed
            new_row['Possession Against Argentina'] = new_row['Possession For Argentina']
            new_row['Passing Accuracy Against Argentina'] = new_row['Passing Accuracy For Argentina']
            new_row['Shots On Target Against Argentina'] = new_row['Shots On Target For Argentina']
            new_row['Saves Against Argentina'] = new_row['Saves For Argentina']
            new_row['Goal Against Argentina'] = new_row['Goal For Argentina']
            new_row['Goal per Shot Against Argentina'] = new_row['Goal per Shot For Argentina']
            # Append the modified row to the new DataFrame
            new_df = new_df.append(new_row, ignore_index=True)
            
    # Concatenate the original DataFrame with the new DataFrame
    data = pd.concat([data, new_df], ignore_index=True)
    for idx, row in data.iterrows():
    # Check if the opponent name starts with 'Performance'
        if 'Performance' not in row['Opponent']:
        # Rename the opponent name
            data.at[idx, 'Opponent'] = 'Performance of ' + row['Opponent'] + ' Against Argentina'
            
    data = data.sort_values('Opponent')
    data= data.drop(['Possession For Argentina','Passing Accuracy For Argentina','Shots On Target For Argentina','Saves For Argentina','Passing Accuracy For Argentina','Goal per Shot For Argentina','Goal Against Argentina','Goal For Argentina'], axis=1)
    data = data.rename(columns=lambda x: x.replace(' Against Argentina', ''))
    data['Median_Performance'] = data.median(axis=1).round(2)
    data['Mean_Performance'] = data.mean(axis=1).round(2)
    print("in heatmap2 after mean")
    print(data)
    
    heatmap2_data = data
    heatmap2_data = heatmap2_data.set_index('Opponent')
    heatmap2_data_sorted = heatmap2_data.sort_values(by=('Mean_Performance'), ascending=False)
    
    print("in heatmap2 after mean and data sorted")
    print(heatmap2_data_sorted)
    return heatmap2_data_sorted



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