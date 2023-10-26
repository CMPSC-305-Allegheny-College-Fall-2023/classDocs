#!/usr/bin/env python3

###########################################################
# The database managing code begins here. This code creates
# the schema in order to place data into tables.
# 
# Usage: python3 simpleInsert1.py 
# Outputs text and a table.
# Requirement: None 
###########################################################

import sqlite3

dbFilename_str = "myDB_i.sqlite3" #establish the DB file
conn = sqlite3.connect(dbFilename_str) # open connection to the DB

print("\t _________________________________________________")
print("\n\t  Program to demo automatic INSERT statements using SQLite3") # add bright green to text then set it back to regular white.
print("\t -------------------------------------------------\n")

print("\t [+] Simple table creation")
myTable_str = "StudyMusic" #define the table
attribute1_str = "id INTEGER NOT NULL " # define first attribute statement
attribute2_str = "favSong VARCHAR" # define first attribute statement
attribute3_str = "BandName VARCHAR" # define first attribute statement


# Create the table creation string
myCreation_str = f"CREATE TABLE {myTable_str} ({attribute1_str}, {attribute2_str}, {attribute3_str})"

# Create a test to see whether the insert is possible. If not, then do not crash the program
try:
	print(f"\t my insert: {myCreation_str}")

	# pass the table building string to sqlite3 library
	conn.execute(myCreation_str)

	# Save (i.e., commit) the changes
	conn.commit()

except sqlite3.OperationalError: # does the table already exist? If so, ignore creation statement
	print("\t [-] Note: The table already exists.")


## Check the new table
myQuery_str = f"SELECT * FROM {myTable_str}"

# Insert a row of data

myTable_str = "StudyMusic" # define the table
attrID_str = "10"
attrSONG_str = "Yello Submarine"
attrARTIST_str = "The Beatles"

print(f"\t [+] Simple INSERT into Table {myTable_str}")


# define the insert statement

myInsert_str = f"INSERT INTO {myTable_str} VALUES ({attrID_str}, \"{attrSONG_str}\", \"{attrARTIST_str}\")"

print(f"\t [+] my insert statement {myInsert_str}")


# pass the INSERT string to sqlite3 library
conn.execute(myInsert_str)

# Save (i.e., commit) the changes
conn.commit()

# Do a simple query to check that insert worked
myQuery_str = f"SELECT * FROM {myTable_str}"
result = conn.execute(myQuery_str) # run the query
tables = result.fetchall() # collect query for processing
print("\t "+myQuery_str)
print("\t [+] Results: ")
for i in tables:
	print(f"\t  {i}") # show results of query


conn.close() # close the database connection
