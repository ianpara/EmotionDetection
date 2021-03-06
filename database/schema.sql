CREATE TABLE "user" (
	"googleID"	TEXT UNIQUE,
	"name"	TEXT,
	"email"	TEXT UNIQUE,
	"profile_pic"	TEXT,
	"userID"	INTEGER PRIMARY KEY AUTOINCREMENT

CREATE TABLE "sqlite_sequence" (
	"name"	TEXT,
	"seq"	TEXT
);

CREATE TABLE "motivational_tracker" (
	"userID"	INTEGER,
	"motivationalID"	INTEGER,
	FOREIGN KEY("motivationalID") REFERENCES "motivational_quotes"("motivationalID") ON UPDATE CASCADE,
	FOREIGN KEY("userID") REFERENCES "user"("userID") ON UPDATE CASCADE,
	PRIMARY KEY("userID","motivationalID")
);

CREATE TABLE "motivational_quotes" (
	"motivationalID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"motivational"	TEXT NOT NULL
);

CREATE TABLE "moods_tracker" (
	"userID"	INTEGER,
	"mood"	INTEGER,
	"calenderDate"	INTEGER,
  "moodID" INTERGER PRIMARY KEY AAU
	FOREIGN KEY("moodID") REFERENCES "moods"("moodID") ON UPDATE CASCADE,
	FOREIGN KEY("userID") REFERENCES "user"("userID") ON UPDATE CASCADE,
	PRIMARY KEY("userID","moodID","calenderDate")
);

CREATE TABLE "jokes" (
	"jokeID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"joke"	TEXT NOT NULL
);

CREATE TABLE "joke_tracker" (
	"userID"	INTEGER,
	"jokeID"	INTEGER,
	FOREIGN KEY("jokeID") REFERENCES "jokes"("jokeID") ON UPDATE CASCADE,
	PRIMARY KEY("userID","jokeID"),
	FOREIGN KEY("userID") REFERENCES "user"("userID") ON UPDATE CASCADE
);

CREATE TABLE "contacts" (
	"userID"	INTEGER,
	"contact_number"	TEXT,
	"contact_name"	TEXT NOT NULL,
	FOREIGN KEY("userID") REFERENCES "user"("userID") ON UPDATE CASCADE,
	PRIMARY KEY("userID","contact_number")
);

CREATE TABLE "motivational_tracker" (
	"userID"	INTEGER,
	"motivationalID"	INTEGER,
	FOREIGN KEY("motivationalID") REFERENCES "motivational_quotes"("motivationalID") ON UPDATE CASCADE,
	FOREIGN KEY("userID") REFERENCES "user"("userID") ON UPDATE CASCADE,
	PRIMARY KEY("userID","motivationalID")
);

CREATE TABLE contacts (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  profile_pic TEXT NOT NULL,
  FOREIGN KEY (id)
  REFERENCES mood (user_id)
);
