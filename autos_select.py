import sqlite3

verbindung = sqlite3.connect('meine_datenbank.db')
cursor = verbindung.cursor()

# alle zeilen aus die tabelle
cursor.execute("""
SELECT * FROM autos;
""")
alle_zeilen = cursor.fetchall() # fetchall = alle Ergebniszeilen ale Liste holen 
for zeile in alle_zeilen:
    print(zeile)

# -------------------------------------------------------
# METHODE 2: Nur bestimmte Spalten auswählen
# -------------------------------------------------------

print("\n=== NUR MARKE UND BAUJAHR ===")
cursor.execute("SELECT marke, baujahr FROM autos;")

ergebnisse = cursor.fetchall() # alle ergebnise hollen   
for zeile in ergebnisse:
    print(zeile)


# -------------------------------------------------------
# METHODE 3: Nur die erste Zeile holen
# -------------------------------------------------------
print("\n=== NUR ERSTE ZEILE ===")
cursor.execute("SELECT * FROM autos;")
erste_zeile = cursor.fetchone()  # fetchhone() = nue eine einzige Zeilen holen
print(erste_zeile)

# -------------------------------------------------------
# METHODE 4: Ergebnisse schön formatiert ausgeben
# -------------------------------------------------------
