import sqlite3

# verbindung herstellen 
verbindung = sqlite3.connect('meine_datenbank.db')
# erstellen die cursor befehele für sql ausführung
cursor = verbindung.cursor() 


cursor.execute("""
INSERT INTO autos (id, marke, modell, baujahr, preis)
VALUES 
    (1, 'VW', 'golf', 2019, 18500.00),
    (2, 'BMW', '3er', 2021, 35900.00 ),
    (3, 'Mercedes', 'A-Klasse', 2020, 29999.00),
    (4, 'Toyota', 'Yaris', 2022, 21300);
""")


verbindung.commit()  # alle änderungen in der datenbank speichern 
print("Alle daten gespeichert!!! ")

# Kontrol wie Viele zeilen wir haben i die tabelle 
cursor.execute("SELECT COUNT(*) FROM autos;")  # zahlt alle zeilen 
anzahl = cursor.fetchone()  # holt eine zeile auf die tabelle
print("Anzahl der Zeilen in 'autos': ", anzahl[0])

verbindung.close()  # sauber geschlosen die verbindung 


