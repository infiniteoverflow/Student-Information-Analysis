''' Use this code to define your database tables and their data'''

# importing module 
import sqlite3 

# connecting to the database 
connection = sqlite3.connect("databases/student.db") 

# cursor 
crsr = connection.cursor() 

# SQL command to create a table in the database 
sql_command = '''CREATE TABLE emp1 ( 
staff_number INTEGER PRIMARY KEY, 
fname VARCHAR(20), 
lname VARCHAR(30), 
gender CHAR(1), 
joining DATE);'''



# execute the statement 
crsr.execute(sql_command)

# To save the changes in the files. Never skip this. 
# If we skip this, nothing will be saved in the database. 
connection.commit() 

# close the connection 
connection.close() 
