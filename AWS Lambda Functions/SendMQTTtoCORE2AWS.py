import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    client = boto3.resource("dynamodb")
    table = client.Table("Save_User_Data")
    data = table.scan()["Items"]
    
    client = boto3.client('iot-data', region_name='us-west-2', endpoint_url='https://a25wmxf9jzsaoa-ats.iot.us-west-2.amazonaws.com')
    
    # Change topic, qos and payload
    response = client.publish(
        topic='env/core',
        qos=0,
        payload=json.dumps(data[0]["User_Data"])
    )
    
    
    return response;