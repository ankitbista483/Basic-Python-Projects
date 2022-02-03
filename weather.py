import imp
import requests
from pprint import pprint

API_key = "c3b14c9f27602e292c89ee82eb1164ef "

city = input("Enter a city of your choice: ")
base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)