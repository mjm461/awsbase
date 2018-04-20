import os
import logging
import json

import boto3


class BaseLambda(object):

    @classmethod
    def get_handler(cls, *args, **kwargs):
        def handler(event, context):
            return cls(*args, **kwargs).handle(event, context)
        return handler

    # Subclass needs to define this
    def handle(self, event, context):
        raise NotImplementedError

    def __init__(self, decryption=True, recursive=False):
        # Setup logger
        self._logger = logging.getLogger()
        self._logger.setLevel(BaseLambda.get_environ('LOGGING_LEVEL', 'INFO'))
        self._environment = BaseLambda.get_environ('ENV', 'local')
        self._config_dict = {}
        if self._environment != 'local':
            try:
                # Get SSM parameters
                if 'CONFIG_PATHS' in os.environ and os.environ['CONFIG_PATHS'] and 'ENV' in os.environ and os.environ['ENV']:
                    client = boto3.client('ssm')

                    for config_path in os.environ['CONFIG_PATHS'].split(","):
                        param_details = client.get_parameters_by_path(
                            Path='/' + os.environ['ENV'] + '/' + config_path,
                            Recursive=recursive,
                            WithDecryption=decryption)

                        # Loop through the returned parameters and populate the ConfigParser
                        for param in param_details.get('Parameters'):
                            section_path = "/".join(param.get('Name').split("/")[2:])
                            self._config_dict[section_path] = json.loads(param.get('Value'))
            except Exception:
                pass

    @staticmethod
    def get_environ(var, default):
        try:
            return os.environ[var]
        except KeyError:
            return default

    def get_parameter(self, section_path, var, default=None):
        if self._config_dict:
            return self._config_dict[section_path][var]
        else:
            return self.get_environ(
                ("_".join(section_path.split("/")) + "_" + "_".join(var.split("/"))).upper(), default)
