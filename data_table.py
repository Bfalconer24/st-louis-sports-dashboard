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
cursor.execute("""
CREATE TABLE IF NOT EXISTS AI_Reports(
    report_id INTEGER PRIMARY KEY AUTOINCREMENT,
    report_type TEXT,
    subject TEXT,
    report_text TEXT,
    created_at TEXT
)
""")

connection.commit()

connection.close()
