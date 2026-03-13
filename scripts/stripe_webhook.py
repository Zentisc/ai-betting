from flask import Flask, request
import telebot

TOKEN = "DEIN_TELEGRAM_BOT_TOKEN"
VIP_CHANNEL_ID = -1003819716884

bot = telebot.TeleBot(TOKEN)
app = Flask(**name**)

@app.route("/stripe", methods=["POST"])
def stripe_webhook():

```
data = request.json  

if data["type"] == "checkout.session.completed":  

    session = data["data"]["object"]  

    telegram_id = session.get("client_reference_id")  

    # VIP Invite erstellen (nur einmal nutzbar)
    invite = bot.create_chat_invite_link(
        chat_id=VIP_CHANNEL_ID,
        member_limit=1
    )

    bot.send_message(
        telegram_id,
        f"✅ Payment received!\n\nJoin VIP:\n{invite.invite_link}"
    )

return "ok", 200  
```

if **name** == "**main**":
print("Stripe Webhook Server läuft...")
app.run(port=5000)
