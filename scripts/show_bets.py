import pandas as pd
import os

FILE = "data/top_bets.csv"


def show_bets():

    if not os.path.exists(FILE):
        print("No bets found")
        return

    df = pd.read_csv(FILE)

    print("\n🔥 TOP AI BETS\n")

    for i, row in df.head(10).iterrows():

        print(row["HomeTeam"], "vs", row["AwayTeam"])

        print(
            "Home:",
            round(row["prob_home"], 2),
            "Draw:",
            round(row["prob_draw"], 2),
            "Away:",
            round(row["prob_away"], 2)
        )

        print("Value:", round(row["max_value"], 2))

        print("-" * 30)


if __name__ == "__main__":
    show_bets()