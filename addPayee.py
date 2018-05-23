#! C:\Python36\python
import cgi
import template
from accountDb import Account

print(template.printHead())
acc = Account("", "", "", 0)
form = cgi.FieldStorage()
if form.getvalue("accNo"):
    accountId = form.getvalue("accNo")
    acc = acc.getAccDetails(accountId)
    print(template.printMenuBar().format(accId=accountId))
    print("""
    <br>
    <form method="post" action="payeeDb.py">
    <div class="form-group">
    <label for="payeeNumber">Payee Account Number</label>
    <input type="text" class="form-control" id="payeeNumber" placeholder="1XXXXXXXXX">
    </div>
    <div class="form-group">
    <label for="payeeName">Payee Account Name</label>
    <input type="text" class="form-control" id="payeeName" placeholder="Amith Shah">
    </div>
    <div class="form-group">
    <label for="payeeBank">Payee Account Bank</label>
    <input type="text" class="form-control" id="payeeBank" placeholder="ICICI Bank">
    </div>
    </form>
    """)

print(template.printFoot())
