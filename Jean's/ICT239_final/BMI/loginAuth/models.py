#connect to MongoDB

import pymongo
from flask_login import UserMixin


#connect to the default local server database
connection = pymongo.MongoClient('mongodb://localhost:27017')
db = connection['fitwell']

#Creating a class to allow app.py to access the records
class User(UserMixin):
    def __init__(self, email, record):
        self._email = email
        self._record = record
    
    def get_email(self):
        return self._email

    #{EDITS}!!!!!! - for the Login Manager : Flask Login package
    def get_id(self):
        return self._email

    def get_record(self):
        return self._record

  
#Perform CRUD action to the database and pass the record to the User Class
class fitwellUser():
    def __init__(self, email, name, password):
        #Create a record in the database using insert_one
        db.appUser.insert_one({'email':email, 'name':name,'password':password})

    #for login, search for email in the database and get the record to check 
    def get_user_byId(email):

        filter = {}
        filter['email'] = email

        aCursor = db.appUser.find(filter).limit(1)
        if aCursor.count() == 1:        #one record is return back from the database
            return User(email=email, record=aCursor.next())
        else:       #no records being found with the email pass in
            return None