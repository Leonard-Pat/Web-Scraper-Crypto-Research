import sqlite3
import os

cwd = os.getcwd()
db_path = os.path.join(cwd, "database\\DAOGovernance.db")
db_connection = sqlite3.connect(db_path)
cursor = db_connection.cursor()

def create_table():
	create_governance = """ --sql
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
	create_treasury = """ --sql
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


def execute_sql_script():
	# read the SQL script from a file
	cwd = os.getcwd()
	sql_file = os.path.join(cwd, 'database\\tally.sql')
	with open(sql_file, 'r') as f:
		sql = f.read()
		cursor.executescript(sql)

execute_sql_script()