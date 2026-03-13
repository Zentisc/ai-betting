import pandas as pd

print("Calculating ELO ratings...")

data = pd.read_csv("data/all_matches.csv")

teams = pd.concat([data["HomeTeam"], data["AwayTeam"]]).unique()

elo = {}

for team in teams:
    elo[team] = 1500

K = 20

for i,row in data.iterrows():

    home = row["HomeTeam"]
    away = row["AwayTeam"]

    home_goals = row["FTHG"]
    away_goals = row["FTAG"]

    home_elo = elo[home]
    away_elo = elo[away]

    expected_home = 1 / (1 + 10 ** ((away_elo - home_elo)/400))
    expected_away = 1 - expected_home

    if home_goals > away_goals:
        result_home = 1
        result_away = 0
    elif home_goals < away_goals:
        result_home = 0
        result_away = 1
    else:
        result_home = 0.5
        result_away = 0.5

    elo[home] = home_elo + K * (result_home - expected_home)
    elo[away] = away_elo + K * (result_away - expected_away)

ratings = pd.DataFrame(list(elo.items()), columns=["Team","ELO"])

ratings.to_csv("data/elo_ratings.csv",index=False)

print("ELO ratings saved.")