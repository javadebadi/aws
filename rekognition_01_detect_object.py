"""This is an example which shows hot to use
AWS rekognition service
"""

import os
import base64
import boto3
from botocore.client import ClientError
from config import (
    REGION_NAME,
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
)

# AWS Rekognition is not available in all regions
REGION_NAME = "us-west-1"

BUCKET_NAME = "rekognition-bucket-3"

# =================================================================
# ============= PART 1: create bucket and upload files ============
# =================================================================

# see s3_01_bucket_create.py if the following lines are unfamiliar
s3_client = boto3.client(
    's3',
    region_name=REGION_NAME,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

# create bucket if not exists already
if BUCKET_NAME in [b["Name"] for b in s3_client.list_buckets()['Buckets']]:
    bucket = boto3.resource('s3').Bucket(BUCKET_NAME)
    bucket.objects.all().delete()
    s3_client.delete_bucket(
        Bucket=BUCKET_NAME,
        )

s3_client.create_bucket(
    Bucket=BUCKET_NAME,
    CreateBucketConfiguration={
        'LocationConstraint': REGION_NAME,
    },
)

# ============== upload some images to bucket ==============
IMAGE_URLS = {
    "einstein.jpg": os.path.join(".", "data", "rekognition", "objects", "einstein.jpg"),
    "cars-traffic.jpg": os.path.join(".", "data", "rekognition", "objects", "cars-traffic.jpg"),
    "walk-street.jpg": os.path.join(".", "data", "rekognition", "objects", "walk-street.jpg"),
}

# get and upload images to S3
for name, url in IMAGE_URLS.items():
    with open(url, "rb") as f:
        body = f.read()
    s3_client.put_object(
        Body=body,
        Bucket=BUCKET_NAME,
        Key=name,
    )



# =================================================================
# ============= PART 2: label on images ============
# =================================================================
# AWS Rekognition is not available in all regions
# The images you want to use in AWS Rekognition must be in the same region where AWS Rekognition exists

object_results = {}
text_results = {}
# create Rekognition client
rekog = boto3.client(
    'rekognition',
    region_name='us-west-1',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )

for name, _ in IMAGE_URLS.items():
    response = rekog.detect_labels(
        Image={
            'S3Object': {
                'Bucket': BUCKET_NAME,
                'Name': name,
            }
        },
        MaxLabels=30,
        MinConfidence=80,
    )
    object_results[name] = response
    print(f"image: {name}")
    print([obj["Name"] for obj in response["Labels"]])
    print("---------------------------------------")


# write results to a file
from results import results_to_json
results_to_json(
    {
        "objects": object_results,
        "texts": text_results,
    }
    , __file__)
