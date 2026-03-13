
import pandas as pd

PRED_FILE = "data/predictions.csv"
RAW_FILE = "data/raw_matches.csv"

def backtest():

    print("\nBacktest Results\n----------------")

    preds = pd.read_csv(PRED_FILE)
    raw = pd.read_csv(RAW_FILE)

    bankroll = 100
    wins = 0
    losses = 0

    for i, row in preds.iterrows():

        prob_home = row["prob_home"]
        prob_draw = row["prob_draw"]
        prob_away = row["prob_away"]

        odds_home = row["B365H"]
        odds_draw = row["B365D"]
        odds_away = row["B365A"]

        # Prediction
        probs = {
            "H": prob_home,
            "D": prob_draw,
            "A": prob_away
        }

        result = max(probs, key=probs.get)

        # echtes Ergebnis
        real = raw.iloc[i]["FTR"]

        odds_map = {
            "H": odds_home,
            "D": odds_draw,
            "A": odds_away
        }

        odds = odds_map[result]

        bet = 1

        if real == result:
            bankroll += bet * (odds - 1)
            wins += 1
        else:
            bankroll -= bet
            losses += 1

    bets = wins + losses

    print("Bets:", bets)
    print("Wins:", wins)
    print("Winrate:", round(wins / bets, 3))
    print("Final Bankroll:", round(bankroll, 2))
    print("ROI:", round((bankroll - 100), 2), "%")

if __name__ == "__main__":
    backtest()