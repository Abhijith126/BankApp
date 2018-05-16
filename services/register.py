#! C:\Python36\python

import cgi
from accountDb import Account

acc = Account()

print("Content-type:text/html\r\n\r\n")
print(""" 
<html><head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Bank Application</title>
</head><body>
    <h2 style="text-align: center">Banking App</h2>
    <br>
    <br>
    <div style="text-align: center">
        <form method="POST" action="services/addAccount.py">
            <label for="accountId">Account ID : </label>
            <input type="text" name="accountId" placeholder="Account ID" disabled value='
""") 
print(acc.getAccountNo())
print("""'>
            <br>
            <br>
            <label for="password">Password : </label>
            <input type="text" name="password" placeholder="Password" required>
            <br>
            <br>
            <input type="submit" value="Register New Account">&nbsp;
        </form>
    </div>
</body>
</html> """)
