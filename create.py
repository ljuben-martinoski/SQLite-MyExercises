import sqlite3
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()


cursor.executescript("""
    DROP TABLE IF EXISTS bestellungen;
    DROP TABLE IF EXISTS nutzer;
    DROP TABLE IF EXISTS produkte;

    CREATE TABLE nutzer (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        vorname TEXT,       
        stadt TEXT,
        jahre INT,
        adresse VARCHAR(50),
        email TEXT
        );
    CREATE TABLE produkte (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        artikel TEXT,
        preis REAL
        );
    CREATE TABLE bestellungen (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nutzer_id INTEGER,
        produkte_id INTEGER,
        datum TEXT,
        FOREGIN KEY (nutzer_id) REFERENCES nutzer(id),
        FOREGIN KEY (produkt_id) REFERENCES produkte(id)
        );
                                                               
""")
connection.commit()
connection.close()