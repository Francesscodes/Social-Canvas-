import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="anselemngo97$"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE social_canvas_db")