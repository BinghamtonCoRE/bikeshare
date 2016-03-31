"""Initialize the bikeshare app"""
#pylint: disable=no-name-in-module,import-error,invalid-name,wrong-import-position
from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.bower import Bower

db = MongoEngine()

def create_app(**config_overrides):
    """Function to generate the app, this way we can change settings before
    creating it"""
    app = Flask(__name__)
    Bower(app)
    app.config['MONGODB_SETTINGS'] = {
        'db': 'bikeshare'
    }
    app.config.update(config_overrides)
    db.init_app(app)
    return app

import bikeshare_app.views
