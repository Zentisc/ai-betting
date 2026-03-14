import numpy as np

SIMULATIONS = 10000


def simulate_match(home_xg, away_xg):

    home_goals = np.random.poisson(home_xg, SIMULATIONS)
    away_goals = np.random.poisson(away_xg, SIMULATIONS)

    home_win = np.mean(home_goals > away_goals)
    draw = np.mean(home_goals == away_goals)
    away_win = np.mean(home_goals < away_goals)

    over25 = np.mean((home_goals + away_goals) > 2)

    btts = np.mean((home_goals > 0) & (away_goals > 0))

    return {
        "home_win_prob": home_win,
        "draw_prob": draw,
        "away_win_prob": away_win,
        "over25_prob": over25,
        "btts_yes_prob": btts
    }