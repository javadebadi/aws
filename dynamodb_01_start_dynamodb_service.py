"""A module that shows how to start dynamodb service
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
dynamodb = boto3.client(
    'dynamodb',
    region_name=REGION_NAME,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

results = str(dynamodb)



# write results to a file
from results import results_to_json
results_to_json(results, __file__)