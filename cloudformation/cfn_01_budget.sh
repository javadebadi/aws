# Create stack using AWS CLI

aws cloudformation create-stack \
      --stack-name SimpleBudget \
      --template-body file://cfn_01_budget.yaml


# View the stack information using AWS CLI

aws cloudformation describe-stacks \
    --stack-name SimpleBudget

