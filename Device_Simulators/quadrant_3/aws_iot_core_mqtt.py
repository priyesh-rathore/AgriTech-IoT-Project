# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT

ENDPOINT = "aza7pc8d6ids6-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "soil_sensor_sprinkler_q_3_mqtt_client"
PATH_TO_CERTIFICATE = "./certificates/certificate.pem.crt"
PATH_TO_PRIVATE_KEY = "./certificates/private.pem.key"
PATH_TO_AMAZON_ROOT_CA_1 = "./certificates/AmazonRootCA1.pem"
SOIL_SENSOR_TOPIC = "petrichor_agritech/quadrant_3/soil_sensors"
SPRINKLER_COMMAND_TOPIC = "petrichor_agritech/quadrant_3/sprinkler_command"
SPRINKLER_TELEMETRY_TOPIC = "petrichor_agritech/quadrant_3/sprinkler_telemetry"

SPRINKLER_STATE = 0

def get_sprinkler_state():
    global SPRINKLER_STATE
    return SPRINKLER_STATE

myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
myAWSIoTMQTTClient.configureCredentials(PATH_TO_AMAZON_ROOT_CA_1, PATH_TO_PRIVATE_KEY, PATH_TO_CERTIFICATE)
myAWSIoTMQTTClient.connect()

def subscribe(TOPIC, QOS):
    myAWSIoTMQTTClient.subscribe(TOPIC, QOS, customCallback)
    print(f"Successfully subscribed to topic : {TOPIC} with QoS : {QOS}")

# Custom MQTT message callback
def customCallback(client, userdata, message):

    global SPRINKLER_STATE

    received = message.payload
    received = received.decode("utf-8")

    print("Received : ")
    print(received, type(received))
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")

    if(message.topic == SPRINKLER_COMMAND_TOPIC):
        sprinkler_payload = json.loads(received)
        if(sprinkler_payload['state']==0 or sprinkler_payload['state']==1):
            SPRINKLER_STATE = sprinkler_payload['state']

def publish(message, TOPIC, QOS):
    myAWSIoTMQTTClient.publish(TOPIC, message, QOS) 
    #print("Published: '" + message + "' to the topic: ", TOPIC)

def disconnect():
    myAWSIoTMQTTClient.disconnect()