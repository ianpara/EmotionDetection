from database.db import get_db

def getMood(user_id):
    db = get_db()
    user = db.execute(
        "SELECT * FROM mood WHERE id = ?", (user_id,)
    ).fetchone()
    return mood

@staticmethod
def create(id_, name, email, profile_pic):
    db = get_db()
    db.execute(
        "INSERT INTO user (googleID, name, email, profile_pic) "
        "VALUES (?, ?, ?, ?)",
        (id_, name, email, profile_pic),
    )
    db.commit()


@staticmethod
def delete(user_id):
    db = get_db()
    db.execute(
        "DELETE FROM user WHERE googleID = ?",
        user_id
    )
    db.commit()
