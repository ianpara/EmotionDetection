# New file for DB connection with SQL methods to add new user, remove user by name, and remove user by ID

import pymysql

# Open database connection
dbconn = pymysql.connect(host="localhost", user="root", passwd="1234", database="EmotionDetection")

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
        cursor.execute("INSERT INTO user(Username, Email, ProfilePic) VALUES (%s, %s, %s)", (addName, addEmail, addPic))
        dbconn.commit()

    # removes a user when given username
    # this method will be called when a user wants to delete their own account
    @staticmethod
    def remove_user_name(removeName):
        cursor.execute("DELETE FROM user WHERE Username = %s", removeName)
        dbconn.commit()


    # removes user when given user ID
    # this method will be called when an admin wants to delete a user account
    @staticmethod
    def remove_userID(removeID):
        cursor.execute("DELETE FROM user WHERE UserID = %s", removeID)
        dbconn.commit()

   # dbconn.close()