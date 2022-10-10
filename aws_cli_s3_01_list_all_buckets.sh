#! /bin/bash
# AWS CLI command to show list of all buckets

aws s3api list-buckets --query "Buckets[].Name"