CREATE DATABASE SQL_Conference;

CREATE TABLE `Section` (
    `#section_id` DECIMAL NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL,
    `institute` VARCHAR(64) NOT NULL,
    `status` TINYINT(4) NOT NULL DEFAULT 1,
    `login` VARCHAR(32) NOT NULL,
    `password` VARCHAR(32) NOT NULL,
    PRIMARY KEY (`#section_id`)
);

CREATE TABLE `Jury` (
	`#jury_id` DECIMAL NOT NULL AUTO_INCREMENT,
	`surname` varchar(64) NOT NULL,
	`name` varchar(32) NOT NULL,
	`patronymic` varchar(64) NOT NULL,
	`post` varchar(64) NOT NULL,
	`cathedra` varchar(64) NOT NULL,
	`degree` varchar(64) NOT NULL,
	PRIMARY KEY (`#jury_id`)
);

CREATE TABLE `Director` (
	`#director_id` DECIMAL NOT NULL AUTO_INCREMENT,
	`surname` varchar(64) NOT NULL,
	`name` varchar(32) NOT NULL,
	`patronymic` varchar(64) NOT NULL,
	`main_post` varchar(64) NOT NULL,
	`additional_post` varchar(64),
	`job_org` DECIMAL(64) NOT NULL,
	`degree` varchar(64) NOT NULL,
	`phone_number` varchar(12) NOT NULL,
	`email` varchar(64) NOT NULL,
	PRIMARY KEY (`#director_id`)
);

CREATE TABLE `Work` (
	`#work_id` DECIMAL NOT NULL AUTO_INCREMENT,
	`name` TEXT NOT NULL,
	`theses` BINARY NOT NULL,
	`review` DECIMAL NOT NULL,
	`organization` DECIMAL NOT NULL,
	PRIMARY KEY (`#work_id`)
);

CREATE TABLE `Member` (
	`#member_id` DECIMAL NOT NULL AUTO_INCREMENT,
	`surname` varchar(64) NOT NULL,
	`name` varchar(32) NOT NULL,
	`patronymic` varchar(64) NOT NULL,
	`birthday` DATE NOT NULL,
	`passport` INT NOT NULL,
	`passport_issued` varchar(128) NOT NULL,
	`issue_date` DATE NOT NULL,
	`address` varchar(256) NOT NULL,
	`phone_number` varchar(12) NOT NULL,
	`email` varchar(64) NOT NULL,
	`login` varchar(32) NOT NULL,
	`password` varchar(32) NOT NULL,
	PRIMARY KEY (`#member_id`)
);

CREATE TABLE `Organization` (
	`#org_id` DECIMAL NOT NULL AUTO_INCREMENT,
	`name` varchar(128) NOT NULL,
	`location` DECIMAL NOT NULL,
	`address` varchar(128) NOT NULL,
	`phone_number` varchar(12) NOT NULL,
	`email` varchar(64) NOT NULL,
	PRIMARY KEY (`#org_id`)
);

CREATE TABLE `Address_book` (
	`#book_id` DECIMAL NOT NULL AUTO_INCREMENT,
	`country` varchar(32) NOT NULL,
	`region` varchar(32),
	`district` varchar(32),
	`locality` varchar(32) NOT NULL,	/*Населённый пункт*/
	PRIMARY KEY (`#book_id`)
);

CREATE TABLE `Review` (
	`#review_id` DECIMAL NOT NULL AUTO_INCREMENT,
	`criterion1` DECIMAL NOT NULL,
	`criterion2` DECIMAL NOT NULL,
	`criterion3` DECIMAL NOT NULL,
	`criterion4` DECIMAL NOT NULL,
	`criterion5` DECIMAL NOT NULL,
	`criterion6` DECIMAL NOT NULL,
	`criterion7` DECIMAL NOT NULL,
	`criterion8` DECIMAL NOT NULL,
	`criterion9` DECIMAL NOT NULL,
	`review_text` TEXT NOT NULL,
	`jury_surname` varchar(64) NOT NULL,
	`status` BOOLEAN NOT NULL,
	PRIMARY KEY (`#review_id`)
);

