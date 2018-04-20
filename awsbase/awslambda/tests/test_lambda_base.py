from awsbase.awslambda import BaseLambda
from awsbase import singleton

import unittest


@singleton
class ApiHandler(BaseLambda):

    def __init__(self):
        super().__init__()

    def handle(self, event, context):

        return {
            "statusCode": 200,
            "body": event
        }


handler = ApiHandler.get_handler()


class TestStringMethods(unittest.TestCase):

    def test_handler(self):
        self.assertTrue(handler({}, None)['body'] == {})
