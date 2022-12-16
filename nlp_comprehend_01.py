"""A module to use comprehend to detect the language
"""

import boto3
from config import (
    REGION_NAME,
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
)

comprehend = boto3.client(
    'comprehend',
    region_name=REGION_NAME,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)

TEXT = """
    من خفته بدم به ناز در کتم عدم

    حسن تو به دست خویش بیدارم کرد 
"""

result = comprehend.detect_dominant_language(
    Text=TEXT,
)

print(f"text = {TEXT}")
print('Language: ', result["Languages"][0]["LanguageCode"])

# write results to a file
from results import results_to_json
results_to_json(result, __file__)