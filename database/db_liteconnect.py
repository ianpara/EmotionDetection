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

############ B E G I N __ U S E R __ M E T H O D S ############
    # created a method to print out all rows of user table when method is called
    @staticmethod
    def select_all_users():
        cursor.execute("SELECT * FROM user")
        data = cursor.fetchall()
        return data

    #selet a single user based on the passed in ID
    def select_a_user(givenID):
        cursor.execute("SELECT * FROM user where id = ?", [givenID]) #requires list literal [ ... ]
        data = cursor.fetchall()
        return data

    # method for adding user to the user table
    # takes in three parameters that contains that user's info
    #    !!!   not really working without auto increment.
    @staticmethod
    def add_user(addID, addName, addEmail, addPic):
        cursor.execute("INSERT INTO user(id, name, Email, profile_pic) VALUES (?, ?, ?, ?)", (addID, addName, addEmail, addPic))
        dbconn.commit()

    # removes a user when given username
    # this method will be called when a user wants to delete their own account
    @staticmethod
    def remove_user_name(removeName):
        cursor.execute("DELETE FROM user WHERE name = ?", [removeName])
        dbconn.commit()


    # removes user when given user ID
    # this method will be called when an admin wants to delete a user account
    @staticmethod
    def remove_userID(removeID):
        cursor.execute("DELETE FROM user WHERE id = ?", [removeID])
        dbconn.commit()


############ E N D __ U S E R __ M E T H O D S ############

############ B E G I N __ J O K E __ M E T H O D S ############
    @staticmethod
    #spew forth all cheesiness
    def select_all_jokes():
        cursor.execute("SELECT * FROM user")
        data = cursor.fetchall()
        return data

    @staticmethod
    #select a single joke based on the joke's ID
    def select_a_joke(givenJokeID):
        cursor.execute("SELECT * FROM user where id = ?", [givenJokeID]) #requires list literal [ ... ]
        data = cursor.fetchall()
        return data


    @staticmethod
    def add_joke(newJokeText):
        cursor.execute("INSERT INTO jokes(joke) VALUES (?)", [newJokeText])
        dbconn.commit()


    @staticmethod
    def remove_joke_text(removeJokeText):
        cursor.execute("DELETE FROM jokes WHERE joke = ?", [removeJokeText])
        dbconn.commit()

    @staticmethod
    def remove_jokeID(removeJokeID):
        cursor.execute("DELETE FROM jokes WHERE jokeID = ?", [removeJokeID])
        dbconn.commit()