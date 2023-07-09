import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
)

# print("Database connected successfully")

#prepare a cursor object
cursorObject = dataBase.cursor()

#create database
cursorObject.execute("CREATE DATABASE dcrm")

print("Database created successfully")