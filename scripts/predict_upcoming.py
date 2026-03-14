import pandas as pd
import joblib
from predictions.monte_carlo_simulation import simulate_match

print("Predicting upcoming matches...")

model = joblib.load("models/trained_model.pkl")

matches = pd.read_csv("data/upcoming_matches.csv")

features = joblib.load("models/feature_list.pkl")

X = matches[features]

ml_probs = model.predict_proba(X)

predictions = []

for i, row in matches.iterrows():

    home = row["HomeTeam"]
    away = row["AwayTeam"]

    home_xg = row.get("home_xg", 1.5)
    away_xg = row.get("away_xg", 1.2)

    poisson = simulate_match(home_xg, away_xg)

    ml_home = ml_probs[i][0]
    ml_draw = ml_probs[i][1]
    ml_away = ml_probs[i][2]

    # Ensemble Mischung
    home_prob = (ml_home + poisson["home_win_prob"]) / 2
    draw_prob = (ml_draw + poisson["draw_prob"]) / 2
    away_prob = (ml_away + poisson["away_win_prob"]) / 2

    predictions.append({
        "HomeTeam": home,
        "AwayTeam": away,
        "home_win_prob": home_prob,
        "draw_prob": draw_prob,
        "away_win_prob": away_prob,
        "over25_prob": poisson["over25_prob"],
        "btts_yes_prob": poisson["btts_yes_prob"]
    })

predictions = pd.DataFrame(predictions)

predictions.to_csv("data/predictions.csv", index=False)

print("Predictions saved")