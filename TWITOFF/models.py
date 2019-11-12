"""Database models"""

from flask_sqlalchemy import SQLAlchemy

# import database
DB = SQLAlchemy()

class User(DB.Model):
    """Twitter users to analise"""
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)

class Tweet(DB.Model):
    """The users tweets from twitter"""
    id = DB.Column(DB.Integer, primary_key=True)
    text = DB.Column(DB.Unicode(280))