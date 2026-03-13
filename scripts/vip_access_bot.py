import telebot

TOKEN = "8139937697:AAGel3-mAG2_yBtofHt5R1K7cpNYwiIKS6c"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):

    telegram_id = message.from_user.id

    stripe_link = f"https://buy.stripe.com/test_28E6oG1Az2fq0Tj3iE2Fa00?client_reference_id={telegram_id}"

    text = f"""
🔥 AI BETTING VIP

Price: 19€

Pay here 👇
{stripe_link}

After payment you automatically receive VIP access.
"""

    bot.send_message(message.chat.id, text)

print("VIP BOT RUNNING...")
bot.infinity_polling()