#! C:\Python36\python
import cgi
import template
from accountDb import Account

acc = Account()
form = cgi.FieldStorage()
print(template.printHead())
print (template.printMenuBar())
if form.getvalue("accNo"):
    accountId = form.getvalue("accNo")
    

print(template.printFoot())
