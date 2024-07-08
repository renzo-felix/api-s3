import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = event['body']['bucket']
    
    s3.create_bucket(Bucket=bucket_name)
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'Bucket {bucket_name} creado')
    }
