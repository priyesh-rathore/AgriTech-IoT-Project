import time
import json
import threading
from OpenWeatherAPI import get_weather_info

from aws_iot_core_mqtt import *
from influxdb import *

#-----------------------------------------------#

# Defining properties for the backend.
WEATHER_CHECK_TIMER = 10

MINIMUM_MOISTURE = 20
MAXIMUM_MOISTURE = 70

# Minimum 2 devices MUST be in a quadrant.
MINIMUM_DEVICE_NUMBER = 2

#-----------------------------------------------#

# Runtime buffer(s) for devices.
# The backend logic is dynamic and maintains its own buffers for all statuses.
soil_sensors = {}
sprinklers = {}
# Can be left empty like above buffers but is filled for demonstration purposes.
weather_info = {
    'quadrant_1' : {
        'coordinates' : [23.694063, 88.069879],
        'is_raining'  : 0
    },
    'quadrant_2' : {
        'coordinates' : [23.696363, 88.067579],
        'is_raining'  : 0
    },
    'quadrant_3' : {
        'coordinates' : [23.691763, 88.067579],
        'is_raining'  : 0
    },
    'quadrant_4' : {
        'coordinates' : [23.691763, 88.072179],
        'is_raining'  : 0
    },
    'quadrant_5' : {
        'coordinates' : [23.696363, 88.072179],
        'is_raining'  : 0
    }
}

# Each value is equal to the number of devices that need water.
moisture_checker = {
    'quadrant_1' : 0,
    'quadrant_2' : 0,
    'quadrant_3' : 0,
    'quadrant_4' : 0,
    'quadrant_5' : 0
}

# Add a quadrant based weather status table
def weather_check():
    for quadrant in weather_info:
        lat, long = weather_info[quadrant]['coordinates'][0], weather_info[quadrant]['coordinates'][1]
        try : 
            openweatherAPI_response = get_weather_info(lat, long)
            temperature = openweatherAPI_response['main']['temp']
            pressure = openweatherAPI_response['main']['pressure']
            humidity = openweatherAPI_response['main']['humidity']
            if(openweatherAPI_response["weather"][0]['main'] == 'Rain'):
                # Yes, it is raining
                weather_info[quadrant]['is_raining'] = 1
            else:
                # No, it is not raining 
                weather_info[quadrant]['is_raining'] = 0
        except :
            print("Error in fetching weather data.")
        try:
            write_to_influx(quadrant, 'weather_data', 'temperature', temperature)
            write_to_influx(quadrant, 'weather_data', 'pressure', pressure)
            write_to_influx(quadrant, 'weather_data', 'humidity', humidity)
            write_to_influx(quadrant, 'weather_data', 'is_raining', weather_info[quadrant]['is_raining'])
        except:
            print("Error writing weather data to influx")
    threading.Timer(WEATHER_CHECK_TIMER, weather_check).start()

def soil_sensor_msg_handler(message):
    device_name = message['device_name']
    device_id = message['device_id']
    quadrant = message['quadrant']
    temperature = message['temperature']
    moisture = message['moisture']
    field = device_name + "(" + device_id + ")"
    if(device_name not in soil_sensors):
        soil_sensors[device_name] = {}
        soil_sensors[device_name]['device_id'] = device_id
        soil_sensors[device_name]['coordinates'] = message['coordinates']
        soil_sensors[device_name]['quadrant'] = quadrant
        soil_sensors[device_name]['temperature'] = temperature
        soil_sensors[device_name]['moisture'] = moisture
        soil_sensors[device_name]['needs_water'] = None
    elif(device_name in soil_sensors):
        soil_sensors[device_name]['temperature'] = temperature
        soil_sensors[device_name]['moisture'] = moisture
        try:
            write_to_influx(quadrant, field, 'temperature', temperature)
            write_to_influx(quadrant, field, 'moisture', moisture)
        except:
            print("InfluxDB error!!!")
    if(moisture <= MINIMUM_MOISTURE):
        soil_sensors[device_name]['needs_water'] = 1
    elif(moisture >= MAXIMUM_MOISTURE):
        soil_sensors[device_name]['needs_water'] = 0

