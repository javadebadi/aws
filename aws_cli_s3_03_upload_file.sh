# create a file in 
touch ./data/file1.txt
touch ./data/file2.txt
touch ./data/file3.txt

# copy local file to S3 bucket
aws s3 cp ./data/file1.txt s3://javad-cli-bucket

# mv local file to S3 bucket
aws s3 mv ./data/file2.txt s3://javad-cli-bucket

# mv file from S3 bucket and rename it
aws s3 mv s3://javad-cli-bucket/file2.txt ./data/file3.txt



