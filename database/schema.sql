CREATE TABLE user (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  profile_pic TEXT NOT NULL,
  userID INTEGER NOT NULL,
);

CREATE TABLE moods_tracker (
  userID INTEGER PRIMARY KEY,
  mood TEXT NOT NULL,
  calenderDate INTEGER UNIQUE NOT NULL,
  FOREIGN KEY (userID)
  REFERENCES user (userID)
);

CREATE TABLE joke_tracker (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  profile_pic TEXT NOT NULL,
  FOREIGN KEY (id)
  REFERENCES mood (user_id)
);

CREATE TABLE jokes (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  profile_pic TEXT NOT NULL,
  FOREIGN KEY (id)
  REFERENCES mood (user_id)
);

CREATE TABLE motivational_quotes (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  profile_pic TEXT NOT NULL,
  FOREIGN KEY (id)
  REFERENCES mood (user_id)
);

CREATE TABLE motivational_tracker (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  profile_pic TEXT NOT NULL,
  FOREIGN KEY (id)
  REFERENCES mood (user_id)
);

CREATE TABLE contacts (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  profile_pic TEXT NOT NULL,
  FOREIGN KEY (id)
  REFERENCES mood (user_id)
);