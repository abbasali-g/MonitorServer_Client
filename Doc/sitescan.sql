CREATE TABLE sitescan (
	id INT auto_increment NOT NULL,
	sitecontent varchar(3000) NULL,
	regDateTime DATETIME NULL,
	CONSTRAINT sitescan_PK PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8
COLLATE=utf8_general_ci;

