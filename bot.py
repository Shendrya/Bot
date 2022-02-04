
import telebot
TOKEN = '5242981332:AAGsvhmn5KMoT-EP2Dl_xZPLmJAowaUV9TA' # bot token from @BotFather

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")

@bot.message_handler(content_types = ['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)

# Run
bot.polling(none_stop=True)
