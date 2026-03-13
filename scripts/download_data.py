import pandas as pd
import requests
import os


BASE_URL = "https://www.football-data.co.uk/mmz4281/"

SEASONS = [
    "2324",
    "2223",
    "2122",
    "2021",
    "1920",
    "1819"
]

LEAGUES = {
    "E0": "PremierLeague",
    "D1": "Bundesliga",
    "I1": "SerieA",
    "SP1": "LaLiga",
    "F1": "Ligue1"
}

OUTPUT_FILE = "data/raw_matches.csv"


def download_league(season, league):

    url = f"{BASE_URL}{season}/{league}.csv"

    print("Downloading:", url)

    try:

        df = pd.read_csv(url)

        return df

    except:

        print("Failed:", url)

        return None


def download_all():

    all_data = []

    for season in SEASONS:

        for league in LEAGUES:

            df = download_league(season, league)

            if df is not None:

                df["Season"] = season
                df["League"] = league

                all_data.append(df)

    if len(all_data) == 0:

        print("No data downloaded")
        return

    combined = pd.concat(all_data, ignore_index=True)

    os.makedirs("data", exist_ok=True)

    combined.to_csv(OUTPUT_FILE, index=False)

    print("Saved dataset:", OUTPUT_FILE)


if __name__ == "__main__":
    download_all()