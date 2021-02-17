from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from flask_login import LoginManager 

from models import User, fitwellUser, get_recordings, create_calorie_log, create_log, upload_logs 

from flask import Flask, Response, flash, make_response, redirect, request, render_template, url_for

from app import app

def register(email, password, weight, gender, dob):

    user = fitwellUser.get_user_byId(email=email) # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again  
        flash('Email address already exists')
        return None

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = fitwellUser(email=email, password=generate_password_hash(password, method='sha256'), weight=float(weight), gender=gender, dob=dob)

    return new_user

def login(email, password):

    user = fitwellUser.get_user_byId(email)
    if not user or not check_password_hash(user.record['password'], password): 
            flash('Please check your login details and try again.')
            return None

    # if the above check passes, then we know the user has the right credentials
    login_user(user)
    return user

def logout():
    logout_user()