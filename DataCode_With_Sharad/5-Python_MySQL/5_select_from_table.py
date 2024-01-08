
import mysql.connector
praveendb= mysql.connector.connect(host="localhost", user="root", password = "Admin260" , database ="praveendatabse")

praveencursor= praveendb.cursor()
praveencursor.execute("select * from customers")
praveenresult =praveencursor.fetchall()  # Fetches all roes from the last executed statement
for i in praveenresult:
    print(i)