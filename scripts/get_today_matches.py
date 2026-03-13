import requests
import pandas as pd
from datetime import datetime, timedelta

print("Downloading matches...")

API_KEY = "403d17a9599f1b46c41dc6096d91a9d5"

sports = [
    "soccer_epl",
    "soccer_spain_la_liga",
    "soccer_germany_bundesliga",
    "soccer_italy_serie_a",
    "soccer_france_ligue_one"
]

matches = []

now = datetime.utcnow()
limit = now + timedelta(hours=48)

for sport in sports:

    url = f"https://api.the-odds-api.com/v4/sports/{sport}/odds/?regions=eu&markets=h2h&apiKey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    for game in data:

        game_time = game["commence_time"]
        game_date = datetime.fromisoformat(game_time.replace("Z",""))

        # nur Spiele innerhalb der nächsten 48h
        if game_date < now or game_date > limit:
            continue

        home = game["home_team"]
        away = game["away_team"]

        if len(game["bookmakers"]) == 0:
            continue

        outcomes = game["bookmakers"][0]["markets"][0]["outcomes"]

        home_odds = None
        draw_odds = None
        away_odds = None

        for o in outcomes:

            if o["name"] == home:
                home_odds = o["price"]

            elif o["name"] == away:
                away_odds = o["price"]

            elif o["name"].lower() == "draw":
                draw_odds = o["price"]

        if home_odds and draw_odds and away_odds:

            matches.append({
                "Date": game_date,
                "HomeTeam": home,
                "AwayTeam": away,
                "B365H": home_odds,
                "B365D": draw_odds,
                "B365A": away_odds
            })

df = pd.DataFrame(matches)

df.to_csv("data/upcoming_matches.csv", index=False)

print("Matches in next 48h:", len(df))