# ce28524cced047e5c594dabe55a408be
import requests


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
        print(data["main"]["temp"])
        print(data["main"]["humidity"])
        print(data["dt"])


get_weather_data(url="https://api.openweathermap.org/data/2.5/weather", city=input("City : "))
