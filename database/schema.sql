CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  profile_pic TEXT NOT NULL
);

CREATE TABLE joke (
jokeid INTEGER PRIMARY KEY,
joketext TEXT NOT NULL
);

INSERT INTO joke VALUES (1, 'Test Joke')

CREATE TABLE motivational (
id INTEGER PRIMARY KEY,
motivational TEXT NOT NULL
);

