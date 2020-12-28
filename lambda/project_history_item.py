import json
import boto3
dynamodb = boto3.resource('dynamodb')
s3 = boto3.resource('s3')

def lambda_handler(event, context):
    trip_id = event['trip_id']
    # S3 images of snaps
    bucket = s3.Bucket('project-frontend-web')#/img/trips/'+trip_id+'/')
    images = []
    dir = 'img/trips/'+trip_id+'/'
    for obj in bucket.objects.filter(Prefix=dir):
        img = obj.key
        img = img.split('/')
        img = img[3].split('.')
        img = img[0]
        images.append(img)
    
    table = dynamodb.Table('project-trip-history')
    item = table.get_item(Key={'trip_id': trip_id})
    item = item['Item']
    item['images'] = images
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
        'res': item
    }
