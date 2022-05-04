import requests
import os
import dotenv
from pprint import pprint
import datetime

BASE_DIR = os.path.abspath(os.curdir)

dotenv_file = os.path.join(BASE_DIR, '.env')
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

open_weather_token = os.environ["OPEN_WEATHER_TOKEN"]

class Weather():
    """Прогноз погоды"""
    def get_weather(city, open_weather_token):
        # Иконки для отображения статуса погоды
        code_to_smile = {
            "Clear": "Ясно \U00002600",
            "Clouds": "Облачно \U00002601",
            "Rain": "Дождь \U00002614",
            "Drizzle": "Дождь \U00002614",
            "Thunderstorm": "Гроза \U000026A1",
            "Show": "Снег \U0001F328",
            "Mist": "Туман \U0001F32B"
        }

        try:
            r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric")
            data = r.json()
            # pprint(data)

            weather_description = data["weather"][0]["main" ]
            if weather_description in code_to_smile:
                wd = code_to_smile[weather_description]
            else:
                wd = 'Посмотри, что там за окном'

            city = data["name"]
            country = data["sys"]["country"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            wind =  data["wind"]["speed"]
            sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
            sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
            length_of_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) \
                            - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

            return f"* Прогноз погоды на: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} *\nГород: {city}\nКод страны: {country}\n" \
                   f"Температура: {temp}°C {wd}\nВлажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/c\n" \
                   f"Восход солнца: {sunrise}\nЗакат солнца: {sunset}\nПродолжительность дня: {length_of_day}"

        except Exception:
            return f"Проверьте название города"


# def main(city):
#     print(Weather.get_weather(city, open_weather_token))



# def main():
#     city = input("Введите город: ")
#     res = Weather.get_weather(city, open_weather_token)
#     print(res)


# if __name__ == '__main__':
#     city = 'Sumy'
#     main(city)
