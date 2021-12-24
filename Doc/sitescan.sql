--Mysql

CREATE TABLE sitescan (
	id INT auto_increment NOT NULL,
	sitecontent varchar(3000) NULL,
	regDateTime DATETIME NULL,
	CONSTRAINT sitescan_PK PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8
COLLATE=utf8_general_ci;


--Mssql

CREATE TABLE sitescan(
[id] [int] IDENTITY(1,1) NOT FOR REPLICATION NOT NULL,
[sitecontent] [varchar](3000) NULL,
[regDateTime] [datetime2](7) NULL,
CONSTRAINT [PK_sitescan] PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
