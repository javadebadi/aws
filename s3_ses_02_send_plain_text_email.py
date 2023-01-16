"""SES stands for Simple Email Service

In order to use this service, you need to configure domain or emails.
To to this you need to go to SES from AWS Console and verify domain or emails.

We can use the AWS Boto3 SDK to send plain text emails.
"""

import boto3
from config import (
    REGION_NAME,
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
)

ses_client = boto3.client(
    'ses',
    region_name=REGION_NAME,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)



CHARSET = "UTF-8"

response = ses_client.send_email(
    Destination={
        "ToAddresses": [
            "javad.ebadi.1990@gmail.com",
            "admin@professor-lake.com",
        ],
    },
    Message={
        "Body": {
            "Text": {
                "Charset": CHARSET,
                "Data": "Welcome to Porfessor-Lake, A Lake for Businesses.",
            }
        },
        "Subject": {
            "Charset": CHARSET,
            "Data": "Testing Sending Emails using SES",
        },
    },
    Source="admin@professor-lake.com",
)

# write results to a file
from results import results_to_json
results_to_json(response, __file__)