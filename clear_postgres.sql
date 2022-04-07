DROP TABLE IF EXISTS phones_contacts;
DROP TABLE IF EXISTS phones;
DROP TABLE IF EXISTS contacts;


CREATE TABLE contacts(
	_id varchar(255) NOT NULL,
	firstname varchar(255) NOT NULL,
	lastname varchar(255) NOT NULL,
	email varchar(255) NOT NULL,
	address varchar(255) NOT NULL,
	phone1 varchar(20) not null,
	phone1_type varchar(20) not null,
	phone2 varchar(20),
	phone2_type varchar(20),
	phone3 varchar(20),
	phone3_type varchar(20),
	active bit NOT NULL,
	PRIMARY KEY (_id)
);

