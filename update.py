import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute("""
ALTER TABLE produkte ADD COLUMN preis_text TEXT;
""")

cursor.execute("""
UPDATE produkte SET preis_text = printf("%.2f", preis);
""")

cursor.execute("""
ALTER TABLE produkte DROP COLUMN preis;
""")

cursor.execute("""
ALTER TABLE produkte RENAME COLUMN preis_text TO preis;
""")

connection.commit()
connection.close()