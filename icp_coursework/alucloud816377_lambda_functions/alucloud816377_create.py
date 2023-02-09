import json
import boto3
import uuid

# Function to create a task in dynamodb
def create_task():
    # import the libraries we need
    # create a client to access DynamoDB
    dynamodb = boto3.client('dynamodb')
    # get the data from the API Gateway event
    data = json.loads(event['body'])
    # create a unique id for the task
    task_id = str(uuid.uuid1())
    # create a new item in the DynamoDB table
    dynamodb.put_item(
        TableName='alucloud816377-tasks',
        Item={
            'id': {'S': task_id},
            'task': {'S': data['task']}
        }
    )
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Task created successfully!",
            "task_id": task_id
        }),
    }
    # return the response
    return response