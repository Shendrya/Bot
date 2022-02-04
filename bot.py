import telebot
import config

bot = telebot.Telebot(config.token)

@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)

# Run
bot.polling(none_stop=True)
