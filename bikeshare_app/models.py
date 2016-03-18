"""Models for the app"""
from bikeshare_app import db
from datetime import date


class Profile(db.EmbeddedDocument):
    """Embedded user profile"""
    height = db.IntField(required=True)
    grad_year = db.StringField(required=True, default=date.today().year)
    violations = db.StringField()
    fav_bikes = db.ListField(db.IntField())


class User(db.Document):
    """Model for users"""
    name = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    active = db.BooleanField(required=True, default=True)
    user_type = db.IntField(required=True, default=0)
    banned = db.BooleanField(required=True, default=False)
    profile = db.EmbeddedDocumentField(Profile)
    #TODO: add the personal bike field


class Bike(db.Document):
    """Model for bikes"""
    owner = db.StringField(required=True, default="BUBS")
    bike_id = db.IntField(required=True, unique=True)
    make = db.StringField(require=True)
