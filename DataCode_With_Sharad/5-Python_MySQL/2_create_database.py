# create Database in mysql.
import mysql.connector
praveendb= mysql.connector.connect(host="localhost", user="root", password = "Admin260")
print(praveendb)

""" Here now we will create a databse  """
praveencursor = praveendb.cursor()
#praveencursor.execute("create database praveendatabse")

""" Checking databse if the database exists or not? """
praveencursor.execute("show databases")
for i in praveencursor:
    print(i)