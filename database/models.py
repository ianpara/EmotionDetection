# http://flask.pocoo.org/docs/1.0/tutorial/database/
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

from flask_login import current_user


from datetime import datetime

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
    @staticmethod
    def select_a_user(givenID):
        cursor.execute("SELECT * FROM user where userID = ?", [givenID]) #requires list literal [ ... ]
        data = cursor.fetchall()
        return data
    #selet a single user based on the passed in ID

    # get userID from logged in user
    @staticmethod
    def getID(user_id):
        cursor.execute("SELECT userID FROM user where googleID = ?", [user_id])
        data = cursor.fetchone()
        return data

    # removes a user when given ID
    # this method will be called when a user wants to delete their own account
    @staticmethod
    def remove_user():
        id = Database.getID(current_user.id)
        cursor.execute("DELETE FROM user WHERE userID = ?", [id[0]])
        cursor.execute("DELETE FROM moods_tracker WHERE userID = ?", [id[0]])
        dbconn.commit()

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
        cursor.execute("SELECT joke FROM jokes where jokeID = ?", [givenJokeID]) #requires list literal [ ... ]
        data = cursor.fetchone()
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

############ B E G I N __ J O K E __ T R A C K E R __ M E T H O D S ############
    @staticmethod
    def add_joke_tracked(userID, jokeID):
        cursor.execute("INSERT INTO joke_tracker (userID, jokeID) VALUES (?, ?)", [userID], [jokeID])
        dbconn.commit()


    #@staticmethod
    # def search_joke_tracked(userID, jokeID):
        # TO DO

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

############ B E G I N __ M O O D __ T R A C K E R __ M E T H O D S ############

    # method to output user's mood log
    @staticmethod
    def retrieveMoods():
        id = Database.getID(current_user.id)
        cursor.execute("SELECT mood, calenderDate,moodID FROM moods_tracker WHERE userID = ?", (id[0],))
        mood_data = cursor.fetchall()
        return mood_data

    # method to insert mood into mood_tracker table
    @staticmethod
    def createMood(mood):
        id = Database.getID(current_user.id)
        now = datetime.now()
        cursor.execute("INSERT INTO moods_tracker (userID, mood, calenderDate) "
                       "VALUES (?,?,?)",
                        (id[0],mood,now.strftime('%B %d, %Y %H:%M')),
        )
        dbconn.commit()


    @staticmethod
    def removeMood(mood):
        id = Database.getID(current_user.id)
        cursor.execute("DELETE FROM moods_tracker WHERE moodID = ?", [mood])
        dbconn.commit()

############ B E G I N __ M O O D __ O U T P U T __ M E T H O D S ############

    # method to output user's mood log
    @staticmethod
    def feelBetter(result):
        if result=='angry':
            output = Database.select_a_joke(6);
            return output[0]
        else :
            return "Not a joke"


