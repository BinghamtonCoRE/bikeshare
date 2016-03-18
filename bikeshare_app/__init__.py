from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'bikeshare'
}
app.debug = True
db = MongoEngine(app)

import bikeshare_app.views
