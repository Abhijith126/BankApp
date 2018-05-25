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
    <p> Feel free to deposit your money in our bank. We assure you that your money is safe with us ;)</p>
    <br>
    <form method="post" action="service.py">
    <div class="form-group">
    <label for="amount">Amount in Rs</label>
    <input type="number" class="form-control" name="amount" placeholder="1000 Rs" required>
    <br>
    <div class="text-center">
    <input type="hidden" value="deposit" name="operation">
    <input type="hidden" value="{accID}" name="accountID">
    <input class="btn btn-primary btn-lg" type="submit" value="Transfer">
    </div>
    </div>
    </form>
    """.format(accID=accountId))

print(template.printFoot())
