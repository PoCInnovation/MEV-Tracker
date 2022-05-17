import pandas as pd


def number_of_games(df):
    return df.__len__()

def number_of_games_lfl(df):
    return df[df['league'] == "LFL"].__len__()

def redside_winrate(df):
    return df[df['result'] != 1].__len__() / df['result'].__len__()

def list_equip_lfl(df):
    list_matches_lfl = df[df['league'] == "LFL"]
    redteam = list(list_matches_lfl['redteam'])
    blueteam = list(list_matches_lfl['blueteam'])
    return list(set(blueteam + redteam))

def top_pick_mid(df):
    max_value = 0
    name = ''
    all_names = list(df['redmid'])+ list(df['bluemid'])
    names = list(set(all_names))
    for i in names:
        if all_names.count(i) > max_value:
            max_value = all_names.count(i)
            name = i
    return name


#### faire le reste si besoin

if __name__ == '__main__':
    data = pd.read_csv("./matches2020.csv")
    print(top_pick_mid(data))