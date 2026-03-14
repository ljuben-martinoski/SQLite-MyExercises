import sqlite3


verbindung = sqlite3.connect("meine_datenbank.db")
# erstellen die  cursor Objekt daj kann SQL Befehle ausführen 
cursor = verbindung.cursor()  


# execute befehle 
cursor.execute("DROP TABLE IF EXISTS auto;")
cursor.execute("DROP TABLE IF EXISTS autos;")
print("Erfolgreich! Gibt keine Tabelle mit solche name.")


cursor.execute("""
CREATE TABLE autos (
    id INTEGER, 
    marke TEXT, 
    modell TEXT, 
    baujahr INTEGER, 
    preis REAL); 
""")

verbindung.commit()  # commit für die erstellen auf die sogennante tabele
print("Tabelle 'autos' wurde erstellt.")


# Überprüfen ob die Tabelle existiert—sqlite_master ist eine interne SQLite-Tabelle
cursor.execute("""
SELECT name FROM sqlite_master
WHERE type='table';
""")

tabellen = cursor.fetchall()
print("Vorhandene Tabellen in der Datenbank:", tabellen)

verbindung.close()


