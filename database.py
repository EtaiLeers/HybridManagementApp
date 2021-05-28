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

    def createTableOfUsers(self):
        create_table = '''CREATE TABLE IF NOT EXISTS users(username TEXT PRIMARY KEY NOT NULL,password TEXT NOT NULL);'''
        self.cursor.execute(create_table)
        self.connection.commit()

    def createTableOfInputRecords(self):
        create_table = '''CREATE TABLE IF NOT EXISTS input_records(Budget TEXT , Commitment TEXT, Contract_Type TEXT , Customer_Type TEXT, Duration TEXT , Goals TEXT, Pace TEXT , 
                        Procedures_and_Regulations TEXT, Resources TEXT , Scope TEXT, Team_Availability TEXT , Team_Distribution TEXT, Team_Size TEXT , Uncertainty TEXT);'''
        self.cursor.execute(create_table)
        self.connection.commit()

    def createTableOfOutputRecords(self):
        create_table = '''CREATE TABLE IF NOT EXISTS output_records(rec_approaches_waterfall TEXT, rec_approaches_agile TEXT, rec_approaches_toc TEXT);'''
        self.cursor.execute(create_table)
        self.connection.commit()


    def insertUser(self, data):
        if not data[0] or not data[1]:
            raise ValueError ('Invalid credentials')

        insert_data = '''INSERT INTO users (username, password)VALUES(?, ?)'''
        self.cursor.execute(insert_data, data)
        self.connection.commit()

    #TODO: Insert date and project ID into the query (Feature-1)

    def insertInputRecords(self, data):
        self.cursor.execute('INSERT INTO input_records (Budget,Commitment,Contract_Type,Customer_Type,Duration,Goals,Pace,'
                                                 'Procedures_and_Regulations,Resources,Scope,Team_Availability,'
                                                 'Team_Distribution,Team_Size,Uncertainty) '
                            'VALUES (:Budget, :Commitment, :Contract_Type, :Customer_Type, :Duration, '
                                    ':Goals, :Pace, :Procedures_and_Regulations, :Resources, :Scope, :Team_Availability, '
                                    ':Team_Distribution, :Team_Size, :Uncertainty);', data)
        self.connection.commit()

    def insertOutputRecords(self, waterfallData, agileData, tocData):
        insert_data = '''INSERT INTO output_records (rec_approaches_waterfall, rec_approaches_agile, rec_approaches_toc) VALUES (?, ?, ?)'''
        self.cursor.execute(insert_data, (waterfallData, agileData ,tocData,))
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





