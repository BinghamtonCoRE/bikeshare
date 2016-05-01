# pylint: disable=invalid-name,too-many-instance-attributes,too-many-arguments
"""Models for the app"""
from bikeshare_app import db


class Profile(db.Model):
    """Embedded user profile"""
    __tablename__ = 'profiles'
    id = db.Column(db.Integer(), primary_key=True)
    height = db.Column(db.Integer())
    grad_year = db.Column(db.String(10))
    violations = db.Column(db.String(50))
    #fav_bikes = db.Column(db.ListField(db.IntField())

    def __init__(self, height, grad_year, violations=0):
        self.height = height
        self.grad_year = grad_year
        self.violations = violations


class Bike(db.Model):
    """Model for bikes"""
    __tablename__ = 'bikes'
    id = db.Column(db.Integer(), primary_key=True)
    owner = db.Column(db.String(50))
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    color = db.Column(db.String(50))
    serial = db.Column(db.String(50))
    size = db.Column(db.Integer())
    repair_active = db.Column(db.Boolean())
    location = db.Column(db.String(50))
    #repair_ids = db.ListField(db.ObjectIdField(), required=False)
    reported_missing = db.Column(db.Boolean())

    def __init__(self, owner, make, model, color, serial, size,
                 repair_active=False, location=None, reported_missing=False):
        self.owner = owner
        self.make = make
        self.model = model
        self.color = color
        self.serial = serial
        self.size = size
        self.repair_active = repair_active
        self.location = location
        self.reported_missing = reported_missing


class PersonalBike(db.Model):
    """Model for a users personal bike"""
    __tablename__ = 'personal_bikes'
    id = db.Column(db.Integer(), primary_key=True)
    bike = db.Column(db.ForeignKey('bikes.id'))
    user = db.Column(db.ForeignKey('users.id'))
    owned_since = db.Column(db.Date())
    comment = db.Column(db.String(300))
    lock_brand = db.Column(db.String(50))

    def __init__(self, bike, user, owned_since, lock_brand, comment=None):
        self.bike = bike
        self.user = user
        self.owned_since = owned_since
        self.comment = comment
        self.lock_brand = lock_brand


class User(db.Model):
    """Model for users"""
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(80), unique=True)
    active = db.Column(db.Boolean())
    user_type = db.Column(db.Integer())
    banned = db.Column(db.Boolean())

    def __init__(self, name, email, active=True, user_type=0, banned=False):
        self.name = name
        self.email = email
        self.active = active
        self.user_type = user_type
        self.banned = banned


class ActiveShare(db.Model):
    """Model for the bike share owned bikes"""
    __tablename__ = 'active_share'
    id = db.Column(db.Integer(), primary_key=True)
    available = db.Column(db.Boolean())
    uses = db.Column(db.Integer())
    height_min = db.Column(db.Integer())
    height_max = db.Column(db.Integer())
    last_user_email = db.Column(db.Integer())
    key_number = db.Column(db.String(50))
    bike = db.Column(db.ForeignKey('bikes.id'))

    def __init__(self, height_min, height_max, key_number, bike, available=True,
                 uses=0, last_user_email=None):
        self.height_min = height_min
        self.height_max = height_max
        self.key_number = key_number
        self.bike = bike
        self.available = available
        self.uses = uses
        self.last_user_email = last_user_email
