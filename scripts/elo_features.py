import pandas as pd

data = pd.read_csv("data/features.csv")

teams = {}

K = 20

home_elo = []
away_elo = []

for i,row in data.iterrows():

    home = row["HomeTeam"]
    away = row["AwayTeam"]

    if home not in teams:
        teams[home] = 1500
    if away not in teams:
        teams[away] = 1500

    home_rating = teams[home]
    away_rating = teams[away]

    home_elo.append(home_rating)
    away_elo.append(away_rating)

    expected_home = 1 / (1 + 10 ** ((away_rating-home_rating)/400))
    expected_away = 1 - expected_home

    if row["FTR"] == "H":
        score_home = 1
        score_away = 0
    elif row["FTR"] == "A":
        score_home = 0
        score_away = 1
    else:
        score_home = 0.5
        score_away = 0.5

    teams[home] = home_rating + K*(score_home-expected_home)
    teams[away] = away_rating + K*(score_away-expected_away)

data["home_elo"] = home_elo
data["away_elo"] = away_elo
data["elo_diff"] = data["home_elo"] - data["away_elo"]

data.to_csv("data/features.csv",index=False)

print("ELO Features erstellt!")