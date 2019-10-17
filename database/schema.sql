CREATE TABLE "user" (
	"id"	TEXT NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"email"	TEXT NOT NULL,
	"profile_pic"	TEXT NOT NULL,
	PRIMARY KEY("id")
);

CREATE TABLE "sqlite_sequence" (
	"name"	TEXT,
	"seq"	TEXT
);

CREATE TABLE "motivational_tracker" (
	"userID"	TEXT NOT NULL,
	"motivationalID"	INTEGER NOT NULL,
	FOREIGN KEY("motivationalID") REFERENCES "motivational_quotes"("motivationalID") ON UPDATE CASCADE,
	FOREIGN KEY("userID") REFERENCES "user"("id") ON UPDATE CASCADE
);

CREATE TABLE "motivational_quotes" (
	"motivationalID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"motivational"	TEXT NOT NULL
);

CREATE TABLE "moods" (
	"moodID"	INTEGER NOT NULL UNIQUE,
	"mood"	VARCHAR(20),
	PRIMARY KEY("moodID")
);

CREATE TABLE "mood_tracker" (
	"userID"	TEXT,
	"moodID"	INTEGER,
	"calenderDate"	date NOT NULL,
	FOREIGN KEY("moodID") REFERENCES "moods"("moodID") ON UPDATE CASCADE,
	FOREIGN KEY("userID") REFERENCES "user"("id") ON UPDATE CASCADE
);

CREATE TABLE "jokes" (
	"jokeID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"joke"	TEXT NOT NULL
);

CREATE TABLE "joke_tracker" (
	"userID"	TEXT NOT NULL,
	"jokeID"	INTEGER NOT NULL,
	FOREIGN KEY("jokeID") REFERENCES "jokes"("jokeID") ON UPDATE CASCADE,
	FOREIGN KEY("userID") REFERENCES "user"("id") ON UPDATE CASCADE
);

CREATE TABLE "contacts" (
	"userID"	TEXT NOT NULL UNIQUE,
	"contact_number"	TEXT NOT NULL,
	"contact_name"	TEXT NOT NULL,
	FOREIGN KEY("userID") REFERENCES "user"("id") ON UPDATE CASCADE
);
