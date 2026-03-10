import sqlite3
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute("""
DELETE FROM produkte 
WHERE rowid NOT IN (
    SELECT MIN(rowid) 
    FROM produkte 
    GROUP BY artikel, preis 
);
""")

connection.commit()
connection.close()