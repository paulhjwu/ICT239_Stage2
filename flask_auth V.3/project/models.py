# models.py

from flask_login import UserMixin
import pymongo

# init SQLAlchemy so we can use it later in our models
connection = pymongo.MongoClient('mongodb://localhost:27017')
db = connection['fitwell']


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

    def __init__(self, email, name, password):
        db.appUser.insert_one({'email': email, 'name': name, 'password': password})

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

    
