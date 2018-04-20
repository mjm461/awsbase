# Sample Project for AWS Lambda with DynamoDB

## Development 

## Prerequisites

### Build
For deployment we follow [the SAM documentation](https://github.com/awslabs/aws-sam-local#package-and-deploy-to-lambda)

To build the bundle.zip for lambda use the  `make bundle` target

```bash
python setup.py build
```

### BaseLamda usage
```python
from awsbase.awslambda import BaseLamda
from awsbase.awslambda import singleton

import unittest


@singleton
class ApiHandler(BaseLamda):

    def __init__(self):
        super().__init__()

    def handle(self, event, context):

        return {
            "statusCode": 200,
            "body": event
        }


handler = ApiHandler.get_handler()

```