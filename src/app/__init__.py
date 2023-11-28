'''
CS3250 - Software Development Methods and Tools - Fall 2023
Project 03- Video Playlist Manager Web Application
Description: This program is meant for initializing the application
Group Name: Backroom Gang
'''


from flask import Flask
import os

app = Flask("Video Playlist Manager Web Application")
app.secret_key = os.environ['SECRET_KEY'] = 'you will never guess'

# db initialization
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db' # relative path to the database file
db.init_app(app) # initialize the database for the web app

from app import models
with app.app_context(): 
    db.create_all()

# login manager
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

from app.models import User

# user_loader callback
@login_manager.user_loader
def load_user(id):
    try: 
        return db.session.query(User).filter(User.id==id).one()
    except: 
        return None
    

from app import routes