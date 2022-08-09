import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('GL_IoT_Group_4_New_Device_Data')

def insert_to_dynamoDB(data_packet):
    device_name = str(data_packet['device_name'])
    device_type = str(data_packet['device_type'])
    device_id = str(data_packet['device_id'])
    quadrant = str(data_packet['quadrant'])
    latitude = str(data_packet['latitude'])
    longitude = str(data_packet['longitude'])
    table.put_item(
    Item={
            'device_name': device_name,
            'device_type' : device_type,
            'device_id': device_id,
            'quadrant': quadrant,
            'latitude': latitude,
            'longitude': longitude,
        }
    )