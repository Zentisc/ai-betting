import pandas as pd
import numpy as np
from scipy.stats import poisson

print("Calculating BTTS and Over/Under probabilities...")

df = pd.read_csv("data/predictions.csv")

btts_probs = []
over25_probs = []
under25_probs = []

for _, row in df.iterrows():

    # expected goals schätzen
    home_attack = row.get("home_attack_strength", 1.2)
    away_attack = row.get("away_attack_strength", 1.0)

    home_def = row.get("home_defense_strength", 1.0)
    away_def = row.get("away_defense_strength", 1.0)

    home_xg = home_attack * away_def
    away_xg = away_attack * home_def

    # Poisson Wahrscheinlichkeiten
    home_goals = [poisson.pmf(i, home_xg) for i in range(6)]
    away_goals = [poisson.pmf(i, away_xg) for i in range(6)]

    over25 = 0
    under25 = 0
    btts = 0

    for i in range(6):
        for j in range(6):

            p = home_goals[i] * away_goals[j]

            if i + j > 2:
                over25 += p
            else:
                under25 += p

            if i > 0 and j > 0:
                btts += p

    btts_probs.append(btts)
    over25_probs.append(over25)
    under25_probs.append(under25)

df["btts_yes_prob"] = btts_probs
df["over25_prob"] = over25_probs
df["under25_prob"] = under25_probs

df.to_csv("data/predictions.csv", index=False)

print("Goal markets added.")