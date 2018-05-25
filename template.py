def printHead():
    return """
    <!DOCTYPE html>
    <html>
    <head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"></script>
    <title>Bank Application</title>
    </head>
    <body>
    <div class="container">
    <br>
    <h2 style="text-align: center">Banking App</h2>
    <br>
    """


def printFoot():
    return """
    </div>
    </body></html>
    """


def printMenuBar():
    return """
    <nav class="navbar navbar-expand-lg navbar-light bg-light ml-auto">
    <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="dashboard.py?accNo={accId}">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="addPayee.py?accNo={accId}">Add Payee</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="removePayee.py?accNo={accId}">Remove Payee</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="transfer.py?accNo={accId}">Money Transfer</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="deposit.py?accNo={accId}">Deposit Money</a>
      </li>
    </ul>
    <ul class="navbar-nav ml-auto">
        <li class="nav-item">
            <a href="index.html" class="btn btn-danger" role="button" aria-pressed="false">Logout</a>
        </li>
    </ul>
    </div>
    </nav>
    """
