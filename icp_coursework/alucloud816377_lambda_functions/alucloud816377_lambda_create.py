import json
import boto3 as b
from boto3.dynamodb.conditions import Key, Attr

def create_task(event, context):
    db_table = ""
    dynamodb = b.resource('dynamodb')
    table = dynamodb.Table(db_table)
    table.put_item(
        Item={
            'id': event['id'],
            'name': event['name'],
            'description': event['description'],
            'status': event['status']
        }
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Task added')
    }