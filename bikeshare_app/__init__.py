"""Initialize the bikeshare app"""
# pylint: disable=invalid-name,wrong-import-position
from os import getenv, urandom
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.bower import Bower
import flask.ext.login as flask_login
from bikeshare_app.config import configure_app

app = Flask(__name__)
app.secret_key = getenv('BIKESHARE_APP_SECRET', urandom(24))
configure_app(app)
Bower(app)
db = SQLAlchemy(app)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

import bikeshare_app.views
