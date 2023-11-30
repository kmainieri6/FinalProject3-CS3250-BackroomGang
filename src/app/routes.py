'''
CS3250 - Software Development Methods and Tools - Fall 2023
Project 03- Video Playlist Manager Web Application
Description: This routes.py file is meant for implementing the routes for the application
Group Name: Backroom Gang

'''

from flask import render_template, url_for, flash, redirect, request
from app import app, db
# Make the forms.py file and import the forms from it
from app.forms import RegistrationForm, LoginForm, PlaylistForm, VideoForm
from app.models import User, Playlist, Video
from flask_login import login_user, current_user, logout_user, login_required
import bcrypt


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    """ This function is meant for implementing the index route for the application"""
    return render_template('index.html')


# TODO 1: Implement User Story 1: Registration and Signing up (USE SIGNUP ROUTE FROM PREVIOUS PROJECTS BUT MODIFY IT TO FIT THIS PROJECT)
@app.route('/users/signup', methods=['GET', 'POST'])
def users_signup():
    """ This function is meant for implementing the signup route for the application """
    form = RegistrationForm()  # Create an instance of the RegistrationForm class
    if form.validate_on_submit():  # If the form is validated
        # Check if the user already exists
        existing_user = User.query.filter_by(id=form.id.data).first()
        if existing_user:  # If the user already exists
            flash('This user already exists!', 'error')

        else:  # If the user does not exist
            passwd = form.passwd.data  # Get the password from the form
            # Get the password confirmation from the form
            passwd_confirm = form.passwd_confirm.data
            if passwd == passwd_confirm:  # If the password and password confirmation match
                salt_passwd = bcrypt.gensalt()  # Generate a salt for the password
                hashed_passwd = bcrypt.hashpw(passwd.encode(
                    'utf-8'), salt_passwd)  # Hash the password
                user = User(id=form.id.data, email=form.email.data, passwd=hashed_passwd,
                            creation_date=form.creation_date.data)  # Create a new user
                db.session.add(user)  # Add the user to the database
                db.session.commit()
                flash('You have successfully signed up!', 'success')
                return redirect(url_for('users_login'))
            else:  # If the password and password confirmation do not match
                flash('The passwords do not match!', 'error')
    return render_template('signup.html', title='Sign Up', form=form)


# TODO 2: Implement User Story 2: Login and Signing in (USE LOGIN ROUTE FROM PREVIOUS PROJECTS BUT MODIFY IT TO FIT THIS PROJECT)
@app.route('/users/login', methods=['GET', 'POST'])
def users_login():
    """ This function is meant for implementing the login route for the application """
    form = LoginForm()
    if form.validate_on_submit():  # If the form is validated
        user = User.query.filter_by(id=form.id.data).first() # Get the user from the database
        if user: # If the user exists
            passwd = form.passwd.data # Get the password from the form
            salt_passwd = bcrypt.gensalt() # Generate a salt for the password
            hashed_passwd = bcrypt.hashpw(passwd.encode( 
                'utf-8'), salt_passwd) # Hash the password
            if bcrypt.checkpw(passwd.encode('utf-8'), user.passwd):
                login_user(user)
                flash('You have successfully logged in!', 'success')
                return redirect(url_for('view_playlists'))
            else:
                flash('The password is incorrect!', 'error')
        else:
            flash('This user does not exist!', 'error')
    return render_template('signin.html', title='Login', form=form)


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
def view_playlists():
    """ This function is meant for implementing the view playlists route for the application """
    return render_template('playlists.html', title='Playlists')

# TODO 4: Implement User Story 3: Create a Playlist (Refer to one of the previous homeworks when creating an invoice for this)


@app.route('/playlists/create', methods=['GET', 'POST'])
@login_required
def create_playlists():
    """ This function is meant for implementing the create playlist route for the application """
    pass

# TODO 5: Implement User Story 3: View Videos in a Playlist (Refer to one of the previous homeworks when viewing all of the items for this)


@app.route('/playlists/<playlist_id>/videos', methods=['GET', 'POST'])
@login_required
def view_playlists_videos(playlist_id):
    """ This function is meant for implementing the view videos in playlist route for the application """
    pass

# TODO 6: Implement User Story 4: Adding videos to a playlist


@app.route('/playlists/<playlist_id>/videos/add', methods=['GET', 'POST'])
@login_required
def add_playlists_videos(playlist_id):
    """ This function is meant for implementing the add videos to playlist route for the application """
    pass

# TODO 7: Implement User Story 5: Deleting videos from a playlist(Refer to Homework 3 when deleting an invoice item for this)


@app.route('/playlists/<playlist_id>/videos/delete', methods=['GET', 'POST'])
@login_required
def delete_playlists_videos(playlist_id):
    """ This function is meant for implementing the delete videos from playlist route for the application """
    pass

# TODO 8: Implement User Story 6: Deleting a playlist (Refer to Homework 3 when deleting an invoice for this)


@app.route('/playlists/<playlist_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_playlists(playlist_id):
    """ This function is meant for implementing the delete playlist route for the application """
    pass
