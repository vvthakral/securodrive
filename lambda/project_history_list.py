import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

db_client = boto3.resource('dynamodb')
hist_table = 'project-trip-history'

def lambda_handler(event, context):
    email_id = event["email_id"]

    response = db_client.Table(hist_table).query(
        IndexName='email_id-index',
        KeyConditionExpression=Key('email_id').eq(email_id)
    )

    if 'Items' in response:
        res = response['Items']
        # TODO implement
        return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!'),
            'res': res
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Hello from Lambda!'),
            'res': {'error': 'Some error occurred at lambda'}
        }
