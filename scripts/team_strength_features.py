import pandas as pd

data = pd.read_csv("data/features.csv")

# Teams
teams = pd.concat([data["HomeTeam"], data["AwayTeam"]]).unique()

# neue Spalten
data["home_strength"] = 0.0
data["away_strength"] = 0.0

for team in teams:

    # Spiele des Teams
    team_games = data[(data["HomeTeam"] == team) | (data["AwayTeam"] == team)]

    goals_scored = []
    goals_conceded = []

    for i, row in team_games.iterrows():

        if row["HomeTeam"] == team:
            scored = row["FTHG"]
            conceded = row["FTAG"]
        else:
            scored = row["FTAG"]
            conceded = row["FTHG"]

        goals_scored.append(scored)
        goals_conceded.append(conceded)

    # Durchschnitt
    attack_strength = sum(goals_scored) / len(goals_scored)
    defense_strength = sum(goals_conceded) / len(goals_conceded)

    # Werte setzen
    data.loc[data["HomeTeam"] == team, "home_strength"] = attack_strength - defense_strength
    data.loc[data["AwayTeam"] == team, "away_strength"] = attack_strength - defense_strength


data["strength_diff"] = data["home_strength"] - data["away_strength"]

data.to_csv("data/features.csv", index=False)

print("Team Strength Features erstellt!")