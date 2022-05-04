import telebot
from telebot import types

bot = telebot.TeleBot("5150954661:AAG_APsnKkm2BCSfpwtVGxWrVkGm5JnRac8")
@bot.message_handler(commands=["start"])


def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_weater = types.KeyboardButton("Прогноз погоды")
    item2_currency = types.KeyboardButton("Курс валют")
    markup.add(item_weater)
    markup.add(item2_currency)
    bot.send_message(m.chat.id, 'Здравствуйте! Вас приветствует информационный телеграм бот',
                     reply_markup=markup)

bot.polling(none_stop=True, interval=0)