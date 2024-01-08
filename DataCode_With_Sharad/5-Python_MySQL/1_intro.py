# Python Needs a MySql Driver to access the Database.
import mysql.connector
praveendb= mysql.connector.connect(host="localhost", user="root", password = "Admin260")
print(praveendb)