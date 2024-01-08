import mysql.connector
praveendb= mysql.connector.connect(host="localhost", user="root", password = "Admin260" , database ="praveendatabse")

praveencursor= praveendb.cursor()

praveensql = "select * from customers where address like '%pur%' "
praveencursor.execute(praveensql)
praveenresult= praveencursor.fetchall()
for i in praveenresult:
    print(i)