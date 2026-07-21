import sqlite3

connection =sqlite3.connect("sports.db")

cursor = connection.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS Teams(
               id INTEGER PRIMARY KEY,
               team_name TEXT,
               location TEXT,
               league TEXT
       )
         """)

connection.commit()

connection.close()
