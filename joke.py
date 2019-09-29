from flask_login import UserMixin

from db import get_db

class Joke(UserMixin):
    def __init__(self, jokeid, joketext):
        self.joke_id = jokeid
        self.joke = joketext

    @staticmethod
    def get(joke_id):
        db = get_db()
        joke = db.execute(
            "SELECT * FROM joke WHERE jokeid = ? ", (joke_id,)
        ).fetchone()
        if not joke:
            return None

        joke = Joke(
            jokeid=joke[0], joketext=joke[1]
        )
        return joke

    @staticmethod
    def create(jokeid, joke):
        db = get_db()
        db.execute(
            "INSERT INTO joke (jokeid, joketext) "
            "VALUES (?, ?)",
            (jokeid, joke,),
        )
        db.commit()

