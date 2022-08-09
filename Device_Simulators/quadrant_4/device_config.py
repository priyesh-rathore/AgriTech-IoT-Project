import random

MAX_DRYING_RATE = 0.64 # percentage

SET_WEATHER_INFO_TIMER  = 10 # seconds
SET_TEMPERATURE_TIMER   = 10 # seconds
SET_MOISTURE_TIMER      = 5 # seconds

device_names = ["soil_sensor_q4_1", 
                "soil_sensor_q4_2", 
                "soil_sensor_q4_3", 
                "soil_sensor_q4_4"]

device_ids = {
    "soil_sensor_q4_1" : 'f8f6ca96-1282-11ed-bd7d-a8b13bacd0d2',
    "soil_sensor_q4_2" : 'fd102720-1282-11ed-9c73-a8b13bacd0d2',
    "soil_sensor_q4_3" : '04538d48-1283-11ed-92d6-a8b13bacd0d2',
    "soil_sensor_q4_4" : '0994ca05-1283-11ed-92b9-a8b13bacd0d2'
}

quadrants = {
    "soil_sensor_q4_1" : 'quadrant_4',
    "soil_sensor_q4_2" : 'quadrant_4',
    "soil_sensor_q4_3" : 'quadrant_4',
    "soil_sensor_q4_4" : 'quadrant_4'
}

coordinates = {
    "soil_sensor_q4_1" : [23.692263, 88.072179],	
    "soil_sensor_q4_2" : [23.691763, 88.071679],
    "soil_sensor_q4_3" : [23.691263, 88.072179],
    "soil_sensor_q4_4" : [23.691763, 88.072679]
}

moisture_values = {
    "soil_sensor_q4_1" : round(random.normalvariate(30, 1.3), 1),
    "soil_sensor_q4_2" : round(random.normalvariate(30, 1.3), 1),
    "soil_sensor_q4_3" : round(random.normalvariate(30, 1.3), 1),
    "soil_sensor_q4_4" : round(random.normalvariate(30, 1.3), 1)
}

temperature_values = {
    "soil_sensor_q4_1" : 26,
    "soil_sensor_q4_2" : 26,
    "soil_sensor_q4_3" : 26,
    "soil_sensor_q4_4" : 26
}

sprinkler_info = {
    "name"          : "sprinkler_q4",
    "id"            : '0f10bf24-1283-11ed-a30d-a8b13bacd0d2',
    "quadrant"      : 'quadrant_4',
    "coordinates"   : [23.691763, 88.072179],
    "state"         : 0
}

weather_info = {
    "temperature"   : 26,
    "is_raining"    : 0
}