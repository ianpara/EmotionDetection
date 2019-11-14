CREATE TABLE "user" (
	"googleID"	TEXT UNIQUE,
	"name"	TEXT,
	"email"	TEXT UNIQUE,
	"profile_pic"	TEXT,
	"userID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"joke_counter"	INTEGER DEFAULT 0
);

CREATE TABLE "moods_tracker" (
	"userID"	INTEGER,
	"mood"	TEXT NOT NULL,
	"calenderDate"	INTEGER NOT NULL,
	"moodID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	FOREIGN KEY("userID") REFERENCES "user"("userID")
);

CREATE TABLE "joke_tracker" (
	"userID"	INTEGER,
	"jokeID"	INTEGER,
	FOREIGN KEY("jokeID") REFERENCES "jokes"("jokeID") ON UPDATE CASCADE,
	PRIMARY KEY("userID","jokeID"),
	FOREIGN KEY("userID") REFERENCES "user"("userID") ON UPDATE CASCADE
);

CREATE TABLE "jokes" (
	"jokeID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"joke"	TEXT NOT NULL UNIQUE
);

CREATE TABLE "motivational_quotes" (
	"motivationalID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"motivational"	TEXT NOT NULL
);

CREATE TABLE "motivational_tracker" (
	"userID"	INTEGER,
	"motivationalID"	INTEGER,
	FOREIGN KEY("motivationalID") REFERENCES "motivational_quotes"("motivationalID") ON UPDATE CASCADE,
	FOREIGN KEY("userID") REFERENCES "user"("userID") ON UPDATE CASCADE,
	PRIMARY KEY("userID","motivationalID")
);

CREATE TABLE "contacts" (
	"userID"	INTEGER,
	"contact_number"	TEXT,
	"contact_name"	TEXT NOT NULL,
	FOREIGN KEY("userID") REFERENCES "user"("userID") ON UPDATE CASCADE,
	PRIMARY KEY("userID","contact_number")
);

CREATE TABLE "moods" (
	"moodID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"mood"	VARCHAR(20) NOT NULL UNIQUE
);