import pandas as pd
import os

VALUE_FILE = "data/value_bets.csv"
OUTPUT_FILE = "data/top_bets.csv"


def select_top_bets():

    if not os.path.exists(VALUE_FILE):
        print("ERROR: value_bets.csv not found")
        return

    df = pd.read_csv(VALUE_FILE)

    df["max_value"] = df[[
        "value_home",
        "value_draw",
        "value_away"
    ]].max(axis=1)

    df = df.sort_values("max_value", ascending=False)

    top = df.head(10)

    top.to_csv(OUTPUT_FILE, index=False)

    print("Top bets saved:", OUTPUT_FILE)


if __name__ == "__main__":
    select_top_bets()