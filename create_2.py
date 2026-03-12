import sqlite3

connection = sqlite3.connect('my_database_1.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE Abteilung(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(50)
);
"""

)

connection.commit()
connection.close()