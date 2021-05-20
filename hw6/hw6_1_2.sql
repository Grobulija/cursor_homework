CREATE TABLE phones (
	id int NOT NULL AUTO_INCREMENT,
	phone_name varchar(128) NULL,
	company_id int NOT NULL,
	user_id int NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE phone_companies (
	id int NOT NULL AUTO_INCREMENT,
	name varchar(100) NULL,
	PRIMARY KEY (id)
);

/*
sudo mysql -u root -p my_items -e "SELECT * FROM users WHERE is_developer=1;" > devs.txt
*/


INSERT INTO phone_companies (name)
VALUES ('xiaomi'), ('apple'), ('samsung');

INSERT INTO phones (phone_name, company_id, user_id)
VALUES ('Xiaomi Poco X3 NFC ', 1, 2),
       ('Samsung Galaxy S20+ 5G', 3, 1), 
       ('Apple iPhone 12 Pro', 2, 3);

/*
sudo mysql -u root -p my_items -e "SELECT * FROM phones WHERE company_id IN (SELECT id FROM phone_companies WHERE name = 'xiaomi');" > xi_phones.txt
*/

SELECT * FROM users
WHERE id IN (SELECT user_id FROM phones);
