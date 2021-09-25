CREATE table person (
name text PRIMARY KEY,
age integer NOT NULL);

CREATE table person_archive (
name text PRIMARY KEY,
age integer NOT NULL,
time time NOT NULL);

-- DELETE from person ;

-- CREATE TRIGGER tri_age BEFORE INSERT ON person BEGIN
-- SELECT  
--     CASE
--     when new.age < 18 THEN
--     RAISE (ABORT,"Please Enter Valid age !!")
--     end;
-- END;

create trigger check_age before insert on person begin
select
	case
	when new.age < 18 then
	raise(abort,"Invalid Age, Plese Try Again!!")
	end;
end;

insert into person VALUES ("yash","18" );
-- ("meet","20"),
-- ("akash","19"),
-- ("jay","15"),
-- ("maulik","23");

SELECT * FROM person;

DROP table person_archive;
DROP table person;
