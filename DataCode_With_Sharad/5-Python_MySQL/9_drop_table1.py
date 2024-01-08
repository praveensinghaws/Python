# Execting Table droping
import mysql.connector
praveendb= mysql.connector.connect(host="localhost", user="root", password = "Admin260" , database ="praveendatabse")

praveencursor= praveendb.cursor()
praveensql = "drop table if exists customers" # it is used  if exists table then delete orderwise no error 
praveencursor.execute(praveensql)
