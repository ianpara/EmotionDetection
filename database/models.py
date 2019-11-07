from flask_login import UserMixin

from database.db import get_db

class User(UserMixin):
    def __init__(self, id_, name, email, profile_pic):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_pic

    @staticmethod
    def get(user_id):
        db = get_db()
        user = db.execute(
            "SELECT * FROM user WHERE id = ?", (user_id,)
        ).fetchone()
        if not user:
            return None

        user = User(
            id_=user[0], name=user[1], email=user[2], profile_pic=user[3]
        )
        return user

    @staticmethod
    def create(id_, name, email, profile_pic):
        db = get_db()
        db.execute(
            "INSERT INTO user (id, name, email, profile_pic) "
            "VALUES (?, ?, ?, ?)",
            (id_, name, email, profile_pic),
        )
        db.commit()


    @staticmethod
    def delete(user_id):
        db = get_db()
        db.execute(
            "DELETE FROM user WHERE id = ?",
            user_id
        )
        db.commit()

    @staticmethod
    def getID(user_id):
        db = get_db()
        user = db.execute(
            "SELECT userID FROM user WHERE id like ?", (user_id,)
        ).fetchone()
        if not user:
            return None

class Mood():
    def _init_(self, id_, mood, date):
        self.UserID = id_
        self.moodID = mood
        self.calenderDate = date

    @staticmethod
    def get(user_id):
        db = get_db()
        mood = db.execute(
            "SELECT * FROM mood_tracker WHERE userID = ?", (user_id,)
        ).fetchall()
        if not mood:
            return None

        mood = Mood(
            id_=mood[0], mood=user[1], date=user[2]
        )
        return mood

    @staticmethod
    def create(id_, mood, date):
        db = get_db()
        db.execute(
            "INSERT INTO mood_tracker (userID, moodID, calenderDate) "
            "VALUES (?, ?, ?)",
            (id_, mood, date),
        )
        db.commit()
