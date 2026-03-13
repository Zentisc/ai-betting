import pandas as pd
from predictions.monte_carlo_simulation import simulate_match
from models.ml_model import model, features

# Daten laden
data = pd.read_csv("data/features.csv")
elo = pd.read_csv("data/elo_ratings.csv")


def ensemble_prediction(home, away):

    # letztes Spiel des Heimteams
    home_data = data[data["HomeTeam"] == home].tail(1)

    # letztes Spiel des Auswärtsteams
    away_data = data[data["AwayTeam"] == away].tail(1)

    if len(home_data) == 0 or len(away_data) == 0:
        return None

    # ML Features
    X = home_data[features]

    ml_probs = model.predict_proba(X)[0]

    ml_home = ml_probs[0]
    ml_draw = ml_probs[1]
    ml_away = ml_probs[2]

    # erwartete Tore
    home_lambda = home_data["FTHG"].mean()
    away_lambda = away_data["FTAG"].mean()

    # Monte Carlo Simulation
    poisson = simulate_match(home_lambda, away_lambda)

    p_home = poisson["home_win"]
    p_draw = poisson["draw"]
    p_away = poisson["away_win"]

    # ELO Ratings
    try:

        home_elo = elo[elo["Team"] == home]["ELO"].values[0]
        away_elo = elo[elo["Team"] == away]["ELO"].values[0]

    except:
        return None

    elo_home = 1 / (1 + 10 ** ((away_elo - home_elo) / 400))
    elo_away = 1 - elo_home
    elo_draw = 0.15

    # Ensemble Gewichtung
    home_final = (
        0.4 * ml_home +
        0.3 * p_home +
        0.3 * elo_home
    )

    draw_final = (
        0.4 * ml_draw +
        0.3 * p_draw +
        0.3 * elo_draw
    )

    away_final = (
        0.4 * ml_away +
        0.3 * p_away +
        0.3 * elo_away
    )

    return {
        "home": home_final,
        "draw": draw_final,
        "away": away_final
    }


    import numpy as np

def ensemble(models, X):

    probs = []

    for model in models:
        probs.append(model.predict_proba(X))

    return np.mean(probs, axis=0)