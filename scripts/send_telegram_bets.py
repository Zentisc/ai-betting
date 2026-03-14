import pandas as pd
import requests

TOKEN = "8139937697:AAGel3-mAG2_yBtofHt5R1K7cpNYwiIKS6c "

FREE_CHAT_ID = -1003787743236
VIP_CHAT_ID = -1003819716884

print("Sending Telegram bets...")

free = pd.read_csv("data/free_bets.csv")
vip = pd.read_csv("data/premium_bets.csv")

# ---------- FREE BET ----------

if len(free) > 0:

    row = free.iloc[0]

    text = f"""
🔥 AI FREE BET

{row['match']}

BET: {row['bet']}

Probability: {round(row['prob']*100,1)}%

━━━━━━━━━━━━

💎 Want the 4 PREMIUM AI bets?

Invite your friends to unlock VIP bets 🚀
"""

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": FREE_CHAT_ID, "text": text}
    )

    print("FREE bet sent")

else:

    text = "No strong AI bets found today."

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": FREE_CHAT_ID, "text": text}
    )

    print("No free bets today")


# ---------- VIP BETS ----------

if len(vip) > 0:

    text = "💎 AI VIP BETS\n\n"

    for _, row in vip.iterrows():

        text += f"""
{row['match']}

BET: {row['bet']}

Probability: {round(row['prob']*100,1)}%

━━━━━━━━━━━━
"""

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": VIP_CHAT_ID, "text": text}
    )

    print("VIP bets sent")

else:

    print("No VIP bets today")