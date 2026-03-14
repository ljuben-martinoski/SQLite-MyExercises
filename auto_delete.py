import sqlite3

verbinudng = sqlite3.connect('meine_datenbank.db')
cursor = verbinudng.cursor()


cursor.execute("DROP TABLE IF EXISTS auto;")
print("Erfolgreich! ")

verbinudng.commit()
verbinudng.close()

