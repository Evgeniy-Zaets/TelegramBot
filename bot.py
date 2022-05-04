import telebot
import os
from telebot import types
import dotenv
import weather
from pprint import pprint

BASE_DIR = os.path.abspath(os.curdir)

dotenv_file = os.path.join(BASE_DIR, '.env')
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

bot = telebot.TeleBot(os.environ["TOKEN_BOT"])
open_weather_token = os.environ["OPEN_WEATHER_TOKEN"]

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start_messages(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_weater = types.KeyboardButton("Прогноз погоды")
    item_currency = types.KeyboardButton("Курс валют")
    markup.add(item_weater)
    markup.add(item_currency)
    msg = bot.send_message(message.chat.id, 'Привет! Выбери, что тебя интересует', reply_markup=markup)
    bot.register_next_step_handler(msg, send_text)


# Получение сообщений от юзера
def send_text(message):
    if message.text == 'Прогноз погоды' :
        bot.send_message(message.chat.id, 'Какой город интересует?')
        @bot.message_handler(content_types=["text"])
        def handle_text(message):
            bot.send_message(message.chat.id, weather.Weather.get_weather(message.text, open_weather_token))
    if message.text == 'Курс валют':
        pass

# Запускаем бота4
bot.polling(none_stop=True, interval=0)