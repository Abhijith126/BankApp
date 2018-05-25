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
            return 1000000

    def registerAcc(self, accNo, name, password, deposit):
        query = "Insert into users values(%s,%s,%s,%s)"
        args = (accNo, name, password, deposit)
        cursor = self.db.cursor()
        cursor.execute(query, args)
        self.db.commit()
        cursor.close()
        return """<br><br>
        <div class="alert alert-primary" role="alert">
        Yayyy!! Celebrate. Your account has been created. Please <a href="index.html" class="alert-link">Login</a> to access the bank
        </div>
        """

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

    def depositMoney(self, accNo, amount):
        query = "UPDATE users  SET balance= balance+ %s where account_no = %s"
        args = (amount, accNo)
        cursor = self.db.cursor()
        cursor.execute(query, args)
        self.db.commit()
        cursor.close()
        return """<br><br>
        <div class="alert alert-primary" role="alert">
        Yayyy!! Celebrate. Your account has been credited with <b> {amt} Rupees</b>. Please visit <a href="dashboard.py?accNo={accNo}" class="alert-link">Home page</a>
         to check the account details.
        </div>
        """.format(amt=amount, accNo=accNo)

    def debitAmt(self, accNo, amount):
        query = "UPDATE users  SET balance= balance- %s where account_no = %s"
        args = (amount, accNo)
        cursor = self.db.cursor()
        cursor.execute(query, args)
        self.db.commit()
        cursor.close()
        return """<br>
        <div class="alert alert-primary" role="alert">
        Your account has been debited with <b> {amt} Rupees</b>. Please visit <a href="dashboard.py?accNo={accNo}" class="alert-link">Home page</a>
        to check the account details.
        </div>
        """.format(amt=amount, accNo=accNo)

    def updatePass(self, accNo, password):
        query = "UPDATE users  SET password= %s where account_no = %s"
        args = (password, accNo)
        cursor = self.db.cursor()
        cursor.execute(query, args)
        self.db.commit()
        cursor.close()
        return """<br>
        <div class="alert alert-primary" role="alert">
        Your account password is changed and the password is : <b> {password}</b>. Please <a href="index.html" class="alert-link">Login</a> to access the bank
        to check the account details.
        </div>
        """.format(password=password)
