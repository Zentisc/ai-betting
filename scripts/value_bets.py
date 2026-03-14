import pandas as pd

print("Calculating value bets...")

df = pd.read_csv(
    "data/predictions.csv",
    usecols=[
        "HomeTeam",
        "AwayTeam",
        "home_win_prob",
        "draw_prob",
        "away_win_prob",
        "btts_yes_prob",
        "over25_prob"
    ]
)

bets = []

for _, row in df.iterrows():

    match = f"{row['HomeTeam']} vs {row['AwayTeam']}"

    markets = [
        ("HOME", row["home_win_prob"]),
        ("DRAW", row["draw_prob"]),
        ("AWAY", row["away_win_prob"]),
        ("BTTS YES", row["btts_yes_prob"]),
        ("OVER 2.5", row["over25_prob"]),
    ]

    best_market = max(markets, key=lambda x: x[1])

    bet = best_market[0]
    prob = best_market[1]

    if prob >= 0.55:

        bets.append({
            "match": match,
            "bet": bet,
            "prob": prob
        })

bets = pd.DataFrame(bets)

bets.to_csv("data/value_bets.csv", index=False)

print("Value bets saved")