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

        user = User(
            id_=user[0], name=user[1], email=user[2], profile_pic=user[3]
        )
        return user

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
#     def create_ED_users(id_):
#         db = get_db()
#         sor = db.cursor()
#         cucurrsor.exectue("INSERT INTO ED_users (userID, id) VALUES (1, 'test')")
# #        db.execute("INSERT INTO ED_users (id) VALUES (?)", id_)  ### THIS IS THE LINE THAT BREAKS THIS METHOD -> TEST WHY
#         db.commit()
#         print("just finished running create_ED_users method with test data")

    @staticmethod
    def create_ED_users():
        db = get_db()
        db.exectue("INSERT INTO ED_users (userID, id) VALUES (1, 'test')")
#        db.execute("INSERT INTO ED_users (id) VALUES (?)", id_)  ### THIS IS THE LINE THAT BREAKS THIS METHOD -> TEST WHY
        db.commit()
        print("just finished running create_ED_users method with test data")



        db.commit()


    @staticmethod
    def delete(user_id):
        db = get_db()
        db.execute(
            "DELETE FROM user WHERE id = ?",
            user_id
        )
        db.commit()




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

