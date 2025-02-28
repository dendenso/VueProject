import mysql.connector
import os

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = os.getenv("MYSQL_PASSWORD"),
    database="mydb"
)
