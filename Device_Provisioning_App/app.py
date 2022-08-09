import uuid
import time
from aws_iot_create_thing import createThing
from aws_dynamo_db import insert_to_dynamoDB
from pywebio.input import *
from pywebio.output import *

while(1):
    device_data = {}
    put_text("Agritech : New Device Registration")
    device_data['device_name'] = input("Enter Device(AWS-Thing) Name", TEXT)
    device_data['device_type'] = select("Select Device Type", ['soil_sensor', 'sprinkler'])
    device_data['quadrant'] = select("Select Quadrant", ['quadrant_1', 'quadrant_2', 'quadrant_3', 'quadrant_4', 'quadrant_5', 'quadrant_6'])
    device_data['latitude'] = input("Enter Latitude", FLOAT)
    device_data['longitude'] = input("Enter Longitude", FLOAT)
    device_data['device_id'] = str(uuid.uuid1())

    createThing(device_data['device_name'])
    insert_to_dynamoDB(device_data)

    put_text('Device Registered on AWS IoT Core!')
    put_text(f"Device Name : {device_data['device_name']}\nDevice Type : {device_data['device_type']}\nDevice ID : {device_data['device_id']}\nQuadrant : {device_data['quadrant']}\nCoordinates = [{device_data['latitude']},{device_data['longitude']}]")

    action = actions("Register another device?", ["YES", "NO"])

    if(action == "YES"):
        clear()
        continue
    elif(action == "NO"):
        put_text("App has exited.\nYou can close the browser now.")
        time.sleep(5)
        exit()
