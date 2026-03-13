import pandas as pd

data = pd.read_csv("data/E0.csv")

teams = pd.concat([data["HomeTeam"], data["AwayTeam"]]).unique()

elo = {}

for team in teams:
    elo[team] = 1500


K = 20

for index, row in data.iterrows():

    home = row["HomeTeam"]
    away = row["AwayTeam"]

    home_elo = elo[home]
    away_elo = elo[away]

    expected_home = 1 / (1 + 10 ** ((away_elo - home_elo) / 400))
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

    elo[home] = home_elo + K * (score_home - expected_home)
    elo[away] = away_elo + K * (score_away - expected_away)


sorted_elo = sorted(elo.items(), key=lambda x: x[1], reverse=True)

print("Top Teams nach ELO:")

for team, rating in sorted_elo[:10]:
    print(team, round(rating))