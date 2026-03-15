import pandas as pd

print("Selecting best bets...")

df = pd.read_csv("data/predictions.csv")

df["match"] = df["HomeTeam"] + " vs " + df["AwayTeam"]

bets = []

for _, row in df.iterrows():

    markets = {
        "HOME": row["prob_home"],
        "DRAW": row["prob_draw"],
        "AWAY": row["prob_away"]
    }

    bet = max(markets, key=markets.get)
    prob = markets[bet]

    bets.append({
        "match": row["match"],
        "bet": bet,
        "prob": prob
    })

bets = pd.DataFrame(bets)

bets = bets.sort_values("prob", ascending=False)

bets.to_csv("data/value_bets.csv", index=False)

print("Value bets saved:", len(bets))