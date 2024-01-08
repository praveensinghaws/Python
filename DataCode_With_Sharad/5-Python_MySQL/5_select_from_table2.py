
import mysql.connector
praveendb= mysql.connector.connect(host="localhost", user="root", password = "Admin260" , database ="praveendatabse")

praveencursor= praveendb.cursor()
praveencursor.execute("select * from customers ")
praveenresult =praveencursor.fetchone()  # Fetchone method will return the 1st row of the result

print(praveenresult)