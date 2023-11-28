'''
CS3250 - Software Development Methods and Tools - Fall 2023
Project 03- Video Playlist Manager Web Application
Description: This forms.py file is meant for implementing the forms for the application
Group Name: Backroom Gang

'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange

# TODO 1: Implement User Story 1: Registration and Signing up (USE SIGNUP FORM FROM PREVIOUS PROJECTS BUT MODIFY IT TO FIT THIS PROJECT)
class RegistrationForm(FlaskForm):
    """ This class is meant for implementing the registration form for the application """
    pass

# TODO 2: Implement User Story 2: Login and Signing in (USE LOGIN FORM FROM PREVIOUS PROJECTS BUT MODIFY IT TO FIT THIS PROJECT)
class LoginForm(FlaskForm):
    """ This class is meant for implementing the login form for the application """
    pass

# TODO 3: Implement User Story 3: Create a Playlist (USE INVOICE FORM FROM PREVIOUS PROJECTS BUT MODIFY IT TO FIT THIS PROJECT BY USING THE CLASS DIAGRAM) 
class PlaylistForm(FlaskForm):
    """ This class is meant for implementing the playlist form for the application """
    pass

# TODO 4: Implement User Story 3: Add a Video to a Playlist (USE ITEM FORM FROM PREVIOUS PROJECTS BUT MODIFY IT TO FIT THIS PROJECT BY USING THE CLASS DIAGRAM)
class VideoForm(FlaskForm):
    """ This class is meant for implementing the video form for the application """
    pass

