import sqlite3
import plotly

class TestDatabase(object):

    def __init__(self, test_db):
        self.test_db = test_db

    def create(self):

        """create db, add dummy data"""

        # establish connection
        with sqlite3.connect(self.test_db) as connection:

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

    def search(self):

        """search db, add data to list"""

        # variables
        name=[]
        age=[]
        all_data=[]

        # establish connection
        with sqlite3.connect(self.test_db) as connection:

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

        return all_data


if __name__ == '__main__':

    # Instantiate
    new_db = TestDatabase("test_database")

    # call our instance methods
    new_db.create()
    all_data = new_db.search()

    print all_data == [['Bobby', 'Michael', 'John'], [10, 20, 20]]

    py = plotly.plotly("GET_YOUR_OWN_USERNAME", "GET_YOUR_OWN_KEY")
    py.plot(all_data[0],all_data[1])

    py.plot([name][age])
