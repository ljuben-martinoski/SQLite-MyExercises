import sqlite3

connection = sqlite3.connect('my_database_1.db')
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE Mitarbeiter (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(50),
    AbtID INTEGER,
    FOREIGN KEY (AbtID) REFERENCES Abteilung (ID)
);
"""
)


connection.commit()
connection.close()