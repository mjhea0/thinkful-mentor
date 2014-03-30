import sqlite3

# create a new database if the database doesn't already exist 
with sqlite3.connect("flashcards.db") as connection:

    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # create the table
    c.execute("""CREATE TABLE questions
             (question_id INTEGER primary key autoincrement, description TEXT) 
              """)

    c.execute("""CREATE TABLE answers
             (answer_id INTEGER primary key autoincrement, description TEXT, question_id INTEGER) 
              """)




