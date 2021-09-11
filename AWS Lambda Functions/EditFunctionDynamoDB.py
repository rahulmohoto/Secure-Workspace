import json
import boto3
from pprint import pprint

def lambda_handler(event, context):
    
    # TODO implement
    
    client = boto3.resource("dynamodb")
    table = client.Table("Save_User_Data")
    data = table.scan()["Items"]
    
    response = table.update_item(
        Key={
            'Record_Time': data[0]["Record_Time"]
        },
        UpdateExpression="set User_Data.Name_Data=:n, User_Data.Message=:m, User_Data.Password=:p,  User_Data.Tag=:t",
        ExpressionAttributeValues={
            ':n': event["Name_Data"],
            ':m': event["Message"],
            ':p': event["Password"],
            ':t': event["Tag"]
        },
        ReturnValues="UPDATED_NEW"
    )
    return response