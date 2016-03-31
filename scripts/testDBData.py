# pylint: skip-file
import sys
from pymongo import MongoClient
from random import randint

while (True):
    userInput = input("This script will drop all data from your DB's before inserting, continue? [y/n]")
    userInput = str(userInput)
    if (userInput == 'y'):
        break
    elif (userInput == 'n'):
        sys.exit()
    else:
        continue

"""Random data to pull from when populating the DB"""
names = ['Joe Palazzolo', 'Taylor Foxhall', 'Ryan Donovan', 'Alan Plotko']
emails = ['jpalazz3@binghamton.edu', 'tfoxhal1@binghamton.edu', 'rdonova1@binghamton.edu', 'aplotko1@binghamton.edu']
brands = ['Schwinn', 'Giant', 'Trek']

client = MongoClient()

db = client['bikeshare-test']
print("Created database: 'bikeshare-test'")
db.user.drop()
db.activeshare.drop()

def genUsers():
    print("Created collection 'user'")
    user = db.user
    for i in range(0, len(names)):
        user.insert_one({
            'name': names[i],
            'email': emails[i],
            'active': True,
            'user_type': 0,
            'banned': False
        })
    print("Added", len(names), "users...")

def genActiveShareBikes():
    print("Created collection 'activeshare'")
    bike = db.activeshare
    for i in range(0, 25):
        bike.insert_one({
            'available': True,
            'uses': randint(0,5),
            'height_min': randint(50, 55),
            'height_max': randint(55, 60),
            'last_user_email': emails[randint(0,3)],
            'key_number': randint(0,25),
            'bike': {
                'owner': 'BUBS',
                'make': brands[randint(0,2)],
                'model': 'someModelName',
                'color': 'someColorName',
                'serial': '123lol',
                'size': randint(50,65),
                'repair_active': False,
                'location': 'Union',
                'reported_missing': False
                }
            })
    print("Added 25 bikes...")

genUsers()
genActiveShareBikes()

print("Inserted some random test data into your mongodb")
