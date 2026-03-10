import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute("SELECT artikel, preis FROM produkte")
rows = cursor.fetchall()

for row in rows:
    print(f"{row[0]}: {row[1]}")

connection.close()