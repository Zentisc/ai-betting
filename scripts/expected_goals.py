import pandas as pd

data = pd.read_csv("data/all_matches.csv")

teams = {}

for index,row in data.iterrows():

    home = row["HomeTeam"]
    away = row["AwayTeam"]

    home_goals = row["FTHG"]
    away_goals = row["FTAG"]

    if home not in teams:
        teams[home] = {"scored":0,"conceded":0,"games":0}

    if away not in teams:
        teams[away] = {"scored":0,"conceded":0,"games":0}

    teams[home]["scored"] += home_goals
    teams[home]["conceded"] += away_goals
    teams[home]["games"] += 1

    teams[away]["scored"] += away_goals
    teams[away]["conceded"] += home_goals
    teams[away]["games"] += 1

rows = []

for team in teams:

    attack = teams[team]["scored"]/teams[team]["games"]
    defense = teams[team]["conceded"]/teams[team]["games"]

    rows.append({
        "Team":team,
        "Attack":attack,
        "Defense":defense
    })

df = pd.DataFrame(rows)

df.to_csv("data/team_attack_defense.csv",index=False)

print("Attack/Defense strengths saved.")