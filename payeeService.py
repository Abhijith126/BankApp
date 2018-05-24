#! C:\Python36\python
import cgi
import template
from payeeDB import Payee

payee = Payee(0, "", "", "")
form = cgi.FieldStorage()


def addPayee():
    print(template.printMenuBar().format(accId=form.getvalue("accountID")))
    accId = form.getvalue("accountID")
    accName = form.getvalue("payeeName")
    payeeBank = form.getvalue("payeeBank")
    payeeAccNO = form.getvalue("payeeNumber")
    print(payee.addPayee(accId, payeeAccNO, accName, payeeBank))


def removePayee():
    print(template.printMenuBar().format(accId=form.getvalue("accountID")))
    id = form.getvalue("payeeID")
    print(payee.deletePayee(id))


print(template.printHead())

if form.getvalue("operation") == "add":
    addPayee()
if form.getvalue("operation") == "del":
    removePayee()

print(template.printFoot())
