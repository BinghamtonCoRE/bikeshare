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
    # TODO: add the personal bike field


class Bike(db.EmbeddedDocument):
    """Model for bikes"""
    owner = db.StringField(required=True, default="BUBS")
    make = db.StringField(require=True)
    model = db.StringField(required=True)
    color = db.StringField(required=True)
    serial = db.StringField(required=True)
    size = db.IntField(required=True)
    repair_active = db.BooleanField(required=True, default=False)
    location = db.StringField(required=True)
    repair_ids = db.ListField(db.ObjectIdField(), required=True)
    reported_missing = db.BooleanField(required=True, default=False)
