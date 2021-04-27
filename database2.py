import sqlite3
import bcrypt


class Database:

    def __init__(self):
        try:
            self.conn = sqlite3.connect('test.db')
            print('Successfully Opened Database')
            self.curr = self.conn.cursor()
        except:
            print('Failed')


    def createTable(self):
        create_table = '''CREATE TABLE IF NOT EXISTS cred(id Integer PRIMARY KEY AUTOINCREMENT,username TEXT NOT NULL,password TEXT NOT NULL);'''
        self.curr.execute(create_table)
        self.conn.commit()


    def insertData(self, data):
        insert_data = '''INSERT INTO cred(username, password)VALUES(?, ?);'''
        self.curr.execute(insert_data, data)
        self.conn.commit()


    def searchData(self, data):
        search_data = '''SELECT * FROM cred WHERE username = (?);'''
        self.curr.execute(search_data, data)


    rows = self.cursor.fetchall()
        if rows == []:
            return 1
        return 0


    def validateData(self, data, inputData):
        print(data)
        print(inputData)

    validate_data = '''SELECT * FROM cred WHERE username = (?);'''

    self.cursor.execute(validate_data, data)
    row = self.cursor.fetchall()

    if row[0][1] == inputData[0]:
        return row[0][2] == bcrypt.hashpw(inputData[1].encode(), row[0][2])