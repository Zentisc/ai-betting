import pandas as pd

data = pd.read_csv("data/features.csv")

# Expected Goals Proxy
data["home_xg"] = data["HS"] * 0.1
data["away_xg"] = data["AS"] * 0.1

data["xg_diff"] = data["home_xg"] - data["away_xg"]

data.to_csv("data/features.csv", index=False)

print("xG Features erstellt!")