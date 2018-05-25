#! C:\Python36\python
import cgi
import template
from accountDb import Account

print(template.printHead())
acc = Account("", "", "", 0)
form = cgi.FieldStorage()
if form.getvalue("accNo"):
    accountId = form.getvalue("accNo")
    password = form.getvalue("pass")
    conPass = form.getvalue("conPass")
    if password == conPass:
        print(acc.updatePass(accountId, password))
    else:
        print("""<br>
        <p> Passwords do not match or the Account is not registered with the Bank. Please <a href="register.py" class="alert-link">Register</a> a new account or visit the Bank for more clarifications :)
        """)

print(template.printFoot())
