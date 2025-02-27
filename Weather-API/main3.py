from queries import create, read
import requests
from datetime import datetime


def normalizer(data):
    dt = str(datetime.fromtimestamp(data['dt']))
    temp = float(str(data['main']['temp'] - 273.15)[:4])
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    city = data['name']

    return {'city': city, 'dt': dt, 'temp': temp, 'wind_speed': wind_speed, 'humidity': humidity}


def get_weather_data(url, city):
    params = {
        "q": city,
        "appid": "ce28524cced047e5c594dabe55a408be",
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data['cod'] == '404':
        print("Invalid city name")
    else:
        data = normalizer(data)
        print(data)


get_weather_data(url="https://api.openweathermap.org/data/2.5/weather", city=input("City : "))
