print("Sports Betting AI gestartet")


import pandas as pd
from scipy.stats import poisson

data = pd.read_csv("data/E0.csv")

home_avg = data["FTHG"].mean()
away_avg = data["FTAG"].mean()

home_attack = data.groupby("HomeTeam")["FTHG"].mean() / home_avg
home_defense = data.groupby("HomeTeam")["FTAG"].mean() / away_avg

away_attack = data.groupby("AwayTeam")["FTAG"].mean() / away_avg
away_defense = data.groupby("AwayTeam")["FTHG"].mean() / home_avg

home_team = "Arsenal"
away_team = "Chelsea"

home_goals = home_attack[home_team] * away_defense[away_team] * home_avg
away_goals = away_attack[away_team] * home_defense[home_team] * away_avg

home_win = 0
draw = 0
away_win = 0

for i in range(6):
    for j in range(6):
        p = poisson.pmf(i, home_goals) * poisson.pmf(j, away_goals)

        if i > j:
            home_win += p
        elif i == j:
            draw += p
        else:
            away_win += p

print("Heimsieg:", round(home_win,2))
print("Unentschieden:", round(draw,2))
print("Auswärtssieg:", round(away_win,2))

print("\n--- Buchmacher Quoten Beispiel ---")

sample = data[["HomeTeam","AwayTeam","B365H","B365D","B365A"]].head()

print(sample)

print("\n--- Buchmacher Wahrscheinlichkeiten ---")

data["book_home_prob"] = 1 / data["B365H"]
data["book_draw_prob"] = 1 / data["B365D"]
data["book_away_prob"] = 1 / data["B365A"]

print(data[["HomeTeam","AwayTeam","book_home_prob","book_draw_prob","book_away_prob"]].head())

print("\n--- Value Bet Beispiel ---")

odds = 2.40
prob = 0.52

value = prob * odds - 1

print("Value:", round(value,3))
def check_value(probability, odds):

    value = probability * odds - 1

    if value > 0:
        return True
    else:
        return False
    print("\n--- Value Bet Scan ---")

for index,row in data.iterrows():

    odds = row["B365H"]

    probability = 1/odds

    value = probability * odds - 1

    if value > 0.05:

        print("Value Bet:",row["HomeTeam"],"vs",row["AwayTeam"])

        def kelly(prob, odds):

    b = odds - 1
    q = 1 - prob

    k = (b * prob - q) / b

    return k