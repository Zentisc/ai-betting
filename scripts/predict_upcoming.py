import pandas as pd
import joblib
import os

print("Predicting upcoming matches...")

file = "data/upcoming_matches.csv"

if not os.path.exists(file):
    print("No upcoming matches file")
    exit()

matches = pd.read_csv(file)

if matches.empty:
    print("No upcoming matches")
    exit()

model = joblib.load("models/trained_model.pkl")
features = joblib.load("models/feature_list.pkl")


# bookmaker implied probability
matches["imp_home"] = 1 / matches["B365H"]
matches["imp_draw"] = 1 / matches["B365D"]
matches["imp_away"] = 1 / matches["B365A"]


# fehlende Features erzeugen
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