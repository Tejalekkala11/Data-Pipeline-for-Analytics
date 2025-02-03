import json
import boto3

def lambda_handler(event, context):
    for record in event['Records']:
        payload = json.loads(record['kinesis']['data'])
        print("Decoded payload: " + str(payload))
        # Add your data processing logic here
    return {
        'statusCode': 200,
        'body': json.dumps('Data processed successfully')
    }
