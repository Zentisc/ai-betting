
import pandas as pd

print("Building features...")

df = pd.read_csv("data/raw_matches.csv")

# Zielvariable
df["target"] = df["FTR"].map({
    "H": 0,
    "D": 1,
    "A": 2
})

# Wettquoten → implied probability
df["imp_home"] = 1 / df["B365H"]
df["imp_draw"] = 1 / df["B365D"]
df["imp_away"] = 1 / df["B365A"]

total = df["imp_home"] + df["imp_draw"] + df["imp_away"]

df["imp_home"] = df["imp_home"] / total
df["imp_draw"] = df["imp_draw"] / total
df["imp_away"] = df["imp_away"] / total

# Goal difference
df["goal_diff"] = df["FTHG"] - df["FTAG"]

# Team Strength
home_strength = df.groupby("HomeTeam")["goal_diff"].mean()
away_strength = df.groupby("AwayTeam")["goal_diff"].mean()

df["home_strength"] = df["HomeTeam"].map(home_strength)
df["away_strength"] = df["AwayTeam"].map(away_strength)

df["strength_diff"] = df["home_strength"] - df["away_strength"]

# fehlende Werte ersetzen
df = df.fillna(0)

features = [
    "imp_home",
    "imp_draw",
    "imp_away",
    "home_strength",
    "away_strength",
    "strength_diff"
]

X = df[features]
y = df["target"]

data = pd.concat([X, y], axis=1)

data.to_csv("data/features.csv", index=False)

print("Features built:", len(data))