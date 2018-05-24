#! C:\Python36\python
import cgi
import template
from accountDb import Account
from payeeDB import Payee

print(template.printHead())
acc = Account("", "", "", 0)
payee = Payee(0, "", "", "")

form = cgi.FieldStorage()
if form.getvalue("accNo"):
    accountId = form.getvalue("accNo")
    acc = acc.getAccDetails(accountId)
    print(template.printMenuBar().format(accId=accountId))
    print("""
    <br>
    <form method="post" action="payeeService.py">
    <div class="form-group">
    <label for="payeeNumber">Payee Account Number</label>
    <input type="text" class="form-control" name="payeeNumber" placeholder="1XXXXXXXXX" required>
    </div>
    <div class="form-group">
    <label for="payeeName">Payee Account Name</label>
    <input type="text" class="form-control" name="payeeName" placeholder="Amith Shah" required>
    </div>
    <div class="form-group">
    <label for="payeeBank">Payee Account Bank</label>
    <input type="text" class="form-control" name="payeeBank" placeholder="ICICI Bank" required>
    <br>
    <div class="text-center">
    <input type="hidden" value="del" name="operation" >
    <input class="btn btn-primary btn-lg" type="submit" value="Add Payee">
    </div>
    </div>
    </form>
    """)
    print(payee.getAllPayee(10000000))


print(template.printFoot())
