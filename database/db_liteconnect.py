# http://flask.pocoo.org/docs/1.0/tutorial/database/
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

# Open database connection
dbconn = sqlite3.connect("sqlite_db", detect_types=sqlite3.PARSE_DECLTYPES)
# prepare a cursor object using cursor() method
cursor = dbconn.cursor()


class Database():

    # created a method to print out all rows of user table when method is called
    @staticmethod
    def select_user():
        cursor.execute("SELECT * FROM user")
        data = cursor.fetchall()
        print(data)

    # method for adding user to the user table
    # takes in three parameters that contains that user's info, and auto-increments the user id
    @staticmethod
    def add_user(addName, addEmail, addPic):
        cursor.execute("INSERT INTO user(name, Email, profile_pic) VALUES (%s, %s, %s)", (addName, addEmail, addPic))
        dbconn.commit()

    # removes a user when given username
    # this method will be called when a user wants to delete their own account
    @staticmethod
    def remove_user_name(removeName):
        cursor.execute("DELETE FROM user WHERE name = %s", removeName)
        dbconn.commit()


    # removes user when given user ID
    # this method will be called when an admin wants to delete a user account
    @staticmethod
    def remove_userID(removeID):
        cursor.execute("DELETE FROM user WHERE id = %s", removeID)
        dbconn.commit()

