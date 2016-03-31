"""Module containing configurations for the flask server"""
from os import getenv
import logging
# TODO: Setup a logging environment

# pylint: disable=too-few-public-methods
class BaseConfig(object):
    """The base configuration that should be used in production"""
    DEBUG = False
    TESTING = False
    MONGODB_SETTINGS = {'db': 'bikeshare'}
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'bikeshare.log'
    LOGGING_LEVEL = logging.INFO

class TestingConfig(BaseConfig):
    """Configuration for running unit tests"""
    TESTING = True
    MONGODB_SETTINGS = {'db': 'bikeshare-test'}
    LOGGING_LEVEL = logging.DEBUG

class DevelopmentConfig(BaseConfig):
    """The configuration that should be run during development"""
    DEBUG = True
    TESTING = True
    MONGODB_SETTINGS = {'db': 'bikeshare-test'}
    LOGGING_LEVEL = logging.DEBUG

CONFIG = {
    'development': 'bikeshare_app.config.DevelopmentConfig',
    'testing': 'bikeshare_app.config.TestingConfig',
    'default': 'bikeshare_app.config.BaseConfig',
}

def configure_app(app):
    """Configure the app based on where it is deployed. First check for the
    FLASK_ENVIRONMENT environment variable, fallback to the default
    BaseConfig"""
    config_name = getenv('FLASK_ENVIRONMENT', 'default')
    app.config.from_object(CONFIG[config_name])
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    logging.getLogger().setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
