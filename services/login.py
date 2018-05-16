#! C:\Python36\python
import cgi
import mysql

print("Content-type:text/html\r\n\r\n")
print("<html><body>")
form = cgi.FieldStorage()
if form.getvalue("accountId") and form.getvalue("password"):
    accountId = form.getvalue("accountId")
    print("<h1>Hello "+accountId+"! Thanks for using my script!</h1><br />")
    password = form.getvalue("password")
    print("<h1>Hello "+password+"! Thanks for using my script!</h1><br />")
    
print("</body></html>")
