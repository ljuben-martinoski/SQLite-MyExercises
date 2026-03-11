import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute("""
INSERT INTO bestellungen (nutzer_id, produkte_id, datum )
    VALUES 
        (1, 1, '2023-12-03'),
        (1, 2, '2023-11-08'),
        (2, 3, '2023-10-15'),
        (4, 4, '2023-08-28'),      
        (5, 2, '2023-09-15');       
               
""")

connection.commit()
connection.close()


