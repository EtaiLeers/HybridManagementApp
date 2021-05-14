import sqlite3

class Database:

    def __init__(self):
        try:
            # Create a database or connect to one
            self.connection = sqlite3.connect('users.db')
            print('Successfully Opened Database')
            self.cursor = self.connection.cursor()
        except:
            print('Failed')


    def createTable(self):
        create_table = '''CREATE TABLE IF NOT EXISTS users(username TEXT PRIMARY KEY NOT NULL,password TEXT NOT NULL);'''
        self.cursor.execute(create_table)
        self.connection.commit()

    def insertData(self, data):
        if not data[0] or not data[1]:
            raise ValueError ('Invalid credentials')

        insert_data = '''INSERT INTO users (username, password)VALUES(?, ?)'''
        self.cursor.execute(insert_data, data)
        self.connection.commit()

    def searchData(self, data):

        if not data:
            raise ValueError ('Invalid credentials')

        search_data = '''SELECT * FROM users WHERE username = ? '''
        self.cursor.execute(search_data, (data, ))

        rows = self.cursor.fetchall()
        if rows == []:
            return 1
        return 0

    def validateData(self, data, inputData):
        print(data)
        print(inputData)

        if not data or not inputData[1]:
            raise ValueError('You must provide credentials')

        validate_data = '''SELECT * FROM users WHERE username = ? '''

        self.cursor.execute(validate_data, (data,))
        # self.cursor.execute(validate_data, ('Etai',))
        row = self.cursor.fetchall()

        if row[0][0] == inputData[0]:
            return row[0][1] == str(inputData[1])


def run():
    startDB = Database()
    startDB.run()

# ======================================================================================


'''
records = cursor.execute("SELECT * FROM users")

print(cursor.fetchall())

#Commit changes
connection.commit()

#close Connection
connection.close()


root.mainloop()
'''





