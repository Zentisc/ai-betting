import pandas as pd
from scripts.advanced_match_model import get_best_bet

print("Finding best bets...")

matches = pd.read_csv("data/upcoming_matches.csv")

bets = []

for _, row in matches.iterrows():

    home = row["HomeTeam"]
    away = row["AwayTeam"]

    home_attack = row["home_strength"]
    away_attack = row["away_strength"]

    bet = get_best_bet(home, away, home_attack, away_attack)

    if bet["prob"] > 0.55:
        bets.append(bet)

bets = pd.DataFrame(bets)

bets = bets.sort_values("prob", ascending=False)

free_bets = bets.head(1)
vip_bets = bets.head(4)

free_bets.to_csv("data/free_bets.csv", index=False)
vip_bets.to_csv("data/premium_bets.csv", index=False)

print("Bets saved")