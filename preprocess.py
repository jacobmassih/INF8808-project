import pandas as pd
import numpy as np
# from scipy import stats


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
    # Define the columns to pivot
    cols_to_pivot = ['Possession For Argentina', 'Possession Against Argentina', 
                     'Passing Accuracy For Argentina', 'Passing Accuracy Against Argentina', 
                     'Shots On Target For Argentina', 'Shots On Target Against Argentina', 
                     'Saves For Argentina', 'Saves Against Argentina', 
                     'Goal For Argentina', 'Goal Against Argentina', 
                     'Goal per Shot For Argentina', 'Goal per Shot Against Argentina']
    # Melt the data to long format
    melted_data = pd.melt(MatchReport_df, id_vars=['Opponent'], value_vars=cols_to_pivot,
                          var_name='Metric', value_name='Value')
    melted_data['Full Name Metric'] = melted_data['Opponent'] + ' ' + melted_data['Metric']
    melted_data= melted_data.drop(['Opponent', 'Metric'], axis=1)
    lollipop_data = melted_data.set_index('Full Name Metric')
    # Pivot the data to wide format
    #pivoted_data = melted_data.pivot(index='Opponent', columns='Metric', values='Value')
    # Reset the index
    #pivoted_data = pivoted_data.reset_index()
    #print(pivoted_data)
    # Return the pivoted data
    return lollipop_data




def viz3_get_offensive_stats(shooting_df, passing_df, gca_df):
    df = pd.concat([shooting_df, passing_df, gca_df], axis=1)
    df = df.loc[:, ~df.columns.duplicated()]
    df = df[['Player', 'Pos', 'Gls', 'KP', 'GCA']]
    df = df.iloc[:-2]
    df = df[df['Pos'].isin(['FW', 'MFFW', 'MF'])]
    df = df[df['KP'] != 0]
    return df


def viz4_get_stats(shooting_df, passing_df, def_act_df, goalkeeping_df, possession_df, s_n_f_df):
    sot = shooting_df.loc[shooting_df['Player'] == 'Squad Total', ['SoT%']]
    
    cmp = passing_df.loc[passing_df['Player'] == 'Squad Total', ['Cmp%']]
    
    tkl_tklw = def_act_df.loc[def_act_df['Player'] == 'Squad Total', ['Tkl', 'TklW']]
    tkl_tklw['TklW/Tkl'] = round(tkl_tklw['TklW'] / tkl_tklw['Tkl'] * 100, 1)
    tkl_tklw = tkl_tklw.drop(['Tkl', 'TklW'], axis=1)
    
    save = goalkeeping_df.loc[goalkeeping_df['Player'] == 'Squad Total', ['Save%']]
    save = save.reset_index(drop=True)
    
    poss = possession_df['Poss']
    poss = possession_df['Poss'].iloc[11]
    
    g_p_sh = s_n_f_df['G/Sh']
    g_p_sh = s_n_f_df['G/Sh'].iloc[11] * 100
    
    df = pd.concat([sot, cmp, tkl_tklw], axis=1).reset_index(drop=True)
    df = pd.concat([df,save], axis=1)
    df['Poss'] = poss
    df['G/Sh'] = g_p_sh
    
    return df


def viz5_get_stats(shooting_df):
    df = pd.DataFrame(shooting_df[['Player','Sh', 'Gls']])
    df['nGls'] = shooting_df['Sh'] - shooting_df['Gls']

    df = df.drop(df[df['Gls'] == 0].index)
    df = df.drop(df.tail(2).index)
    
    df = df.sort_values(['nGls', 'Gls'])

    return df