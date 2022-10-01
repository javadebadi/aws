"""A module that shows how to create bucket.
"""

# import packages
import boto3

# import config information
from config import (
    REGION_NAME,
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
)

# create S3 bucket client
s3 = boto3.client(
    's3',
    region_name=REGION_NAME,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )


# list all buckets in the AWS Cloud in give region
buckets = s3.list_buckets()

print("List of Buckets Before")
for bucket in buckets['Buckets']:
    print(bucket)


# create new bucket
new_bucket = s3.create_bucket(
    Bucket='javad-second-bucket',
    CreateBucketConfiguration={
        'LocationConstraint': REGION_NAME,
    },
    )

print(new_bucket)