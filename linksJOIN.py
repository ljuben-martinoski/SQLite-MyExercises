import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute("""
SELECT nutzer.name, bestellungen.id
FROM nutzer
INNER JOIN bestellungen ON nutzer.id = bestellungen.nutzer_id;
""")


ergebnisse = cursor.fetchall()
connection.commit()

print("Nutzer und ihre Bestell-IDs:")
for zeile in ergebnisse:
    print(f"Nutzer: {zeile[0]} | Bestell-Nr: {zeile[1]}")
connection.close()