import requests
import datetime


def cryptocurrency(crypto):
    """Функция предоставляет информацию о курсе криптовалюты"""

    url = f"https://min-api.cryptocompare.com/data/pricemulti?fsyms={crypto}&tsyms=USD,EUR,UAH,RUB"
    responce = requests.get(url).json()

    for res in responce:
        if res == crypto:
            return f"*Курс {crypto} на {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n*" \
                   f"USD: {responce[res]['USD']}\n" \
                   f"EUR: {responce[res]['EUR']}\n" \
                   f"UAH: {responce[res]['UAH']}"