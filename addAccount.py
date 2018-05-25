#! C:\Python36\python

import cgi
import sys
from accountDb import Account
import template

acc = Account(0, "", "", "")

print(template.printHead())
form = cgi.FieldStorage()
if form.getvalue("accountId") and form.getvalue("password") and form.getvalue("accName") and form.getvalue("deposit"):
    accountId = str(form.getvalue("accountId"))
    password = str(form.getvalue("password"))
    name = str(form.getvalue("accName"))
    deposit = str(form.getvalue("deposit"))
    print(acc.registerAcc(accountId, name, password, deposit))
    print("""
    """)

print(template.printFoot())
