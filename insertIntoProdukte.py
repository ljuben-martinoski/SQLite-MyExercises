import sqlite3
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()


cursor.execute("""
UPDATE produkte (artikel, preis) 
    VALUES 
        ('Iphone 10', 1800.00 ),
        ('Redmi 10', 450.00 ),
        ('Nokia', 890.00 ),
        ('DongSeng', 540.00 ),
        ('Iphone 12', 841.00 );                                
""")
connection.commit()
connection.close()


