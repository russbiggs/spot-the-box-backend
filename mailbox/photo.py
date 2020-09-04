
import base64
from io import BytesIO
import json
import os

import boto3

s3_client = boto3.client('s3')

header = {
    "Access-Control-Allow-Origin": "https://spot-the-box.us",
    "Access-Control-Allow-Credentials": True
}

def add_photo(event, context):
    """
    expected json body with keys:
    'name' - name of file
    'image' - base64 encoded string of photo data
    """
    body = json.loads(event['body'])
    try:
        name = body['name']
        img_data = body['image']
    except KeyError:
        return {"statusCode": 400, "headers": header, "body": {}}
    image = base64.b64decode(img_data)
    buffer = BytesIO()
    buffer.write(image)
    buffer.seek(0)
    s3_client.upload_fileobj(
        buffer, 
        os.environ['BUCKET'], 
        f'{name}.jpg', 
        ExtraArgs={"ACL": "public-read"}
    )
    response = {
        "statusCode": 200,
        "headers": headers,
        "body": {
            "status":"success"
        }
    }
    return reponse
