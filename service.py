#! C:\Python36\python
import cgi
import template
from transferDB import Transfer
from accountDb import Account

transaction = Transfer(0, 0, 0, "", 0)
acc = Account(0, "", "", "")
form = cgi.FieldStorage()
print(template.printHead())


def doDeposit():
    if form.getvalue("accountID"):
        print(template.printMenuBar().format(accId=form.getvalue("accountID")))
        accId = form.getvalue("accountID")
        amount = form.getvalue("amount")
        print(acc.depositMoney(accId, amount))


def doTransaction():
    if form.getvalue("accountID"):
        print(template.printMenuBar().format(accId=form.getvalue("accountID")))
        accId = form.getvalue("accountID")
        amount = form.getvalue("payeeAmount")
        payeeBank = form.getvalue("payeeBank")
        payeeAccNO = form.getvalue("payeeNumber")
        print(transaction.addTransaction(accId, payeeAccNO, payeeBank, amount))
        print(acc.debitAmt(accId, amount))


if form.getvalue("operation") == "transfer":
    doTransaction()
if form.getvalue("operation") == "deposit":
    doDeposit()

print(template.printFoot())
