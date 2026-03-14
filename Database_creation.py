import sqlite3

## Verbindung zur Datenbank herstellen
# Wenn die Datei "meine_datenbank.db" noch nicht existiert, wird sie automatisch erstellt
verbindung = sqlite3.connect('meine_datenbank.db')
# Einen "Cursor" erstellen — das ist unser Werkzeug zum Ausführen von SQL-Befehlen
# Stell dir den Cursor wie einen Stift vor, mit dem wir in die Datenbank schreiben/lesen
cursor = verbindung.cursor() # Cursor-Objekt erstellen, um SQL-Befehle auszuführen

cursor.execute("SELECT sqlite_version()") # execute () führt einen SQL - Befehl,

ergebnis = cursor.fetchone() # Das Ergebnis holen — fetchone() holt genau EINE Zeile aus dem Ergebnis

print("SQL Veriosn: ", ergebnis[0])
print("Verbindung erfolgerich! Die Datei 'meine_datenbank.db' wurde erstellt.")