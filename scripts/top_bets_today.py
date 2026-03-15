import pandas as pd

print("Selecting best bets...")

from datetime import datetime

today = datetime.utcnow().strftime("%d/%m/%Y")

df = df[df["Date"] == today]

df = pd.read_csv("data/upcoming_predictions.csv")

for _, row in df.iterrows():

    options = {
        "HOME": row["home_prob"],
        "DRAW": row["draw_prob"],
        "AWAY": row["away_prob"],
        "BTTS YES": row["btts_prob"],
        "OVER 2.5": row["over25_prob"]
    }

    best_bet = max(options, key=options.get)
    best_prob = options[best_bet]

    bets.append({
        "match": f"{row['HomeTeam']} vs {row['AwayTeam']}",
        "bet": best_bet,
        "prob": best_prob
    })

bets = []

for _, row in df.iterrows():

    options = {
        "HOME": row["prob_home"],
        "DRAW": row["prob_draw"],
        "AWAY": row["prob_away"]
    }

    bet = max(options, key=options.get)
    prob = options[bet]

    match = f"{row['HomeTeam']} vs {row['AwayTeam']}"

    bets.append({
        "match": match,
        "bet": bet,
        "prob": prob
    })

bets = pd.DataFrame(bets)

bets = bets.sort_values("prob", ascending=False)

free = bets.iloc[0:1]
vip = bets.iloc[1:4]

free.to_csv("data/free_bet.csv", index=False)
vip.to_csv("data/vip_bets.csv", index=False)

print("Free bet saved")
print("VIP bets saved")