CREATE TABLE `Documents` (
	`#doc_id` DECIMAL NOT NULL AUTO_INCREMENT,
	`receipt` BINARY NOT NULL,
	`members_sertificate` BINARY NOT NULL,
	`directors_sertificate` BINARY NOT NULL,
	`member_id` DECIMAL NOT NULL,
	PRIMARY KEY (`#doc_id`)
);

CREATE TABLE `Entry` (	/*Entry*/
	`#entry_id` DECIMAL NOT NULL AUTO_INCREMENT,
	`#work_id` DECIMAL NOT NULL,
	`#member_id` DECIMAL NOT NULL,
	`#section_id` DECIMAL NOT NULL,
	`last_update` DATE NOT NULL,
	`comission_checked` BOOLEAN NOT NULL,
	`admission` BOOLEAN NOT NULL,
	`intrnal_round_place` DECIMAL NOT NULL,
	PRIMARY KEY (`#entry_id`)
);

CREATE TABLE `Jury_Section` (
	`#section_id` DECIMAL NOT NULL,
	`#jury_id` DECIMAL NOT NULL,
	`status` BOOLEAN NOT NULL,
	PRIMARY KEY (`#section_id`)
);

CREATE TABLE `Director_Member` (
	`#member_id` DECIMAL NOT NULL,
	`#director_id` DECIMAL NOT NULL,
	`#work_id` DECIMAL NOT NULL,
	PRIMARY KEY (`#member_id`,`#director_id`)
);

ALTER TABLE `Director` ADD CONSTRAINT `Director_fk0` FOREIGN KEY (`job_org`) REFERENCES `Organization`(`#org_id`);

ALTER TABLE `Work` ADD CONSTRAINT `Work_fk0` FOREIGN KEY (`Review`) REFERENCES `Review`(`#review_id`);

ALTER TABLE `Work` ADD CONSTRAINT `Work_fk1` FOREIGN KEY (`Organization`) REFERENCES `Organization`(`#org_id`);

ALTER TABLE `Organization` ADD CONSTRAINT `Organization_fk0` FOREIGN KEY (`location`) REFERENCES `Address_book`(`#book_id`);

ALTER TABLE `Documents` ADD CONSTRAINT `Documents_fk0` FOREIGN KEY (`member_id`) REFERENCES `Member`(`#member_id`);

ALTER TABLE `Entry` ADD CONSTRAINT `Entry_fk0` FOREIGN KEY (`#work_id`) REFERENCES `Work`(`#work_id`);

ALTER TABLE `Entry` ADD CONSTRAINT `Entry_fk1` FOREIGN KEY (`#member_id`) REFERENCES `Member`(`#member_id`);

ALTER TABLE `Entry` ADD CONSTRAINT `Entry_fk2` FOREIGN KEY (`#section_id`) REFERENCES `Section`(`#section_id`);

ALTER TABLE `Jury_Section` ADD CONSTRAINT `Jury_Sction_fk0` FOREIGN KEY (`#section_id`) REFERENCES `Section`(`#section_id`);

ALTER TABLE `Jury_Section` ADD CONSTRAINT `Jury_Sction_fk1` FOREIGN KEY (`#jury_id`) REFERENCES `Jury`(`#jury_id`);

ALTER TABLE `Director_Member` ADD CONSTRAINT `Director_Member_fk0` FOREIGN KEY (`#member_id`) REFERENCES `Member`(`#member_id`);

ALTER TABLE `Director_Member` ADD CONSTRAINT `Director_Member_fk1` FOREIGN KEY (`#director_id`) REFERENCES `Director`(`#director_id`);

ALTER TABLE `Director_Member` ADD CONSTRAINT `Director_Member_fk2` FOREIGN KEY (`#work_id`) REFERENCES `Work`(`#work_id`);

