CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  profile_pic TEXT NOT NULL,
  FOREIGN KEY (id)
  REFERENCES mood (user_id)
);

CREATE TABLE mood (
  mood_id TEXT PRIMARY KEY,
  user_id TEXT NOT NULL,
  recording TEXT UNIQUE NOT NULL
);
