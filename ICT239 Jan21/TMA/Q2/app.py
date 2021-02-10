import csv
from datetime import date, datetime, timedelta
import io
import os
import json

from flask import Flask, Response, flash, make_response, redirect, request, render_template, url_for, jsonify

import pymongo

app = Flask(__name__)

# To run mongod in Windows: mongod --dbpath ~/data &
# Configure MongoDB

connection = pymongo.MongoClient('mongodb://localhost:27017')
db = connection['cluster']

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

def get_recordings(_date=None):
    filter = {}
    if _date is not None:
        end = datetime(_date.year, _date.month, _date.day)
        start = end - timedelta(days=6)
        filter['datetime'] = {
            '$lte': end,
            '$gte': start
        }

    recordings = []
    aLog = db.calorieLogs.find_one()
    #for recording in db.calorieLogs.find(filter):
    for recording in db.calorieLogs.find({}):
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

@app.route("/register", methods=['GET', 'POST'])
def register():

    cwd = os.getcwd()
    #flash(cwd)
    if request.method == 'GET':
        return render_template("register.html")

    elif request.method == 'POST':
        email = request.form.get('email')           # e.g. 'hello@world.com'
        password = request.form.get('password')     # e.g. 'P@ssword'
    
        print(f"The email is {email} and the password is {password}")

        return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
@app.route("/")
def login():

    cwd = os.getcwd()
    #flash(cwd)
    if request.method == 'GET':
        return render_template("index.html")

    elif request.method == 'POST':
        email = request.form.get('email')           # e.g. 'hello@world.com'
        password = request.form.get('password')     # e.g. 'P@ssword'
    
        print(f"The email is {email} and the password is {password}")

        return render_template("log.html", user_id=email)
        
@app.route("/upload", methods=['GET','POST'])
def seed():
    if request.method == 'GET':
        return render_template("upload.html")

    elif request.method == 'POST':

        type = request.form.get('type')

        if type == 'create':
            print("No create Action yet")
        elif type == 'upload':
            file = request.files.get('file')
            upload_logs(file)

        return render_template("upload.html")

@app.route("/dashboard", methods=['GET','POST'])
def dashboard():
    if request.method == 'GET':
        return render_template("dashboard.html")

@app.route("/api/recordings", methods=['GET'])
def recordings():
    _date = request.args.get('date')
    
    if _date is not None:
        try:
            _date = date.fromisoformat(_date)
        except ValueError:
            return {'error': 'date format should be YYYY-MM-DD'}, 400
    
    recordings = get_recordings(_date)

    return {'recordings': recordings}


@app.route("/log", methods=['GET', 'POST'])
def log():
    if request.method == 'GET':
        return render_template("log.html")

    elif request.method == 'POST':

        weight = float(request.form.get('weight')) 
        run = float(request.form.get('run'))
        walk = float(request.form.get('walk'))
        swim = float(request.form.get('swim')) 
        bike = float(request.form.get('bike'))  

        totalCal = 0

        if run != 0:
            totalCal += (run * 0.21 * weight)
        
        if swim != 0:
            totalCal += (swim * 0.13 * weight)
        
        if walk != 0:
            totalCal += (walk * 0.084 * weight)

        if bike != 0:
            totalCal += (run * 0.064 * bike)
        
        totalCal_str = str(totalCal)
        return jsonify({'calorie': totalCal_str})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')