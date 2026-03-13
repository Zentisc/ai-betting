import pandas as pd

data = pd.read_csv("data/features.csv")

teams = {}

home_form = []
away_form = []

for _, row in data.iterrows():

    home = row["HomeTeam"]
    away = row["AwayTeam"]

    if home not in teams:
        teams[home] = []
    if away not in teams:
        teams[away] = []

    home_points = sum(teams[home][-5:])
    away_points = sum(teams[away][-5:])

    home_form.append(home_points)
    away_form.append(away_points)

    if row["FTR"] == "H":
        teams[home].append(3)
        teams[away].append(0)
    elif row["FTR"] == "A":
        teams[home].append(0)
        teams[away].append(3)
    else:
        teams[home].append(1)
        teams[away].append(1)

data["home_points_last5"] = home_form
data["away_points_last5"] = away_form

data.to_csv("data/features.csv", index=False)

print("Form last5 Features hinzugefügt")