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


# change directory
import os
os.chdir('results')
# download the file to directory
object_data = s3.download_file(
    Filename='profile.jpg',
    Bucket='javad-first-bucket',
    Key='profile.jpg',
)