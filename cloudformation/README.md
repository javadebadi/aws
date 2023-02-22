# AWS CloudFormation
AWS CloudFormation => Infrastructure as Code

Install [cfn-lint](https://github.com/aws-cloudformation/cfn-lint) in your OS (environment) and extension in VSCode. The details of the installation are available in [cfn-lint](https://github.com/aws-cloudformation/cfn-lint).


List of VSCode extension for CloudFormation:
- [CloudFormation Linter](https://marketplace.visualstudio.com/items?itemName=kddejong.vscode-cfn-lint)
- [CloudFormation Snippets](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cloudformation-yaml-snippets)

To view visualizations of the CloudFormation template in VScode, you need to install [pydot](https://pypi.org/project/pydot/).

## CloudFormation Concepts
Search the web and AWS documentation for following concepts related to AWS CloudFormation:
- **Resources**
- **Templates**
- **Stack**
- **StackSet**

## CloudFormation Components
### CLoudFormation Parameters
CloudFormation Parameters => Widgets in UI
Each Parameter has a name, type , ... => These information will determine the widget type in UI
For example, a parameter can have list of values and in UI we will see a dropdown with that values.

### CloudFormation Functions
CloudFormation Functions can be invoked by following syntax:
```yaml
Fn::Base64: some_string
```
or the shorter form
```yaml
!Base64 some_string
```
Using the shorter form, you cannot chain functions.
#### Substitution Functions
Substitution Function: Fetch values from throughout the template.

Ref
GetAtt
Sub

*** TODO: read more




# Examples

### Example 1
The example [cfn_01_budget.yaml]("./cfn_01_budget.yaml") shows an example of an AWS CloudFormation templates which is get from free courses of AWS skillbuilder app.

We can use the CloudFormation Console or AWS CLI to create stack from this template.
The AWS CLI commands to create stack from this template is as follows:
```bash

```


 
