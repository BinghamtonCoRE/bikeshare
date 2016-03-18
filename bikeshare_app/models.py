from bikeshare_app import db

class User(db.Document):
    email = db.StringField(required=True, unique=True)
    name = db.StringField(required=True)
    active = db.BooleanField(required=True, default=True)

class Bike(db.Document):
    owner = db.StringField(required=True, default="BUBS")
    bike_id = db.IntField(required=True, unique=True)
