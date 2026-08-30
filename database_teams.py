import sqlite3
import requests

# Get API data
url = "https://www.thesportsdb.com/api/v1/json/123/searchteams.php?t=Arsenal"

response = requests.get(url)

data = response.json()

# Connect to database
connection = sqlite3.connect("sports.db")

cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Teams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_name TEXT NOT NULL,
    location TEXT,
    league TEXT
)
""")
# Insert team data
for team in data["teams"]:
    cursor.execute("""
    INSERT OR IGNORE INTO Teams (team_name, location, league)
    VALUES (?, ?, ?)
    """, (
        team["strTeam"],
        team["strLocation"],
        team["strLeague"]
    ))

connection.commit()

connection.close()

print("Team added to database!")
