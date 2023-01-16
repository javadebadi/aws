"""SES stands for Simple Email Service

In order to use this service, you need to configure domain or emails.
To to this you need to go to SES from AWS Console and verify domain or emails.

Here we see an example of SES with attachments. To do this we will use 
the `.send_raw_email`.
"""

# Pythons email library packages
from email import encoders
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
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

# create message
msg = MIMEMultipart("alternative")
msg["Subject"] = "Subscription Contract"
msg["From"] = "admin@professor-lake.com"
msg["To"] = "javad.ebadi.1990@gmail.com"

# Set message body
plain_text = MIMEText(
    """Your contract with Professor Lake is attached.
    
    Thank you,
    Professor Lake
    """,
    "plain",
    )
body = MIMEText(
    """<h1 style="color:red;">Professor Lake</h1>
    <h2>Hi Javad</h2>
    <a href="http://professor-lake.com">Visit our website</a>
    <p>We are happy you are with us. You contract is attached to this email.</p>
    <p>Thank you,</p>
    <p>Porfessor Lake</p>
    """,
    "html"
    )
msg.attach(plain_text)
msg.attach(body)
filepath = "./data/contract.pdf"
with open(filepath, "rb") as attachment:
    part = MIMEApplication(attachment.read())
    part.add_header(
        "Content-Disposition",
        "attachment",
        filename=filepath.split("/")[-1],
    )
msg.attach(part)

# convert message to string and send it
response = ses_client.send_raw_email(
    Source=msg["From"],
    Destinations=[
        msg["To"]
    ],
    RawMessage={"Data": msg.as_string()},
)


# write results to a file
from results import results_to_json
results_to_json(response, __file__)