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
        return list(cursor.fetchall())

    def deletePayee(self, payeeID):
        query = "DELETE FROM payee WHERE id =" + payeeID
        cursor = self.db.cursor()
        cursor.execute(query)
        self.db.commit()
        return """ <br><br>
        <div class="alert alert-danger" role="alert">
        Well, you just deleted the details of a payee. I hope you are happy now. :(
        </div>"""

    def addPayee(self, accNo, payeeAccNo, payeeName, payeeBank):
        query = "INSERT INTO payee VALUES(0,%s,%s,%s,%s)"
        cursor = self.db.cursor()
        args = (accNo, payeeAccNo, payeeName, payeeBank)
        cursor.execute(query, args)
        self.db.commit()
        return """ <br><br>
        <div class="alert alert-success" role="alert">
           The Payee with Acc No: {accID} is added to your Account Number: {accNo}
        </div>""".format(accID=payeeAccNo, accNo=accNo)
