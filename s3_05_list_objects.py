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


# get list of files in a bucket named: javad-first-bucket
objects_list = s3.list_objects(
    Bucket='javad-first-bucket',
    MaxKeys=1,
    Prefix='profile',
)
print(objects_list)


# write results to a file
from results import results_to_json
results_to_json(objects_list, __file__)