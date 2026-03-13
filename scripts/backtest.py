import pandas as pd

PRED_FILE = "data/predictions.csv"

BANKROLL = 1000
BET_SIZE = 10


def backtest():

    df = pd.read_csv(PRED_FILE)

    bankroll = BANKROLL
    bets = 0
    wins = 0

    for _, row in df.iterrows():

        bets_data = [
            ("H", row["prob_home"], row["B365H"]),
            ("D", row["prob_draw"], row["B365D"]),
            ("A", row["prob_away"], row["B365A"]),
        ]

        best_value = 0
        best_bet = None

        for result, prob, odds in bets_data:

            if pd.isna(odds):
                continue

            value = prob * odds

            if value > best_value:
                best_value = value
                best_bet = (result, prob, odds)

        # nur wetten wenn Value > 1
        if best_value <= 1:
            continue

        result, prob, odds = best_bet

        bets += 1

        if row["FTR"] == result:

            profit = BET_SIZE * (odds - 1)
            bankroll += profit
            wins += 1

        else:

            bankroll -= BET_SIZE

    winrate = wins / bets if bets > 0 else 0
    roi = ((bankroll - BANKROLL) / BANKROLL) * 100

    print("")
    print("Backtest Results")
    print("----------------")
    print("Bets:", bets)
    print("Wins:", wins)
    print("Winrate:", round(winrate, 3))
    print("Final Bankroll:", round(bankroll, 2))
    print("ROI:", round(roi, 2), "%")


if __name__ == "__main__":
    backtest()