import sqlite3

connection= sqlite3.connect('my_database_1.db')
cursor = connection.cursor()

cursor.execute("""
INSERT INTO  Abteilung (Name)
VALUES 
    ('Entwicklung'),
    ('Marketing'),
    ('Vertrieb');
    
""")

connection.commit()
connection.close()