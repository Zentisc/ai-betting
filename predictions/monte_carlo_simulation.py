import numpy as np


def simulate_match(home_prob, draw_prob, away_prob, simulations=10000):

    outcomes = np.random.choice(
        ["home", "draw", "away"],
        size=simulations,
        p=[home_prob, draw_prob, away_prob]
    )

    home_rate = np.mean(outcomes == "home")
    draw_rate = np.mean(outcomes == "draw")
    away_rate = np.mean(outcomes == "away")

    return home_rate, draw_rate, away_rate