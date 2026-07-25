import sqlite3
import requests

# Get player data
url = "https://www.thesportsdb.com/api/v1/json/123/lookup_all_players.php?id=133604"

response = requests.get(url)

data = response.json()

# Connect to database
connection = sqlite3.connect("sports.db")

cursor = connection.cursor()

# Insert player data
for player in data["player"]:
    cursor.execute("""
    INSERT OR IGNORE INTO Players
    (player_id, player_name, team_name, position, nationality)
    VALUES (?, ?, ?, ?, ?)
    """, (
        player["idPlayer"],
        player["strPlayer"],
        player["strTeam"],
        player["strPosition"],
        player["strNationality"]
    ))

connection.commit()

connection.close()

print("Players added to database!")