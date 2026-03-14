import pandas as pd
import requests

TOKEN = "DEIN_BOT_TOKEN"

FREE_CHAT_ID = -1003787743236
VIP_CHAT_ID = -1003819716884

print("Sending Telegram bets...")

free = pd.read_csv("data/free_bets.csv")
vip = pd.read_csv("data/premium_bets.csv")

# ---------- FREE BET ----------

row = free.iloc[0]

text = f"""
🔥 AI FREE BET

{row['match']}

BET: {row['bet']}

Probability: {row['prob']}

━━━━━━━━━━━━

💎 Want the 3 PREMIUM AI bets?

The VIP AI bets will be unlocked when we reach 100 members in this channel 🚀

Invite your friends to unlock the VIP bets!
"""

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={"chat_id": FREE_CHAT_ID, "text": text}
)

print("FREE bet sent")


# ---------- VIP BETS ----------

text = "💎 AI VIP BETS\n\n"

for _, row in vip.iterrows():

    text += f"""
{row['match']}

BET: {row['bet']}

Probability: {row['prob']}

━━━━━━━━━━━━
"""

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={"chat_id": VIP_CHAT_ID, "text": text}
)

print("VIP bets sent")