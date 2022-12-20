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

TEXTS = [
    "I am so excited to learn AWS ...",
    "GOD is great!",
    "GOD exists",
    "Evil exist",
    "Evil does not exist",
    "I am nobody!",
    "I am nobody! Who are you?",
    "I am very sad",
    "Water boils at 100 degrees of centigrad",
]

all_results = []
for text in TEXTS:
    result = comprehend.detect_sentiment(
        Text=text,
        LanguageCode='en',
    )
    all_results.append(result)
    print(f"text = {text}")
    print("Sentiment = ", result["Sentiment"])
    print("=================================")


# write results to a file
from results import results_to_json
results_to_json(all_results, __file__)