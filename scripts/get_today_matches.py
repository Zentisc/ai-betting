import requests
import pandas as pd
from datetime import datetime, timedelta

print("Downloading upcoming matches...")

url = "https://www.football-data.co.uk/fixtures.csv"

try:
    df = pd.read_csv(url)
except:
    print("Could not download fixtures")
    exit()

df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

now = datetime.utcnow()
limit = now + timedelta(hours=48)

df = df[(df["Date"] >= now) & (df["Date"] <= limit)]

matches = pd.DataFrame()

matches["HomeTeam"] = df["HomeTeam"]
matches["AwayTeam"] = df["AwayTeam"]
matches["B365H"] = df["B365H"]
matches["B365D"] = df["B365D"]
matches["B365A"] = df["B365A"]

matches.to_csv("data/upcoming_matches.csv", index=False)

print("Upcoming matches:", len(matches))