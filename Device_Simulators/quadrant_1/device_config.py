import random

MAX_DRYING_RATE = 2.70 # percentage

SET_WEATHER_INFO_TIMER  = 10 # seconds
SET_TEMPERATURE_TIMER   = 10 # seconds
SET_MOISTURE_TIMER      = 5 # seconds

device_names = ["soil_sensor_q1_1", 
                "soil_sensor_q1_2", 
                "soil_sensor_q1_3", 
                "soil_sensor_q1_4"]

device_ids = {
    "soil_sensor_q1_1" : '839d184c-0866-11ed-a098-fcde56ff0106',
    "soil_sensor_q1_2" : '8e0d96a6-0866-11ed-9568-fcde56ff0106',
    "soil_sensor_q1_3" : '9b43c2ce-0866-11ed-b767-fcde56ff0106',
    "soil_sensor_q1_4" : 'a59e0e7e-0866-11ed-9b48-fcde56ff0106'
}

quadrants = {
    "soil_sensor_q1_1" : 'quadrant_1',
    "soil_sensor_q1_2" : 'quadrant_1',
    "soil_sensor_q1_3" : 'quadrant_1',
    "soil_sensor_q1_4" : 'quadrant_1'
}

coordinates = {
    "soil_sensor_q1_1" : [23.694563, 88.069879],	
    "soil_sensor_q1_2" : [23.694063, 88.069379],
    "soil_sensor_q1_3" : [23.693563, 88.069879],
    "soil_sensor_q1_4" : [23.694063, 88.070379]
}

moisture_values = {
    "soil_sensor_q1_1" : round(random.normalvariate(30, 1.3), 1),
    "soil_sensor_q1_2" : round(random.normalvariate(30, 1.3), 1),
    "soil_sensor_q1_3" : round(random.normalvariate(30, 1.3), 1),
    "soil_sensor_q1_4" : round(random.normalvariate(30, 1.3), 1)
}

temperature_values = {
    "soil_sensor_q1_1" : 26,
    "soil_sensor_q1_2" : 26,
    "soil_sensor_q1_3" : 26,
    "soil_sensor_q1_4" : 26
}

sprinkler_info = {
    "name"          : "sprinkler_q1",
    "id"            : 'c9f73e82-0866-11ed-a5d2-fcde56ff0106',
    "quadrant"      : 'quadrant_1',
    "coordinates"   : [23.694063, 88.069879],
    "state"         : 0
}

weather_info = {
    "temperature"   : 26,
    "is_raining"    : 0
}