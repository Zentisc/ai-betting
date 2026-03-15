import pandas as pd
import requests

TOKEN = "8139937697:AAGel3-mAG2_yBtofHt5R1K7cpNYwiIKS6c"

FREE_CHAT_ID = -1003787743236
VIP_CHAT_ID = -1003819716884

print("Sending Telegram bets...")

free = pd.read_csv("data/free_bet.csv")
vip = pd.read_csv("data/vip_bets.csv")


# FREE BET
row = free.iloc[0]

free_message = f"""
🔥 AI FREE BET

{row['match']}

BET: {row['bet']}

Probability: {round(row['prob']*100,1)}%

━━━━━━━━━━━━

💎 Want the 3 PREMIUM AI bets?

The VIP AI bets will be unlocked when we reach 100 members in this channel 🚀

Invite your friends to unlock the VIP bets!
"""

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={"chat_id": FREE_CHAT_ID, "text": free_message}
)

print("FREE bet sent")


# VIP BETS
vip_message = "💎 AI VIP BETS\n\n"

for _, row in vip.iterrows():

    vip_message += f"""{row['match']}

BET: {row['bet']}

Probability: {round(row['prob']*100,1)}%

━━━━━━━━━━━━
"""

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={"chat_id": VIP_CHAT_ID, "text": vip_message}
)

print("VIP bets sent")