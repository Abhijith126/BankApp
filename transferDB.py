#! C:\Python36\python
import mysql.connector


class Transfer:

    id = 0
    accNo = 0
    payee_acc_no = 0
    bank_name = ""
    amount = 0

    db = mysql.connector.connect(
        host="localhost", user="root", password="", database="bank_app")

    def __init__(self, id, accNo, payee_acc_no, bank_name, amount):
        self.id = id
        self.accNo = accNo
        self.payee_acc_no = payee_acc_no
        self.amount = amount
        self.bank_name = bank_name

    def getAllTransfers(self, accNo):
        query = "Select * from transfers where account_no=" + accNo
        cursor = self.db.cursor()
        cursor.execute(query)
        return list(cursor.fetchall())

    def addTransaction(self, accNo, payeeAccNo, payeeBank, amount):
        query = "INSERT INTO transfers VALUES(0,%s,%s,%s,%s)"
        cursor = self.db.cursor()
        args = (accNo, payeeAccNo, payeeBank, amount)
        cursor.execute(query, args)
        self.db.commit()
        return """ <br><br>
        <div class="alert alert-success" role="alert">
           The amount of {amount} is transfered to Account: {accNo}
        </div>""".format(amount=amount, accNo=payeeAccNo)
