import sqlite3

connection = sqlite3.connect('my_database_1.db')
cursor = connection.cursor()

cursor.execute("""
INSERT INTO Mitarbeiter (name)
VALUES 
       ('Schmidt'),
       ('Müller'),
       ('Weber'),
       ('Klein');
""")

connection.commit()
connection.close()