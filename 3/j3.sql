.open j3.db
-- create table person (
-- 	names text,
-- 	age integer
-- );
-- insert into person VALUES ("yash","18" ),
-- ("meet","20"),
-- ("akash","19"),
-- ("jay","15"),
-- ("maulik","23");

-- create table person_archive (
-- 	names text,
-- 	age integer,
-- 	time text
-- );

--3.1
-- .open j3.db
-- .output scemma.sql
-- .schema
-- .quit

-- 3.2
-- .open j3.db
-- .output dumptbl.sql
-- .dump person person_archive
-- .quit

-- 3.3
-- .open j3.db
-- .header on
-- .mode csv
-- .output csv.csv
-- SELECT * from person;
-- .quit 
