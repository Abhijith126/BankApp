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
    payeeList = payee.getAllPayee(accountId)
    print(template.printMenuBar().format(accId=accountId))
    print("""<br>
        <p>Below are the list of Payee added to your account. 
        Feel free to delete them when ever you want.</p>
        <table class="table table-bordered">
            <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Payee Account No</th>
                <th scope="col">Payee Account Name</th>
                <th scope="col">Payee Account Bank</th>
                <th scope="col">Actions</th>
            </tr>
            </thead>
            <tbody>
    """)
    if len(payeeList) == 0:
        print("<tr><td colspan=5><p style='text-align:center;'> <b>No records found</b></p></td></tr>")
    else:
        for idx, payee in enumerate(payeeList):
            print("""
            <tr>
                <th scope="row">{rowId}</th>
                <td>{accNo}</td>
                <td>{name}</td>
                <td>{bank}</td>
                <td><form method="post" action="payeeService.py">
                    <input type="hidden" name="operation" value="del" >
                    <input type="hidden" name="payeeID" value="{id}" >
                    <input type="hidden" name="accountID" value="{accID}" >                    
                    <input class="btn btn-warning" type="submit" value="Delete Payee"></form>
                </td>
            </tr>
            """.format(rowId=idx+1, id=payee[0], accNo=payee[2], name=payee[3], bank=payee[4], accID=accountId))
    print("</tbody></table>")


print(template.printFoot())
