#! C:\Python36\python
import cgi
import template
from accountDb import Account

acc = Account("", "", "", 0)
form = cgi.FieldStorage()
print(template.printHead())
if form.getvalue("accNo"):
    accountId = form.getvalue("accNo")
    acc = acc.getAccDetails(accountId)
    print(template.printMenuBar().format(accId=accountId))
    print("""
    <br>
    <table class="table w-50 table-borderless">
    <tbody>
    <tr>
      <th scope="row">Account No:</th>
      <td>{accountId}</td>
    </tr>
    <tr>
      <th scope="row">Name:</th>
      <td>{accName} </td>
    </tr>
    <tr>
      <th scope="row">Balance:</th>
      <td>{accBal}</td>
    </tr>
    </tbody>
    </table>
    """.format(accountId=acc.accNo, accName=acc.accName, accBal=acc.balance))

print(template.printFoot())
