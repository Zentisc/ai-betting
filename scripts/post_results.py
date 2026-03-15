import pandas as pd
import requests
import os

TOKEN = "8139937697:AAGel3-mAG2_yBtofHt5R1K7cpNYwiIKS6c"
FREE_CHAT_ID = -1003787743236

print("Posting AI results...")

# prüfen ob bet files existieren
if not os.path.exists("data/free_bet.csv"):
    print("No bets found")
    exit()

free_bets = pd.read_csv("data/free_bet.csv")
vip_bets = pd.read_csv("data/vip_bets.csv")

bets = pd.concat([free_bets, vip_bets], ignore_index=True)

# doppelte Spiele entfernen
bets = bets.drop_duplicates(subset=["match"])

# max 5 bets anzeigen
bets = bets.head(5)

matches = pd.read_csv("data/raw_matches.csv")

results_text = "📊 AI RESULTS\n\n"

wins = 0
losses = 0

for _, bet in bets.iterrows():

    match_text = bet["match"]
    home, away = match_text.split(" vs ")

    bet_type = bet["bet"]

    if bet_type == "HOME":
        pred = "H"
    elif bet_type == "DRAW":
        pred = "D"
    else:
        pred = "A"

    match = matches[
        (matches["HomeTeam"] == home) &
        (matches["AwayTeam"] == away)
    ]

    if match.empty:
        result = "⏳ PENDING"
        results_text += f"{home} vs {away} {result}\n"
        continue

    real = match.iloc[-1]["FTR"]

    if pred == real:
        result = "✅ WIN"
        wins += 1
    else:
        result = "❌ LOSS"
        losses += 1

    results_text += f"{home} vs {away} {result}\n"


results_text += f"\nDaily Record\nWins: {wins}\nLosses: {losses}"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": FREE_CHAT_ID,
    "text": results_text
})

print("Results posted")