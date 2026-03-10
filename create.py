import sqlite3
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()


cursor.executescript("""
    DROP TABLE IF EXISTS bestellungen;
    
    CREATE TABLE bestellungen (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nutzer_id INTEGER,
        produkte_id INTEGER,
        datum TEXT,
        FOREIGN KEY (nutzer_id) REFERENCES nutzer(id),
        FOREIGN KEY (produkte_id) REFERENCES produkte(id)
        );
                                                               
""")

connection.commit()
connection.close()