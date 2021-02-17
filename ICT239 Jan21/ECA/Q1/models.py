# models.py

import csv
from datetime import date, datetime, timedelta
import io
import os

from flask_login import UserMixin

#
# Begin: moved from app.py
#

import pymongo


# init SQLAlchemy so we can use it later in our models
connection = pymongo.MongoClient('mongodb://localhost:27017')
db = connection['fitwell']

# COLLECTION: users

def get_users():
    return db.users.find({})

def get_user(email):
    assert email is not None
    
    return db.users.find_one({'email': email})

def create_user(email, password):
    assert email is not None
    assert password is not None

    db.users.insert_one({"email": email, "password": password})

# COLLECTOIN: logs

def get_recordings(_id=None):
    
    filter = {}

    # if _date is not None:
    #     end = datetime(_date.year, _date.month, _date.day)
    #     start = end - timedelta(days=6)
    #     filter['email'] = {
    #         '$lte': end,
    #         '$gte': start
    #     }

    if _id != 'admin@fitwell.com':
        filter['user_id']=_id

    recordings = []
    aLog = db.calorieLogs.find_one()
    #for recording in db.calorieLogs.find(filter):
    for recording in db.calorieLogs.find(filter):
        recordings.append({
            "user_id": recording['user_id'],
            "datetime": datetime.strftime(recording['datetime'], "%Y-%m-%dT%H:%M"),
            "calorie": recording['calorie'],
        })
    return recordings

def create_calorie_log(user_id, _datetime, weight, walking, running, swimming, bicycling):
    assert user_id is not None
    assert _datetime is not None
    assert weight is not None
    assert walking is not None
    assert running is not None
    assert swimming is not None
    assert bicycling is not None

    calorie = 0

    if walking != 0.0:
        calorie += walking * 0.084
    
    if running != 0.0:
        calorie += running * 0.021

    if swimming != 0.0:
        calorie += swimming * 0.013

    if bicycling != 0.0:
        calorie += bicycling * 0.064

    db.calorieLogs.insert_one({
        "user_id": user_id,
        "datetime": _datetime,
        "calorie": calorie    
    })

def create_log(user_id, _datetime, weight, walking, running, swimming, bicycling):
    assert user_id is not None
    assert _datetime is not None
    assert weight is not None
    assert walking is not None
    assert running is not None
    assert swimming is not None
    assert bicycling is not None

    db.logs.insert_one({
        "user_id": user_id,
        "datetime": _datetime,
        "weight": weight,
        "walking": walking,
        "running": running,
        "swimming": swimming,
        "bicycling": bicycling
    })

    # Update other collections as a result of creating new recording
    # This replaces the logic in Cloud Functions
    #create_or_update_trolley(trolley, _datetime)
    #create_or_update_stat(trolley, _datetime, temperature)

    create_calorie_log(user_id, _datetime, weight, walking, running, swimming, bicycling)

    return 

def upload_logs(file):
    assert file is not None

    data = file.read().decode('utf-8')
    reader = csv.reader(io.StringIO(data), delimiter=',', quotechar='"')

    for row in reader:
        user_id, _datetime, weight, walking, running, swimming, bicycling = row

        _datetime = datetime.strptime(_datetime, "%Y-%m-%dT%H:%M")
        weight = float(weight)
        walking = float(walking)
        running = float(running)
        swimming = float(swimming)
        bicycling = float(bicycling)

        create_log(user_id, _datetime, weight, walking, running, swimming, bicycling)

    return

#
# End: moved from app.py
#


class User(UserMixin):
    def __init__(self, email, record):
        self.email = email
        self.record = record

    def get_email(self):
        return self.email

    def get_id(self):
        return self.email

    def get_record(self):
        return self.record

class fitwellUser():

    def __init__(self, email, password, dob, gender, weight):
        db.appUser.insert_one({'email': email, 'password': password, 'dob': dob, 'gender': gender, 'weight' : weight})

    def get_user_byId(email):
        filter = {}
        filter['email'] = email

        aCursor = db.appUser.find(filter).limit(1)

        if aCursor.count() == 1:
            return User(email=email, record=aCursor.next())
        else: 
            return None

        # for aUser in db.appUser.find(filter):
        #     oneUser.append(aUser)
        # if oneUser!= []:
        #     return User(email=email, record=oneUser[0])
        # else:
        #     return None

    
