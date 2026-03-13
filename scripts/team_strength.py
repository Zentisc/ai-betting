import pandas as pd

print("Calculating team strength...")

data = pd.read_csv("data/all_matches.csv")

league_home_goals = data["FTHG"].mean()
league_away_goals = data["FTAG"].mean()

teams = pd.concat([data["HomeTeam"], data["AwayTeam"]]).unique()

attack_strength = {}
defense_strength = {}

for team in teams:

    home_games = data[data["HomeTeam"] == team]
    away_games = data[data["AwayTeam"] == team]

    home_scored = home_games["FTHG"].mean()
    home_conceded = home_games["FTAG"].mean()

    away_scored = away_games["FTAG"].mean()
    away_conceded = away_games["FTHG"].mean()

    attack = (home_scored + away_scored) / (league_home_goals + league_away_goals)
    defense = (home_conceded + away_conceded) / (league_home_goals + league_away_goals)

    attack_strength[team] = attack
    defense_strength[team] = defense

df = pd.DataFrame({
    "Team": teams,
    "AttackStrength": [attack_strength[t] for t in teams],
    "DefenseStrength": [defense_strength[t] for t in teams]
})

df.to_csv("data/team_strength.csv", index=False)

print("Team strength saved.")