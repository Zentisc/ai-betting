import pandas as pd
import joblib

print("Predicting upcoming matches...")

MODEL_FILE = "models/trained_model.pkl"
FEATURE_LIST = "models/feature_list.pkl"

model = joblib.load(MODEL_FILE)
features = joblib.load(FEATURE_LIST)

matches = pd.read_csv("data/upcoming_matches.csv")
history = pd.read_csv("data/raw_matches.csv")

# Team strength aus historischen Spielen berechnen
home_strength = history.groupby("HomeTeam")["FTHG"].mean()
away_strength = history.groupby("AwayTeam")["FTAG"].mean()

matches["home_strength"] = matches["HomeTeam"].map(home_strength)
matches["away_strength"] = matches["AwayTeam"].map(away_strength)

matches["home_strength"] = matches["home_strength"].fillna(home_strength.mean())
matches["away_strength"] = matches["away_strength"].fillna(away_strength.mean())

matches["strength_diff"] = matches["home_strength"] - matches["away_strength"]

# Dummy implied odds falls keine vorhanden
matches["imp_home"] = 0.33
matches["imp_draw"] = 0.33
matches["imp_away"] = 0.33

# fehlende Features hinzufügen
for f in features:
    if f not in matches.columns:
        matches[f] = 0

X = matches[features]

probs = model.predict_proba(X)

matches["prob_home"] = probs[:,0]
matches["prob_draw"] = probs[:,1]
matches["prob_away"] = probs[:,2]

matches.to_csv("data/upcoming_predictions.csv", index=False)

print("Upcoming predictions saved")