import sqlite3
connection = sqlite3.connect('my_database')
cursor = connection.cursor()


cursor.execute("""
    INSERT INTO nutzer (name, vorname, stadt, jahre, adresse, email)
    VALUES
        ('Anna', 'Frank', 'Berlin', 33, 'Jon Wayn Nr:35', 'dddd@ggg.com'),
        ('Robert', 'Green', 'Münich', 33, 'Kochstr. Nr:23', 'asdas@ggg.com'),
        ('Ema', 'Mononoka', 'Erlangen', 33, 'Johan-Kalb-Str. Nr:56',
         'defr@ggg.com'),
        ('Bruce', 'Wain', 'Nürnberg', 43, 'Rathensbergerstraße Nr:44',
         'aasd@g.com')
""")
connection.commit()
connection.close()