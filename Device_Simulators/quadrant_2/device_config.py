import random

MAX_DRYING_RATE = 0.33 # percentage

SET_WEATHER_INFO_TIMER  = 10 # seconds
SET_TEMPERATURE_TIMER   = 10 # seconds
SET_MOISTURE_TIMER      = 5 # seconds

device_names = ["soil_sensor_q2_1", 
                "soil_sensor_q2_2", 
                "soil_sensor_q2_3", 
                "soil_sensor_q2_4"]

device_ids = {
    "soil_sensor_q2_1" : 'bc76da1d-1282-11ed-b290-a8b13bacd0d2',
    "soil_sensor_q2_2" : 'c568db46-1282-11ed-aab6-a8b13bacd0d2',
    "soil_sensor_q2_3" : 'cbb5e74f-1282-11ed-ad09-a8b13bacd0d2',
    "soil_sensor_q2_4" : 'd1228c4a-1282-11ed-b522-a8b13bacd0d2'
}

quadrants = {
    "soil_sensor_q2_1" : 'quadrant_2',
    "soil_sensor_q2_2" : 'quadrant_2',
    "soil_sensor_q2_3" : 'quadrant_2',
    "soil_sensor_q2_4" : 'quadrant_2'
}

coordinates = {
    "soil_sensor_q2_1" : [23.696863, 88.067579],	
    "soil_sensor_q2_2" : [23.696363, 88.067079],
    "soil_sensor_q2_3" : [23.696363, 88.068079],
    "soil_sensor_q2_4" : [23.695863, 88.067579]
}

moisture_values = {
    "soil_sensor_q2_1" : round(random.normalvariate(30, 1.3), 1),
    "soil_sensor_q2_2" : round(random.normalvariate(30, 1.3), 1),
    "soil_sensor_q2_3" : round(random.normalvariate(30, 1.3), 1),
    "soil_sensor_q2_4" : round(random.normalvariate(30, 1.3), 1)
}

temperature_values = {
    "soil_sensor_q2_1" : 26,
    "soil_sensor_q2_2" : 26,
    "soil_sensor_q2_3" : 26,
    "soil_sensor_q2_4" : 26
}

sprinkler_info = {
    "name"          : "sprinkler_q2",
    "id"            : 'd754c869-1282-11ed-8b4d-a8b13bacd0d2',
    "quadrant"      : 'quadrant_2',
    "coordinates"   : [23.696363, 88.067579],
    "state"         : 0
}

weather_info = {
    "temperature"   : 26,
    "is_raining"    : 0
}