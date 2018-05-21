#! C:\Python36\python

import cgi
from accountDb import Account
import template

acc = Account()
print(template.printHead())
print("""
    <h2 style="text-align: center">Banking App</h2>
    <br>
    <br>
    <div style="text-align: center;">
        <form method="GET" action="addAccount.py">
        <table align='center'>
        <tr><td>
            <label for="accountId">Account ID : </label></td><td>
            <input type="text" name="accountId" placeholder="Account ID" value="{accountId}" readonly>
            </td></tr><tr><td>
            <label for="password">Password : </label></td><td>
            <input type="text" name="password" placeholder="Password" required>
            </td></tr><tr><td>
            <label for="accName">Name : </label></td><td>
            <input type="text" name="accName" placeholder="Name" required>
            </td></tr><tr><td>
            <label for="deposit">Initial Deposit : </label></td><td>
            <input type="number" name="deposit" placeholder="Initial Deposit" required>
            </td></tr>
            </table>
            <br>
            <br>
            <input type="submit" value="Register New Account">&nbsp;
        </form>
    </div>
""".format(accountId=acc.getAccountNo()))

print(template.printFoot())
