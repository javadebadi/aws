"""In this module, we show an example of how to create a static website.

The content of the static website are in ./data/static_website/ directory.
"""


import logging
import os
import json
from string import Template

import boto3
from botocore.errorfactory import ClientError

from config import (
    REGION_NAME,
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
)


BUCKET_NAME = "scientists"
STATIC_WEBSITE_ROOT_DIR = os.path.join(".", "data", "static_website")
WEBSITE_INDEX_PAGE = "index.html"
ERROR_PAGE = "404.html"


# initialize s3 client
s3 = boto3.client(
    's3',
    region_name=REGION_NAME,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)


# ========== Create Bucket ==========
# create a S3 bucket and if it already exists ignore it
try:
    s3.create_bucket(
        Bucket=BUCKET_NAME,
        CreateBucketConfiguration={
        'LocationConstraint': REGION_NAME,
        },
    )
except ClientError as e:
    logging.error(e)


# ========== Website Configuration ==========
# Define the website configuration
website_configuration = {
    'ErrorDocument': {'Key': '404.html'},
    'IndexDocument': {'Suffix': WEBSITE_INDEX_PAGE},
}

print(" ===== Put Website Configuration ===== ")
s3.put_bucket_website(
    Bucket=BUCKET_NAME,
    WebsiteConfiguration=website_configuration,
    )


# ========== Bucket policy ==========
# add this bucket policy to give access to read bucket

bucket_policy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Sid': 'PublicReadGetObject',
        'Effect': 'Allow',
        'Principal': '*',
        'Action': [
            's3:GetObject'
            ],
        'Resource': f'arn:aws:s3:::{BUCKET_NAME}/*'
    }]
}

bucket_policy = json.dumps(bucket_policy)

print(" ===== Bucket Policy =====")
print(bucket_policy)

print(" ===== Uploads Bucket Policy =====")
s3.put_bucket_policy(
    Bucket=BUCKET_NAME,
    Policy=bucket_policy,
    )


# ========== Upload Content ==========
# find paths of files to upload
paths = {}
for path, subdirs, files in os.walk(STATIC_WEBSITE_ROOT_DIR):
    for name in files:
        p =os.path.join(path, name)
        x = p.split("static_website")[-1]
        print(x)
        if x.startswith("/") or x.startswith("\\"):
            x = x[1:]
        paths[x.replace("\\","/")] = p

print("PATHS = ", paths)

# upload static website content to bucket
for key, path in paths.items():
    s3.upload_file(
        Bucket=BUCKET_NAME,
        Key=key,
        Filename=path,
        ExtraArgs={
            "ContentType": "text/html",
            }
    )


