
import sqlite3
import plotly
import pdb


# Function to create a sample database
def create_sample_db(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS test_table')
    cursor.execute('CREATE TABLE test_table(name varchar(10), number int)')
    cursor.execute('INSERT INTO test_table (name, number) values(?, ?)', ('Bobby', 10))
    cursor.execute('INSERT INTO test_table (name, number) values(?, ?)', ('Michael', 20))
    cursor.execute('INSERT INTO test_table (name, number) values(?, ?)', ('John', 20))
    connection.commit()
    cursor.close()
    connection.close()

# Function to search sample database
def search_db(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM test_table') # execute sql
    name=[]
    number=[]
    all_data=[]
    for row in cursor.fetchall(): #grabs all data
        name.append(str(row[0]))
        number.append(row[1])
    all_data.extend([name, number])
        # print name
        # print all_data[0]
    print all_data
    cursor.close()
    connection.close()


# Push to plot.ly
def plotly_api(data):
    py = plotly.plotly('FOO', 'BAR')
    py.plot(data[0], data[1])


create_sample_db("test_db")
# search_db("test_db")
data = search_db("test_db")
# plotly_api(data)


