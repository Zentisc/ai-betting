from flask import Flask, request
import telebot
import time

TOKEN = "8139937697:AAGel3-mAG2_yBtofHt5R1K7cpNYwiIKS6c"
VIP_CHANNEL_ID = -1003819716884

bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)


@app.route("/stripe", methods=["POST"])
def stripe_webhook():

    data = request.json

    if data["type"] == "checkout.session.completed":

        session = data["data"]["object"]

        telegram_id = int(session.get("client_reference_id"))

        # Einmal-Invite erstellen (läuft nach 5 Minuten ab)
        invite = bot.create_chat_invite_link(
            chat_id=VIP_CHANNEL_ID,
            member_limit=1,
            expire_date=int(time.time()) + 300
        )

        bot.send_message(
            telegram_id,
            f"✅ Payment received!\n\nJoin VIP:\n{invite.invite_link}"
        )

    return "ok", 200


if __name__ == "__main__":
    print("Stripe Webhook Server läuft...")
    app.run(host="0.0.0.0", port=5000)