import random

MAX_DRYING_RATE = 1.95 # percentage

SET_WEATHER_INFO_TIMER  = 10 # seconds
SET_TEMPERATURE_TIMER   = 10 # seconds
SET_MOISTURE_TIMER      = 5 # seconds

device_names = ["soil_sensor_q5_1", 
                "soil_sensor_q5_2", 
                "soil_sensor_q5_3", 
                "soil_sensor_q5_4"]

device_ids = {
    "soil_sensor_q5_1" : '1bbf1d32-1283-11ed-9523-a8b13bacd0d2',
    "soil_sensor_q5_2" : '203f0df9-1283-11ed-ae27-a8b13bacd0d2',
    "soil_sensor_q5_3" : '2579b236-1283-11ed-9f1d-a8b13bacd0d2',
    "soil_sensor_q5_4" : '2c22ed24-1283-11ed-87cf-a8b13bacd0d2'
}

quadrants = {
    "soil_sensor_q5_1" : 'quadrant_5',
    "soil_sensor_q5_2" : 'quadrant_5',
    "soil_sensor_q5_3" : 'quadrant_5',
    "soil_sensor_q5_4" : 'quadrant_5'
}

coordinates = {
    "soil_sensor_q5_1" : [23.696863, 88.072179],	
    "soil_sensor_q5_2" : [23.696363, 88.071679],
    "soil_sensor_q5_3" : [23.695863, 88.072179],
    "soil_sensor_q5_4" : [23.696363, 88.072679]
}

moisture_values = {
    "soil_sensor_q5_1" : round(random.normalvariate(30, 1.3), 1),
    "soil_sensor_q5_2" : round(random.normalvariate(30, 1.3), 1),
    "soil_sensor_q5_3" : round(random.normalvariate(30, 1.3), 1),
    "soil_sensor_q5_4" : round(random.normalvariate(30, 1.3), 1)
}

temperature_values = {
    "soil_sensor_q5_1" : 26,
    "soil_sensor_q5_2" : 26,
    "soil_sensor_q5_3" : 26,
    "soil_sensor_q5_4" : 26
}

sprinkler_info = {
    "name"          : "sprinkler_q5",
    "id"            : '325dedf1-1283-11ed-af81-a8b13bacd0d2',
    "quadrant"      : 'quadrant_5',
    "coordinates"   : [23.696363, 88.072179],
    "state"         : 0
}

weather_info = {
    "temperature"   : 26,
    "is_raining"    : 0
}