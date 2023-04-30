CREATE TABLE cabins(
	id SERIAL PRIMARY KEY,
	name TEXT,
	location TEXT,
	size INT,
	price INT,
	year INT,
	availability INT,
	owner_id INTEGER REFERENCES users
);

CREATE TABLE users(
	id SERIAL PRIMARY KEY,
	username TEXT UNIQUE,
	password TEXT
);

CREATE TABLE reviews(
	id SERIAL PRIMARY KEY,
	user_id INTEGER REFERENCES users,
	cabin_id INTEGER REFERENCES cabins,
	comment TEXT,
	grade INTEGER
);

CREATE TABLE reservations(
	id SERIAL PRIMARY KEY,
	cabin_id INTEGER REFERENCES cabins,
	owner_id INTEGER REFERENCES users,
	reservation TIMESTAMP,
	length INTEGER
);
