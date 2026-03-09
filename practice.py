
import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()


# Jetzt führen wir den Befehl aus:
cursor.execute("""DELETE FROM nutzer WHERE rowid NOT IN (SELECT MIN(rowid) FROM nutzer GROUP BY name)""")
connection.commit()
