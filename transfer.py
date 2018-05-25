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
    <h3> Available Balance: {bal}</h3>
    <div class="alert alert-danger" style="display:{disp}" role="alert">
        Oops!! You dont have any money left in your account to transfer. Deposit some money to transfer
    </div>
    <form method="post" action="service.py">
    <div class="form-group">
    <label for="payeeNumber">Payee Account Number</label>
    <input type="text" class="form-control" name="payeeNumber" placeholder="1XXXXXXXXX" pattern="[0-9]*" 
    title="Only Digits, not text" maxlength="11" required {check}>
    </div>
    <div class="form-group">
    <label for="payeeBank">Payee Account Bank</label>
    <input type="text" class="form-control" name="payeeBank" placeholder="ICICI Bank" required {check}>
    </div>
    <div class="form-group">
    <label for="payeeAmount">Amount in Rs</label>
    <input type="number" class="form-control" name="payeeAmount" placeholder="1000 Rs" min=1 max={bal} step="0.1" required {check}>
    <br>
    <div class="text-center">
    <input type="hidden" value="{accID}" name="accountID">
    <input type="hidden" value="transfer" name="operation">
    <input class="btn btn-primary btn-lg" type="submit" value="Transfer" {check}>
    </div>
    </div>
    </form>
    """.format(accID=accountId, bal=acc.balance, check=("disabled" if acc.balance == 0 else ""), disp=("block" if acc.balance == 0 else "none")))

print(template.printFoot())
