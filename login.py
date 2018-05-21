#! C:\Python36\python
import cgi
import template
from accountDb import Account

acc = Account()
form = cgi.FieldStorage()
if form.getvalue("accountId") and form.getvalue("password"):
    accountId = form.getvalue("accountId")
    password = form.getvalue("password")
    if(acc.validateAcc(accountId, password)):
        print("Location:dashboard.py?accNo="+accountId)
    else:
        print("Location:index.html?validated=False")
print(template.printFoot())
