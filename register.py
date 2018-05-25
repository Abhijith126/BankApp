#! C:\Python36\python

import cgi
from accountDb import Account
import template

acc = Account(0, "", "", "")
print(template.printHead())
print("""
    <div style="text-align: center;">
        <form method="POST" action="addAccount.py">
        <table class="table w-50  table-borderless" align='center'>
        <tr><td>
            <label for="accountId">Account ID : </label></td><td>
            <input type="text" class="form-control" name="accountId" placeholder="Account ID" value="{accountId}" readonly>
            </td></tr><tr><td>
            <label for="password">Password : </label></td><td>
            <input type="text" class="form-control" name="password" placeholder="Password" required>
            </td></tr><tr><td>
            <label for="accName">Name : </label></td><td>
            <input type="text" class="form-control" name="accName" placeholder="Name" required>
            </td></tr><tr><td>
            <label for="deposit">Initial Deposit : </label></td><td>
            <input type="number" class="form-control" name="deposit" placeholder="Initial Deposit" required>
            </td></tr>
            </table>
            <br>
            <input class="btn btn-success" type="submit" value="Register New Account">&nbsp;
        </form>
    </div>
""".format(accountId=acc.getAccountNo()))

print(template.printFoot())
