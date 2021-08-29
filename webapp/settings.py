import os
from dotenv import load_dotenv
load_dotenv()


class Config(object):
    TESTING = False
    MAXIMUM_LENGTH = os.environ.get('MAXIMUM_LENGTH')
    ALLOWED_COMMANDS = os.environ.get('DEV_COMMANDS')
    YAML_FILE = os.getcwd() + "/autoscript/workflow.yaml"


class ProductionConfig(Config):
    PORT = os.environ.get('PORT')
    MAXIMUM_LENGTH = os.environ.get('MAXIMUM_LENGTH')
    ALLOWED_COMMANDS = os.environ.get('PROD_COMMANDS')


class TestingConfig(Config):
    TESTING = True


enviroment = os.environ.get('FLASK_ENV')
