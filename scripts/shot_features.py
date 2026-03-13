import pandas as pd

data = pd.read_csv("data/features.csv")

data["shots_diff"] = data["HS"] - data["AS"]
data["shots_target_diff"] = data["HST"] - data["AST"]

data.to_csv("data/features.csv", index=False)

print("Shot Features erstellt!")