import os
import telebot
from telebot import types
import dotenv
import weather, crypto

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
    item_weather = types.KeyboardButton("Прогноз погоды")
    item_currency = types.KeyboardButton("Курс криптовалюты")
    markup.row(item_weather, item_currency)
    msg = bot.send_message(message.chat.id, 'Привет! Выбери, что тебя интересует', reply_markup=markup)
    bot.register_next_step_handler(msg, send_text)


# Получение сообщений от юзера
def send_text(message):
    # Описание действий при выборе прогноза погоды
    if message.text == 'Прогноз погоды' :
        bot.send_message(message.chat.id, 'Какой город интересует?')
        @bot.message_handler(content_types=["text"])
        def handle_text(message):
            msg = bot.send_message(message.chat.id, weather.Weather.get_weather(message.text, open_weather_token),
                             parse_mode="Markdown")


    # Описание действий при выборе курса криптовалюты
    if message.text == 'Курс криптовалюты':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item_btc = types.InlineKeyboardButton("BTC")
        item_eth = types.InlineKeyboardButton("ETH")
        item_ape = types.InlineKeyboardButton("APE")
        item_usdt = types.InlineKeyboardButton("USDT")
        markup.row(item_btc, item_eth)
        markup.row(item_ape, item_usdt)
        msg = bot.send_message(message.chat.id, 'Выбери, какая криптовалюта интересует', reply_markup=markup)
        @bot.message_handler(content_types=["text"])
        def handle_text(message):
            msg = bot.send_message(message.chat.id, crypto.cryptocurrency(message.text), parse_mode="Markdown")

# Запускаем бота
bot.polling(none_stop=True, interval=0)