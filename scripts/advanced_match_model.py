import numpy as np
import pandas as pd

SIMULATIONS = 10000

def simulate_match(home_attack, away_attack):

    home_goals = np.random.poisson(home_attack, SIMULATIONS)
    away_goals = np.random.poisson(away_attack, SIMULATIONS)

    home_win = np.sum(home_goals > away_goals) / SIMULATIONS
    draw = np.sum(home_goals == away_goals) / SIMULATIONS
    away_win = np.sum(home_goals < away_goals) / SIMULATIONS

    over25 = np.sum((home_goals + away_goals) > 2) / SIMULATIONS
    over15 = np.sum((home_goals + away_goals) > 1) / SIMULATIONS
    under25 = 1 - over25

    btts = np.sum((home_goals > 0) & (away_goals > 0)) / SIMULATIONS
    no_btts = 1 - btts

    return {
        "HOME": home_win,
        "DRAW": draw,
        "AWAY": away_win,
        "BTTS YES": btts,
        "BTTS NO": no_btts,
        "OVER 2.5": over25,
        "UNDER 2.5": under25,
        "OVER 1.5": over15
    }


def get_best_bet(home, away, home_attack, away_attack):

    probs = simulate_match(home_attack, away_attack)

    best_market = max(probs, key=probs.get)

    return {
        "match": f"{home} vs {away}",
        "bet": best_market,
        "prob": round(probs[best_market], 2)
    }