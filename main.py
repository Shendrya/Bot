import config
import telebot

bot = telebot.TeleBot(config.TOKEN)

#from telebot import types

@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет')

@bot.message_handler(content_types = 'text')
def message_reply(message):
    if message.text == "Курс":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btc = types.KeyboardButton("BTC")
        markup.add(btc)
        ton = types.KeyboardButton("TONCOIN")
        markup.add(ton)
    elif message.text=="BTC":
        bot.send_message(message.chat.id,'44500$')
    elif message.text=="TONCOIN":
        bot.send_message(message.chat.id,'3$')

bot.infinity_polling()
