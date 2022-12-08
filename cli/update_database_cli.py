import sqlite3
import os
from rich import print
from rich.console import Console

console = Console()

cwd = os.getcwd()
db_path = os.path.join(cwd, "database\\DAOGovernance.db")
db_connection = sqlite3.connect(db_path)
cursor = db_connection.cursor()

def check_exists(dao_name):
	select_query = f"SELECT * FROM Governance WHERE DAO = '{dao_name}';"
	cursor.execute(select_query)
	results = cursor.fetchall()
	return results  # If the DAO exists, update its values in the table

def update_existing_record(table, column, new_val, dao):
    # Update a row from a given table
    if check_exists(dao):
        # prompt the user for confirmation
        response = input(f"Are you sure you want to update the '{column}' column with value '{new_val}' for the record with DAO '{dao}' in the '{table}' table? (y/n)")

        # check if the user pressed "y"
        if response == "y":
            query = f"""UPDATE {table} SET 
            `{column}` = '{new_val}'
            WHERE DAO = '{dao}'
            """
            cursor.execute(query)
            db_connection.commit()
            print(f"Updated DAO: {dao} from the {table} table.")

    # if the record does not exist, print a message
    else:
        print(f"Sorry the DAO ('{dao}') you have tried to update does not exist")



def delete_existing_record(table, dao):
    # Delete a row from a given table
    if check_exists(dao):
        # prompt the user for confirmation
        response = input(f"Are you sure you want to delete the record with DAO '{dao}' from the '{table}' table? (y/n)")

        # check if the user pressed "y"
        if response == "y":
            query = f"DELETE FROM {table} WHERE DAO = '{dao}'"
            cursor.execute(query)
            db_connection.commit()
            print(f"Deleted DAO: {dao} from the {table} table.")

    # if the record does not exist, print a message
    else:
        print(f"Sorry the DAO ('{dao}') you have tried to delete does not exist")

def add_new_column(table, column_name, var_or_int):
	# Add columns for a given table
	if var_or_int == "1":
		query = f"ALTER TABLE Governance ADD {column_name} varchar(30)"
	query = f"ALTER TABLE Governance ADD {column_name} INT"
	cursor.execute(query)
	db_connection.commit()
	print(f"Added column: {column_name} to the {table} table.")

def delete_existing_column(table, column_name):
    # Delete columns from a given table
    # prompt the user for confirmation
    response = input(f"Are you sure you want to delete the '{column_name}' column from the '{table}' table? (y/n)")

    # check if the user pressed "y"
    if response == "y":
        query = f"ALTER TABLE {table} DROP COLUMN {column_name}"
        cursor.execute(query)
        db_connection.commit()
        print(f"Deleted column: {column_name} from the {table} table.")


option_functions = {
		1: update_existing_record,
		2: delete_existing_record,
		3: add_new_column,
		4: delete_existing_column
}


# Define a function to handle editing the database
def editing_prompt():
	
	# Prompt the user for an option
	beginning_prompt()
	user_input = int(input('Select an option [1/4]: '))

	# Validate the user input
	if user_input not in option_functions:
		print("Invalid input please try again")
		return

	# Call the corresponding function based on the user input
	if user_input == 1:
		table_selection = select_table_prompt()
		print('Please select the name of the column you would like to update the value of: ')
		column_name = select_column_prompt(table_selection)
		dao_name = input(f'Enter DAO would you like to update from the {table_selection} table: ')
		new_val = input(f'Enter new value: ')
		option_functions[user_input](table_selection, column_name, new_val, dao_name)
		if table_selection == -1:
			print('Invalid table goodbye.')
			return
		if column_selection == -1:
			print('Invalid column selection')
			return
	elif user_input == 2:
		table_selection = select_table_prompt()
		dao_name = input(f'Enter DAO would you like to remove from the {table_selection} table: ')
		option_functions[user_input](table_selection, dao_name)
		if table_selection == -1:
			print('Invalid table goodbye.')
			return
	elif user_input == 3:
		table_selection = select_table_prompt()
		column_name = input('Please enter the name of the new column: ')
		var_or_int = input('Enter column type Var (0) or INT (1): ')
		option_functions[user_input](table_selection, column_name, var_or_int)
		if table_selection == -1:
			print('Invalid table goodbye.')
			return
		if column_selection == -1:
			print('Invalid column selection')
			return
	elif user_input == 4:
		table_selection = select_table_prompt()
		print('Please select which column you would like to delete: ')
		column_selection = select_column_prompt(table_selection)
		option_functions[user_input](table_selection, column_selection)
		if table_selection == -1:
			print('Invalid table goodbye.')
			return
		if column_selection == -1:
			print('Invalid column selection')
			return

	

# Define a function to prompt the user for a table selection
def select_table_prompt():
	# Query the list of tables in the database
	table_names = """SELECT name FROM sqlite_master
	WHERE type='table';"""
	cursor.execute(table_names)
	table_list = cursor.fetchall()

	# Prompt the user to select a table
	print('Please select one of the following tables:')
	num_of_tables = len(table_list)
	for i, table in enumerate(table_list):
		print(f'{i+1}. ', table[0])
	table_input = int(input(f'Select an option [1/{num_of_tables}]: '))

	# Validate the user input and return the selected table
	if table_input > num_of_tables and table_input < 1:
		return -1
	else:
		table_selection = table_list[table_input-1][0]
		return table_selection

def select_column_prompt(table):
	cursor.execute(f"PRAGMA table_info({table})")
	column_list = [row[1] for row in cursor]
	num_of_cols = len(column_list)
	for i,row in enumerate(column_list):
		print(f'{i+1}. ', row)
	column_input = int(input(f'Select an option [1/{num_of_cols}]: '))

	if column_input > num_of_cols and num_of_cols < 1:
		return -1
	else:
		column_input = column_list[column_input-1]
		print(column_input)
		return column_input

def beginning_prompt():
		print('\nPlease select one of the following options:')
		print(" 1. Update existing record\n",
		"2. Delete existing record\n",
		"3. Add new column\n",
		"4. Delete existing column\n"
		)



if __name__ == "__main__":
	try:
		# Prompt the user for options to edit the database
		editing_prompt()
	except KeyboardInterrupt:
		console.print("\nThank you goodbye", style="magenta")