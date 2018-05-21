#! C:\Python36\python
import cgi
import mysql
import template

print(template.printHead())
form = cgi.FieldStorage()
if form.getvalue("accountId") and form.getvalue("password"):
    accountId = form.getvalue("accountId")
    print("<h1>Hello "+accountId+"! Thanks for using my script!</h1><br />")
    password = form.getvalue("password")
    print("<h1>Hello "+password+"! Thanks for using my script!</h1><br />")

print(template.printFoot())
