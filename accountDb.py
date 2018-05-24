#! C:\Python36\python
import mysql.connector


class Account:

    accNo = ""
    accName = ""
    balance = 0
    password = ""
    db = mysql.connector.connect(
        host="localhost", user="root", password="", database="bank_app")

    def __init__(self, accNo, accName, password, balance):
        self.accNo = accNo
        self.accName = accName
        self.password = password
        self.balance = balance

    def getAccountNo(self):
        query = "Select max(account_no) from users"
        cursor = self.db.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        if row[0] is not None:
            return row[0]+1
        else:
            return 10000000001

    def registerAcc(self, accNo, password, name, deposit):
        query = "Insert into users values(%s,%s,%s,%s)"
        args = (accNo, password, name, deposit)
        cursor = self.db.cursor()
        cursor.execute(query, args)
        if cursor.lastrowid:
            return 'last insert id' + str(cursor.lastrowid)
        else:
            return 'last insert id not found'

    def validateAcc(self, accNo, password):
        query = "Select * from users where account_no= %s and password= %s"
        args = (accNo, password)
        cursor = self.db.cursor()
        cursor.execute(query, args)
        row = cursor.fetchone()
        if row is not None:
            return True
        else:
            return False

    def getAccDetails(self, accNo):
        query = "Select * from users where account_no="+accNo
        cursor = self.db.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            return Account(row[0], row[1], row[2], row[3])
