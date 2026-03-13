import pandas as pd
import requests

print("Sending Telegram bets...")

# TELEGRAM BOT
TOKEN = "8139937697:AAGel3-mAG2_yBtofHt5R1K7cpNYwiIKS6c"

# CHANNELS
FREE_CHAT_ID = -1003787743236
VIP_CHAT_ID = -1003819716884

# FILE WITH PREDICTIONS
FILE = "data/upcoming_predictions.csv"


def send_message(chat_id, text):

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    response = requests.post(url, data={
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    })

    print(response.text)


# LOAD PREDICTIONS

df = pd.read_csv(FILE)

df["max_prob"] = df[["prob_home", "prob_draw", "prob_away"]].max(axis=1)

df = df.sort_values("max_prob", ascending=False)


# SELECT BETS

free_bet = df.iloc[0]
vip_bets = df.iloc[1:5]


# FREE BET MESSAGE

free_msg = f"""
🔥 <b>AI FREE BET</b>

{free_bet['HomeTeam']} vs {free_bet['AwayTeam']}

Home: {free_bet['prob_home']:.2f}
Draw: {free_bet['prob_draw']:.2f}
Away: {free_bet['prob_away']:.2f}

━━━━━━━━━━━━

💎 Want the <b>4 PREMIUM AI bets</b>?

DM the bot 👇
@deinbetbot_bot
"""


# VIP MESSAGE

vip_msg = "💎 <b>AI VIP BETS</b>\n\n"

for _, row in vip_bets.iterrows():

    vip_msg += f"""
{row['HomeTeam']} vs {row['AwayTeam']}

Home: {row['prob_home']:.2f}
Draw: {row['prob_draw']:.2f}
Away: {row['prob_away']:.2f}

━━━━━━━━━━━━
"""


# SEND MESSAGES

print("Sending FREE bet...")
send_message(FREE_CHAT_ID, free_msg)

print("Sending VIP bets...")
send_message(VIP_CHAT_ID, vip_msg)

print("Telegram bets sent")