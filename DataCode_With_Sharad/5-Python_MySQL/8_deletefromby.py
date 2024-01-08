import mysql.connector
praveendb= mysql.connector.connect(host="localhost", user="root", password = "Admin260" , database ="praveendatabse")

praveencursor= praveendb.cursor()
praveensql = "delete from customers where address = 'Lucknow'"
praveencursor.execute(praveensql)
praveendb.commit()  # if you want to delete permanently then use this statement
print(praveencursor.rowcount, "Record Deleted")