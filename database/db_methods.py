# http://flask.pocoo.org/docs/1.0/tutorial/database/
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)

# Open database connection
dbconn = sqlite3.connect("sqlite_db", detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)
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
        cursor.execute("SELECT * FROM user where userID = ?", [givenID]) #requires list literal [ ... ]
        data = cursor.fetchall()
        return data

    # method for adding user to the user table
    # takes in three parameters that contains that user's info
    #    !!!   not really working without auto increment.
    @staticmethod
    def add_user(addName, addEmail, addPic):
        cursor.execute("INSERT INTO user(name, Email, profile_pic) VALUES (?, ?, ?, ?)", (addName, addEmail, addPic))
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
        cursor.execute("DELETE FROM user WHERE userID = ?", [removeID])
        dbconn.commit()


############ E N D __ U S E R __ M E T H O D S ############

############ B E G I N __ J O K E __ M E T H O D S ############
    @staticmethod
    # spew forth all cheesiness
    def select_all_jokes():
        cursor.execute("SELECT * FROM jokes")
        data = cursor.fetchall()
        return data

    @staticmethod
    # select a single joke based on the joke's ID
    def select_a_joke(givenJokeID):
        cursor.execute("SELECT * FROM jokes where jokeID = ?", [givenJokeID]) #requires list literal [ ... ]
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

############ E N D __ J O K E __ M E T H O D S ############

############ B E G I N __ J O K E __ T R A C K E R __ M E T H O D S ############
    @staticmethod
    def add_joke_tracked(userID, jokeID):
        cursor.execute("INSERT INTO joke_tracker (userID, jokeID) VALUES (?, ?)", [userID], [jokeID])
        dbconn.commit()


    #@staticmethod
    # def search_joke_tracked(userID, jokeID):
        # TO DO
############ E N D __ J O K E __ T R A C K E R __ M E T H O D S ############


############ B E G I N __ M O T I V A T I O N A L __ M E T H O D S ############

    @staticmethod
    # spew forth all cheesiness
    def select_all_motivationals():
        cursor.execute("SELECT * FROM motivational_quotes")
        data = cursor.fetchall()
        return data

    @staticmethod
    # select a single joke based on the joke's ID
    def select_a_motivational(givenMotivationalID):
        cursor.execute("SELECT * FROM motivational_quotes where motivationalID = ?", [givenMotivationalID]) #requires list literal [ ... ]
        data = cursor.fetchall()
        return data


    @staticmethod
    def add_motivational(newMotivationalText):
        cursor.execute("INSERT INTO motivational_quotes (motivational) VALUES (?)", [newMotivationalText])
        dbconn.commit()


    @staticmethod
    def remove_joke_text(removeJokeText):
        cursor.execute("DELETE FROM motivational_quotes WHERE motivational = ?", [removeJokeText])
        dbconn.commit()

    @staticmethod
    def remove_jokeID(removeJokeID):
        cursor.execute("DELETE FROM motivational_quotes WHERE motivationalID = ?", [removeJokeID])
        dbconn.commit()

############ E N D __ M O T I V A T I O N A L __ M E T H O D S ############


############ B E G I N __ MOOD TRACKER__ M E T H O D S ############

    # method to output user's mood log
    @staticmethod
    def retrieve_userMoods():
        cursor.execute("SELECT t.calenderDate, m.mood "             # select date from mood_tracker table & mood from mood table
                       "FROM mood_tracker t INNER JOIN moods m "    # join attributes from two tables 
                       "ON t.moodID = m.moodID "                    # on the condition that the records have the same moodID
                       "WHERE userID = (SELECT userID FROM user WHERE googleID = ?)", [current_user.id])    # do this for the logged in user
        mood_data = cursor.fetchall()
        print(mood_data)
        # return mood_data