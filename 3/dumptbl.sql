PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE person (
	names text,
	age integer
);
INSERT INTO person VALUES('yash',18);
INSERT INTO person VALUES('meet',20);
INSERT INTO person VALUES('akash',19);
INSERT INTO person VALUES('jay',15);
INSERT INTO person VALUES('maulik',23);
CREATE TABLE person_archive (
	names text,
	age integer,
	time text
);
COMMIT;
