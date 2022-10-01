"""A module that shows how to upload a file to a bucket.
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


# get metadata of object from bucket
object_metadata = s3.head_object(
    Bucket='javad-first-bucket',
    Key='profile.jpg',
)


# write results to a file
from results import results_to_json
results_to_json(object_metadata, __file__)