# You can also set the limit of no of records from the table by using the limit statement
import mysql.connector
praveendb= mysql.connector.connect(host="localhost", user="root", password = "Admin260" , database ="praveendatabse")

praveencursor= praveendb.cursor()

praveencursor.execute("select  * from customers limit 3 offset 2")

praveenresult =praveencursor.fetchall()  # Fetches all roes from the last executed statement
for x in praveenresult:
    print(x)