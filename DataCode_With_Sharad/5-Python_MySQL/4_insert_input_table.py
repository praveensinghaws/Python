
import mysql.connector
praveendb= mysql.connector.connect(host="localhost", user="root", password = "Admin260" , database ="praveendatabse")

praveencursor= praveendb.cursor()
sql = "insert into customers (name , address) values (%s , %s)"
val = ("Praveen" , "Lucknow")
praveencursor.execute(sql,val)
praveendb.commit()  # very importent for saving the changes
print(praveencursor.rowcount,"record done")