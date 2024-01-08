import mysql.connector
praveendb= mysql.connector.connect(host="localhost", user="root", password = "Admin260" , database ="praveendatabse")


praveencursor= praveendb.cursor()
praveencursor.execute("create table customers(id int auto_increment primary key, name varchar(255), address varchar(255))")

