import random

MAX_DRYING_RATE = 1.62 # percentage

SET_WEATHER_INFO_TIMER  = 10 # seconds
SET_TEMPERATURE_TIMER   = 10 # seconds
SET_MOISTURE_TIMER      = 5 # seconds

device_names = ["soil_sensor_q3_1", 
                "soil_sensor_q3_2", 
                "soil_sensor_q3_3", 
                "soil_sensor_q3_4"]

device_ids = {
    "soil_sensor_q3_1" : 'de111f20-1282-11ed-8761-a8b13bacd0d2',
    "soil_sensor_q3_2" : 'e344f61c-1282-11ed-ab6e-a8b13bacd0d2',
    "soil_sensor_q3_3" : 'e8993f04-1282-11ed-a85b-a8b13bacd0d2',
    "soil_sensor_q3_4" : 'edd5a890-1282-11ed-b142-a8b13bacd0d2'
}

quadrants = {
    "soil_sensor_q3_1" : 'quadrant_3',
    "soil_sensor_q3_2" : 'quadrant_3',
    "soil_sensor_q3_3" : 'quadrant_3',
    "soil_sensor_q3_4" : 'quadrant_3'
}

coordinates = {
    "soil_sensor_q3_1" : [23.692263, 88.067579],	
    "soil_sensor_q3_2" : [23.691763, 88.067079],
    "soil_sensor_q3_3" : [23.691263, 88.067579],
    "soil_sensor_q3_4" : [23.691763, 88.068079]
}

moisture_values = {
    "soil_sensor_q3_1" : round(random.normalvariate(30, 1.3), 1),
    "soil_sensor_q3_2" : round(random.normalvariate(30, 1.3), 1),
    "soil_sensor_q3_3" : round(random.normalvariate(30, 1.3), 1),
    "soil_sensor_q3_4" : round(random.normalvariate(30, 1.3), 1)
}

temperature_values = {
    "soil_sensor_q3_1" : 26,
    "soil_sensor_q3_2" : 26,
    "soil_sensor_q3_3" : 26,
    "soil_sensor_q3_4" : 26
}

sprinkler_info = {
    "name"          : "sprinkler_q3",
    "id"            : 'f2d7f8eb-1282-11ed-a75b-a8b13bacd0d2',
    "quadrant"      : 'quadrant_3',
    "coordinates"   : [23.691763, 88.067579],
    "state"         : 0
}

weather_info = {
    "temperature"   : 26,
    "is_raining"    : 0
}