import sqlite3

# create a new database if the database doesn't already exist 
with sqlite3.connect("checklist.db") as connection:

    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # create the table
    c.execute("""CREATE TABLE items
             (item_id INTEGER primary key autoincrement, description TEXT, amount NUMBER, status INTEGER) 
              """)



