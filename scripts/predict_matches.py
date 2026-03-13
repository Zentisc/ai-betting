import pandas as pd
import joblib

MODEL_FILE = "models/trained_model.pkl"
FEATURE_LIST = "models/feature_list.pkl"

print("Loading model...")

model = joblib.load(MODEL_FILE)
features = joblib.load(FEATURE_LIST)

# ursprüngliche Daten laden
raw = pd.read_csv("data/raw_matches.csv")

# Feature Datensatz laden
df = pd.read_csv("data/features.csv")

X = df[features]

probs = model.predict_proba(X)

df["prob_home"] = probs[:,0]
df["prob_draw"] = probs[:,1]
df["prob_away"] = probs[:,2]

# Odds aus original Dataset hinzufügen
df["B365H"] = raw["B365H"]
df["B365D"] = raw["B365D"]
df["B365A"] = raw["B365A"]

# Teams hinzufügen (für Anzeige)
df["HomeTeam"] = raw["HomeTeam"]
df["AwayTeam"] = raw["AwayTeam"]

df.to_csv("data/predictions.csv", index=False)

print("Predictions saved:", len(df))