# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT

ENDPOINT = "aza7pc8d6ids6-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "gl_iot_group_4_ec2_mqtt_client"
PATH_TO_CERTIFICATE = "./certificates/certificate.pem.crt"
PATH_TO_PRIVATE_KEY = "./certificates/private.pem.key"
PATH_TO_AMAZON_ROOT_CA_1 = "./certificates/AmazonRootCA1.pem"
ALL_SOIL_SENSORS = "petrichor_agritech/+/soil_sensors"
ALL_SPRINKLERS = "petrichor_agritech/+/sprinkler_telemetry"

SPRINKLER_STATE = 0

def generate_sprinkler_command_topic(quadrant):
    return "petrichor_agritech/" + quadrant + "/sprinkler_command"

def get_sprinkler_state():
    global SPRINKLER_STATE
    return SPRINKLER_STATE

myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
myAWSIoTMQTTClient.configureCredentials(PATH_TO_AMAZON_ROOT_CA_1, PATH_TO_PRIVATE_KEY, PATH_TO_CERTIFICATE)
myAWSIoTMQTTClient.connect()

def publish(message, TOPIC, QOS):
    myAWSIoTMQTTClient.publish(TOPIC, message, QOS) 
    #print("Published: '" + message + "' to the topic: ", TOPIC)

def disconnect():
    myAWSIoTMQTTClient.disconnect()