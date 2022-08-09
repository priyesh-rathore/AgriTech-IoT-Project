import random
import time
import threading
import json
import datetime as dt

from device_config import *
from OpenWeatherAPI import *
from aws_iot_core_mqtt import *

def set_weather_info():
    global weather_info
    # Calling the OpenWeather API and get the temperature value at the sprinkler's coordinates.
    lat, long = sprinkler_info["coordinates"][0], sprinkler_info["coordinates"][1]
    try:
        openweatherAPI_response = get_weather_info(lat, long)
        if(openweatherAPI_response["weather"][0]['main'] == 'Rain'):
            # Yes, it is raining
            weather_info['is_raining'] = 1 
        else:
            # No, it is not raining
            weather_info['is_raining'] = 0 
        # Getting temperature in Celsius
        weather_info['temperature'] = openweatherAPI_response["main"]["temp"] 
    except:
        print("Error in openweatherAPI response!!!")
    #print(f"Got temperature {weather_info['temperature']}")
    threading.Timer(SET_WEATHER_INFO_TIMER, set_weather_info).start()

def set_temperature():
    global temperature_values
    global weather_info
    temperature = weather_info['temperature']
    for device in temperature_values:
        temperature_values[device] = random.normalvariate(temperature, 1.5)
    #print(f"Setting temperature {temperature}")
    threading.Timer(SET_TEMPERATURE_TIMER, set_temperature).start()

def set_moisture():
    global moisture_values
    global sprinkler_info
    global weather_info
    temperature = weather_info['temperature']
    drying_rate = MAX_DRYING_RATE*(temperature/100)
    if(weather_info['is_raining']):
        for device in moisture_values:
            if(moisture_values[device] < 100):
                moisture_values[device] += random.uniform(0.5,1)
            elif(moisture_values[device] > 100):
                moisture_values[device] = 100
    elif(sprinkler_info["state"] == 0):
        for device in moisture_values:
            if(moisture_values[device] > 0):
                moisture_values[device] -= drying_rate
            elif(moisture_values[device] < 0):
                moisture_values[device] = 0
    elif(sprinkler_info["state"] == 1):
        for device in moisture_values:
            if(moisture_values[device] < 100):
                moisture_values[device] += random.uniform(0.5,1)
            elif(moisture_values[device] > 100):
                moisture_values[device] = 100
    #print(f"Setting moisture at rate {drying_rate}")
    threading.Timer(SET_MOISTURE_TIMER, set_moisture).start()
    
set_weather_info()
set_temperature()
set_moisture()

subscribe(SPRINKLER_COMMAND_TOPIC, 0)

while(1):
    print("")
    print(f"Weather in Quadrant 4 : {weather_info}")
    print(sprinkler_info)
    # Publish sprinkler data
    sprinkler_info['state'] = get_sprinkler_state()
    sprinkler_info['timestamp'] = str(dt.datetime.now())
    sprinkler_telemetry = json.dumps(sprinkler_info)
    try:
        publish(sprinkler_telemetry, SPRINKLER_TELEMETRY_TOPIC, 0)
    except:
        print("Sprinkler telemetry publish error!")

    # Generate packet for each device and publish to AWS IoT Core
    for device_name in device_names:
        packet = {}
        packet['device_name'] = device_name
        packet['device_id'] = device_ids[device_name]
        packet['quadrant'] = quadrants[device_name]
        packet['coordinates'] = coordinates[device_name]
        packet['moisture'] = round(moisture_values[device_name], 2)
        packet['temperature'] = round(temperature_values[device_name], 2)
        packet['timestamp'] = str(dt.datetime.now())
        message = json.dumps(packet)
        try:
            publish(message, SOIL_SENSOR_TOPIC, 0)
        except:
            print(f"Device data {device_name} publish error!")

    time.sleep(10)