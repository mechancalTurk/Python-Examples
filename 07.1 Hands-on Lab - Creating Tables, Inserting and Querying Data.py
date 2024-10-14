####### IBM Data Science Professional ##################################
####### Databases and SQL for Data Science with Python #################
####### Hands-on Lab: Creating Tables, Inserting and Querying Data ##### 
################### B. Ege #############################################

# In this lab, you will practice creating tables, inserting, and querying 
# Data using an SQLite database with python in the Skills Network Lab environment

# SQLite is a software library that implements a self-contained, serverless, zero-configuration, 
# transactional SQL database engine. SQLite is the most widely deployed SQL database engine in the world.


# TASK-1: Create DB using SQLite
# Install & load sqlite3
# pip install sqlite3
import sqlite3

# Connecting to sqlite
# connection object
conn = sqlite3.connect('INSTRUCTOR.db')

# cursor object
cursor_obj = conn.cursor()

# TASK-2: Create table in the DB
# Drop the table if already exists
cursor_obj.execute("DROP TABLE IF EXISTS INSTRUCTOR")

# Creating table
table = """ create table IF NOT EXISTS INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2));"""
cursor_obj.execute(table)
print("Table is Ready")

#TASK-3: Insert data into the table
# We will start by inserting just the first row of data:
cursor_obj.execute('''insert into INSTRUCTOR values (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')''')
print("Rav Ahuja has been inserted into the table")
# Now use a single query to insert the remaining two rows of data
cursor_obj.execute('''insert into INSTRUCTOR values (2, 'Raul', 'Chong', 'Markham', 'CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')''')
print("Rahul Chong has been inserted into the table")
print("Hima Vasudevan has been inserted into the table")

#TASK-4: Query data in the table
# Fetch all rows from the table
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
print("All the data in the DB:")
output_all = cursor_obj.fetchall()
for row_all in output_all:
  print(row_all)

## Fetch few rows from the table
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
print("First 2 rows of all of the data:")
# If you want to fetch few rows from the table we use fetchmany(numberofrows) and mention the number 
# how many rows you want to fetch
output_many = cursor_obj.fetchmany(2) 
for row_many in output_many:
  print(row_many)

# Fetch only FNAME from the table
statement = '''SELECT FNAME FROM INSTRUCTOR'''
cursor_obj.execute(statement)
print("Only the first names:")
output_column = cursor_obj.fetchall()
for fetch in output_column:
  print(fetch)

## Fetch only column for column from the table
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
print("Reading a single row column for column:")
# If you want to fetch few rows from the table we use fetchmany(numberofrows) and mention the number 
# how many rows you want to fetch
output_many = cursor_obj.fetchone() 
for row_many in output_many:
  print(row_many)

# Now write and execute an update statement that changes the Rav's CITY to MOOSETOWN
query_update='''update INSTRUCTOR set CITY='MOOSETOWN' where FNAME="Rav"'''
cursor_obj.execute(query_update)
print("Now, updating the Rav's city to MOOSETOWN")
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
  
print("All the data")
output1 = cursor_obj.fetchall()
for row in output1:
  print(row)

# TASK-5: Retrieve data into Pandas
# In this step we will retrieve the contents of the INSTRUCTOR table into a Pandas dataframe:
import pandas as pd
# retrieve the query results into a pandas dataframe
df = pd.read_sql_query("select * from instructor;", conn)
print("Now, the query results have been into a pandas dataframe retrieved")
#print the dataframe
print("df: ", df)
print("the last name in the first record:", df.LNAME[0])
print("the last name in all of the records:", df[['LNAME']])
print("the first and last name in the first record:", df[['FNAME','LNAME']])

# Once the data is in a Pandas dataframe, you can do the typical pandas operations on it.
# For example you can use the shape method to see how many rows and columns are in the dataframe
print("you can use the shape method to see how many rows and columns are in the dataframe")
print("df.shape:", df.shape)

# TASK-6: Close the Connection
conn.close
print("the connection has been closed!")

# SUMMARY
# In this tutorial you created a database & table in Python notebook using SQLite3. 
# Then created a table and insert a few rows of data into it. Then queried the data. 
# You also retrieved the data into a pandas dataframe.
# Original file: 2. Week4_Insert_Update_SQLite.ipynb


