"""Configuration to connect to AWS Cloud
"""

from dotenv import dotenv_values

# read configurations from .env file 
config = dotenv_values(".env")


# define config variables to import in program
REGION_NAME = config.get("REGION_NAME")
AWS_ACCESS_KEY_ID = config.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config.get("AWS_SECRET_ACCESS_KEY")
