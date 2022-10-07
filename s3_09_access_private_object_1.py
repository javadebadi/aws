"""A module that shows how to access private objects in S3 bucket.
"""

# import packages
import pandas as pd
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


# upload a csv file to bucket
s3.upload_file(
    Bucket='javad-first-bucket',
    Filename='data/data.csv',
    Key='data.csv',
)

# try to read object with pandas
obj = s3.get_object(
    Bucket='javad-first-bucket',
    Key='data.csv',
)
df = pd.read_csv(
    obj['Body']
)

# write results to a file
from results import results_to_json
results_to_json(df.to_dict(), __file__)