#! C:\Python36\python
import mysql.connector


class Payee:

    id = ""
    accNo = ""
    payee_name = 0
    bank_name = ""

    db = mysql.connector.connect(
        host="localhost", user="root", password="", database="bank_app")

    def __init__(self, id, accNo, payee_name, bank_name):
        self.id = id
        self.accNo = accNo
        self.payee_name = payee_name
        self.bank_name = bank_name

    def getAllPayee(self, accNo):
        query = "Select * from payee where account_no=" + str(accNo)
        cursor = self.db.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        print("working")
        payeeList = []
        while row is not None:
            print(row)
            payee = Payee(0, "", "", "")
            payee.id = row[0]
            payee.accNo = row[1]
            payee.payee_name = row[2]
            payee.bank_name = row[3]
            payeeList.append(payee)
            row = cursor.fetchone()
        return payeeList
