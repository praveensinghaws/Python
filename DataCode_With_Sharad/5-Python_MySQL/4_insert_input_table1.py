
import mysql.connector
praveendb= mysql.connector.connect(host="localhost", user="root", password = "Admin260" , database ="praveendatabse")

praveencursor= praveendb.cursor()
sql = "insert into customers (name , address) values (%s , %s)"
val = [('ravi' ,'Sultanpur'),
       ('Mahesh' ,'Kanpur'),
       ('Vinay' ,'Ballia'),
       ('Rahul' ,'Gorakhpur'),
       ('Sujeet' ,'Azamgarh'),
       ('Kallu' ,'Mau')
       ]
praveencursor.executemany(sql ,val)
praveendb.commit()
print(praveencursor.rowcount,"Was Inserted")