def sprinkler_telemetry_msg_handler(message):
    device_name = message['name']
    device_id = message['id']
    quadrant = message['quadrant']
    coordinates = message['coordinates']
    state = message['state']
    field = device_name + "(" + device_id + ")"

    # Adding quadrant if not already there in backend buffer.
    if(quadrant not in moisture_checker):
        moisture_checker[quadrant] = 0
        weather_info[quadrant] = {
            'coordinates' : [coordinates[0], coordinates[1]],
            'is_raining'  : 0     
        }

    if(device_name not in sprinklers):
        sprinklers[device_name] = {}
        sprinklers[device_name]['name'] = device_name
        sprinklers[device_name]['id'] = device_id
        sprinklers[device_name]['coordinates'] = coordinates
        sprinklers[device_name]['quadrant'] = quadrant
        # Writing lat,long of the quadrant to database.
        write_to_influx(quadrant, 'coordinates', 'latitude', coordinates[0])
        write_to_influx(quadrant, 'coordinates', 'longitude', coordinates[1])

    if(device_name in sprinklers):
        sprinklers[device_name]['state'] = state
        try:
            write_to_influx(quadrant, field, 'state', message['state'])
        except:
            print("InfluxDB error !!!")

def customCallback(client, userdata, msg):
    received = msg.payload
    received = received.decode("utf-8")
    #print("Recieved : ", msg.topic+ " " + received)
    if(msg.topic[-12:] == 'soil_sensors'):
        soil_sensor_msg_handler(json.loads(received))
    elif(msg.topic[-19:] == 'sprinkler_telemetry'):
        sprinkler_telemetry_msg_handler(json.loads(received))

def subscribe(TOPIC, QOS):
    myAWSIoTMQTTClient.subscribe(TOPIC, QOS, customCallback)
    print(f"Successfully subscribed to topic : {TOPIC} with QoS : {QOS}")

subscribe(ALL_SOIL_SENSORS, 0)
subscribe(ALL_SPRINKLERS, 0)

def check_soil_sensor_moisture():  
    global soil_sensors
    global sprinklers
    # Implement Rain Check
    # if Raining then sprinkler OFF
    # else :
    for quadrant in moisture_checker:
        moisture_checker[quadrant] = 0
    for quadrant in moisture_checker:
        # Checking for rain, if there is rain the sprinkler is turned OFF
        # and no futher check is done.
        if(weather_info[quadrant]['is_raining'] == 1):
            for sprinkler in sprinklers:
                if(sprinklers[sprinkler]['quadrant'] == quadrant):
                    prev_state = sprinklers[sprinkler]['state']
                    sprinklers[sprinkler]['state'] = 0                              # Turning Sprinkler OFF
                    if(prev_state != sprinklers[sprinkler]['state']):
                        TOPIC = generate_sprinkler_command_topic(quadrant)
                        publish(json.dumps(sprinklers[sprinkler]), TOPIC, 0)
        else:
            for device in soil_sensors:
                if(soil_sensors[device]['quadrant'] == quadrant):
                    if(soil_sensors[device]['needs_water'] == 1):
                        moisture_checker[quadrant] += 1                             # Incrementing number of devices that need water
            if(moisture_checker[quadrant] >= MINIMUM_DEVICE_NUMBER):
                for sprinkler in sprinklers:
                    if(sprinklers[sprinkler]['quadrant'] == quadrant):
                        prev_state = sprinklers[sprinkler]['state']
                        sprinklers[sprinkler]['state'] = 1                          # Turning Sprinkler ON
                        if(prev_state != sprinklers[sprinkler]['state']):
                            TOPIC = generate_sprinkler_command_topic(quadrant)
                            publish(json.dumps(sprinklers[sprinkler]), TOPIC, 0)
            elif(moisture_checker[quadrant] < MINIMUM_DEVICE_NUMBER):
                for sprinkler in sprinklers:
                    if(sprinklers[sprinkler]['quadrant'] == quadrant):
                        prev_state = sprinklers[sprinkler]['state']
                        sprinklers[sprinkler]['state'] = 0                          # Turning Sprinkler OFF
                        if(prev_state != sprinklers[sprinkler]['state']):
                            TOPIC = generate_sprinkler_command_topic(quadrant)
                            publish(json.dumps(sprinklers[sprinkler]), TOPIC, 0)

# Initiating threaded weather check function.
# It will run in background. For more details check its implementation.
weather_check()

while(1):
    check_soil_sensor_moisture()
    for soil_sensor in soil_sensors:
        print(soil_sensors[soil_sensor])
    print("")
    for sprinkler in sprinklers:
        print(sprinklers[sprinkler])
    print("")
    # for quadrant in weather_info:
    #     print(weather_info[quadrant])
    # print("")
    print(moisture_checker)
    print("")
    time.sleep(10)