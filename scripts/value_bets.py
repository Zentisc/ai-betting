import pandas as pd
import os


PRED_FILE = "data/predictions.csv"
OUTPUT_FILE = "data/value_bets.csv"


def find_odds_columns(df):

    possible_home = ["B365H", "PSH", "MaxH", "AvgH"]
    possible_draw = ["B365D", "PSD", "MaxD", "AvgD"]
    possible_away = ["B365A", "PSA", "MaxA", "AvgA"]

    home = next((c for c in possible_home if c in df.columns), None)
    draw = next((c for c in possible_draw if c in df.columns), None)
    away = next((c for c in possible_away if c in df.columns), None)

    return home, draw, away


def find_value_bets():

    if not os.path.exists(PRED_FILE):
        print("ERROR: predictions.csv not found")
        return

    df = pd.read_csv(PRED_FILE, low_memory=False)

    home_col, draw_col, away_col = find_odds_columns(df)

    if home_col is None:
        print("ERROR: No odds columns found")
        print(df.columns)
        return

    df["home_odds"] = df[home_col]
    df["draw_odds"] = df[draw_col]
    df["away_odds"] = df[away_col]

    df["value_home"] = df["prob_home"] * df["home_odds"]
    df["value_draw"] = df["prob_draw"] * df["draw_odds"]
    df["value_away"] = df["prob_away"] * df["away_odds"]

    value_bets = df[
        (df["value_home"] > 1) |
        (df["value_draw"] > 1) |
        (df["value_away"] > 1)
    ]

    value_bets.to_csv(OUTPUT_FILE, index=False)

    print("Value bets saved:", OUTPUT_FILE)


if __name__ == "__main__":
    find_value_bets()