"""Initialize the bikeshare app"""
# pylint: disable=no-name-in-module,import-error,invalid-name,wrong-import-position
from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.bower import Bower
import flask.ext.login as flask_login
from bikeshare_app.config import configure_app
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("BIKESHARE_APP_SECRET")
configure_app(app)
Bower(app)
db = MongoEngine(app)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

import bikeshare_app.views
