import pandas as pd

INPUT_FILE = "data/upcoming_predictions.csv"

FREE_BETS = 3
PREMIUM_BETS = 10

print("Finding top bets for next 48 hours...")

df = pd.read_csv(INPUT_FILE)

bets = []

for _, row in df.iterrows():

    match = f"{row['HomeTeam']} vs {row['AwayTeam']}"

    bets.append({
        "match": match,
        "bet": "HOME",
        "prob": row["prob_home"],
        "odds": row["B365H"],
        "value": row["prob_home"] * row["B365H"]
    })

    bets.append({
        "match": match,
        "bet": "DRAW",
        "prob": row["prob_draw"],
        "odds": row["B365D"],
        "value": row["prob_draw"] * row["B365D"]
    })

    bets.append({
        "match": match,
        "bet": "AWAY",
        "prob": row["prob_away"],
        "odds": row["B365A"],
        "value": row["prob_away"] * row["B365A"]
    })


bets_df = pd.DataFrame(bets)

# nur Value Bets
bets_df = bets_df[bets_df["value"] > 1]

# nach Value sortieren
bets_df = bets_df.sort_values("value", ascending=False)

free = bets_df.head(FREE_BETS)
premium = bets_df.head(PREMIUM_BETS)

print("")
print("🔥 FREE BETS")
print("")

for _, row in free.iterrows():

    print(row["match"])
    print("Bet:", row["bet"])
    print("Probability:", round(row["prob"], 2))
    print("Odds:", row["odds"])
    print("Value:", round(row["value"], 2))
    print("--------------------------")


print("")
print("🔒 PREMIUM BETS")
print("")

for _, row in premium.iterrows():

    print(row["match"])
    print("Bet:", row["bet"])
    print("Probability:", round(row["prob"], 2))
    print("Odds:", row["odds"])
    print("Value:", round(row["value"], 2))
    print("--------------------------")


free.to_csv("data/free_bets.csv", index=False)
premium.to_csv("data/premium_bets.csv", index=False)

print("")
print("Saved:")
print("data/free_bets.csv")
print("data/premium_bets.csv")