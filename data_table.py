import sqlite3

connection = sqlite3.connect("sports.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Teams(
    id INTEGER PRIMARY KEY,
    team_name TEXT UNIQUE,
    location TEXT,
    league TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Events(
    event_id TEXT PRIMARY KEY,
    event_name TEXT,
    event_date TEXT,
    home_team TEXT,
    away_team TEXT,
    league TEXT,
    venue TEXT,
    country TEXT
)
  """) 

cursor.execute("""
CREATE TABLE IF NOT EXISTS Players(
    player_id TEXT PRIMARY KEY,
    player_name TEXT,
    team_name TEXT,
    position TEXT,
    nationality TEXT
)
""")

connection.commit()

connection.close()
