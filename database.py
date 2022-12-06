import sqlite3


db_connection = sqlite3.connect("DeepDao.db")
cursor = db_connection.cursor()

def create_table():
	create_governance = """
	CREATE TABLE IF NOT EXISTS `Governance` (
	`DAO` VARCHAR(30) DEFAULT NULL,
	`Treasury AUM (usd)` VARCHAR(30),
	`Token Holders` VARCHAR(30),
	`Total No. Proposals` INT,
	`Total No. Voters` INT,
	`Proposal Creators` INT,
	`Participation Rates (%)` DECIMAL,
	`Avg voters per proposal` DECIMAL,
	`Success Rate (%)` DECIMAL,
	`Total Votes` INT,
	`On-Chain Governance (type)` VARCHAR(30),
	`Off-Chain Governance (snapshot)` INT(1),
	PRIMARY KEY (`DAO`)
	);   
	"""
	cursor.execute(create_governance)
	create_treasury = """
	CREATE TABLE IF NOT EXISTS `Treasury` (
		`DAO` VARCHAR(30),
		`Top 1 Token (name)` VARCHAR(30),
		`Top 2 Token (name)` VARCHAR(30),
		`Top 3 Token (name)` VARCHAR(30),
		`Top 4 Token (name)` VARCHAR(30),
		`Top 5 Token (name)` VARCHAR(30),
		`Top 1 Token (usd)` DECIMAL,
		`Top 2 Token (usd)` DECIMAL,
		`Top 3 Token (usd)` DECIMAL,
		`Top 4 Token (usd)` DECIMAL,
		`Top 5 Token (usd)` DECIMAL,
		`Top 1 Token (% of treasury)` DECIMAL,
		`Top 2 Token (% of treasury)` DECIMAL,
		`Top 3 Token (% of treasury)` DECIMAL,
		`Top 4 Token (% of treasury)` DECIMAL,
		`Top 5 Token (% of treasury)` DECIMAL,
		`Top 1 Token (token balance)` VARCHAR(30),
		`Top 2 Token (token balance)` VARCHAR(30),
		`Top 3 Token (token balance)` VARCHAR(30),
		`Top 4 Token (token balance)` VARCHAR(30),
		`Top 5 Token (token balance)` VARCHAR(30),
		PRIMARY KEY (`DAO`)
	);
	"""
	cursor.execute(create_treasury)



def del_query():
	query = f""" 
	DELETE FROM Treasury WHERE DAO='Kusama';
	"""
	cursor.execute(query)
	db_connection.commit()

def create_column():
	query = """ALTER TABLE Governance
		ADD Tag varchar(30);"""
	cursor.execute(query)
	db_connection.commit()

# create_table()

# del_query()

create_column()
