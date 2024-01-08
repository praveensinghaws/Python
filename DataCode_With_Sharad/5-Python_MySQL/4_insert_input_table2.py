
import mysql.connector
praveendb= mysql.connector.connect(host="localhost", user="root", password = "Admin260" , database ="praveendatabse")

praveencursor= praveendb.cursor()
sql = "insert into customers (name , address) values (%s , %s)"
val = ("Kallu" , "Jhansi")
praveencursor.execute(sql ,val)
praveendb.commit()
print("1 record inserted , ID: " ,praveencursor.lastrowid)