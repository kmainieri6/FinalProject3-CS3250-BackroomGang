'''
CS3250 - Software Development Methods and Tools - Fall 2023
Project 03- Video Playlist Manager Web Application
Description: This program is meant for implementing the models for the application
Group Name: Backroom Gang
Developed by: Joseph Tewolde
'''

from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.String, primary_key=True) # user id
    email = db.Column(db.String, unique=False, nullable=False) # email address
    passwd = db.Column(db.String) # password 
    creation_date = db.Column(db.String) # date of creation

    playlists = db.relationship('Playlist', cascade="all,delete", backref='user', lazy=True) # playlists created by user, cascade deletes all playlists created by user when user is deleted

class Playlist(db.Model):
    __tablename__ = "playlists"

    id = db.Column(db.String, primary_key=True) # playlist id
    name = db.Column(db.String, unique=False, nullable=False) # playlist name
    creation_date = db.Column(db.String) # date of creation
    creator_name = db.Column(db.String) # creator id
    quantity = db.Column(db.Integer) # number of videos in playlist

    users_id = db.Column(db.String, db.ForeignKey('users.id'), nullable=False) # user id
    videos = db.relationship('Video', cascade="all,delete", backref='playlist', lazy=True) # videos in playlist, cascade deletes all videos in playlist when playlist is deleted

class Video(db.Model):
    __tablename__ = "videos"

    id = db.Column(db.String, primary_key=True) # video id
    name = db.Column(db.String, unique=False, nullable=False) # video name
    url = db.Column(db.String) # url of video

    playlist_id = db.Column(db.String, db.ForeignKey('playlists.id'), nullable=False) # playlist id
    





