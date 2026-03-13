import pandas as pd

print("Downloading matches...")

leagues = {
    "E0": "Premier League",
    "D1": "Bundesliga",
    "SP1": "La Liga",
    "I1": "Serie A",
    "F1": "Ligue 1"
}

all_matches = []

for code in leagues:

    url = f"https://www.football-data.co.uk/mmz4281/2425/{code}.csv"

    try:
        data = pd.read_csv(url)

        data = data[[
            "Date",
            "HomeTeam",
            "AwayTeam",
            "B365H",
            "B365D",
            "B365A"
        ]]

        data["League"] = leagues[code]

        all_matches.append(data)

    except:
        print("Failed:", code)

matches = pd.concat(all_matches)

# nur Test: letzte Spiele
matches = matches.tail(50)

matches.to_csv("data/upcoming_matches.csv", index=False)

print("Matches saved:", len(matches))