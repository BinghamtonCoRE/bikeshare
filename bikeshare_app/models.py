"""Models for the app"""
from bikeshare_app import db
from datetime import date


class Profile(db.EmbeddedDocument):
    """Embedded user profile"""
    height = db.IntField(required=True)
    grad_year = db.StringField(required=True, default=date.today().year)
    violations = db.StringField()
    fav_bikes = db.ListField(db.IntField())


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
    repair_ids = db.ListField(db.ObjectIdField(), required=False)
    reported_missing = db.BooleanField(required=True, default=False)


class Personal_Bike(db.EmbeddedDocument):
    """Model for a users personal bike"""
    bike = db.EmbeddedDocumentField(Bike, required=True)
    user = db.ObjectIdField(required=True)
    owned_since = db.DateTimeField(required=True)
    comment = db.StringField(required=True)
    lock_brand = db.StringField(required=False)


class User(db.Document):
    """Model for users"""
    name = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    active = db.BooleanField(required=True, default=True)
    user_type = db.IntField(required=True, default=0)
    banned = db.BooleanField(required=True, default=False)
    profile = db.EmbeddedDocumentField(Profile, required=False)
    bike = db.EmbeddedDocumentField(Personal_Bike, required=False)

class Active_Share(db.Document):
    """Model for the bike share owned bikes"""
    available = db.BooleanField(required=True, default=False)
    uses = db.IntField(required=True, default=0)
    height_min = db.IntField(required=True)
    height_max = db.IntField(required=True)
    last_user_email = db.EmailField(required=True)
    key_number = db.StringField(required=True)
