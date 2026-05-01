import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="anselemngo97$",  # missing comma
    database="social_canvas_db"
)

mycursor = mydb.cursor()

sql = "INSERT INTO users (name, email, password_hash, role, phone) VALUES (%s, %s, %s, %s, %s)"
val = ('Zee', 'zee@email.com', 'test123', 'client', '08012345678')

mycursor.execute(sql, val)
mydb.commit()

print(f"User inserted! ID: {mycursor.lastrowid}")