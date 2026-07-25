import sqlite3

connection = sqlite3.connect("sports.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM Teams")

teams = cursor.fetchall()

for team in teams:
    print(team)

cursor.execute("""
SELECT * FROM Events
""")

events = cursor.fetchall()

for event in events:
    print(event)   

cursor.execute("SELECT * FROM Players")

players = cursor.fetchall()

for player in players:
    print(player)

connection.close()