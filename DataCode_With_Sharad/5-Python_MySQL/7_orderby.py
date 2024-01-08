import mysql.connector
praveendb= mysql.connector.connect(host="localhost", user="root", password = "Admin260" , database ="praveendatabse")

praveencursor= praveendb.cursor()

praveensql = "select * from customers order by address asc "
praveencursor.execute(praveensql)
praveenresult= praveencursor.fetchall()
for i in praveenresult:
    print(i)