'''
CS3250 - Software Development Methods and Tools - Fall 2023
Project 03- Video Playlist Manager Web Application
Description: This routes.py file is meant for implementing the routes for the application
Group Name: Backroom Gang

'''

from flask import render_template, url_for, flash, redirect, request
from app import app, db
from app.forms import RegistrationForm, LoginForm, PlaylistForm, VideoForm # Make the forms.py file and import the forms from it
from app.models import User, Playlist, Video
from flask_login import login_user, current_user, logout_user, login_required
import bcrypt

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index(): 
    return render_template('index.html')


# TODO 1: Implement User Story 1: Registration and Signing up (USE SIGNUP ROUTE FROM PREVIOUS PROJECTS BUT MODIFY IT TO FIT THIS PROJECT)
@app.route('/users/signup', methods=['GET', 'POST'])
def users_signup():
    """ This function is meant for implementing the signup route for the application """
    pass

# TODO 2: Implement User Story 2: Login and Signing in (USE LOGIN ROUTE FROM PREVIOUS PROJECTS BUT MODIFY IT TO FIT THIS PROJECT)
@app.route('/users/login', methods=['GET', 'POST'])
def users_login():
    """ This function is meant for implementing the login route for the application """
    pass

@login_required
@app.route('/users/signout', methods=['GET', 'POST'])
def users_signout():
    """This route handles the signout process, logging out the user and redirecting the user to the index page."""
    logout_user()
    flash('You were successfully logged out!')
    return redirect(url_for('index'))

# TODO 3: Implement User Story 2: View Playlists (Refer to one of the previous homeworks when viewing all of the invoices for this)
@app.route('/playlists', methods=['GET', 'POST'])
@login_required
def playlists():
    """ This function is meant for implementing the view playlists route for the application """
    pass

# TODO 4: Implement User Story 3: Create a Playlist (Refer to one of the previous homeworks when creating an invoice for this)
@app.route('/playlists/create', methods=['GET', 'POST'])
@login_required
def playlists_create():
    """ This function is meant for implementing the create playlist route for the application """
    pass

# TODO 5: Implement User Story 3: View Videos in a Playlist (Refer to one of the previous homeworks when viewing all of the items for this)
@app.route('/playlists/<playlist_id>/videos', methods=['GET', 'POST'])
@login_required
def playlists_videos(playlist_id):
    """ This function is meant for implementing the view videos in playlist route for the application """
    pass

# TODO 6: Implement User Story 4: Adding videos to a playlist
@app.route('/playlists/<playlist_id>/videos/add', methods=['GET', 'POST'])
@login_required
def playlists_videos_add(playlist_id):
    """ This function is meant for implementing the add videos to playlist route for the application """
    pass

# TODO 7: Implement User Story 5: Deleting videos from a playlist(Refer to Homework 3 when deleting an invoice item for this)
@app.route('/playlists/<playlist_id>/videos/delete', methods=['GET', 'POST'])
@login_required
def playlists_videos_delete(playlist_id):
    """ This function is meant for implementing the delete videos from playlist route for the application """
    pass

# TODO 8: Implement User Story 6: Deleting a playlist (Refer to Homework 3 when deleting an invoice for this)
@app.route('/playlists/<playlist_id>/delete', methods=['GET', 'POST'])
@login_required
def playlists_delete(playlist_id):
    """ This function is meant for implementing the delete playlist route for the application """
    pass

