from __init__ import create_app 

import csv
from datetime import date, datetime, timedelta
import io
import os

from flask import Flask, Response, flash, make_response, redirect, request, render_template, url_for

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import login_user, logout_user, login_required, current_user
from flask_login import LoginManager 

from models import User, fitwellUser, get_recordings, create_calorie_log, create_log, upload_logs 

#import pymongo

#app = Flask(__name__)
app = create_app()

# To run mongod in Windows: mongod --dbpath ~/data &
# Configure MongoDB

# connection = pymongo.MongoClient('mongodb://localhost:27017')
# db = connection['cluster']


@app.route("/register", methods=['GET', 'POST'])
def register():

    cwd = os.getcwd()
    #flash(cwd)
    if request.method == 'GET':
        return render_template("register.html")

    elif request.method == 'POST':
        email = request.form.get('email')           # e.g. 'hello@world.com'
        password = request.form.get('password')     # e.g. 'P@ssword'
        weight = request.form.get('weight')
        gender = request.form.get('gender')
        dob = request.form.get('datetime')
    
        print(f"The email is {email}, the password is {password}, the weight is {weight}, and the gender is {gender}")

        user = fitwellUser.get_user_byId(email=email) # if this returns a user, then the email already exists in database

        if user: # if a user is found, we want to redirect back to signup page so user can try again  
            flash('Email address already exists')
            return redirect(url_for('signup'))

        # create new user with the form data. Hash the password so plaintext version isn't saved.
        new_user = fitwellUser(email=email, password=generate_password_hash(password, method='sha256'), weight=float(weight), gender=gender, dob=dob)

  
        return redirect(url_for('login'))


@app.route("/login", methods=['GET', 'POST'])
@app.route("/")
def login():

    cwd = os.getcwd()
    #flash(cwd)
    if request.method == 'GET':
        return render_template("index.html")

    elif request.method == 'POST':
        email = request.form.get('email')           # e.g. 'hello@world.co
        password = request.form.get('password')     # e.g. 'P@ssword'
    
        print(f"The email is {email} and the password is {password}")

        user = fitwellUser.get_user_byId(email=email)

        # check if user actually exists
        # take the user supplied password, hash it, and compare it to the hashed password in database
        if not user or not check_password_hash(user.record['password'], password): 
            flash('Please check your login details and try again.')
            return redirect(url_for('login')) # if user doesn't exist or password is wrong, reload the page

        # if the above check passes, then we know the user has the right credentials
        login_user(user)

        return render_template("log.html", user_id=email, gender=user.record['gender'], dob=user.record['dob'], weight=user.record['weight'])
        
@app.route("/upload", methods=['GET','POST'])
@login_required
def seed():
    if request.method == 'GET':
        return render_template("upload.html", user_id=current_user.record['email'], gender=current_user.record['gender'], dob=current_user.record['dob'], weight=current_user.record['weight'])
        #render_template("upload.html")

    elif request.method == 'POST':

        type = request.form.get('type')

        if type == 'create':
            print("No create Action yet")
        elif type == 'upload':
            file = request.files.get('file')
            upload_logs(file)

        return render_template("upload.html", user_id=current_user.record['email'], gender=current_user.record['gender'], dob=current_user.record['dob'], weight=current_user.record['weight'])

@app.route("/dashboard", methods=['GET','POST'])
@login_required
def dashboard():
    if request.method == 'GET':
        return render_template("dashboard.html", user_id=current_user.record['email'], gender=current_user.record['gender'], dob=current_user.record['dob'], weight=current_user.record['weight'])

@app.route("/api/recordings", methods=['GET'])
@login_required
def recordings():
    _date = request.args.get('date')
    
    if _date is not None:
        try:
            _date = date.fromisoformat(_date)
        except ValueError:
            return {'error': 'date format should be YYYY-MM-DD'}, 400
    
    recordings = get_recordings(current_user.record['email'])

    return {'recordings': recordings}


@app.route("/log", methods=['GET', 'POST'])
@login_required
def log():
    if request.method == 'GET':
        return render_template("log.html", user_id=current_user.record['email'], gender=current_user.record['gender'], dob=current_user.record['dob'], weight=current_user.record['weight'])

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
        
        return {'calorie': totalCal}

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')