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
    def get(user_id):
        db = get_db()
        user = db.execute(
            "SELECT * FROM user WHERE googleID = ?", (user_id,)
        ).fetchone()
        if not user:
            return None

        user = User(
            id_=user[0], name=user[1], email=user[2], profile_pic=user[3]
        )
        return user

    @staticmethod
    def get_ED_user(user_id):
        db = get_db()
        user = db.execute(
            "SELECT * FROM ED_users WHERE id = ?", (user_id,)
        ).fetchone()
        if not user:
            return None

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
    def create(id_, name, email, profile_pic):
        db = get_db()
        db.execute(
            "INSERT INTO user (googleID, name, email, profile_pic) "
            "VALUES (?, ?, ?, ?)",
            (id_, name, email, profile_pic),
        )
        # db.exectue(
        #     "INSERT INTO ED_users (userID, id) "
        #     "VALUES (1, 'test')")
        db.commit()
        print("finished inside create method")

#     @staticmethod
#     def create_ED_users():
#         db = get_db()
#         db.exectue("INSERT INTO ED_users (userID, id) VALUES (1, 'test')")
# #        db.execute("INSERT INTO ED_users (id) VALUES (?)", id_)  ### THIS IS THE LINE THAT BREAKS THIS METHOD -> TEST WHY
#         db.commit()
#         print("just finished running create_ED_users method with test data")


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
    def delete(user_id):
        db = get_db()
        db.execute(
            "DELETE FROM user WHERE googleID = ?",
            user_id
        )
        db.commit()


class Mood():
    def _init_(self, id_, mood, date):
        self.UserID = id_
        self.moodID = mood
        self.calenderDate = date

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
        return mood



    # @staticmethod
    # def get_ED_user(user_id):
    #     db = get_db()
    #     user = db.execute(
    #         "SELECT * FROM ED_users WHERE id = ?", (user_id,)
    #     ).fetchone()
    #     if not user:
    #         return None
    #
    #     user = User(
    #         id_=user[0], name=user[1], email=user[2], profile_pic=user[3]
    #     )
    #     return user
        dbconn.commit()


    @staticmethod
    def removeMood(mood):
        id = Database.getID(current_user.id)
        cursor.execute("DELETE FROM moods_tracker WHERE moodID = ?", [mood])
        dbconn.commit()



