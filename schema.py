import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute("PRAGMA table_info(produkte)")
schema = cursor.fetchall()

print("Table schema:")
for col in schema:
    print(col)

connection.close()