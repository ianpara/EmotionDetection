#!/usr/bin/python3

import pymysql

# Open database connection
dbconn = pymysql.connect(host="localhost",user="root",passwd="1234",database="EmotionDetection")



def selectUser():
    cursor = dbconn.cursor()
    cursor.execute("SELECT * FROM user")
    data = cursor.fetchall()
    print(data)
    dbconn.close()


# # prepare a cursor object using cursor() method
# cursor = dbconn.cursor()
#
# # execute SQL query using execute() method.
# cursor.execute("SELECT * FROM user")
#
# # Fetch a single row using fetchone() method.
# data = cursor.fetchall()
# print(data)
#
# # disconnect from server
# dbconn.close()
