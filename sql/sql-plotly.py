import sqlite3
import plotly

def create_db(test_db):

    """create db, add dummy data"""

    # establish connection
    connection = sqlite3.connect(test_db)

	# add values
    cursor = connection.cursor()
    cursor.execute('drop table if exists test_table')
    cursor.execute('create table test_table(name varchar(10), number int)')
    cursor.execute('insert into test_table (name, number) values(?, ?)', ('Bobby', 10))
    cursor.execute('insert into test_table (name, number) values(?, ?)', ('Michael', 20))
    cursor.execute('insert into test_table (name, number) values(?, ?)', ('John', 20))
    cursor.execute('select * from test_table')

    # commit data
    connection.commit()

    # close cursor, connection
    cursor.close()
    connection.close()

def search_db(test_db):

    """search db, add data to list"""

    # variables
    name=[]
    age=[]
    all_data=[]

    # establish connection
    connection = sqlite3.connect(test_db)

    # grab all data
    cursor = connection.cursor()
    cursor.execute('select * from test_table')
    for row in cursor.fetchall():
        name.append(str(row[0]))
        age.append(row[1])

    # append lists to a list
    all_data.extend([name,age])

    # close cursor, connection
    cursor.close()
    connection.close()

    return all_data

def call_plotly(list_of_list,username,key):

    """connect to plot.ly API, send data, create graph"""

    py = plotly.plotly(username,key)
    py.plot(list_of_list[0],list_of_list[1])

create_db("test_database")
all_data = search_db("test_database")
print all_data == [['Bobby', 'Michael', 'John'], [10, 20, 20]]
call_plotly(all_data,"GET_YOUR_OWN_USERNAME", "GET_YOUR_OWN_KEY")
