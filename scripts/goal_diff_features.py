import pandas as pd

data = pd.read_csv("data/E0.csv")

home_goals_for = data.groupby("HomeTeam")["FTHG"].mean()
home_goals_against = data.groupby("HomeTeam")["FTAG"].mean()

away_goals_for = data.groupby("AwayTeam")["FTAG"].mean()
away_goals_against = data.groupby("AwayTeam")["FTHG"].mean()

home_goal_diff = []
away_goal_diff = []

for _, row in data.iterrows():

    home = row["HomeTeam"]
    away = row["AwayTeam"]

    home_goal_diff.append(home_goals_for[home] - home_goals_against[home])
    away_goal_diff.append(away_goals_for[away] - away_goals_against[away])

data["home_goal_diff"] = home_goal_diff
data["away_goal_diff"] = away_goal_diff

data.to_csv("data/features.csv", index=False)

print("Goal difference features erstellt")