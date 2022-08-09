import random
import time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = "-33bzB1IWPPrFaTc7jkbl6qe0uq20pCwI3LOYZlr3OCDQxFbmx6L7usDHA9li46eQqSzgYQZuVLaczfTajkdWA=="
org = "gl_iot_group_4"

client = InfluxDBClient(url="http://54.196.189.22:8086/", token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

def write_to_influx(bucket, measurement, field_name, field_value):
    data = f"{measurement},host=host1 {field_name}={field_value}"
    write_api.write(bucket, org, data)