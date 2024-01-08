import mysql.connector
praveendb= mysql.connector.connect(host="localhost", user="root", password = "Admin260" , database ="praveendatabse")


praveencursor= praveendb.cursor()
praveencursor.execute(" show tables")
for i in praveencursor:
    print(i)

