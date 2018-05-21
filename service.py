#! C:\Python36\python
import mysql.connector


db = mysql.connector.connect(host="localhost",user="root",password="",database="bank_app" )
cursor = db.cursor()
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()