from pymongo import MongoClient
from random import randint

names = ['Joe Palazzolo', 'Taylor Foxhall', 'Ryan Donovan', 'Alan Plotko']
emails = ['jpalazz3@binghamton.edu', 'tfoxhal1@binghamton.edu', 'rdonova1@binghamton.edu', 'aplotko1@binghamton.edu']
brands = ['Schwinn', 'Giant', 'Trek']

client = MongoClient()

db = client.bikeshare
db.user.drop()

users = db.user

for i in range(0, len(names)):
  users.insert_one({'name':names[i], 'email':emails[i], 'active':True, 'user_type':0, 'banned':False})

db.bike.drop()
bikes = db.bike

for i in range(0, 10):
  bikes.insert_one({'owner':'BUBS','make':brands[randint(0,1)]})

for name in names:
  bikes.insert_one({'owner':name,'make':brands[randint(0,1)]})

print("Inserted some random test data into your mongodb")
