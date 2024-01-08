
# you can update the existing records in a table by using statement.
import mysql.connector
praveendb= mysql.connector.connect(host="localhost", user="root", password = "Admin260" , database ="praveendatabse")

praveencursor= praveendb.cursor()
praveensql = "update customers set name = 'Cheeku' where id = 8"
praveencursor.execute(praveensql)
praveendb.commit()
print(praveencursor.rowcount, "Record updated")