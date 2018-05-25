#! C:\Python36\python
import cgi
import template

print(template.printHead())
form = cgi.FieldStorage()
if form.getvalue("accNo"):
    accountId = form.getvalue("accNo")
    print(template.printMenuBar().format(accId=accountId))
    print("""
    <br>
    <form method="post" action="payeeService.py">
    <div class="form-group">
    <label for="payeeNumber">Payee Account Number</label>
    <input type="text" class="form-control" name="payeeNumber" placeholder="1XXXXXXXX" pattern="[0-9]*" 
    title="Only Digits, not text" maxlength="11"  required>
    </div>
    <div class="form-group">
    <label for="payeeName">Payee Account Name</label>
    <input type="text" class="form-control" name="payeeName" placeholder="Jane Doe" required>
    </div>
    <div class="form-group">
    <label for="payeeBank">Payee Account Bank</label>
    <input type="text" class="form-control" name="payeeBank" placeholder="ICICI Bank" required>
    <br>
    <div class="text-center">
    <input type="hidden" value="add" name="operation" >
    <input type="hidden" value="{accID}" name="accountID">
    <input class="btn btn-primary btn-lg" type="submit" value="Add Payee">
    </div>
    </div>
    </form>
    """.format(accID=accountId))

print(template.printFoot())
