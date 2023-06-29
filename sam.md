SAM is an open source framework to build Serverless Applications.

To install SMA in MacOS do the follwing steps:
- brew upgrade
- brew update
- brew install aws-sam-cli
then check the version of the sam using `sam --version`.

# Start SAM Project
To start a SAM project create a directroy
```
mkdir first-sam-project
cd first-sam-project
```

Then start the same project in new directory
```
sam init --runtime python3.10
code .
```

Inside the folder you will see `template.yaml` which contains name of the Lambda functions and their properties.
You can set the Timeout of the function to amount you want but by default here is 3 seconds.

Also you see the handler application:
Handler: app.lambdaHandler

Also you will see hello_world.py, you can write functions you want similar to this hello_world lambda function.


# Develop you own Lambda function
To develop you own Lambda function, first you need to change the `template.yaml`:
```yaml
TimeFunction:
	Type: AWS:Serverless::Function
	Properties:
		CodeUri: time_function/
		Handler: handler.time_function
		Runtime: Python3.10
		Events:
			TimeFunctionAPI:
				Type: API
				Properties:
					Path: /time
					Method: get

```
Now, it is time to create files and write codes
```bash
mkdir time_function
cd time_function
# install dependencies
touch handler.py

```

Now, we need to write the function inside `handler.py` such as 
```python
import time
def time_function(event, context) {
	t = time.time()

	response = {
		"statusCode": 200,
		"body": json.dumps({"time": t})
	}

	return response
}
```

# Build and Deploy

To build here is the command we have to wirte
```bash
sam package --template-file template.yaml --output-template-file package.yml
	--s3-bucket <name-of-the-s3-bucket>
```

So, first we create bucket
```
aws s3 --region us-east-1 mb s3://my-first-sam-project/
```

and then
```bash
sam package --template-file template.yaml --output-template-file pck.yml --s3-bucket my-first-sam-project
```

abd then it will package artifacts. To dploy artifacts run
```
san deploy --region us-east-1 --capabilities CAPABILITY_IAM --template-file pck.yml --stack-name first-same-project-stack
```


To view the logs
```
sam logs --name TimeFunction --stack-name first-same-project-stack --region-name us-east-1
```

To view live logs add `-tail` to end of above command.


To clean you AWS resources
```
aws cloudformation delete-stack -stack-name first-sam-project-stack
```
