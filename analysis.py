import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("Captures", exist_ok=True)

# Connect to database
connection = sqlite3.connect("sports.db")

players = pd.read_sql_query("""
SELECT player_name, position, nationality
FROM Players
""", connection)

print(players.columns)

connection.close()

# Count players by position
position_counts = players["position"].value_counts()

nationality_counts = players["nationality"].value_counts()

print(position_counts)

print("\n=== Players by Nationality ===")
print(nationality_counts)


# Create chart
plt.figure(figsize=(10,6))

position_counts.plot(kind="bar")

plt.title("Arsenal Players by Position")
plt.xlabel("Position")
plt.ylabel("Number of Players")

plt.tight_layout()

# Create images folder if it doesn't exist
os.makedirs("Sports_Dashboard_Captures", exist_ok=True)

# Save chart
plt.savefig("Sports_Dashboard_Captures/players_by_position.png", dpi=300)

print("Chart saved to Sports_Dashboard_Captures/players_by_position.png")

# Create nationality chart
plt.figure(figsize=(10,6))

nationality_counts.plot(kind="bar")

plt.title("Players by Nationality")
plt.xlabel("Nationality")
plt.ylabel("Number of Players")

plt.tight_layout()

plt.savefig("Sports_Dashboard_Captures/players_by_nationality.png", dpi=300)

print("Nationality chart saved!")

plt.show()