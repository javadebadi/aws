"""SES stands for Simple Email Service

In order to use this service, you need to configure domain or emails.
To to this you need to go to SES from AWS Console and verify domain or emails.

Here we see and example of creation of custom verifcation email and sending
a verification email.

Creating a template and sending a verification email are two separate things.

We can create various templates. We also can delete the templates we already have
created. It is not allowed to create two templates with same name.

We can send a verification email using the custom templates that we have defined.
"""


# AWS Boto packages and configuration
import boto3
from config import (
    REGION_NAME,
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
)

# AWS SES client
ses_client = boto3.client(
    'ses',
    region_name=REGION_NAME,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)


VERIFICATION_SUCCESS_URL = "http://professor-lake.com/success"
VERIFICATION_FAILURE_URL = "http://professor-lake.com/failure"
TEMPLATE_NAME = "CustomVerificationTemplate"  # template name to refer later


# STEP 0: Delete custom verification template
ses_client.delete_custom_verification_email_template(TemplateName=TEMPLATE_NAME)

# STEP 1: Create a verification email template
response = ses_client.create_custom_verification_email_template(
    TemplateName= TEMPLATE_NAME,
    FromEmailAddress= "admin@professor-lake.com",
    TemplateSubject= "Please confirm your email address",
    TemplateContent= """
        <html>
        <head></head>
        <h1 style="color:red;">Professor Lake</h1>
        <h1 style='text-align:center'>Please verify your account</h1>
        <p>Before we can let you access our product, please verify your email.</p>
        </body>
        </html>
    """,
    SuccessRedirectionURL= VERIFICATION_SUCCESS_URL,
    FailureRedirectionURL= VERIFICATION_FAILURE_URL,
)
print(response)



# STEP 2: Send verification email using the defined template in STEP 1
response = ses_client.send_custom_verification_email(
    EmailAddress="javad.ebadi.1990@gmail.com",
    TemplateName=TEMPLATE_NAME
)
print(response)

# write results to a file
from results import results_to_json
results_to_json(response, __file__)
