import pandas as pd

print("Selecting top bets...")

df = pd.read_csv("data/value_bets.csv")

# nach Wahrscheinlichkeit sortieren
df = df.sort_values("prob", ascending=False)

# pro Spiel nur ein Bet
df = df.drop_duplicates("match")

# Top 5
top5 = df.head(5)

free = top5.head(1)
vip = top5.iloc[1:]

free.to_csv("data/free_bets.csv", index=False)
vip.to_csv("data/premium_bets.csv", index=False)

print("Top bets saved")