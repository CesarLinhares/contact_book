DROP TABLE IF EXISTS phones_contacts;
DROP TABLE IF EXISTS phones;
DROP TABLE IF EXISTS contacts;


CREATE TABLE contacts(
	_id varchar(255) NOT NULL,
	first_name varchar(255) NOT NULL,
	last_name varchar(255) NOT NULL,
	email varchar(255) NOT NULL,
	address varchar(255) NOT NULL,
	status bit NOT NULL,
	PRIMARY KEY (_id)
);

CREATE TABLE phones(
	_id serial not null,
	phone1 varchar(20) not null,
	phone1_type varchar(20) not null,
	phone2 varchar(20),
	phone2_type varchar(20),
	phone3 varchar(20),
	phone3_type varchar(20),
	PRIMARY KEY (_id)
);

CREATE TABLE phones_contacts(
	_id serial not null,
	contact_id varchar(255) not null,
	phone_id int not null,
	PRIMARY KEY (_id),
	FOREIGN KEY (contact_id) REFERENCES contacts(_id),
	FOREIGN KEY (phone_id) REFERENCES phones(_id)
);