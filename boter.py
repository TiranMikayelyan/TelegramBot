import telebot
from telebot import types

token = '8073368982:AAGorvlf-F-NwO1gAOmuwAz_34KEoDD-E6s'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Enter To See A Surprise", callback_data="show_surprise")
    markup.add(button)

    bot.send_message(
        message.chat.id,
        "Hello {}! 👋✨ If you want to see a surprise 🎁, please tap the button below ⬇️!".format(message.from_user.first_name),
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == "show_surprise")
def handle_surprise(call):
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="🎉 💖 Happy Birthday! 🥳 Another year, another adventure! May your life be filled with love, success, and beautiful moments. Celebrate big and make unforgettable memories! 🎊🎁🎉"
    )

    try:
        video = open("C:\\Users\\user\\Desktop\\To.mp4", "rb")
        bot.send_video(call.message.chat.id, video, caption="🎂 Enjoy this birthday surprise video!")
        video.close()  
    except Exception as e:
        bot.send_message(call.message.chat.id, f"❌ Error sending video: {str(e)}")

bot.infinity_polling()

