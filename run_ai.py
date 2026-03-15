import os
import time
from datetime import datetime


def reset_pipeline():

    files = [
        "data/features.csv",
        "data/predictions.csv",
        "data/value_bets.csv",
        "data/free_bet.csv",
        "data/vip_bets.csv",
        "models/trained_model.pkl",
        "models/feature_list.pkl"
    ]

    for f in files:
        if os.path.exists(f):
            os.remove(f)
            print("Deleted:", f)


print("Resetting pipeline...")
reset_pipeline()


def run_pipeline():

    print("Downloading historical data...")
    os.system("python scripts/download_data.py")

    print("Building features...")
    os.system("python scripts/build_features.py")

    print("Training model...")
    os.system("python models/ml_model.py")

    print("Predicting matches...")
    os.system("python scripts/predict_matches.py")

    print("Running backtest...")
    from scripts.backtest import backtest
    backtest()

    print("Downloading upcoming matches...")
    os.system("python scripts/get_today_matches.py")

    print("Predicting upcoming matches...")
    os.system("python scripts/predict_upcoming.py")

    print("Calculating goal markets...")
    os.system("python scripts/goal_markets.py")

    print("Selecting top bets for upcoming matches...")
    os.system("python scripts/top_bets_today.py")

    print("Showing bets...")
    os.system("python scripts/show_bets.py")

    print("Sending Telegram bets...")
    os.system("python scripts/send_telegram_bets.py")

    print("Pipeline finished")


def wait_for_results():

    print("Waiting to post results...")

    while True:

        now = datetime.utcnow()

        # Ergebnisse um 02:00 UTC posten
        if now.hour == 2 and now.minute == 0:

            print("Posting results...")
            os.system("python scripts/post_results.py")

            break

        time.sleep(600)


if __name__ == "__main__":

    run_pipeline()

    wait_for_results()