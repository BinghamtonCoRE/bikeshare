from bikeshare_app import db


class User(db.Document):
    """Model for users"""
    email = db.StringField(required=True, unique=True)
    name = db.StringField(required=True)
    active = db.BooleanField(required=True, default=True)


class Bike(db.Document):
    """Model for bikes"""
    owner = db.StringField(required=True, default="BUBS")
    bike_id = db.IntField(required=True, unique=True)
    make = db.StringField(require=True)
