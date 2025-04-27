# Getting Weather Information Python Project

import requests
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

print('...api_key...', API_KEY)

city = input("Enter a city: ")

base_url = f"http://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city}"
# base_url = f"http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API_KEY}&q={city}"

weather_data = requests.get(base_url).json()

pprint(weather_data)