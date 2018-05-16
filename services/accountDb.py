#! C:\Python36\python
import mysql.connector


class Account:

    db = mysql.connector.connect(
        host="localhost", user="root", password="", database="bank_app")

    def getAccountNo(self):
        query = "Select max(account_no) from users"
        cursor = self.db.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        if row[0] is not None:
            return row[0]+1
        else:
            return 10000000001
