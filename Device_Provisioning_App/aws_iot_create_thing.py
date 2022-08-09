# Connecting to AWS
import boto3
import json

# Parameters for Thing
thingArn = ''
thingId = ''
defaultPolicyName = 'gl_iot_group_4_policy'
###################################################


def createThing(thingName):
    global thingClient
    thingResponse = thingClient.create_thing(
        thingName=thingName
    )
    data = json.loads(json.dumps(thingResponse, sort_keys=False, indent=4))
    for element in data:
        if element == 'thingArn':
            thingArn = data['thingArn']
        elif element == 'thingId':
            thingId = data['thingId']
            createCertificate(thingName)

def createCertificate(thingName):
    global thingClient
    certResponse = thingClient.create_keys_and_certificate(
        setAsActive=True
    )
    data = json.loads(json.dumps(certResponse, sort_keys=False, indent=4))
    for element in data:
        if element == 'certificateArn':
            certificateArn = data['certificateArn']
        elif element == 'keyPair':
            PublicKey = data['keyPair']['PublicKey']
            PrivateKey = data['keyPair']['PrivateKey']
        elif element == 'certificatePem':
            certificatePem = data['certificatePem']
        elif element == 'certificateId':
            certificateId = data['certificateId']

    with open('./Created_Certificates/public.key', 'w') as outfile:
        outfile.write(PublicKey)
    with open('./Created_Certificates/private.key', 'w') as outfile:
        outfile.write(PrivateKey)
    with open('./Created_Certificates/cert.pem', 'w') as outfile:
        outfile.write(certificatePem)

    response = thingClient.attach_policy(
        policyName=defaultPolicyName,
        target=certificateArn
    )
    response = thingClient.attach_thing_principal(
        thingName=thingName,
        principal=certificateArn
    )

thingClient = boto3.client('iot')