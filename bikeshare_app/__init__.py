"""Initialize the bikeshare app"""
#pylint: disable=no-name-in-module,import-error,invalid-name,wrong-import-position
from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.bower import Bower
from bikeshare_app.config import configure_app

app = Flask(__name__)
configure_app(app)
Bower(app)
db = MongoEngine(app)

import bikeshare_app.views
