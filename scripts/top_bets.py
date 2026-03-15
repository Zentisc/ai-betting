import pandas as pd

print("Selecting top bets...")

df = pd.read_csv("data/value_bets.csv")

# richtige Spalte verwenden
df = df.sort_values("probability", ascending=False)

top_bets = df.head(10)

top_bets.to_csv("data/top_bets.csv", index=False)

print("Top bets saved:", len(top_bets))