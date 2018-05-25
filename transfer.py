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
    print("""<br>
    <p> Feel free to transfer any amount without the fear of transaction charges. 
    It absolotely free!!!. Provided you have cash in your account. :) </p>
    <br>
    <form method="post" action="payeeService.py">
    <div class="form-group">
    <label for="payeeNumber">Payee Account Number</label>
    <input type="text" class="form-control" name="payeeNumber" placeholder="1XXXXXXXXX" required>
    </div>
    <div class="form-group">
    <label for="payeeBank">Payee Account Bank</label>
    <input type="text" class="form-control" name="payeeBank" placeholder="ICICI Bank" required>
    </div>
    <div class="form-group">
    <label for="payeeAmount">Amount in Rs</label>
    <input type="number" class="form-control" name="payeeAmount" placeholder="1000" required>
    <br>
    <div class="text-center">
    <input type="hidden" value="add" name="operation" >
    <input type="hidden" value="{accID}" name="accountID">
    <input class="btn btn-primary btn-lg" type="submit" value="Transfer">
    </div>
    </div>
    </form>
    """.format(accID=accountId))

print(template.printFoot())
