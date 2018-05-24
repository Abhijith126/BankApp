#! C:\Python36\python
import cgi
import template
from accountDb import Account

def addPayee():
    print("add")

def removePayee():
    print("remove")

print(template.printHead())
acc = Account("", "", "", 0)
form = cgi.FieldStorage()
if form.getvalue("operation") == "add":
    addPayee()
if form.getvalue("operation") == "del":
    removePayee()

print(template.printFoot())
