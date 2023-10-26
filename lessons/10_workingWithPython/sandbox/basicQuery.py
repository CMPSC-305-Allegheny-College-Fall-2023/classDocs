#!/usr/bin/env python3

###########################################################
# The database managing code to read an existing database. 
# Note, that the Python code needs to know the attributes 
# of the table in order to access them using code. 
#
# Usage: python3 basicQuery.py 
# Output: Text extracted from database query
# Requirement: database file; myCampusDB.sqlite3
###########################################################

# load libraries
import sqlite3

# name the database file
myDBfile = "myCampusDB.sqlite3"

# define table attributes to use in query
myTable_str = "Instructor"
attribute1_str = "name"
attribute2_str = "deptName"
attribute3_str = "salary"

# define a query to pass to the db. add attributes from above to form the print statement
myQuery_str = f"SELECT {attribute1_str}, {attribute2_str}, {attribute3_str} FROM {myTable_str}"
print(f" [+] Running Query:\n {myQuery_str}")

# connect to the database
dbFile_str = myDBfile # name of the current database
conn = sqlite3.connect(dbFile_str) # open a connection to the base

# Send query to DB
myResult = conn.execute(myQuery_str) # run the query
print(f" [+] Results from query: {myResult}")

# Get result from query
queryInfo_list = myResult.fetchall()
print(f" [+] Fetchall results from query: {queryInfo_list}")

# print out formatted results
for i in queryInfo_list:
	print(f"\t[+] {i}")

# close the database connection
conn.close() 