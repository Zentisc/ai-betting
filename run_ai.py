import os

import os

def reset_pipeline():

    files = [
        "data/features.csv",
        "data/predictions.csv",
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

    print("Finding value bets...")
    os.system("python scripts/value_bets.py")

    print("Selecting top bets...")
    os.system("python scripts/top_bets.py")

    print("Showing bets...")
    os.system("python scripts/show_bets.py")

    print("Running backtest...")

    from scripts.backtest import backtest

    backtest()

    print("Downloading upcoming matches...")
    os.system("python scripts/get_today_matches.py")

    print("Predicting upcoming matches...")
    os.system("python scripts/predict_upcoming.py")

    print("Finding best bets next 48h...")
    os.system("python scripts/top_bets_today.py")

    print("Pipeline finished")

    print("Sending Telegram bets...")
    os.system("python scripts/send_telegram_bets.py")


if __name__ == "__main__":
    run_pipeline()