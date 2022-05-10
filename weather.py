import requests
import datetime



def get_weather(city, open_weather_token):
    """Функция предоставляет информацию о прогноз погоды"""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"

    # Иконки для отображения состояния погоды
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
        data = requests.get(url).json()

        # Описываем состояние погоды
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
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M:%S")
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M:%S")
        length_of_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) \
                        - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        # Формирование сообщения с описанием погоды
        return \
                f"*Прогноз погоды на: {datetime.datetime.now().strftime('%d.%m.%Y %H:%M')}*\n" \
                f"Город: {city}\nКод страны: {country}\nТемпература: {temp}°C {wd}\nВлажность: {humidity}%\n" \
                f"Давление: {pressure} мм.рт.ст\nВетер: {wind} м/c\nВосход солнца: {sunrise}\n" \
                f"Закат солнца: {sunset}\nПродолжительность дня: {length_of_day}"

    except Exception:
        # Возвращаем текст, если город был не найден
        return f"Проверьте название города."