"""SES stands for Simple Email Service

In order to use this service, you need to configure domain or emails.
To to this you need to go to SES from AWS Console and verify domain or emails.

We can use the AWS Boto3 SDK to send emails from Amazon to add that email
as one of verified identities.
The user will get a verfication email and if the user clicks on the
verification link, the email will be added to the verified accounts.
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


response = ses_client.verify_email_identity(
    EmailAddress="javad.ebadi.1990@gmail.com",
)
print(response)


# write results to a file
from results import results_to_json
results_to_json(response, __file__)