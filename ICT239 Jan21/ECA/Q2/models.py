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

# for calculating age

def calculate_age(born):
    today = date.today()
    try: 
        birthday = born.replace(year=today.year)
    except ValueError: # raised when birth date is February 29 and the current year is not a leap year
        birthday = born.replace(year=today.year, month=born.month+1, day=1)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year

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
        calorie += walking * 0.084 * weight
    
    if running != 0.0:
        calorie += running * 0.021 * weight

    if swimming != 0.0:
        calorie += swimming * 0.013 * weight

    if bicycling != 0.0:
        calorie += bicycling * 0.064 * weight

    filter = {}
    filter['user_id'] = user_id

    _newDay = datetime(_datetime.year, _datetime.month, _datetime.day)
    filter['datetime'] = _newDay

    # end = start + timedelta(days=1)

    # filter['datetime'] = {
    #     '$lt': end,
    #     '$gte': start
    # }
    
    aCursor = db.calorieLogs.find(filter).limit(1)

    if aCursor.count() == 1:

        aRecord=aCursor.next()
        newCalorie = aRecord['calorie'] + calorie

        # https://www.geeksforgeeks.org/python-mongodb-update_one/
        
        newValues = {  "$set" : { "calorie": newCalorie} }
        
        db.calorieLogs.update_one(filter, newValues)
    
    else:

        aUser = fitwellUser.get_fitwellUser_byId(user_id)

        # Men	BMR = 88.362 + (13.397 × weight in kg) + (4.799 × height in cm) - (5.677 × age in years)
        # Women	BMR = 447.593 + (9.247 × weight in kg) + (3.098 × height in cm) - (4.330 × age in years)

        born = datetime.strptime(aUser['dob'], "%Y-%m-%d")

        age = calculate_age(born.date())

        if aUser['gender'] == 'M':
            bmr = 88.362 + (12.397 * weight ) + (4.799 * aUser['height']) - (5.677 * age)
        else:
            bmr = 447.593 + (9.247 * weight ) + (3.098 * aUser['height']) - (4.330 * age)
 
        db.calorieLogs.insert_one({
            "user_id": user_id,
            "weight": weight,
            "datetime": _newDay,
            "calorie": (calorie + bmr)
        })

    return calorie

    # if _date is not None:
    #     end = datetime(_date.year, _date.month, _date.day)
    #     start = end - timedelta(days=6)
    #     filter['email'] = {
    #         '$lte': end,
    #         '$gte': start
    #     }

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

    calorie = create_calorie_log(user_id, _datetime, weight, walking, running, swimming, bicycling)

    return calorie

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

    def __init__(self, email, password, dob, gender, weight, height):
        db.appUser.insert_one({'email': email, 'password': password, 'dob': dob, 'gender': gender, 'weight' : weight, 'height': height})

    def get_user_byId(email):
        filter = {}
        filter['email'] = email

        aCursor = db.appUser.find(filter).limit(1)

        if aCursor.count() == 1:
            return User(email=email, record=aCursor.next())
        else: 
            return None
    
    def get_fitwellUser_byId(email):
        filter = {}
        filter['email'] = email

        aCursor = db.appUser.find(filter).limit(1)

        if aCursor.count() == 1:
            return aCursor.next()
        else: 
            return None
