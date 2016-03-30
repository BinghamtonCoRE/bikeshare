"""Initialize the bikeshare app"""
#pylint: disable=no-name-in-module,import-error,invalid-name,wrong-import-position
from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'bikeshare'
}
app.debug = True
db = MongoEngine(app)

import bikeshare_app.views
