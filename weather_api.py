# weather_api.py
import requests
from weather_data import WeatherData  # Correct import statement

API_KEY = "3ec95dd976578af31025357134bcc4e6"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if 'main' in data and 'temp' in data['main']:
        weather_data = {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }

        return WeatherData(**weather_data)
    else:
        return None
