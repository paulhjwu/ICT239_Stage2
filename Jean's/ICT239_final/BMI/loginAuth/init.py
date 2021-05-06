from flask import Flask
from flask import render_template, redirect, url_for, request, flash

#Sign up
from werkzeug.security import generate_password_hash, check_password_hash

#model - import 2 classes from models.py
from models import fitwellUser, User


#Login In
from flask_login import login_user, logout_user, login_required, current_user
from flask_login import LoginManager




def create_app():

    app = Flask(__name__)

    #configure for your web application (1) Secret key
    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    #Login Manager to manage the login and logout sessions
    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    #this load_user method will be called by app.py to check if the input email is in the database

    #{EDITS}!!!!! remove self
    @login_manager.user_loader
    def load_user(user_id):
        #checking against the email address to get the email, name, password
        #we are using the user_id to query for our user in the database : user_id = email
        return fitwellUser.get_user_byId(user_id)


    return app


