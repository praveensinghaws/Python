# Execting Table droping
import mysql.connector
praveendb= mysql.connector.connect(host="localhost", user="root", password = "Admin260" , database ="praveendatabse")

praveencursor= praveendb.cursor()
praveensql = "drop table customers"
praveencursor.execute(praveensql)
