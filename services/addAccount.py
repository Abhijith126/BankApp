#! C:\Python36\python

import cgi
from accountDb import Account


acc = Account()
print("Content-type:text/html\r\n\r\n")
print("<html><body>")
print("<h1>heeello</h1>")
form = cgi.FieldStorage()
if form.getvalue("accountId") and form.getvalue("password") and form.getvalue("accName") and form.getvalue("deposit"):
    accountId = str(form.getvalue("accountId"))
    password = str(form.getvalue("password")) 
    name = str(form.getvalue("name"))
    deposit = str(form.getvalue("deposit"))
    retval = acc.registerAcc(accountId, password, name, deposit)


print("</body></html>")
