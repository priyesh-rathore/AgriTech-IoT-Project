import requests
import json

api_key = "06fc2a6b18bc511d32d9bcb9eeac342c"

def get_weather_info(lat,long):
    lat, long = str(lat), str(long)
    url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=metric" % (lat, long, api_key)
    response = requests.get(url)
    data = json.loads(response.text)
    #print(data)
    return data