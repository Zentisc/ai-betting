import pandas as pd
import joblib

FEATURE_FILE = "data/features.csv"
RAW_FILE = "data/raw_matches.csv"
MODEL_FILE = "models/trained_model.pkl"
FEATURE_LIST = "models/feature_list.pkl"
OUTPUT_FILE = "data/predictions.csv"

print("Loading model...")

features_df = pd.read_csv(FEATURE_FILE)
raw_df = pd.read_csv(RAW_FILE)

model = joblib.load(MODEL_FILE)
feature_list = joblib.load(FEATURE_LIST)

X = features_df[feature_list]

probs = model.predict_proba(X)

home = probs[:,0]
draw = probs[:,1]
away = probs[:,2]

temperature = 3

home = home ** (1/temperature)
draw = draw ** (1/temperature)
away = away ** (1/temperature)

total = home + draw + away

features_df["prob_home"] = home / total
features_df["prob_draw"] = draw / total
features_df["prob_away"] = away / total

# Teams und Odds wieder hinzufügen
features_df["HomeTeam"] = raw_df["HomeTeam"]
features_df["AwayTeam"] = raw_df["AwayTeam"]
features_df["B365H"] = raw_df["B365H"]
features_df["B365D"] = raw_df["B365D"]
features_df["B365A"] = raw_df["B365A"]

features_df.to_csv(OUTPUT_FILE, index=False)

print("Predictions saved:", len(features_df))