import sqlite3
import requests

# Get API data
url = "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Arsenal_vs_Chelsea"

response = requests.get(url)

data = response.json()

# Connect to database
connection = sqlite3.connect("sports.db")

cursor = connection.cursor()

# Insert event data
for event in data["event"]:
    cursor.execute("""
    INSERT INTO Events (event_id, event_name, event_date, home_team, away_team, league, venue, country)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        event["idEvent"],
        event["strEvent"],
        event["dateEvent"],
        event["strHomeTeam"],
        event["strAwayTeam"],
        event["strLeague"],
        event["strVenue"],
        event["strCountry"]
    ))

# Save changes
connection.commit()

connection.close()

print("Event added to database!")